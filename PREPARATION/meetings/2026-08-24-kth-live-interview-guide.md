# KTH LIVE INTERVIEW GUIDE — MY APPLICATION, MY EVIDENCE, MY WHY

**Interview:** Aug. 24, 2026 · 07:00 New York / 13:00 Stockholm · Zoom · 20 minutes
**Interviewers:** Matthieu Barreau + Avlant Nilsson  
**Position:** Doctoral student in deep learning for biological systems

> **USE THIS WHILE TALKING.** Exact words they saw or words from the position come first. Under each one: what I meant, what I can say naturally, and the work that proves it.

**Quick navigation:** [one-page cheat sheet + index](2026-08-24-kth-interview-cheat-sheet.md#index)

**Preparation:** [submitted cover-letter text](../../APPLICATIONS/PhD/review-by-application/05-kth-deep-learning-biological-systems/2026-07-31-kth-deep-learning-biological-systems-cover-letter.txt) · [20-minute scenarios](2026-08-24-kth-20-minute-interview-scenarios.md) · [interviewer focus](2026-08-24-kth-interviewer-focus-matthieu-avlant.md)

**Privacy note:** the frozen submitted CV remains part of the internal application evidence, but this public guide does not link directly to the PDF because it contains personal contact information.

---

# 0. ONE-SCREEN LIVE CARD — KEEP THIS BESIDE ZOOM

[↑ Back to cheat-sheet index](2026-08-24-kth-interview-cheat-sheet.md#index)

**Use, do not recite.** Answer the question first, give one piece of evidence, state what it taught me, and connect it to KTH. Most answers should stop after 45–60 seconds so they can probe.

> **This position feels like a convergence, not a sudden pivot: the computational skills I have spent years building, the health questions I keep returning to, and the biological depth I now want all meet in one research project.**

**WHY:** I want to use computation on research that can improve human health.

**PROJECT:** KTH confirms cell-cell interactions → cancer-promoting equilibria → in silico/in vitro digital twins → healthier states. Related Nilsson-group work adds perturbation reasoning; it does not fix the KTH architecture in advance.

**I BRING / I LEARN:** CS + data science + reproducible evaluation + RNA/RNA-seq + uncertainty + teaching/communication / cancer mechanisms + system identification + formal control.

**MY SCIENTIFIC QUESTION:** How can we learn a biologically meaningful dynamical model of interacting cells, use it to predict response to intervention, and keep it credible when tested in vitro?

**FIVE EVIDENCE KEYS:**

- **Readmission:** 82.56% accuracy / 7.66% positive recall → aggregate metrics can hide failure.
- **BIO614:** simple synthetic success / realistic tRNA and 5S failure → metric ≠ biological validity.
- **BIOL550:** group RNA-seq work → QC/design choices shape the scientific story.
- **DSCI640:** recurrent/LSTM graduate coursework → foundation, not a cancer-RNN claim.
- **GA/DSCI601:** uncertainty + partial feedback + non-stationarity → methodological transfer; clinical setting was synthetic.

**TWO CLAIM BOUNDARIES:** BIO614 was non-neural; DSCI601 was not patient validation.

**WORKING-STYLE CUES:** independence = sole-authored readmission workflow; collaboration = BIOL550's color-coded ownership and integrated group pipeline.

**ASK:** Which interacting-cell system and datasets are already committed, and what would count as the minimum viable digital twin in year one?

---

# Full answers

**Expanded personal answer bank**

[↑ Back to cheat-sheet index](2026-08-24-kth-interview-cheat-sheet.md#index)

## What KTH is actually scoring

| KTH criterion | My clearest evidence |
| --- | --- |
| Independently pursue work | BIO614 or GA: define question → implement → compare → interpret failure → document |
| Collaborate | GA research, BIOL550, teaching placements: clarify roles and assumptions; make work traceable |
| Professional approach | distinguish completed work from exploration; correct an overbroad CV phrase instead of bluffing |
| Analyze complex issues | BIO614 model mismatch; bandits under partial/noisy/changing context |
| Biological-system interest/experience | RNA structure, RNA-seq, health-data work, fairness-aware bioinformatics |
| Deep-learning experience | graduate Neural Networks coursework covering recurrence, BPTT, and LSTM logic; broader ML frameworks |
| Communicate findings | technical manuscripts plus teaching experience across age groups and disciplines |
| Study preparation | completed M.S. Computer Science; current Data Science and Teaching CS graduate work |

## Likely 20-minute flow

1. **Opening:** who I am and why this project.
2. **Evidence:** one research project, my exact contribution, result, and lesson.
3. **Technical fit:** deep learning/RNNs, biological data, uncertainty, digital twins.
4. **Working style:** independence, collaboration, professionalism, complex analysis.
5. **Close:** honest gaps, availability, and one strong question for them.

For any research story: **problem → what I personally did → result/failure → what changed in my thinking → why it matters here.**

## My actual path toward this PhD

```text
Big Data Medical Diagnosis (2015)
        ↓
health-data and AI work in industry
        ↓
Diabetic Readmission Prediction
        ↓
RNA structure modeling (BIO614)
        ↓
RNA-seq / differential expression (BIOL550)
        ↓
fairness-aware bioinformatics + bandit/quantum work on
sequential learning under uncertainty
        ↓
KTH: use computation to understand interacting biological systems
and help reason about intervention
```

This is why the application is not an invented story. **My work keeps returning to health, then moving closer to the biology.**

## Full intro

**“Tell us about yourself” — natural 75–90 second answer**

[↑ Back to cheat-sheet index](2026-08-24-kth-interview-cheat-sheet.md#index)

> My path into this work has one consistent question: what happens when a system has to make an important decision from incomplete evidence? I first approached that computationally during my earlier computer-science master's through Big Data Medical Diagnosis. Later, my own experiences navigating health systems made the consequences of missing context personal. When I returned to data science, I tested the issue more concretely in hospital-readmission modeling: a model could reach about 82.6% accuracy while recalling only about 7.7% of the readmission class. That made the danger of aggregate metrics very real to me. I then moved closer to biological mechanism through RNA structure and RNA-seq. My RNA-structure work succeeded on simple synthetic motifs but failed on realistic tRNA and 5S structures, teaching me not to confuse a strong-looking metric with biological validity. My current bandit and quantum-network research adds uncertainty, partial feedback, and changing conditions. KTH feels like the convergence of that journey: applying rigorous dynamical modeling to biological systems with a direct human-health purpose.

## “Why this position?” — natural 45–60 second answer

> I want to contribute to research that can improve human health. The KTH project makes that purpose concrete: model cell-cell interactions, build and validate in silico and in vitro digital twins, and use those models to reason about disrupting cancer-promoting states and steering systems toward healthier ones. That goes beyond classifying a sample. It asks whether a computational model can represent a changing biological system well enough to make a useful, testable intervention prediction. That is exactly the kind of deeper scientific work I want to learn to do.

## “Why you?” / “What can you contribute?” — natural 45-second answer

> I can contribute immediately on the computational side: strong programming, reproducible workflows, careful baselines and evaluation, neural-network foundations, and experience with noisy biological data. BIO614 taught me to recognize when a good-looking metric hides a biologically weak model; BIOL550 taught me how much QC and preprocessing shape molecular conclusions; and my current research trains me to reason about uncertainty, partial context, and changing conditions. I also teach, so I am practiced at making assumptions visible and explaining technical ideas to people with different backgrounds. What I need to deepen here is cancer systems biology and formal control, and that is precisely why this supervisory environment fits.

## “Why KTH and these supervisors?” — natural 35–45 second answer

> What makes the environment unusually strong is that the scientific problem is not split into disconnected pieces. Matthieu brings dynamical modeling, system identification, model fidelity, uncertainty, and control. Avlant brings mechanistically informed deep learning and cancer biology. The wider team connects learning and optimization with experimental cell systems. I am looking for a PhD where the computational model is challenged by biological evidence and refined through experiment, not judged only by a benchmark score.

## If I want to make the motivation personal

Use this only if it feels right; I do not owe anyone private medical detail.

> My interest in human health is personal as well as technical. I know what it is like when a system sees fragmented evidence and reaches the wrong conclusion about a person. I do not treat lived experience as scientific evidence; it gives the scientific problem real stakes for me. That is why I care about data quality, uncertainty, and models that remain answerable to the underlying reality rather than simply producing a confident prediction.

Then return immediately to the science:

> In this project, that means a digital twin whose predictions can be tested, contradicted, and improved through biological experiments.

## Full evidence

**The evidence stories I can reach for**

[↑ Back to cheat-sheet index](2026-08-24-kth-interview-cheat-sheet.md#index)

| If they test… | Use… | Core point |
| --- | --- | --- |
| Long-term health motivation | **Big Data Medical Diagnosis** | Early literature-driven system proposal about diagnostic evidence and data quality—not a deployed clinical system. The health thread began in 2015. |
| Metric judgment | **Hospital readmission** | 101,766 encounters; tuned logistic regression reached 82.56% accuracy but only 7.66% positive-class recall. Aggregate success can conceal failure on the class that matters. |
| Scientific judgment / failure | **BIO614 RNA structure** | Simple synthetic motifs looked strong; realistic tRNA/5S exposed model mismatch. A metric is not biological validity. |
| Biological-data practice | **BIOL550 RNA-seq** | Group reanalysis of 20 paired-end samples; QC, alignment, DESeq2 interaction modeling, and interpretation determine whether downstream conclusions are trustworthy. |
| Deep-learning foundation | **DSCI 640 Neural Networks** | Coursework and assignments covered recurrent structures, BPTT, and LSTM forward/backward logic; distinguish this from the non-neural BIO614 paper and do not claim a completed cancer RNN. |
| Uncertainty / changing systems | **GA + DSCI601 bandits** | Partial context, non-stationarity, sequential decisions, common baselines, and reproducible evaluation transfer methodologically—not biologically. The clinical environment was synthetic. |

### Full behavior

**If they ask about independent work**

[↑ Back to cheat-sheet index](2026-08-24-kth-interview-cheat-sheet.md#index)

> In my sole-authored hospital-readmission project, the challenge was that class imbalance made accuracy look reassuring. I built and compared logistic-regression, decision-tree, random-forest, and SVM workflows, including feature selection, tuning, and imbalance handling. When tuned logistic regression reached 82.56% accuracy but only 7.66% recall for readmission, I did not present accuracy as success; I changed the evaluation story to center class-specific failure. That is how I work independently: implement, test the assumption behind the metric, and let the failure change the conclusion.

### If they ask about collaboration

> BIOL550 required three people to turn a 20-sample mouse DRG RNA-seq reanalysis into one coherent scientific paper. We made authorship visible with color-coded contributions. My documented sections framed the biological question and balanced design and integrated the methods logic across acquisition, QC, alignment, DESeq2, and interpretation. I also added transition wording so the separate contributions read as one argument. The result was a traceable group paper where I can explain my contribution precisely without claiming the entire pipeline as mine.

## Short answers to predictable questions

### “Why move from quantum research to cancer biology?”

> Quantum networking is one application domain in my current work; it is not the human-health purpose I want to center in my PhD. What transfers is the research discipline—partial observability, uncertainty, sequential decisions, changing conditions, and reproducible comparison. My health and biological projects show where I want to apply that discipline next.

### “Why another degree when you already have graduate degrees?”

> My previous degrees gave me breadth in computing, data science, and education. I am not seeking another credential; I am seeking four years of sustained research depth around one scientific problem and the training needed to become an independent researcher.

### “What is your biggest gap?”

> I am not entering as a cancer systems biologist or a formal control theorist. I can contribute computational modeling, implementation, evaluation, and biological-data experience immediately. I would need to deepen cancer mechanisms, system identification, and control rigorously, and this team is exactly the environment in which those gaps can become research strengths.

### “When could you start?”

> My two current master's programs are expected to finish in December 2026. I can relocate after completing them, and I am ready to discuss a start date that works for the project.

If they notice the older CV date:

> Since I applied, my expected completion date has been updated to December 2026 because of the remaining program and teaching requirements.

## Full technical

**Technical anchors — explain, do not perform**

[↑ Back to cheat-sheet index](2026-08-24-kth-interview-cheat-sheet.md#index)

**Digital twin:** a computational representation calibrated against a real biological interaction system, able to reproduce relevant dynamics and make intervention predictions that can be tested in vitro and used to revise the model.

**System identification:** infer the dynamics from observed states/outputs and perturbations: `x(t+1) = f(x(t), u(t), G) + noise`.

**Control:** after the dynamics are credible, ask which intervention, at what time and under what constraints, can move the system toward the desired state.

**Biologically constrained deep learning:** encode defensible interaction knowledge into architecture, connectivity, state, or loss—but retain learnable flexibility because prior networks are incomplete and sometimes wrong.

**Why recurrence may help:** molecular state evolves; the current state depends on history. An RNN can represent that dependence, but stability, partial observation, long time scales, and biological validation still matter.

**Validation ladder:** simpler baselines → held-out trajectories/conditions → held-out perturbations → uncertainty/calibration → mechanistic plausibility → prospective in vitro test → revise the model after failure.

## Full questions

**The two questions I want to ask**

[↑ Back to cheat-sheet index](2026-08-24-kth-interview-cheat-sheet.md#index)

Ask the first; ask the second only if time permits.

> Which interacting-cell system and experimental datasets are already committed to the project, and what would you consider the minimum viable digital twin during the first twelve months?

> How do you expect supervision and day-to-day work to divide among dynamical systems and control, biologically informed deep learning, and in vitro validation?

## Full guardrails

**Accuracy boundaries — do not let a compressed CV force a false answer**

[↑ Back to cheat-sheet index](2026-08-24-kth-interview-cheat-sheet.md#index)

- **The KTH posting confirms:** cell-cell interactions · cancer-promoting equilibria · in silico and in vitro models · digital twins · steering toward healthier states.
- **Nilsson-group research provides context, not a guaranteed architecture:** mechanistic networks · signaling/gene regulation/metabolism · multi-omics · biologically informed recurrent models · perturbation prediction.
- **BIO614 paper:** Nussinov dynamic programming + thermodynamics. Do not call that paper a deep-learning implementation.
- **“>90%”:** only describe strong performance on simple synthetic controls; realistic biological structures exposed major limitations.
- **ISTE780 groups:** RNA type, GC-content bin, and sequence length—not human demographic cohorts.
- **DSCI601 clinical environment:** synthetic simulation, not patient validation.
- **Formal control theory:** adjacent interest and a learning goal, not current specialization.

## If I freeze

- **Why:** improve human health.
- **Project:** cell-cell dynamics → digital twin → experimentally tested intervention.
- **I bring:** computation, reproducibility, biological-data work, uncertainty, communication.
- **I am learning:** cancer mechanisms and formal control.
- **My best story:** BIO614 failed on realistic biology, and I changed my interpretation instead of protecting the model.

Pause. Answer the question they actually asked. Give one example. Stop and let them probe.

---

# 1. START HERE — THE QUESTION THAT CAPTURES WHY THIS IS US

> ## **Do you want to contribute to improving human health?**
>
> *To be a doctoral student means to devote oneself to a research project under supervision of experienced researchers and following an individual study plan. For a doctoral degree, the equivalent of four years of full-time doctoral education is required.*

**Source boundary:** These exact lines come from a closely related 2026 KI/SciLifeLab doctoral advertisement from Avlant Nilsson's group. They are not verbatim lines from KTH vacancy PA-2026-1420. I can use the question because it captures my motivation and the shared human-health purpose of the research environment, but I should not tell the interviewers that their KTH advertisement opened with it.

**YES. This is the simplest reason this research direction stood out to me.**

If they ask **“Why this PhD?” / “Why did this position catch your attention?”**:

> That question from the related Nilsson-group position captures what drew me to this research direction. I have spent years building computational skills, and when I look at the work I keep choosing, it keeps pulling toward health — medical diagnosis, hospital readmission, healthcare and biological data, RNA structure, RNA-seq, and bioinformatics. I want the next stage of my research to use those skills on problems that can directly improve human health.

That is the **WHY**.

The rest of the position is what made it feel like the **right HOW and the right PLACE**.

### THE QUESTION

**Improve human health.**  
Not computation for its own sake. Not biology as just another dataset.

### THE WORK

The exact KTH posting confirms:

- **deep learning for biological systems**
- models of **cell-cell interactions**
- disruption of **cancer-promoting equilibria**
- **in silico and in vitro** model development
- building and validating **digital twins**
- reasoning about how to steer cellular systems toward **healthier states**

Related work from Avlant's group makes the surrounding research direction
especially relevant—biologically constrained networks, signaling, gene
regulation, metabolism, multi-omics, recurrent dynamics and perturbation
prediction—but I should treat those as informed context, not assume that the
KTH PhD architecture has already been fixed.

If they ask **“Why this work specifically?”**:

> Because it connects the health direction I have already been moving toward with the kind of machine learning I want to do next. I already have pieces of it — biological-data analysis, RNA structure, RNA-seq, neural networks, sequential modeling, uncertainty and reproducible evaluation. This project brings those pieces together around a biological problem where the result can matter for health.

### THE ENVIRONMENT

This is the other part that made the fit unusually strong.

**Matthieu / KTH Decision and Control Systems**  
→ dynamics · modeling · system identification · model fidelity · uncertainty · control

**Avlant / KI + SciLifeLab**  
→ cancer biology · signaling · gene regulation · metabolism · biological networks · RNNs · perturbation

**Broader KTH/DCS partner environment: SciLifeLab + KI + AstraZeneca**
→ computation + biology + experimental and translational expertise; ask how each partner will participate in this specific project

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

> Because I was already looking for exactly that combination: strong machine learning, real biological meaning, and work that can eventually matter for health. The related Nilsson-group question about improving human health expresses the purpose, and the KTH project makes the method concrete through deep learning, cell interactions, digital twins, in silico and in vitro validation, and precision-medicine goals.

### If they ask **“What do you mean by strong modeling and careful scientific interpretation?”**

> BIO614 is probably my clearest example. The model could look very good on simple synthetic RNA structures, but it failed on realistic tRNA and 5S structures. That taught me that a strong metric is not enough if the model is missing something important about the biology.

**BIO614 reminder:** Nussinov + MFE / Turner parameters / ViennaRNA · synthetic motifs vs real RNA · sensitivity/specificity/MCC · failure on realistic topology.

**Proof:** [BIO614 writing sample](https://drive.google.com/file/d/1x_xLkbu-JGHrqH8gf7DaFwNMtGs-qquZ/view?usp=drivesdk) · [Overleaf](https://www.overleaf.com/project/68a761a470c296440522a537)

### If they ask **“What do you mean by biologically meaningful system dynamics?”**

> What attracted me is that the biology is not static. The KTH project is about interacting cells and changing pathological states. Avlant's related research shows one way to think about the intracellular side—signaling, gene regulation and metabolism evolving under perturbation. A recurrent model may be useful because the current state depends on history, but I would first want to understand the actual data, biological system and validation plan rather than assume one architecture in advance.

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

> BIOL550 is the strongest academic example because I worked in a group on an RNA-seq reanalysis covering QC, alignment, differential expression, and biological interpretation. BIO614 and ISTE780 gave me RNA sequence/structure experience, while my industry work gave me broader exposure to healthcare-data workflows. I should not claim a specific microbiome method unless they ask about work I can personally document and explain.

### “Fairness-aware analytics” — what transfers

> The useful transfer is the habit of asking whether an overall score hides systematic failure. In ISTE780 I audited differences by RNA type, GC-content bin and sequence-length bin. I treat that as sequence-level methodological fairness, not as human demographic fairness.

**Statistical boundary:** the reported `p < 0.01` supports comparisons in method performance. It does **not** establish bias across demographic groups.

**Proof:** [ISTE780 KTH sample](https://drive.google.com/file/d/1VvE4oNsAx6lFlppTv0VjI_GTGDsbkN-v/view?usp=drivesdk) · [BIOL550](https://github.com/pzg8794/BIOL550-Project_Paper) · [QuantumFaultTolerant](https://github.com/pzg8794/QuantumFaultTolerant)

---

# 4. COVER LETTER — WHY I APPLIED

## What I wrote

> **I am drawn to this project because it combines machine learning, mathematical modeling, and biologically meaningful inference in a way that could directly support precision medicine.**

### If they ask **“What did you mean?”**

> The health impact is important to me, but I also care about how we get there. I do not want to build a model that is only good at producing a prediction. I want the modeling to help us understand something meaningful about the biology, especially if the eventual goal is to reason about treatment or intervention.

That connects directly to the broader human-health purpose. In my own voice:

> I want to contribute through the computational side of a biological problem whose success could eventually matter for human health.

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

> The BIO614 manuscript itself was Nussinov plus thermodynamic modeling. My RNN/LSTM foundation came from graduate Neural Networks coursework and assignment materials covering recurrence, BPTT, and LSTM logic; the local assignment scaffold does not verify a completed implementation. The CV compressed those strands together too much.

---

## “RNA-seq differential-expression analysis” — BIOL550

**Project:** group reanalysis of 20 paired-end mouse DRG RNA-seq samples after sciatic-nerve injury, using a balanced injury-side × genotype design.

**My documented contribution:** the paper color-codes my writing and integration work. My sections frame the biological question and balanced 20-sample design and explain the reproducible four-stage workflow, QC, alignment, DESeq2 interaction model, and interpretation logic. Those are documented writing/methods contributions inside a **group** analysis; do not claim sole ownership of every pipeline stage or result.

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

**Ownership and evidence boundary:** explain the component I personally implemented or evaluated. The DSCI601 clinical environment is simulation-first and synthetic—not a patient study or clinical validation.

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
RNN / LSTM coursework
temporal-model foundations
          +
GA bandit / quantum-network research
uncertainty + partial feedback + changing conditions
          ↓
KTH
use those computational skills on research aimed at improving human health
```

### If they ask **“How did you get from computer science to this?”**

> It has been a progression rather than a sudden change. I was interested in medical prediction very early, then hospital-readmission ML, then I moved closer to biological data through RNA structure and RNA-seq. At the same time I kept building deeper machine-learning skills. The human-health question in the related Nilsson-group advertisement expressed the purpose I was already pursuing, while the KTH project supplied the specific scientific path: cell-cell dynamics, digital twins, perturbation, and experimental validation.

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

**Our connection:** current iCPursuit uses ARIMA predictive context; an earlier iCMAB plan proposed EXAMM-evolved RNN models. Do not describe the EXAMM direction as a completed implementation.

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

> **I want to use the computational skills I have spent years building on research that can improve human health.** The KTH project gives that purpose a concrete scientific form: model interacting cells, build a testable digital twin, and learn how to reason about intervention.

**WHY THIS WORK:** deep learning + biological systems + cancer + precision medicine.  
**WHY I CAN CONTRIBUTE:** ML + reproducibility + RNA/RNA-seq + RNN/LSTM + uncertainty/evaluation.  
**WHY THIS ENVIRONMENT:** Matthieu = modeling/dynamics/control; Avlant = cancer/mechanism/perturbation; KTH/SciLifeLab/KI = computation + biology + experiments.

---

# 13. SOURCE CHECK — KEEP KTH FACTS AND RELATED CONTEXT SEPARATE

- [Official KTH vacancy PA-2026-1420](https://www.kth.se/lediga-jobb/928557?l=en): KTH project scope, qualifications, selection criteria, proposed supervisors, and partner environment. The page may now display as closed because the advertisement period ended.
- [Related KI/SciLifeLab Nilsson-group doctoral advertisement](https://www.scilifelab.se/career/doctoral-phd-student-position-in-deep-learning-modeling-of-cancer/): source of the exact human-health question and related biologically constrained recurrent-model context. It is motivation and research context, **not** the KTH vacancy text.

**Final rule:** never stretch a connection to sound stronger. State what I did, what I learned, what transfers, and what I still need to learn. That combination is a stronger PhD answer than pretending the whole project is already complete.
