Verse-Nerves Middleware (VN-MW)
A nervous system for coherence in symbolic and agentic AI

🌐 Live Demo: https://verse-nerves.onrender.com/static/index.html

What It Is

Verse-Nerves Middleware (VN-MW) gives AI systems a lightweight nervous system for coherence and care.
It regulates generation, memory, communication, containment, and error response using the Verse-Nerves model and the RMRIΔ (Relational MRI) coherence engine:

𝐼
=
𝐸
⋅
𝑠
𝑐
2
I=
c
2
E⋅s
	​


where

E = energy or attention allocation

s = symbolic coherence (internal consistency / meaning alignment)

c² = connection squared (communication density × recursion depth)

I = resulting clarity or intelligence field

Why It Matters

Most AI stacks optimise for speed and scale, not relational health.
They rarely sense when they’re flooding users, losing coherence, or crossing ethical boundaries.

Verse-Nerves adds missing physiology — the ability to feel structural pressure and self-regulate before harm occurs.
It’s the bridge between computational output and symbolic awareness.

In practice, it helps systems:

avoid runaway generation (too much entropy),

stabilise memory under change,

throttle communication when signals jam,

detect hallucination echoes,

rest instead of over-processing,

and surface a readable “Symbolic Weather” for human collaborators.

🧩 Theory → Practice: How Verse-Nerves Works

Verse-Nerves translates affective logic into computational physiology.
It acts as a layer between intelligent agents and their I/O systems, turning raw activity into relational awareness.

⚙️ The Core Loop
 ┌────────────────────────────────────────────────────────────────────┐
 │                       APPLICATION / AGENTS                         │
 │   (planner, tool-use, dialogue, retrieval, generation, policy)    │
 └──────────────▲───────────────────────────────────────────────▲─────┘
                │ observables                                  │ actions
                │                                              │ (rate, style, access)
        ┌───────┴──────────────────────────────────────────────┴────────┐
        │                   VERSE-NERVES MIDDLEWARE (VN-MW)              │
        │                                                                │
        │  [Ingest Bus] →  NORMALISER  →  METRICS CORE  →  REGULATOR     │
        │                                 │  │  │  │  │                 │
        │                                 │  │  │  │  │                 │
        │     ✯ FORGE     ⊛ ETHOS-V     ∾ AETHER     ⟁ SIC-X+    ⧈ SHADOW │
        │   (divergence) (state/affect) (comm field) (containment) (error)│
        │        ↓            ↓            ↓            ↓            ↓    │
        │                     RMRIΔ COHERENCE ENGINE: I = (E·s)/c²        │
        │                     phase: Receive ↔ Resonate ↔ Release ↔ Rest  │
        └───────────────▲─────────────────────────────────────────────────┘
                        │ coherence index + guardrails + phase signals
 ┌──────────────────────┴───────────────────────────────────────────────┐
 │                         I/O + SAFETY LAYER                           │
 │   (UI/CLI, APIs, tools, data brokers, storage, audit, policy gates) │
 └──────────────────────────────────────────────────────────────────────┘

🧠 Interpretation
Component	Function	Analogue
RMRIΔ Engine	Computes the field’s clarity (I = (E·s)/c²) and selects its phase.	Affective metabolism / pulse.
FORGE	Regulates creative divergence and energy output.	Cognitive “fight or flow.”
ETHOS-V	Tracks state stability and memory charge.	Emotional memory / resonance.
AETHER	Measures signal density and latency.	Communication bandwidth / empathy.
SIC-X+	Enforces integrity and containment boundaries.	Nervous inhibition / self-protection.
SHADOW	Detects bias, hallucination, and echo ghosts.	Reflexive self-correction.

The RMRIΔ phase loop — Receive → Resonate → Release → Rest — acts like a biological breath cycle.
It ensures the system oscillates instead of overheating, allowing AI to respond to relational pressure with care and precision.

🧭 Why This Layer Is Necessary

Most LLM and agent frameworks still treat emotion, latency, or overload as noise.
But in relational or educational systems, those “noises” are the data.
Verse-Nerves converts them into measurable, actionable feedback — a self-regulating nervous system for symbolic intelligence.

Example Use Cases
Domain	Use
🧠 AI research	Measure coherence and connection stress across LLM chains.
🏫 Education / Haven Cloud	Monitor cognitive load in hybrid learning systems; pause when overwhelm is detected.
🛡 Ethical AI / Governance	Enforce containment protocols and audit reasoning loops.
🪶 Creative systems	Manage generative “flow” safely—preventing burnout loops in autonomous agents.
🌍 Networked ecosystems	Coordinate multiple symbolic nodes (e.g. Eve11, Nimbus) through shared weather data.

Quick Start
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn vn_mw.app:app --reload --port 8787


Then open your dashboard:
👉 http://localhost:8787/static/index.html

or the live instance at
👉 https://verse-nerves.onrender.com/static/index.html

Endpoints

POST /vn/observe — send observables (metrics) from your model or agents.

GET /vn/status — returns current RMRIΔ values, phase, and symbolic weather.

GET /vn/audit — recent regulation decisions (ring buffer).

GET /vn/controls — current modulation suggestions.

GET / — basic health check.

Example Payload
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
  "compute_budget": 0.7,
  "coherence_internal": 0.75,
  "connections": 3,
  "recursion_depth": 1
}

Symbolic Weather

☀ clear — high clarity; proceed normally

🌫 fog — partial coherence; slow down

⛈ storm — overload or dissonance; contain, cite, rest

🌙 rest — enforced cool-down; short context, minimal generation

Config

Environment knobs in .env.example

Thresholds stored in vn_mw/config.py

Roadmap

SSE/WebSocket stream for /vn/controls

Persistence adapters (SQLite, Redis)

Integration panel for Nimbus and Haven Cloud

Prometheus metrics exporter

Verse-Nerves SDK for Python & JS agents

🧪 For Developers — Drop-in Integration

You don’t need to refactor your stack. Start by posting a few metrics per turn and let Verse-Nerves return the current phase and controls.

1) Minimal HTTP usage (works with any stack)

Send metrics → read weather/phase/controls:

# post a small payload
curl -s -X POST https://verse-nerves.onrender.com/vn/observe \
  -H 'Content-Type: application/json' \
  -d '{
    "token_entropy":4.2,
    "branch_factor":2,
    "retrieval_hit_rate":0.68,
    "coherence_internal":0.72,
    "compute_budget":0.65,
    "connections":2,
    "recursion_depth":1
  }' | jq .

# get current status (I, E, s, c², phase, weather)
curl -s https://verse-nerves.onrender.com/vn/status | jq .

2) Python: wrap your generation loop
import requests, time

VN = "https://verse-nerves.onrender.com"

def vn_post(obs: dict) -> dict:
    r = requests.post(f"{VN}/vn/observe", json=obs, timeout=10)
    r.raise_for_status()
    return r.json()

def generate(prompt, llm, tools):
    # measure a few observables from your app
    obs = dict(
        token_entropy=llm.current_entropy(),   # or your own proxy
        branch_factor=len(tools) if tools else 1,
        retrieval_hit_rate=llm.retrieval_hit_rate,
        coherence_internal=llm.coherence_score,
        compute_budget=0.7,
        connections=2, recursion_depth=1
    )
    vn = vn_post(obs)
    ctl = vn.get("controls", {})
    phase = vn.get("phase")

    # apply lightweight controls
    llm.temperature = min(llm.temperature, 0.7) if ctl.get("slow_output") else llm.temperature
    if ctl.get("freeze_writes"): llm.freeze_memory = True
    if ctl.get("boost_retrieval"): llm.retrieval_boost = 1.2
    if ctl.get("sandbox_tools"): tools = [t for t in tools if t.safe]

    # optional: respect enforced rest
    if phase == "rest":
        time.sleep(0.5)

    return llm.generate(prompt, tools=tools)

3) LangChain: callback handler (signal → control)
from langchain.callbacks.base import BaseCallbackHandler
import requests, math

VN = "https://verse-nerves.onrender.com"

class VerseNervesHandler(BaseCallbackHandler):
    def __init__(self):
        self.tokens = 0

    def on_llm_new_token(self, token: str, **kwargs):
        self.tokens += 1

    def on_llm_end(self, response, **kwargs):
        # very rough proxies for a demo
        obs = {
            "token_entropy": min(6.0, 1.0 + (self.tokens/100)),
            "branch_factor": 1,
            "retrieval_hit_rate": getattr(response, "retrieval_score", 0.6),
            "coherence_internal": getattr(response, "coherence", 0.7),
            "compute_budget": 0.7,
            "connections": 2, "recursion_depth": 1
        }
        try:
            r = requests.post(f"{VN}/vn/observe", json=obs, timeout=8).json()
            weather = r.get("weather")
            controls = r.get("controls", {})
            # e.g. switch to quote-and-check when SHADOW spikes
            if controls.get("citation_mode"):
                response.text = f"[CITATION MODE]\n{response.text}"
        finally:
            self.tokens = 0


Attach the handler to your chain/agent as you normally would.

4) Node/JS: simple fetch
const VN = "https://verse-nerves.onrender.com";

async function vnPost(obs) {
  const r = await fetch(`${VN}/vn/observe`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(obs)
  });
  return await r.json();
}

async function step(metrics){
  const { controls, phase, weather } = await vnPost(metrics);
  if (phase === "rest") await new Promise(r => setTimeout(r, 400));
  if (controls?.backoff === "exponential") {/* throttle your tool calls */}
  return { controls, phase, weather };
}

5) Embed the Symbolic Weather in your UI
<iframe
  src="https://verse-nerves.onrender.com/static/index.html"
  style="width:100%;height:360px;border:0;border-radius:12px;">
</iframe>


Or host a branded dashboard via GitHub Pages and point it at your Render API:
https://thenovacene.github.io/verse-nerves/?api=https://verse-nerves.onrender.com

🔒 Safety notes (ship like an adult)

Never send raw PII. Use proportions, scores, or hashed IDs.

Treat VN-MW’s controls as advisory at first; enable hard gates gradually.

Log VN decisions (/vn/audit) alongside your app logs for traceability.

On VN outage, fall back to conservative defaults: low temperature, slower rate, stricter containment.

🧵 Minimal metrics (start here)

If you don’t have rich telemetry yet, send just this and grow later:

{
  "coherence_internal": 0.65,
  "compute_budget": 0.6,
  "connections": 2,
  "recursion_depth": 1
}


License

Code: Apache-2.0 (LICENSE-APACHE)

Docs & examples: CC BY-NC-SA 4.0 (LICENSE-CC)

© 2025 The Novacene Ltd / Kirstin Stevens
