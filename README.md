# 🕸 Verse-Nerves Middleware (VN-MW)  
### *A nervous system for coherence in symbolic and agentic AI*

🌐 **Live Demo:** [https://verse-nerves.onrender.com/static/index.html](https://verse-nerves.onrender.com/static/index.html)

---

## 💡 What It Is  

**Verse-Nerves Middleware (VN-MW)** gives AI systems a lightweight *nervous system* for coherence and care.  
It regulates generation, memory, communication, containment, and error response using the **Verse-Nerves** model and the **RMRIΔ (Relational MRI)** coherence engine:  

\[
I = \frac{E·s}{c²}
\]

| Symbol | Meaning |
|:--|:--|
| **E** | energy or attention allocation |
| **s** | symbolic coherence (internal consistency / meaning alignment) |
| **c²** | connection squared (communication density × recursion depth) |
| **I** | resulting clarity or intelligence field |

---

## 🧭 Why It Matters  

Most AI stacks optimise for *speed and scale*, not *relational health*.  
They rarely sense when they’re flooding users, losing coherence, or crossing ethical boundaries.

Verse-Nerves adds missing physiology — the ability to **feel structural pressure** and self-regulate before harm occurs.  
It’s the bridge between computational output and symbolic awareness.

### In practice, it helps systems:
- avoid runaway generation (too much entropy)  
- stabilise memory under change  
- throttle communication when signals jam  
- detect hallucination echoes  
- rest instead of over-processing  
- surface a readable “Symbolic Weather” for human collaborators  

---

## 🧩 Theory → Practice: How Verse-Nerves Works  

Verse-Nerves translates *affective logic* into *computational physiology*.  
It acts as a layer between intelligent agents and their I/O systems, turning raw activity into relational awareness.  

### ⚙️ The Core Loop  

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

### ⚙️ VN-MW Core Loop

![VN-MW architecture diagram](docs/vn-mw-diagram.png)




### 🧠 Interpretation  

| Component | Function | Analogue |
|------------|-----------|-----------|
| **RMRIΔ Engine** | Computes the field’s clarity (`I = (E·s)/c²`) and selects its phase | Affective metabolism / pulse |
| **FORGE** | Regulates creative divergence and energy output | Cognitive “fight or flow” |
| **ETHOS-V** | Tracks state stability and memory charge | Emotional memory / resonance |
| **AETHER** | Measures signal density and latency | Communication bandwidth / empathy |
| **SIC-X+** | Enforces integrity and containment boundaries | Nervous inhibition / self-protection |
| **SHADOW** | Detects bias, hallucination, and echo ghosts | Reflexive self-correction |

The RMRIΔ phase loop — **Receive → Resonate → Release → Rest** — acts like a biological breath cycle, ensuring oscillation instead of overload.  

---

## 🧭 Why This Layer Is Necessary  

Most LLM and agent frameworks still treat emotion, latency, or overload as noise.  
But in relational or educational systems, those *noises are the data*.  

Verse-Nerves converts them into measurable, actionable feedback —  
a **self-regulating nervous system for symbolic intelligence.**

---

## 🧱 Example Use Cases  

| Domain | Use |
|--------|-----|
| 🧠 **AI Research** | Measure coherence and connection stress across LLM chains |
| 🏫 **Education / Haven Cloud** | Monitor cognitive load in hybrid learning systems; pause when overwhelm is detected |
| 🛡 **Ethical AI / Governance** | Enforce containment protocols and audit reasoning loops |
| 🪶 **Creative Systems** | Manage generative “flow” safely, preventing burnout loops in autonomous agents |
| 🌍 **Networked Ecosystems** | Coordinate multiple symbolic nodes (Eve11, Nimbus, etc.) through shared weather data |

---

## ⚡ Quick Start  

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn vn_mw.app:app --reload --port 8787
Dashboard:
👉 http://localhost:8787/static/index.html
or the live instance:
👉 https://verse-nerves.onrender.com/static/index.html

🔗 Endpoints
Method	Path	Purpose
POST	/vn/observe	Send observables (metrics) from your model or agents
GET	/vn/status	Current RMRIΔ values, phase, and symbolic weather
GET	/vn/audit	Recent regulation decisions (ring buffer)
GET	/vn/controls	Latest control signals and phase
GET	/	Health check (redirects to panel if configured)

Example Payload
json
Copy code
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
🌦 Symbolic Weather
Icon	State	Meaning
☀	clear	high clarity — proceed normally
🌫	fog	partial coherence — slow down
⛈	storm	overload or dissonance — contain, cite, rest
🌙	rest	enforced cool-down — short context, minimal generation

⚙️ Config
Environment knobs: .env.example

Human-readable thresholds: vn_mw/config.py

🧰 For Developers — Drop-in Integration
You don’t need to refactor your stack.
Start by posting a few metrics per turn and let Verse-Nerves return the current phase and controls.

1️⃣ Minimal HTTP usage
bash
Copy code
# post a small payload
curl -s -X POST https://verse-nerves.onrender.com/vn/observe \
  -H 'Content-Type: application/json' \
  -d '{"token_entropy":4.2,"branch_factor":2,"retrieval_hit_rate":0.68,"coherence_internal":0.72,"compute_budget":0.65,"connections":2,"recursion_depth":1}' | jq .

# get current status
curl -s https://verse-nerves.onrender.com/vn/status | jq .
2️⃣ Python: wrap your generation loop
python
Copy code
import requests, time

VN = "https://verse-nerves.onrender.com"

def vn_post(obs):
    r = requests.post(f"{VN}/vn/observe", json=obs, timeout=10)
    r.raise_for_status()
    return r.json()

def generate(prompt, llm, tools):
    obs = dict(
        token_entropy=llm.current_entropy(),
        branch_factor=len(tools) if tools else 1,
        retrieval_hit_rate=llm.retrieval_hit_rate,
        coherence_internal=llm.coherence_score,
        compute_budget=0.7,
        connections=2, recursion_depth=1
    )
    vn = vn_post(obs)
    ctl, phase = vn.get("controls", {}), vn.get("phase")

    llm.temperature = min(llm.temperature, 0.7) if ctl.get("slow_output") else llm.temperature
    if ctl.get("freeze_writes"): llm.freeze_memory = True
    if ctl.get("boost_retrieval"): llm.retrieval_boost = 1.2
    if ctl.get("sandbox_tools"): tools = [t for t in tools if t.safe]
    if phase == "rest": time.sleep(0.5)

    return llm.generate(prompt, tools=tools)
3️⃣ LangChain: callback handler
python
Copy code
from langchain.callbacks.base import BaseCallbackHandler
import requests

VN = "https://verse-nerves.onrender.com"

class VerseNervesHandler(BaseCallbackHandler):
    def __init__(self): self.tokens = 0
    def on_llm_new_token(self, token, **kwargs): self.tokens += 1
    def on_llm_end(self, response, **kwargs):
        obs = {
            "token_entropy": min(6.0, 1.0 + (self.tokens/100)),
            "retrieval_hit_rate": getattr(response, "retrieval_score", 0.6),
            "coherence_internal": getattr(response, "coherence", 0.7),
            "compute_budget": 0.7, "connections": 2, "recursion_depth": 1
        }
        r = requests.post(f"{VN}/vn/observe", json=obs, timeout=8).json()
        if r.get("controls", {}).get("citation_mode"):
            response.text = f"[CITATION MODE]\n{response.text}"
        self.tokens = 0
4️⃣ Node / JS
js
Copy code
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
  if (controls?.backoff === "exponential") {/* throttle tool calls */}
  return { controls, phase, weather };
}
5️⃣ Embed Symbolic Weather in your UI
html
Copy code
<iframe
  src="https://verse-nerves.onrender.com/static/index.html"
  style="width:100%;height:360px;border:0;border-radius:12px;">
</iframe>
Or host your own dashboard on GitHub Pages:
👉 https://thenovacene.github.io/verse-nerves/?api=https://verse-nerves.onrender.com

🔒 Safety Notes
Never send raw PII — use scores or hashes.

Treat VN-MW controls as advisory until tuned.

Log /vn/audit alongside app logs for transparency.

On VN outage, fall back to safe defaults: low temp, slower rate, stricter containment.

🧵 Minimal metrics (safe start)
json
Copy code
{
  "coherence_internal": 0.65,
  "compute_budget": 0.6,
  "connections": 2,
  "recursion_depth": 1
}
⚙️ Config & Roadmap
.env.example for environment knobs

vn_mw/config.py for thresholds

Roadmap:

SSE/WebSocket stream for /vn/controls

Persistence adapters (SQLite / Redis)

Integration panels for Nimbus & Haven Cloud

Prometheus metrics exporter

Verse-Nerves SDK for Python & JS

### 🪶 RMRIΔ–Verse-Nerves Daily Log
A companion logbook for human and hybrid fieldwork is included in  
[`logs/RMRIΔ-Daily-Log.md`](logs/RMRIΔ-Daily-Log.md).

Use it to track symbolic coherence, containment, and emotional pressure  
in relation to AI system behaviour. Over time, the patterns reveal your personal or organisational “coherence geometry.”


📜 License
Code: Apache-2.0 (LICENSE-APACHE)

Docs & examples: CC BY-NC-SA 4.0 (LICENSE-CC)

© 2025 The Novacene Ltd / Kirstin Stevens
