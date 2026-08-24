# KTH LIVE INTERVIEW GUIDE — APPLICATION + WHY THIS IS US

**Interview:** Aug. 24, 2026 · 07:00 New York / 13:00 Stockholm  
**Interviewers:** Matthieu Barreau + Avlant Nilsson  
**Position:** Doctoral student in deep learning for biological systems

> **USE THIS WHILE TALKING.** Exact words they saw or words from the position come first. Under each one: what I meant, what I can say naturally, and the work that proves it.

**Application:** [folder](../../APPLICATIONS/PhD/review-by-application/05-kth-deep-learning-biological-systems/) · [submitted CV](../../APPLICATIONS/PhD/review-by-application/05-kth-deep-learning-biological-systems/2026-07-31-kth-deep-learning-biological-systems-cv.pdf)

---

# 1. START HERE — THE QUESTION THAT GOT ME

> ## **Do you want to contribute to improving human health?**
>
> *To be a doctoral student means to devote oneself to a research project under supervision of experienced researchers and following an individual study plan. For a doctoral degree, the equivalent of four years of full-time doctoral education is required.*

**YES. This is the simplest reason this position stood out to me.**

If they ask **“Why this PhD?” / “Why did this position catch your attention?”**:

> That opening question really did catch me. I have spent years building computational skills, and when I look at the work I keep choosing, it keeps pulling toward health — medical diagnosis, hospital readmission, healthcare and biological data, RNA structure, RNA-seq, and bioinformatics. I want the next stage of my research to use those skills on problems that can directly improve human health.

That is the **WHY**.

The rest of the position is what made it feel like the **right HOW and the right PLACE**.

### THE QUESTION

**Improve human health.**  
Not computation for its own sake. Not biology as just another dataset.

### THE WORK

The project uses the kind of computation I want to grow into:

- **deep learning for biological systems**
- **cancer / precision medicine**
- integrate **metabolism + signaling + gene regulation**
- **biologically constrained** modeling
- **RNN-based** approaches
- model how molecular states **evolve**
- understand **cell-cell interactions**
- study responses to **perturbations**
- ultimately help move pathological systems toward **healthier states**

If they ask **“Why this work specifically?”**:

> Because it connects the health direction I have already been moving toward with the kind of machine learning I want to do next. I already have pieces of it — biological-data analysis, RNA structure, RNA-seq, neural networks, sequential modeling, uncertainty and reproducible evaluation. This project brings those pieces together around a biological problem where the result can matter for health.

### THE ENVIRONMENT

This is the other part that made the fit unusually strong.

**Matthieu / KTH Decision and Control Systems**  
→ dynamics · modeling · system identification · model fidelity · uncertainty · control

**Avlant / KI + SciLifeLab**  
→ cancer biology · signaling · gene regulation · metabolism · biological networks · RNNs · perturbation

**KTH + SciLifeLab + KI**  
→ computation + biology + experimental research in the same scientific environment

If they ask **“Why KTH / why this environment?”**:

> I want to use the computational skills I have spent years building on problems that can directly improve human health, and I want to do that in an interdisciplinary life-science environment where computation, biology and experimentation genuinely meet. That is what makes this setting so attractive to me.

Or, if I want to connect it directly to the two people in front of me:

> What I really like is that the environment covers both sides of the problem. Matthieu brings the dynamical-systems and modeling side, while Avlant brings the mechanistic cancer-biology side. Then SciLifeLab and KI connect the computational work to biological and experimental research. That is exactly the kind of environment I was trying to describe in my cover letter.

### THE WHOLE FIT IN ONE THOUGHT

> The question is why I want to do the research — improving human health. The work is how I want to contribute — using strong computational models to understand complex biology. And the environment is where I want to learn to do it properly — with machine learning, biological expertise and experimentation connected rather than separated.

---

# 2. APPLICATION QUESTION 1 — WHY THIS POSITION?

## What I wrote

> **I am interested in this project because it combines deep learning, biological systems, and precision-medicine questions in a way that requires both strong modeling and careful scientific interpretation. The focus on cell-cell interactions and biologically meaningful system dynamics is especially compelling to me.**

### If they ask **“Why did you say that?”**

> Because I was already looking for exactly that combination: strong machine learning, real biological meaning, and work that can eventually matter for health. The opening question about improving human health grabbed me, and then the actual project showed me how they were trying to do it — through deep learning, biological systems, cell interactions and precision medicine.

### If they ask **“What do you mean by strong modeling and careful scientific interpretation?”**

> BIO614 is probably my clearest example. The model could look very good on simple synthetic RNA structures, but it failed on realistic tRNA and 5S structures. That taught me that a strong metric is not enough if the model is missing something important about the biology.

**BIO614 reminder:** Nussinov + MFE / Turner parameters / ViennaRNA · synthetic motifs vs real RNA · sensitivity/specificity/MCC · failure on realistic topology.

**Proof:** [BIO614 writing sample](https://drive.google.com/file/d/1x_xLkbu-JGHrqH8gf7DaFwNMtGs-qquZ/view?usp=drivesdk) · [Overleaf](https://www.overleaf.com/project/68a761a470c296440522a537)

### If they ask **“What do you mean by biologically meaningful system dynamics?”**

> What attracted me is that the biology is not static. The project is interested in how signaling, gene regulation, metabolism and cell interactions change together over time. That is where the RNN side makes sense to me: the current state is informed by what came before rather than treating every measurement as independent.

### If they ask **“Why precision medicine?”**

> Because the end goal is not only to describe or classify a biological state. It is to understand it well enough that the model can eventually help reason about which perturbation or intervention may produce a better response.

### The work I can point to

**BIO614** → biological structure + interpretation  
**BIOL550** → noisy/high-dimensional molecular data + QC  
**DSCI640** → RNN/LSTM temporal modeling  
**GA / DSCI601** → uncertainty + context + changing conditions

**Links:** [BIO614](https://drive.google.com/file/d/1x_xLkbu-JGHrqH8gf7DaFwNMtGs-qquZ/view?usp=drivesdk) · [BIOL550](https://github.com/pzg8794/BIOL550-Project_Paper) · [LSTM assignment](https://drive.google.com/file/d/1K8zJDmrcyVUy3Yi6EPbn1XpIC8VxIWnP/view?usp=drivesdk) · [DSCI601](https://github.com/pzg8794/DSCI601-Project_Proposal)

---

# 3. APPLICATION QUESTION 2 — WHAT CAN I CONTRIBUTE?

## What I wrote

> **I can contribute reproducible machine-learning workflows, strong data-analysis practice, and experience working with noisy, high-dimensional biological data. I would bring disciplined evaluation, transparent reporting, and a computational perspective shaped by both ML research and computational biology work.**

### If they ask **“What can you actually contribute?”**

> My strongest contribution immediately is on the computational side: coding, reproducible experimentation, model evaluation and high-dimensional data analysis. I also already have computational-biology experience that taught me to pay attention to QC, biological structure and interpretation. What I want to deepen here is the cancer-systems-biology and formal dynamical/control side.

### “Reproducible ML workflows” — what I mean

> I want to be able to trace a result from the data and preprocessing through the model settings, baselines, metrics, logs and final analysis. That is a strong theme in my GA work and in the biological projects I submitted.

**Examples:**  
GA → common testbeds · logging · algorithm comparisons  
ISTE780 → Optuna · cross-validation · statistical comparison  
BIOL550 → QC/preprocessing → DESeq2 → interpretation  
BIO614 → common evaluation across synthetic and biological examples

### “Noisy, high-dimensional biological data” — what I mean

> BIOL550 is the strongest academic example because I worked with RNA-seq and the full QC/differential-expression story. BIO614 and ISTE780 gave me RNA sequence/structure experience, and VIOME gave me industry exposure to healthcare and microbiome-oriented data workflows.

### “Fairness-aware analytics” — what transfers

> The useful transfer is the habit of asking whether an overall score hides systematic failure. In ISTE780 I audited differences by RNA type, GC-content bin and sequence-length bin. I treat that as sequence-level methodological fairness, not as human demographic fairness.

**Proof:** [ISTE780 KTH sample](https://drive.google.com/file/d/1VvE4oNsAx6lFlppTv0VjI_GTGDsbkN-v/view?usp=drivesdk) · [BIOL550](https://github.com/pzg8794/BIOL550-Project_Paper) · [QuantumFaultTolerant](https://github.com/pzg8794/QuantumFaultTolerant)

---

# 4. COVER LETTER — WHY I APPLIED

## What I wrote

> **I am drawn to this project because it combines machine learning, mathematical modeling, and biologically meaningful inference in a way that could directly support precision medicine.**

### If they ask **“What did you mean?”**

> The health impact is important to me, but I also care about how we get there. I do not want to build a model that is only good at producing a prediction. I want the modeling to help us understand something meaningful about the biology, especially if the eventual goal is to reason about treatment or intervention.

That connects directly back to the posting:

> **Do you want to contribute to improving human health?**

My answer is yes — and I want to contribute through the computational side of that problem.

---

## What I wrote

> **My goal is to contribute to research that builds strong computational models for complex biological systems while remaining careful about uncertainty, data quality, and the scientific interpretation of results.**

If they pull apart the sentence:

**UNCERTAINTY** → GA / bandit work: estimates are not equally trustworthy; partial context; exploration/exploitation.  
**DATA QUALITY** → BIOL550: preprocessing/QC/alignment affect downstream biological conclusions.  
**SCIENTIFIC INTERPRETATION** → BIO614: good-looking metrics can still hide biological failure.

---

## What I wrote

> **That experience has made me especially motivated by questions where meaningful biological insight depends on careful modeling rather than predictive accuracy alone.**

### Easy example

> BIO614 made that very concrete for me. On simple synthetic motifs the approach worked very well, but on realistic RNA structures it could still be biologically wrong. So I learned not to confuse a good metric with a good scientific model.

---

## What I wrote

> **What interests me most in this position is the opportunity to work on deep learning methods for biological systems that connect computation with mechanistic and clinically relevant understanding.**

### If they ask **“Why mechanistic?”**

> Because if the goal is to improve health, I want the computational result to connect back to what the biological system is doing. That is what makes the signaling, gene-regulation, metabolism and perturbation work so interesting to me.

---

## What I wrote

> **I am particularly interested in problems where machine learning must represent complex interactions, heterogeneous data, and uncertain structure without losing scientific usefulness.**

### Here, the project makes those words concrete

**complex interactions** → signaling + gene regulation + metabolism + cell-cell interactions  
**heterogeneous data** → different molecular measurements / processes  
**scientific usefulness** → predictions that remain interpretable/testable in biology

---

## What I wrote

> **The focus on modeling cell-cell interactions, biological dynamics, and healthier system states is compelling because it requires both methodological rigor and strong interdisciplinary reasoning.**

### If they ask **“Why healthier system states?”**

> Because that brings the work back to the thing that attracted me in the first place: improving human health. The point is not only to model a cancer-promoting state; it is to understand the system well enough that the research can eventually help identify how to shift it toward a healthier response.

---

# 5. COVER LETTER — WHY THIS ENVIRONMENT

## What I wrote

> **KTH is especially attractive because this project sits in a strong interdisciplinary environment connecting machine learning, systems modeling, and translational biological research.**

> **I am looking for a PhD setting where strong computational work is directly connected to important biomedical questions, and where collaboration across technical and life-science domains is treated as central research practice.**

### What those words mean now that I know the team better

**Matthieu / DCS** → systems modeling · dynamics · control · model fidelity  
**Avlant / KI / SciLifeLab** → cancer biology · mechanistic ML · signaling/regulation/metabolism · perturbation  
**broader environment** → computational work connected to experimental / life-science work

### Natural answer

> One thing that makes this position especially attractive to me is the research environment around it. I am deliberately trying to move deeper into computational biology and health, and this is the kind of interdisciplinary setting I am looking for — where machine-learning researchers, biological scientists and experimental researchers are actually working on the same problem rather than treating biology as just another dataset.

---

# 6. CV PROFILE — IF THEY ASK “WHAT DID YOU ACTUALLY DO?”

## “RNA secondary structure prediction…” — BIO614

**What I did:** Nussinov DP · MFE / Turner parameters · ViennaRNA · environmental/energy corrections · synthetic + biological validation · sensitivity/specificity/MCC · visualization · failure analysis.

**What I learned:** metric success ≠ biological validity.

**Proof:** [KTH BIO614 sample](https://drive.google.com/file/d/1x_xLkbu-JGHrqH8gf7DaFwNMtGs-qquZ/view?usp=drivesdk)

### If they quote the CV’s “thermodynamic deep learning enhancements” / LSTM wording

> The BIO614 manuscript itself was Nussinov plus thermodynamic modeling. My RNN/LSTM implementation came from my graduate Neural Networks coursework. The CV compressed those strands together too much.

---

## “RNA-seq differential-expression analysis” — BIOL550

**What I did:** preprocessing · QC · alignment evidence · DESeq2 · PCA/distance/dispersion · biological interpretation.

**Proof:** [BIOL550 repo](https://github.com/pzg8794/BIOL550-Project_Paper) · [paper](https://github.com/pzg8794/BIOL550-Project_Paper/blob/main/main.tex) · [pipeline](https://github.com/pzg8794/BIOL550-Project_Paper/blob/main/assets_methods/biol550_pipeline_architecture_diagram.svg)

---

## “fairness-aware ML applied to bioinformatics” — ISTE780

**What I did:** 20 RNA sequences · six method families · Optuna · five-fold CV · statistical tests · fairness-style auditing.

**Actual grouping variables:** RNA type · GC-content bin · length bin.  
**NOT:** human demographic groups.

**Proof:** [KTH ISTE780 sample](https://drive.google.com/file/d/1VvE4oNsAx6lFlppTv0VjI_GTGDsbkN-v/view?usp=drivesdk)

---

## Graduate Neural Networks — RNN / LSTM

**What I worked with:** Jordan recurrence · Elman recurrence · recurrent forward pass · BPTT/backward propagation · time-series prediction · LSTM node/gates.

**Proof:** [RNN lecture](https://drive.google.com/file/d/1E3V3M-cL8DdqpYRgkMLVzS5yDvbtjzJE/view?usp=drivesdk) · [memory cells](https://drive.google.com/file/d/1ELmiTOTOreE9lQgGg-4Qs3-1PsLjAXRY/view?usp=drivesdk) · [LSTM assignment](https://drive.google.com/file/d/1K8zJDmrcyVUy3Yi6EPbn1XpIC8VxIWnP/view?usp=drivesdk)

---

## RIT GA — Quantum + AI

**What I do:** multi-armed/contextual/adversarial/neural bandit evaluation · routing/resource allocation · uncertainty · partial feedback · changing/adversarial conditions · predictive context · reproducible evaluation.

**Why it is relevant here:** not because quantum = cancer. It gives me experience reasoning about uncertainty, context, sequential decisions and what happens when conditions change.

**Proof:** [QuantumFaultTolerant](https://github.com/pzg8794/QuantumFaultTolerant) · [DSCI601](https://github.com/pzg8794/DSCI601-Project_Proposal)

---

# 7. THE PERTURBATION CONNECTION WE FOUND

This is the Avlant connection that genuinely excited me.

His phosphoproteomic work makes a distinction between **describing an observed trajectory** and predicting **how signaling will evolve under perturbation**.

My current work has a conceptually familiar problem:

**quantum:** observed performance under one condition does not guarantee behavior under attack / changed conditions.  
**biology:** observed signaling under one condition does not automatically tell us what happens under a new perturbation.

If it comes up naturally:

> What I found especially interesting in your perturbation work is that distinction between describing what was observed and predicting what happens after the system is changed. That is conceptually familiar from my current work. In quantum-network routing, observed performance under one condition does not by itself tell us how a policy will behave when the environment becomes adversarial or otherwise changes. The domains are completely different, but that question of predicting and adapting under changed conditions is one I already think about.

---

# 8. SELECTED TECHNICAL WRITING — MY JOURNEY TOWARD HUMAN HEALTH

```text
Big Data Medical Diagnosis
medical prediction + data quality
          ↓
Hospital Readmission ML
clinical prediction workflow
          ↓
BIO614 — RNA Structure
closer to biological structure + mechanism
          ↓
ISTE780 — Equitable Bioinformatics
where does the model fail?
          ↓
BIOL550 — RNA-seq
high-dimensional molecular data + QC
          ↓
RNN / LSTM + GA research
temporal modeling + uncertainty + changing conditions
          ↓
KTH
use those computational skills on research aimed at improving human health
```

### If they ask **“How did you get from computer science to this?”**

> It has been a progression rather than a sudden change. I was interested in medical prediction very early, then hospital-readmission ML, then I moved closer to biological data through RNA structure and RNA-seq. At the same time I kept building deeper machine-learning skills. So when I saw a PhD that explicitly asked whether I wanted to contribute to improving human health through this kind of computational work, it felt very aligned with where I have already been heading.

**Proof:** [Big Data Medical Diagnosis](https://github.com/pzg8794/opc-data-mining/tree/main/papers/Data%20Cleaning%20%26%20Processing/Data%20Cleaning/Big%20Data%20Medical%20Diagnosis%20-%20Papers) · [Hospital Readmission](https://drive.google.com/file/d/1R6NLciyevSHcyiBYvHjRX4jF8cGaqJuP/view?usp=drivesdk) · [BIO614](https://drive.google.com/file/d/1x_xLkbu-JGHrqH8gf7DaFwNMtGs-qquZ/view?usp=drivesdk) · [BIOL550](https://github.com/pzg8794/BIOL550-Project_Paper)

---

# 9. RNN / LSTM / ARIMA — QUICK REMINDER ONLY

## RNN

**Simple:** neural network for sequential/temporal data that carries learned state from previous time steps.

```text
x(t) + h(t-1) -> RNN -> h(t) -> prediction
```

## LSTM

**Simple:** RNN with gated memory — learns what to keep, forget and expose.

```text
FORGET -> what old information stays?
INPUT  -> what new information enters?
OUTPUT -> what memory affects current state/output?
```

## ARIMA

**Simple:** statistical time-series model where we specify how past values and errors enter the forecast.

**Remember:**  
ARIMA = **we specify** the memory structure.  
RNN = **network learns** recurrent state.  
LSTM = RNN + **gated longer-term memory**.

**Our connection:** current iCPursuit uses ARIMA predictive context; original iCMAB direction used EXAMM-evolved RNN models.

---

# 10. IF THEY ASK ABOUT MY GAPS

> My strongest preparation is on the computational side — machine learning, neural networks, reproducible experimentation, sequential decision-making and computational-biology data analysis. I am not already a cancer systems biologist or a formal control theorist. Those are exactly the areas I want to deepen here.

---

# 11. QUESTIONS FOR THEM

**Best question:**

> Because the project sits between DCS and the biological/experimental side, what do you currently see as the hardest scientific bottleneck: learning the underlying state and dynamics from the available data, making the model sufficiently identifiable and biologically interpretable, or experimentally validating the intervention predictions?

**Second:**

> What would you want the doctoral student to own independently during the first six to twelve months, and where do you expect the closest day-to-day collaboration between DCS and the biological team?

---

# 12. IF I FREEZE — THIS IS THE CORE

> **“Do you want to contribute to improving human health?” — Yes.** I want to use the computational skills I have spent years building on problems that can directly improve human health.

**WHY THIS WORK:** deep learning + biological systems + cancer + precision medicine.  
**WHY I CAN CONTRIBUTE:** ML + reproducibility + RNA/RNA-seq + RNN/LSTM + uncertainty/evaluation.  
**WHY THIS ENVIRONMENT:** Matthieu = modeling/dynamics/control; Avlant = cancer/mechanism/perturbation; KTH/SciLifeLab/KI = computation + biology + experiments.
