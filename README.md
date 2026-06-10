<!-- ============================================================
  PROFILE README for github.com/Mannava-Daasaradhi
  Setup: create a PUBLIC repo named exactly  Mannava-Daasaradhi
  and put this file in it as README.md — GitHub renders it on
  your profile page automatically.

  BEFORE COMMITTING — search this file for "FILL:" and resolve
  every one. Do NOT ship a placeholder (you did that on the
  resume once already).

  ALSO REQUIRED or this README is lipstick on a hidden profile:
  1. Settings → Public profile → make activity/contributions PUBLIC
  2. Add bio, location, email, website to profile sidebar
  3. Pin: MiniFlow-Serving · LLM_from_Scratch · S-XG-NID · tcp-stack
  4. Add a description to LLM_from_Scratch (currently blank)
  5. Fix the broken MiniFlow link in MiniFlow-Serving's README
  6. Reduce 30 public repos to ~8 (archive/private the rest)
============================================================ -->

# Hi, I'm Mannava Daasaradhi 👋

**ML researcher who also ships.** B.Tech in AI & Data Science (Class of 2028, CGPA 9.2) at Amrita Vishwa Vidyapeetham. I do applied ML research — explainable AI, multimodal fusion, graph learning — and I build the systems that serve models in production: APIs, drift detection, monitoring, all the way down to a TCP/IP stack in Rust.

🔭 **Currently:** contributing to LLM inference open source (vLLM), building an XAI faithfulness benchmark, and pushing my research to arXiv.
🌍 **Available:** remote work on full **US Eastern business hours** (my 6 PM–2 AM IST = 8:30 AM–4:30 PM ET).
📫 **Reach me:** daasaradhimannava@gmail.com · [LinkedIn](https://linkedin.com/in/mannava-daasaradhi) <!-- FILL: · [Google Scholar](LINK) · [Website](LINK) — add the day they're live -->

---

## 🔬 Research

My research spans applied ML across domains — the common thread is **models you can trust and explain**.

<!-- FILL: as each paper goes on arXiv or gets accepted, convert its row from
     "under review" to a real link. NEVER name the venue of an under-review
     paper publicly (double-blind policies); "under review, 2026" is enough. -->

| Work | Area | Status |
|---|---|---|
| Semantic intrusion detection — heterogeneous GNN over network flows + knowledge-graph reasoning + LLM-generated explanations | Graph ML · XAI · Security | <!-- FILL: arXiv link or "under review, 2026" --> |
| Multimodal semiconductor yield prediction — late fusion of 591 sensor features + 4096 wafer-map vision features | Multimodal · Manufacturing | <!-- FILL --> |
| Explainable AI methods <!-- FILL: one-line description of your XAI paper --> | XAI | <!-- FILL --> |
| <!-- FILL: add remaining papers (PINNs, SAR, seizure prediction, melanoma…) one row each --> | | |

> 📌 My contribution on every listed paper: lead author — problem formulation, method design, and all experiments. <!-- FILL: adjust per-paper if not true for all; never overclaim -->

---

## 🛠️ Featured Projects

### [MiniFlow → MiniFlow-Serving](https://github.com/Mannava-Daasaradhi/MiniFlow-Serving) — a deep-learning framework, then a serving layer for it
The full lifecycle in one project: I wrote a **reverse-mode autograd engine from scratch** (no PyTorch/TF — tensors, computational graph, backprop), trained models on it, then built the layer that serves them.

- **Serving:** FastAPI `/predict`, sticky **A/B testing** with a two-proportion z-test, **PSI-based drift detection** running in the background
- **Observability:** Prometheus metrics → Grafana dashboards, Docker Compose for the whole stack
- **Engineering:** 24 tests, 89% coverage; p99 latency 97 ms <!-- FILL: qualify this — "(local Docker, [CPU model], synthetic load of N rps)" — an unqualified latency number is noise -->
- **Why it matters:** most students train models; almost none have built both the framework *and* the monitoring that catches it degrading in production

### [LLM from Scratch](https://github.com/Mannava-Daasaradhi/LLM_from_Scratch) — a transformer LM, no shortcuts
Tokenizer → multi-head attention → positional encodings → training loop → sampling, all hand-built to own the internals. I can whiteboard attention, KV-caching, and why RoPE works — because I implemented them.
<!-- FILL: add the one number this README needs: model size, dataset, final loss/perplexity, hardware + training time. "Trained a 12M-param GPT on TinyStories to X.XX val loss on a single T4 in N hours" turns this from tutorial-tier into evidence. -->

### [S-XG-NID](https://github.com/Mannava-Daasaradhi/S-XG-NID) — intrusion detection that explains itself
Heterogeneous **graph neural network** over network flows (CICIDS dataset) with a knowledge-graph reasoning stage; every detection ships with an **LLM-generated human-readable explanation** of *why* it was flagged. Bridges my security, graph-ML, and XAI work.
<!-- FILL: headline metric vs a named baseline, e.g. "F1 0.XX vs 0.XX (XGBoost baseline) on CICIDS-2017" -->

### Userspace TCP/IP Stack (Rust) <!-- FILL: link — transfer the repo from the Kernalize account to this one FIRST -->
ARP, IPv4, ICMP, and TCP — congestion control, segment reassembly, RTT estimation — running in Linux userspace over a TUN device. Built to understand what every `model.predict()` HTTP call actually rides on.

### More
- **[FabMind](https://github.com/Mannava-Daasaradhi/FabMind-Semiconductor-AI)** — the research codebase behind the yield-prediction paper, with explainability tooling
- **[GlassBox-Attack](https://github.com/Mannava-Daasaradhi/GlassBox-Attack)** — adversarial attack/defense experiments; robustness evaluation of NN classifiers
- **[StudyMetrics](https://github.com/Mannava-Daasaradhi/StudyMetrics)** + Battleship — two Android apps in Kotlin; StudyMetrics is built as 18 CI-gated Gradle modules

---

## 🧰 What I work with

| | |
|---|---|
| **ML / DL** | PyTorch · NumPy · scikit-learn · transformers & attention internals · GNNs · adversarial ML · explainability (GradCAM/SHAP) |
| **Serving / MLOps** | FastAPI · Docker & Compose · Prometheus · Grafana · PSI drift detection · A/B test design · CI (GitHub Actions) |
| **Languages** | Python · Rust · Kotlin · C++ · SQL · Bash |
| **Systems** | Linux · TCP/IP (implemented one) · Android |

---

## 📊 Activity

<!-- These widgets render real data ONLY after you make your activity public (setup step 1).
     With activity private they show an empty profile — worse than nothing. -->
<p>
  <img src="https://github-readme-stats.vercel.app/api?username=Mannava-Daasaradhi&show_icons=true&hide_rank=true&theme=default" height="160" alt="GitHub stats"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Mannava-Daasaradhi&layout=compact&hide=html,css" height="160" alt="Top languages"/>
</p>

---

## 🤝 Open to

- **Research internships** (Summer 2027) — XAI, multimodal learning, graph ML, LLM systems
- **Remote part-time / contract ML engineering** on US hours — model serving, evaluation harnesses, inference infra
- **Collaboration** on open-source LLM inference (vLLM ecosystem) and XAI benchmarking

*Fastest way to evaluate me: open [MiniFlow-Serving](https://github.com/Mannava-Daasaradhi/MiniFlow-Serving), run `docker compose up`, and hit `/predict`.* <!-- FILL: verify this literally works from a fresh clone before publishing this sentence. If it doesn't, fix the repo, not the sentence. -->
