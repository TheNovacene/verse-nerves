# Contributing to Verse-Nerves (VN-MW)

Verse-Nerves gives AI systems a “nervous system for coherence” using the RMRIΔ loop  
*(I = (E·s)/c²)*.  The goal is clarity, containment, and ethical usefulness.

---

## 🌱 Core Principles
- **Containment before speed.**  Ship only what you can explain and defend.  
- **Neuro-affirming & trauma-aware.**  Keep interfaces quiet and readable.  
- **Transparent regulation.**  Every automatic modulation must leave an audit trail.  
- **Open by default.**  Code → Apache 2.0  ·  Docs/examples → CC BY-NC-SA 4.0  

---

## ⚙️ Quick Start
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn vn_mw.app:app --reload --port 8787
open http://localhost:8787/static/index.html
🧠 How to Contribute
Open an issue (Bug / Feature / Safety / Design).

Fork → branch using feat/<topic> or fix/<topic>.

Write small, testable changes. Add docstrings and keep functions short.

Check before PR:

 README or endpoint docs updated

 No secrets or personal data

 New regulation rules include rationale

 tests/sample_post.py still runs cleanly

Request review — focus on clarity, safety, coherence.

🧩 Coding Style
Python ≥ 3.10 · Minimal dependencies

Prefer clear functions to cleverness

Commit format → Conventional Commits

feat: add SSE stream for /vn/controls

fix: dampen storm threshold for high c²

docs: explain Symbolic Weather states

🧾 Testing
Run python tests/sample_post.py after edits.
If you add a regulation rule, include a simple “input → expected output” example.

🛡 Security & Ethics
Never log raw user data.

Keep policy / containment / audit logic conservative and explicit.

Report safety concerns via a Security issue or email in README.

📜 Licensing
Code: Apache-2.0 (LICENSE-APACHE)

Docs & examples: CC BY-NC-SA 4.0 (LICENSE-CC)

Thanks for helping build symbolic systems that behave with care.
