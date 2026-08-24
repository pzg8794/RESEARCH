# KTH PhD Interview — One-Page Cheat Sheet

**Interview completed:** Aug. 24, 2026 · approximately 07:30–08:03 New York / 13:30–14:03 Stockholm · Zoom · first round

**Panel:** Matthieu Barreau + Avlant Nilsson + Alexandre Proutiere

**Role:** Doctoral student in deep learning for biological systems

Keep this page open. Use the index to jump; use the linked [full evidence guide](2026-08-24-kth-live-interview-guide.md) only if they probe.

## Index

| I need… | Jump |
| --- | --- |
| What happened and what to improve | [First-round debrief](2026-08-24-kth-first-round-interview-debrief.md) |
| My core message | [10-second reset](#reset) |
| My opening answer | [Tell us about yourself](#intro) |
| A fast answer | [Why / why me / why KTH / gap / start](#answers) |
| The right project example | [Evidence switchboard](#evidence) |
| A technical definition | [Technical anchors](#technical) |
| Protection from overclaiming | [Claim guardrails](#guardrails) |
| Independence or teamwork | [Working-style stories](#behavior) |
| What to ask them | [Questions for them](#questions) |
| Final check before joining | [Thirty-second checklist](#checklist) |

---

## Reset

**Ten-second version**

> **This is a convergence, not a sudden pivot:** my computational training, the health questions I keep returning to, and the biological depth I now want meet in this project.

- **Why:** use computation on research that can improve human health.
- **Project:** interacting cells → cancer-promoting state → testable digital twin → healthier state.
- **I bring:** CS, data science, reproducible evaluation, RNA/RNA-seq, uncertainty, communication.
- **I am learning:** cancer mechanisms, system identification, formal control.
- **Best story:** BIO614 looked strong on simple motifs but failed on realistic biology; I changed the conclusion instead of protecting the model.

[↑ Back to index](#index)

---

## Intro

**“Tell us about yourself” — 60–75 seconds**

> My work keeps returning to one question: what happens when a system must make an important decision from incomplete evidence? I first approached that through Big Data Medical Diagnosis. Later, my own experiences navigating health systems made the consequences of missing context personal. In hospital-readmission modeling, a model reached about 82.6% accuracy while recalling only about 7.7% of the readmission class, showing me how aggregate metrics can conceal the failure that matters. I then moved closer to biological mechanism through RNA structure and RNA-seq. My RNA model succeeded on simple motifs but failed on realistic tRNA and 5S structures, which taught me not to confuse a strong-looking metric with biological validity. My current bandit and quantum-network work adds uncertainty, partial feedback, and changing conditions. KTH feels like the convergence of that path.

[Full personal answer and trajectory](2026-08-24-kth-live-interview-guide.md#full-intro) · [↑ Back to index](#index)

---

## Answers

**Fast responses**

### Why this PhD?

> I want research that can improve human health. KTH makes that purpose concrete through cell-cell dynamics, digital twins, biological validation, and reasoning about healthier states.

### Why me?

> I can contribute programming, reproducible experiments, careful baselines and evaluation, biological-data experience, and reasoning under uncertainty. I also teach, so I make assumptions visible and communicate across disciplines.

### Why KTH and these supervisors?

> Matthieu connects machine learning to dynamics, system identification, fidelity, uncertainty, and control. Avlant connects biologically informed learning to cancer mechanisms. I want an environment where experiments can challenge and improve the model.

### Biggest gap?

> I am not yet a cancer systems biologist or formal control theorist. I bring the computational foundation and want to develop those two areas rigorously under supervision.

### When can I start?

> My two current master's programs are expected to finish in December 2026. I can relocate afterward and discuss a project-compatible start date.

[Full answer bank](2026-08-24-kth-live-interview-guide.md#full-answers) · [↑ Back to index](#index)

---

## Evidence

**Project switchboard**

| If they test… | Use this | One result or lesson |
| --- | --- | --- |
| Independent research / metrics | **Hospital readmission** | 101,766 encounters; 82.56% accuracy but 7.66% positive recall |
| Failure / scientific judgment | **BIO614 RNA structure** | synthetic success; realistic tRNA/5S failure; metric ≠ biology |
| Biological-data experience | **BIOL550 RNA-seq** | 20 paired-end samples; design/QC/alignment/DESeq2/interpretation; group work |
| Neural-network foundation | **DSCI640** | recurrence, BPTT, and LSTM coursework; do not claim a completed cancer RNN |
| Uncertainty / dynamic conditions | **GA + DSCI601** | partial feedback, non-stationarity, reproducible comparisons; synthetic clinical setting |
| Long-term health direction | **Big Data Medical Diagnosis** | health-computing thread began in 2015; proposal, not deployed system |

Answer pattern: **problem → what I personally did → result/failure → lesson → KTH connection.**

[Full evidence stories](2026-08-24-kth-live-interview-guide.md#full-evidence) · [↑ Back to index](#index)

---

## Technical

**Fast definitions**

- **Digital twin:** computational representation calibrated against a real biological system; its intervention predictions must be testable in vitro.
- **System identification:** infer dynamics from observed states, outputs, interventions, and noise.
- **Control:** choose a constrained intervention and timing that move the system toward a desired state.
- **Biologically informed deep learning:** encode defensible prior interactions while retaining flexibility because the prior network is incomplete.
- **Omics:** large-scale measurement of one molecular layer—genomics (DNA), transcriptomics (RNA), proteomics/phosphoproteomics (proteins and signaling), or metabolomics (metabolites).
- **Multi-omics:** connect several molecular layers while respecting their different timing, noise, missingness, scale, and biological meaning; do not merely concatenate every feature.
- **Why recurrence:** current biological state depends on history; stability, partial observation, and validation still matter.
- **Validation ladder:** baseline → held-out conditions → held-out perturbations → uncertainty → mechanism → prospective in vitro test → revise after failure.

**If asked how I would integrate multi-omics:** preprocess each modality appropriately, align samples/time points/perturbations, connect measurements through biological pathways or a structured representation, compare fusion strategies, and test what each layer adds through ablation and held-out validation.

[Full technical notes](2026-08-24-kth-live-interview-guide.md#full-technical) · [↑ Back to index](#index)

---

## Guardrails

**Claim boundaries**

- **KTH confirms:** cell-cell interactions, cancer-promoting equilibria, in silico/in vitro models, digital twins, healthier states.
- **Related Nilsson-group work is context:** signaling, regulation, metabolism, biologically informed recurrent models, perturbation prediction. Do not assume KTH's architecture is fixed.
- **BIO614:** Nussinov dynamic programming + thermodynamics; not deep learning.
- **DSCI640:** coursework and assignment materials; do not claim a verified completed LSTM implementation.
- **BIOL550:** group project; identify my documented writing/integration contribution.
- **My verified omics experience:** transcriptomics/RNA-seq. Proteomics, phosphoproteomics, and metabolomics are relevant Nilsson-group context and areas to learn—not completed-work claims.
- **ISTE780 groups:** RNA type, GC bin, and length—not human demographic groups.
- **DSCI601:** synthetic simulation; not patient or clinical validation.
- **Formal control:** learning goal, not current specialization.

[Full accuracy boundaries](2026-08-24-kth-live-interview-guide.md#full-guardrails) · [↑ Back to index](#index)

---

## Behavior

**Working-style stories**

**Independence:** readmission project → built and compared four model families → class-specific recall exposed misleading accuracy → changed the interpretation.

**Collaboration:** BIOL550 → three-person RNA-seq paper → color-coded ownership → I framed the question/design and integrated methods/transitions → coherent paper without claiming everyone's work.

**Professionalism:** if they quote an overcompressed CV phrase, separate the strands clearly: BIO614 was non-neural; RNN/LSTM evidence comes from coursework.

[Full behavioral answers](2026-08-24-kth-live-interview-guide.md#full-behavior) · [↑ Back to index](#index)

---

## Questions

**Questions for them**

Ask the first; ask the second only if time permits.

1. **Which interacting-cell system and experimental datasets are already committed, and what would count as the minimum viable digital twin in the first year?**
2. **How will supervision and day-to-day work divide among dynamics/control, biologically informed deep learning, and in vitro validation?**

[Full interviewer and question notes](2026-08-24-kth-live-interview-guide.md#full-questions) · [↑ Back to index](#index)

---

## Checklist

**Final thirty seconds**

- Answer the question first.
- Give **one** example and my exact contribution.
- Stop after 45–60 seconds and let them probe.
- Do not let an old CV phrase force a false claim.
- Keep the detailed guide and submitted cover-letter text open in separate tabs.
- End with one research question and genuine interest.

[Open the full guide](2026-08-24-kth-live-interview-guide.md) · [↑ Back to index](#index)
