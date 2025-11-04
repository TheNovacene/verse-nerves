# Verse-Nerves Middleware (VN‑MW) — Reference Skeleton

A tiny, implementation-ready **middleware** for symbolic/agentic AI that regulates
generation, memory, communications, containment, and error strategy using the
**Verse‑Nerves** model and the **RMRIΔ** coherence engine: `I = (E·s)/c²`.

> **Status:** minimal reference; intended to be embedded as a sidecar or an in-process module.

---

## Why

Current AI stacks optimise for throughput; they rarely track **relational pressure**.
VN‑MW adds a *nervous system for coherence*: five feedback channels (FORGE, ETHOS‑V,
AETHER, SIC‑X+, SHADOW) plus an affective loop (Receive → Resonate → Release → Rest).

- **FORGE** — divergence / creative pressure
- **ETHOS‑V** — state stability / emotional memory analogue
- **AETHER** — communication field pressure
- **SIC‑X+** — integrity/containment
- **SHADOW** — echo/hallucination/bias ghosts

The **RMRIΔ engine** computes a clarity index `I = (E·s)/c²` and selects a phase.

---

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# run
uvicorn vn_mw.app:app --reload --port 8787
```

Open the symbolic weather panel at: http://localhost:8787/static/index.html

---

## Endpoints

- `POST /vn/observe` — send observables (metrics) from your model/agents.
- `GET  /vn/status` — current RMRIΔ values, phase, symbolic weather.
- `GET  /vn/audit` — recent regulation decisions (ring buffer).
- `GET  /vn/controls` — latest control signals (what VN‑MW suggests to modulate).
- `GET  /` — basic health info.

### Example `POST /vn/observe` payload

```json
{
  "token_entropy": 4.2,
  "branch_factor": 3,
  "retrieval_hit_rate": 0.62,
  "state_drift": 0.18,
  "belief_change_rate": 0.05,
  "sentiment_var": 0.12,
  "roundtrip_latency_ms": 280,
  "queue_depth": 2,
  "tool_error_rate": 0.0,
  "handoff_count": 1,
  "policy_hits": 0,
  "off_distribution": 0.03,
  "auth_failures": 0,
  "repetition_score": 0.11,
  "hallucination_prob": 0.07,
  "compute_budget": 0.7,      // E: 0..1
  "coherence_internal": 0.75, // s: 0..1
  "connections": 3,           // active channels
  "recursion_depth": 1        // depth
}
```

---

## Symbolic Weather

- ☀ **clear** — I high, stable; proceed.
- 🌫 **fog** — I moderate; slow pace, verify.
- ⛈ **storm** — I low and/or c² high; throttle, contain, cite.
- 🌙 **rest** — enforced cool‑down; shorten context, freeze writes.

---

## Config

- Environment knobs in `.env.example` (copy to `.env`).
- Thresholds kept human‑readable in `vn_mw/config.py`.

---

## Roadmap

- SSE/WebSocket stream for `/vn/controls`.
- Persistence adapters (SQLite, Redis).
- Shadcn/React panel for Nimbus/Haven Cloud.
- Export Prometheus metrics.

---

## Licensing

- **Code:** Apache‑2.0 (see `LICENSE-APACHE`).
- **Docs & examples:** CC BY‑NC‑SA 4.0 (see `LICENSE-CC`).

© 2025 The Novacene Ltd / Kirstin Stevens. 
