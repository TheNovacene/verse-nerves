from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Dict, Any, List, Deque
from collections import deque
import math, time

from .config import THRESHOLDS
from .core import compute_rmri_delta, classify_phase, regulate, symbol_weather

app = FastAPI(title="Verse-Nerves Middleware (VN-MW)", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

# ring buffers
AUDIT: Deque[Dict[str, Any]] = deque(maxlen=256)
LAST_CONTROLS: Dict[str, Any] = {}
STATE: Dict[str, Any] = {
    "rmri": {},
    "phase": "rest",
    "weather": "🌙 rest",
    "last_obs": {},
    "ts": time.time(),
}

class Observables(BaseModel):
    token_entropy: float | None = None
    branch_factor: int | None = None
    retrieval_hit_rate: float | None = None
    state_drift: float | None = None
    belief_change_rate: float | None = None
    sentiment_var: float | None = None
    roundtrip_latency_ms: int | None = None
    queue_depth: int | None = None
    tool_error_rate: float | None = None
    handoff_count: int | None = None
    policy_hits: int | None = None
    off_distribution: float | None = None
    auth_failures: int | None = None
    repetition_score: float | None = None
    hallucination_prob: float | None = None
    compute_budget: float | None = None     # E (0..1)
    coherence_internal: float | None = None # s (0..1)
    connections: int | None = None
    recursion_depth: int | None = None

@app.get("/")
def root():
    return {"ok": True, "service": "VN-MW", "version": "0.1.0"}

@app.post("/vn/observe")
def observe(obs: Observables):
    payload = obs.dict(exclude_none=True)
    # Basic normalisation / defaults
    E = float(payload.get("compute_budget", 0.5))
    s = float(payload.get("coherence_internal", 0.5))
    connections = max(1, int(payload.get("connections", 1)))
    depth = max(1, int(payload.get("recursion_depth", 1)))
    c2 = float(connections * depth) ** 2

    rmri = compute_rmri_delta(E=E, s=s, c2=c2)
    phase = classify_phase(E=E, s=s, c2=c2, I=rmri["I"])
    controls, rationale = regulate(payload, rmri, phase, THRESHOLDS)
    weather = symbol_weather(rmri["I"], phase)

    STATE["rmri"] = rmri
    STATE["phase"] = phase
    STATE["weather"] = weather
    STATE["last_obs"] = payload
    STATE["ts"] = time.time()

    global LAST_CONTROLS
    LAST_CONTROLS = {"controls": controls, "phase": phase, "weather": weather, "ts": STATE["ts"]}

    AUDIT.append({
        "ts": STATE["ts"],
        "obs": payload,
        "rmri": rmri,
        "phase": phase,
        "controls": controls,
        "rationale": rationale
    })
    return {"ok": True, "phase": phase, "rmri": rmri, "weather": weather, "controls": controls}

@app.get("/vn/status")
def status():
    return {"ok": True, **STATE}

@app.get("/vn/audit")
def audit(limit: int = 50):
    items = list(AUDIT)[-limit:]
    return {"ok": True, "audit": items}

@app.get("/vn/controls")
def controls():
    return {"ok": True, **LAST_CONTROLS}
