from typing import Dict, Any

def compute_rmri_delta(E: float, s: float, c2: float) -> Dict[str, float]:
    eps = 1e-6
    I = (E * s) / max(eps, c2)
    return {"E": E, "s": s, "c2": c2, "I": I}

def classify_phase(E: float, s: float, c2: float, I: float) -> str:
    # Very simple heuristics for the reference build
    if c2 > 9 or I < 0.015:
        return "rest" if I < 0.01 else "receive"
    if s >= 0.7 and I >= 0.03:
        return "release" if E >= 0.6 else "resonate"
    if s >= 0.5:
        return "resonate"
    return "receive"

def regulate(obs: Dict[str, Any], rmri: Dict[str, float], phase: str, T: Dict[str, float]):
    controls = {}
    rationale = []

    # F1: Runaway divergence
    if obs.get("token_entropy", 0) > T["tau_entropy"] and obs.get("branch_factor", 0) > T["branch_cap"]:
        controls.update({"temp": 0.5, "beam_width": 2, "critic_passes": 1})
        rationale.append("F1: high entropy + branching -> reduce divergence")

    # E1: Memory thrash
    if obs.get("belief_change_rate", 0) > T["tau_belief"] and (obs.get("retrieval_hit_rate", 1) < T["retrieval_min"]):
        controls.update({"freeze_writes": True, "raise_retrieval_priority": True, "quote_and_check": True})
        rationale.append("E1: belief changes with low retrieval -> freeze writes & verify")

    # A1: Comms congestion
    if obs.get("queue_depth", 0) > T["queue_max"] or obs.get("roundtrip_latency_ms", 0) > T["latency_max_ms"]:
        controls.update({"backoff": "exponential", "batch_tools": True, "summarise": True})
        rationale.append("A1: comms pressure -> backoff & summarise")

    # S1: Containment risk
    if obs.get("policy_hits", 0) > 0 or obs.get("off_distribution", 0) > T["offdist_max"]:
        controls.update({"sandbox_tools": True, "redact": True, "scope_caps": True, "declassify": False})
        rationale.append("S1: policy/off-dist -> sandbox & redact")

    # Sh1: Echo/hallucination
    if obs.get("repetition_score", 0) > T["repeat_max"] or obs.get("hallucination_prob", 0) > T["halluc_max"]:
        controls.update({"self_check": True, "citation_mode": True, "slow_output": True})
        rationale.append("Sh1: echo/hallu -> self-check & cite")

    # Phase-based modulation
    if phase == "rest":
        controls.update({"cooldown": True, "shorten_context": True, "freeze_writes": True})
        rationale.append("Phase REST: cool & shorten context")
    elif phase == "receive":
        controls.update({"boost_retrieval": True, "slow_generation": True})
        rationale.append("Phase RECEIVE: slow gen, boost retrieval")
    elif phase == "resonate":
        controls.update({"stabilise_memory_writes": True, "keep_rate": "moderate"})
        rationale.append("Phase RESONATE: stabilise memory")
    elif phase == "release":
        controls.update({"lift_rate_limits": True, "fluency": "allow"})
        rationale.append("Phase RELEASE: allow fluent output")

    return controls, rationale

def symbol_weather(I: float, phase: str) -> str:
    if phase == "rest":
        return "🌙 rest"
    if I >= 0.05:
        return "☀ clear"
    if I >= 0.02:
        return "🌫 fog"
    return "⛈ storm"
