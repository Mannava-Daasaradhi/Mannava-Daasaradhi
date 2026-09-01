<div align="center">

<img src="./ascii.svg" width="460" alt="A hooded figure in a mask, drawn in ASCII"/>

<img src="./stats.svg" width="620" alt="Contributions in the last year"/>

[linkedin](https://linkedin.com/in/mannava-daasaradhi) &nbsp;·&nbsp;
[email](mailto:daasaradhimannava@gmail.com)

</div>

<img src="./hd-about.svg" width="620" alt="about"/>

> I build the systems that make ML and LLMs run in production.<br>
> B.Tech in AI &amp; Data Science, Amrita Vishwa Vidyapeetham, 2024–2028 · CGPA 9.2.

That means the whole column, not one layer of it: the MLOps primitives underneath<br>
a platform, the serving stack that exposes a model with A/B testing and drift<br>
alerts on top of it, and — because it all eventually rides on somebody else's<br>
abstraction — a Raft consensus store in Go and a userspace TCP/IP stack in Rust,<br>
written to find out what that abstraction actually does.

First-author applied-ML research under review, in multimodal sensor-vision fusion<br>
and graph-based intrusion detection.

Open to remote internships · IST, and I work the US-hours overlap.

<img src="./hd-projects.svg" width="620" alt="projects"/>

**[MiniFlow-Serving](https://github.com/Mannava-Daasaradhi/MiniFlow-Serving)** &nbsp;·&nbsp; <samp>python, fastapi, docker</samp><br>
A model-serving stack: FastAPI `/predict` with sticky A/B assignment, PSI drift<br>
detection on a background loop, Prometheus into Grafana, the whole thing up under<br>
Docker Compose. The A/B arm is decided by a two-proportion z-test — B won at<br>
p=0.012, +34% lift. p99 97 ms end-to-end under `hey`; 89% test coverage.

**[MiniFlow](https://github.com/Mannava-Daasaradhi/MiniFlow)** &nbsp;·&nbsp; <samp>python</samp><br>
The three primitives every ML platform is built on, reimplemented with zero<br>
dependencies: an `ExperimentTracker` (SQLite-backed run logging and comparison), a<br>
`ModelRegistry` (versioned save/load with metadata), and a `FeatureStore` (schema'd,<br>
versioned, entity-keyed). 24 tests, 82% coverage. The point was to understand<br>
MLflow, W&amp;B and Feast by rebuilding them.

**[Distributed Raft KV](https://github.com/Mannava-Daasaradhi/Distributed_Raft_KV)** &nbsp;·&nbsp; <samp>go</samp><br>
Raft consensus behind a linearizable KV store: leader election, log replication,<br>
snapshotting and log compaction, disk persistence with crash recovery, a<br>
consistent-hashing ring, and a five-node Docker Compose cluster. `kill -9` the<br>
leader and a new one is elected in under 700 ms with committed data intact. CI runs<br>
vet, build and `test -race`; 76% coverage on the consensus core.

**[tcp-stack](https://github.com/Mannava-Daasaradhi/tcp-stack)** &nbsp;·&nbsp; <samp>rust</samp><br>
A userspace TCP/IP stack over a TUN device — ARP, IPv4, ICMP, UDP and TCP, with<br>
CUBIC and BBR congestion control, segment reassembly and RTT estimation on a<br>
non-blocking event loop. Designed to interoperate with the standard Linux userspace<br>
tools. 153 tests.

**[LLM from Scratch](https://github.com/Mannava-Daasaradhi/LLM_from_Scratch)** &nbsp;·&nbsp; <samp>python, pytorch</samp><br>
A transformer language model end to end — BPE tokenizer, multi-head attention,<br>
RoPE, the full training loop — trained on a Shakespeare corpus. Built to own the<br>
internals rather than import them.

**[StudyMetrics](https://github.com/Mannava-Daasaradhi/StudyMetrics)** &nbsp;·&nbsp; <samp>kotlin, android</samp><br>
A shipped Android app built as 18 CI-gated Gradle modules, because one module is a<br>
script and eighteen is an architecture. [Battleship](https://github.com/Mannava-Daasaradhi/Battleship_android) shipped alongside it.

<img src="./hd-research.svg" width="620" alt="research"/>

**[S-XG-NID](https://github.com/Mannava-Daasaradhi/S-XG-NID)** &nbsp;·&nbsp; <samp>graph ml, xai, security</samp><br>
A heterogeneous GNN over network flows (CICIDS) with a knowledge-graph reasoning<br>
stage, so every detection carries an LLM-written explanation of why it fired.<br>
First author. Manuscript under review.

**[FabMind](https://github.com/Mannava-Daasaradhi/FabMind-Semiconductor-AI)** &nbsp;·&nbsp; <samp>multimodal, manufacturing</samp><br>
Semiconductor yield prediction by late fusion of IoT sensor time-series with<br>
wafer-map vision — 591 sensor features against 4096 image features — with the<br>
explainability tooling to go with it. First author. Manuscript under review.

<img src="./hd-stack.svg" width="620" alt="stack"/>

<samp>python &nbsp; go &nbsp; rust &nbsp; kotlin &nbsp; c++ &nbsp; sql &nbsp; pytorch &nbsp; scikit-learn &nbsp; fastapi &nbsp; docker &nbsp; prometheus &nbsp; grafana &nbsp; linux</samp>

<samp>transformers &nbsp; gnns &nbsp; lora/peft &nbsp; explainable &amp; adversarial ml &nbsp; model serving &nbsp; psi drift detection &nbsp; a/b testing &nbsp; raft &nbsp; tcp/ip &nbsp; github actions</samp>

<img src="./hd-stats.svg" width="620" alt="stats"/>

<div align="center">

<img src="./streak.svg" width="620" alt="Current and longest streak"/>

<img src="./langs.svg" width="620" alt="Top languages by bytes and by repo"/>

<img src="./year.svg" width="620" alt="The last year, one character per day"/>

</div>

<img src="./hd-about-this-page.svg" width="620" alt="about this page"/>

Every graphic here is generated, not embedded from anyone else's server.<br>
`ascii.svg` is a photograph pushed through a thirteen-character ramp by<br>
[`scripts/make_hacker.py`](scripts/make_hacker.py) — the hood is lit against black,<br>
so brightness is the ink and the backdrop falls away to blank paper. The shadow<br>
inside the hood had to be drawn rather than traced: those pixels read exactly zero,<br>
identical to the backdrop, so the script separates them by topology instead of by<br>
tone — flood the darkness in from the border, and whatever it cannot reach is the<br>
inside of the hood. The stat graphics and these section headings are drawn by<br>
[a scheduled action](.github/workflows/stats.yml) straight from the GitHub GraphQL<br>
API, once a day, committing only what changed.

They animate with SMIL inside the SVG, because GitHub strips scripts from<br>
READMEs — and since nothing loads from a third party, nothing here can<br>
rate-limit or go dark. The headings are SVGs for the same reason: GitHub also<br>
strips CSS, so an image is the only way to put this page's own typeface on them.

The typeface is [JetBrains Mono](scripts/fonts), subset to just the characters<br>
each graphic draws and inlined as base64. That isn't only for looks: the<br>
portrait's grid assumes an advance width of exactly 0.600 em, and a viewer whose<br>
default monospace is narrower would otherwise see it squeezed.

Language totals cover public repositories only. `year.svg` uses the portrait's<br>
character ramp: `:` `+` `#` `@`, quiet to loud.
