<div align="center">

<img src="./ascii.svg" width="460" alt="A hooded figure in a mask, drawn in ASCII"/>

<img src="./stats.svg" width="620" alt="Contributions in the last year"/>

[linkedin](https://linkedin.com/in/mannava-daasaradhi) &nbsp;·&nbsp;
[email](mailto:daasaradhimannava@gmail.com)

</div>

<img src="./hd-about.svg" width="620" alt="about"/>

> B.Tech in AI &amp; Data Science at Amrita Vishwa Vidyapeetham, class of 2028.<br>
> Models you can explain, and the systems that serve them.

Most of my work sits on both sides of that line: applied ML research — explainable<br>
AI, multimodal fusion, graph learning — and the infrastructure it has to survive in,<br>
from serving APIs and drift detection down to a TCP/IP stack in Rust. Right now<br>
that's the stack: ARP, IPv4, ICMP and TCP in Linux userspace over a TUN device,<br>
written to understand what every `model.predict()` call actually rides on.

Open to research internships and to remote ML engineering on US Eastern hours —<br>
my 6 PM–2 AM IST is 8:30 AM–4:30 PM ET.

<img src="./hd-research.svg" width="620" alt="research"/>

**Semantic intrusion detection** &nbsp;·&nbsp; <samp>graph ml, xai, security</samp><br>
A heterogeneous GNN over network flows, a knowledge-graph reasoning stage, and an<br>
LLM-written explanation attached to every detection — so a flag comes with its<br>
reason. Under review, 2026.

**Multimodal semiconductor yield prediction** &nbsp;·&nbsp; <samp>multimodal, manufacturing</samp><br>
Late fusion of 591 process-sensor features with 4096 vision features taken from<br>
the wafer map. Under review, 2026.

Lead author on both: problem formulation, method design, and all experiments.

<img src="./hd-stack.svg" width="620" alt="stack"/>

<samp>python &nbsp; rust &nbsp; kotlin &nbsp; c++ &nbsp; sql &nbsp; pytorch &nbsp; scikit-learn &nbsp; fastapi &nbsp; docker &nbsp; prometheus &nbsp; grafana &nbsp; linux</samp>

<img src="./hd-projects.svg" width="620" alt="projects"/>

**[MiniFlow-Serving](https://github.com/Mannava-Daasaradhi/MiniFlow-Serving)** &nbsp;·&nbsp; <samp>python, fastapi, docker</samp><br>
A reverse-mode autograd engine written from scratch — tensors, graph, backprop, no<br>
PyTorch — and then the layer that serves models trained on it: sticky A/B testing<br>
decided by a two-proportion z-test, PSI drift detection on a background loop,<br>
Prometheus into Grafana. 24 tests, 89% coverage.

**[LLM from Scratch](https://github.com/Mannava-Daasaradhi/LLM_from_Scratch)** &nbsp;·&nbsp; <samp>python, pytorch</samp><br>
Tokenizer, multi-head attention, positional encodings, training loop, sampling —<br>
all hand-built. I can whiteboard KV-caching and why RoPE works because I wrote them.

**[S-XG-NID](https://github.com/Mannava-Daasaradhi/S-XG-NID)** &nbsp;·&nbsp; <samp>python, graph ml</samp><br>
The research codebase for the intrusion-detection work above: heterogeneous graph<br>
over CICIDS flows, knowledge-graph reasoning, generated explanations.

**[FabMind](https://github.com/Mannava-Daasaradhi/FabMind-Semiconductor-AI)** &nbsp;·&nbsp; <samp>python</samp><br>
The yield-prediction codebase, with the explainability tooling that goes with it.

**[GlassBox-Attack](https://github.com/Mannava-Daasaradhi/GlassBox-Attack)** &nbsp;·&nbsp; <samp>python</samp><br>
Adversarial attack and defense experiments — robustness evaluation of neural<br>
classifiers, measured rather than asserted.

**[StudyMetrics](https://github.com/Mannava-Daasaradhi/StudyMetrics)** &nbsp;·&nbsp; <samp>kotlin, android</samp><br>
An Android app built as 18 CI-gated Gradle modules, because one module is a script<br>
and eighteen is an architecture.

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

The portrait's source photograph is from [Pixabay](https://pixabay.com/photos/mask-hoodie-hacker-attack-2883635/),<br>
under the Pixabay Content License. The layout and the generated-graphics approach<br>
are adapted, with thanks, from<br>
[andriidrok1](https://github.com/andriidrok1/andriidrok1).
