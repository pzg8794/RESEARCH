# KTH LIVE INTERVIEW GUIDE — APPLICATION + OUR DISCUSSIONS

**Keep this page open during the interview.**  
Use it to answer questions such as:

- **Why did you say this in the application?**
- **What did you mean by this?**
- **What did you actually do?**
- **How does that connect to this PhD?**

The guide follows the **actual application language first**, then gives a **simple natural explanation** based only on the work and connections we already discussed.

**Application files:** [KTH application folder](../../APPLICATIONS/PhD/review-by-application/05-kth-deep-learning-biological-systems/) · [Submitted CV](../../APPLICATIONS/PhD/review-by-application/05-kth-deep-learning-biological-systems/2026-07-31-kth-deep-learning-biological-systems-cv.pdf)

---

# 1. THE MAIN FIT — QUESTION, WORK, ENVIRONMENT

## THE QUESTION THAT ATTRACTS ME

**How can we model a complex biological system well enough to understand how it changes and predict what happens when it is perturbed?**

This is the clearest way to connect what I wrote in the application to what I understand more deeply now.

### If they ask why this is interesting to me

Say:

> I am interested in problems where the model has to do more than predict a label. I want to understand how the system changes, what information matters over time, and how the response changes when the environment is perturbed.

That connects directly to things I already work with:

- **RNA structure:** biological structure matters; a good metric alone is not enough.
- **RNA-seq:** noisy molecular data and QC affect the biological conclusion.
- **RNN/LSTM work:** previous state affects the next state.
- **Bandit work:** context, uncertainty, changing conditions, prediction, and action.

---

## THE WORK I ALREADY BRING

The connection is **not** that my previous work is already cancer-cell modeling.

The connection is that I already work with pieces of the same kind of reasoning:

- **biological data**
- **model validation**
- **temporal / sequential information**
- **uncertainty**
- **context**
- **changing conditions / perturbations**
- **reproducible experiments**

### Simple way to say it

> My previous projects are in different domains, but the questions are familiar: what describes the state of the system, what information from the past matters, what happens when conditions change, and how do we know whether the model is actually reliable?

---

## THE ENVIRONMENT I WAS LOOKING FOR

This is what the cover letter meant by wanting an interdisciplinary environment.

- **Matthieu:** dynamics, model fidelity, uncertainty, system identification, control.
- **Avlant:** signaling, gene regulation, metabolism, recurrent biological models, perturbations.
- **KTH / SciLifeLab / KI:** computation connected to biological and experimental work.

### Simple way to say it

> What makes the environment especially attractive is that the computational model is not isolated from the biology. The machine-learning, dynamical-systems, and experimental sides are all part of the same research problem.

---

# 2. APPLICATION QUESTION 1 — WHY THIS POSITION?

## What is saved in the application record

> **I am interested in this project because it combines deep learning, biological systems, and precision-medicine questions in a way that requires both strong modeling and careful scientific interpretation. The focus on cell-cell interactions and biologically meaningful system dynamics is especially compelling to me.**

## If they ask: **“Why did you say that?”**

Say:

> Because I wanted a PhD where deep learning is being used to understand a biological system, not only to make a prediction. The focus on cell interactions and system dynamics means the model has to represent how the biology changes and how those interactions affect the outcome.

## If they ask: **“What do you mean by biologically meaningful system dynamics?”**

Say:

> I mean that the state at one point should be connected to what came before it and to the underlying biology — signaling, gene regulation, metabolism, and cell interactions — rather than treating each measurement as unrelated.

## If they ask: **“What work makes you ready for that?”**

Pick the most relevant 2–3:

- **BIO614** — structure + thermodynamics + failure on realistic RNA.
- **BIOL550** — RNA-seq + QC + biological interpretation.
- **DSCI640** — RNN/LSTM + temporal state/memory.
- **GA / DSCI601** — context + uncertainty + prediction + changing conditions.

**Proof:** [BIO614](https://drive.google.com/file/d/1x_xLkbu-JGHrqH8gf7DaFwNMtGs-qquZ/view?usp=drivesdk) · [BIOL550](https://github.com/pzg8794/BIOL550-Project_Paper) · [DSCI640 LSTM](https://drive.google.com/file/d/1K8zJDmrcyVUy3Yi6EPbn1XpIC8VxIWnP/view?usp=drivesdk) · [DSCI601](https://github.com/pzg8794/DSCI601-Project_Proposal)

---

# 3. APPLICATION QUESTION 2 — WHAT CAN I CONTRIBUTE?

## What is saved in the application record

> **I can contribute reproducible machine-learning workflows, strong data-analysis practice, and experience working with noisy, high-dimensional biological data. I would bring disciplined evaluation, transparent reporting, and a computational perspective shaped by both ML research and computational biology work.**

## If they ask: **“What do you mean by reproducible ML workflows?”**

Say:

> I mean being able to trace the experiment from preprocessing through the final result — the data preparation, model settings, baselines, metrics, logs, and analysis — so that the result can be repeated and challenged.

Examples:

- **GA:** repeated testbeds, common evaluation, logging, algorithm comparisons.
- **ISTE780:** common framework, Optuna, cross-validation, statistics.
- **BIOL550:** preprocessing/QC through differential expression.
- **BIO614:** same evaluation across synthetic and biological structures.

## If they ask: **“What noisy, high-dimensional biological data?”**

Say:

> The strongest example is the RNA-seq work in BIOL550. I also worked with RNA sequence and structure data in BIO614 and ISTE780, and I have industry experience with healthcare and microbiome-oriented data pipelines.

## If they ask: **“What does fairness-aware analytics contribute here?”**

Say:

> The transferable part is the evaluation habit. I am used to checking whether an overall score hides systematic failure under different kinds of inputs or conditions.

For **ISTE780**, the groups were:

- RNA type
- GC-content bin
- sequence-length bin

**Not human demographic groups.**

**Proof:** [ISTE780](https://drive.google.com/file/d/1VvE4oNsAx6lFlppTv0VjI_GTGDsbkN-v/view?usp=drivesdk) · [BIOL550](https://github.com/pzg8794/BIOL550-Project_Paper) · [QuantumFaultTolerant](https://github.com/pzg8794/QuantumFaultTolerant)

---

# 4. THE OTHER 500-CHARACTER VERSION I SHARED HERE

I also shared this wording in our discussion:

> **This project is compelling because deep learning for biological systems sits at the intersection of data-rich science and practical impact. I am especially interested in research that turns complex biological signals into reliable models, while staying attentive to evaluation quality, reproducibility, and the needs of downstream biomedical interpretation.**

If they use wording like **“complex biological signals,” “reliable models,” or “biomedical interpretation,”** the answer is the same:

> What I mean is that biological data are noisy and high-dimensional, so a useful model has to be evaluated carefully and still produce something that can be interpreted in the biological context.

And I shared this contribution wording:

> **I can contribute disciplined machine learning experimentation, strong coding and data analysis habits, and experience working with high-dimensional datasets and reproducible research workflows. My background in fairness-aware analytics, bioinformatics, and quantum/AI experimentation helps me approach biological modeling with care, quantitative rigor, and clear communication.**

If they ask **“What does quantum/AI experimentation add?”**:

> It gives me experience designing controlled comparisons under uncertainty and changing conditions. The quantum domain itself is different, but the experimental discipline and sequential reasoning transfer.

---

# 5. COVER LETTER — WHY THIS PROJECT

## What I wrote

> **I am drawn to this project because it combines machine learning, mathematical modeling, and biologically meaningful inference in a way that could directly support precision medicine.**

## If they ask: **“What did you mean by that?”**

Say:

> I meant that I want to work on models that do more than learn an input-output relationship. I want the model to represent something meaningful about the biological system so the prediction can support scientific understanding and, eventually, better intervention.

### What I understand more clearly now

The wording maps naturally to the work we later studied:

- **Matthieu:** learned models of dynamical systems + model fidelity + control.
- **Avlant:** biologically informed neural models + molecular interactions + perturbations.

### If they ask: **“Did you know all of that when you applied?”**

Say:

> I knew the scientific themes from the project description when I applied. Reading the group’s work more deeply afterward showed me how closely those themes matched the questions I was already interested in.

---

# 6. COVER LETTER — UNCERTAINTY, DATA QUALITY, SCIENTIFIC INTERPRETATION

## What I wrote

> **My goal is to contribute to research that builds strong computational models for complex biological systems while remaining careful about uncertainty, data quality, and the scientific interpretation of results.**

## If they ask: **“Why uncertainty?”**

Say:

> Because an estimate should not automatically be treated as equally reliable in every condition. In my bandit work, uncertainty affects whether the system trusts the current estimate, explores, or changes its decision.

## If they ask: **“Why data quality?”**

Say:

> BIOL550 made that very concrete. If preprocessing, QC, alignment, or other upstream steps are poor, the downstream differential-expression result can be misleading even if the analysis code runs correctly.

## If they ask: **“Why scientific interpretation?”**

Use BIO614:

> BIO614 is the clearest example. On simple synthetic motifs the method looked very strong, but on realistic tRNA and 5S structures it failed biologically. That showed me that a strong-looking metric is not enough if the model does not represent the structure that matters.

**Proof:** [BIO614](https://drive.google.com/file/d/1x_xLkbu-JGHrqH8gf7DaFwNMtGs-qquZ/view?usp=drivesdk) · [BIOL550](https://github.com/pzg8794/BIOL550-Project_Paper) · [QuantumFaultTolerant](https://github.com/pzg8794/QuantumFaultTolerant)

---

# 7. COVER LETTER — MY BACKGROUND

## What I wrote

> **My background combines graduate training in computer science and data science, applied machine learning experience, and current work in computational biology and high-dimensional data analysis.**

## If they ask: **“What computational biology?”**

Say:

> RNA secondary-structure prediction in BIO614, RNA-seq differential-expression analysis in BIOL550, and fairness-aware evaluation of RNA prediction methods in ISTE780.

Then stop unless they ask for one project in detail.

---

## What I wrote

> **In research and industry settings, I have built reproducible machine learning workflows across local, Colab, and GCP environments, with emphasis on evaluation discipline, data quality, and transparent technical reporting.**

## If they ask: **“Give me an example.”**

Say:

> My current GA work is the strongest research example. We compare multiple learning algorithms across different network conditions and threats using common evaluation, logging, and analysis so that we can tell whether a result is robust or just specific to one test.

If they ask about environment:

- local — development/testing
- Colab — coursework / experiments
- GCP — research compute
- AWS — prior industry work

---

## What I wrote

> **In computational biology coursework and project work, I have focused on sequencing data analysis, structured quality control, and interpretation of noisy biological signal.**

## If they ask: **“What did you actually do?”**

Say:

> In BIOL550 I worked through the RNA-seq pipeline from preprocessing and QC into differential-expression analysis and biological interpretation. In BIO614 I worked at the sequence and structure level, comparing predicted RNA structures with biological and synthetic references.

---

## What I wrote

> **That experience has made me especially motivated by questions where meaningful biological insight depends on careful modeling rather than predictive accuracy alone.**

## If they ask: **“What does that mean?”**

Say:

> BIO614 is the simplest example. The model could look successful on an easy structure and still fail on realistic RNA topology. That taught me that the biological question and the model assumptions matter as much as the final score.

---

# 8. COVER LETTER — WHAT INTERESTS ME MOST

## What I wrote

> **What interests me most in this position is the opportunity to work on deep learning methods for biological systems that connect computation with mechanistic and clinically relevant understanding.**

## If they ask: **“What do you mean by mechanistic understanding?”**

Say:

> I mean that the model should use or recover information about how the biological components interact, not only learn correlations that happen to predict an output.

## If they ask: **“Why is that important to you?”**

Say:

> Because if the goal is eventually to reason about intervention, I want to know why the model expects a response to change, not only that it predicts a different value.

---

## What I wrote

> **I am particularly interested in problems where machine learning must represent complex interactions, heterogeneous data, and uncertain structure without losing scientific usefulness.**

## If they ask: **“What kind of complex interactions?”**

Say:

> In this project, signaling, gene regulation, metabolism, and cell-cell interactions are the clearest examples. They influence one another, so the model needs to represent the state of the system rather than treat them as isolated measurements.

This is where the **RNN connection** fits naturally.

---

## What I wrote

> **The focus on modeling cell-cell interactions, biological dynamics, and healthier system states is compelling because it requires both methodological rigor and strong interdisciplinary reasoning.**

## If they ask: **“Why healthier system states?”**

Say:

> Because the interesting endpoint is not only describing the current cancer-promoting state. It is understanding the dynamics well enough to identify a perturbation that could move the system toward a healthier response.

Do not overclaim that I have already done this experimentally.

---

## What I wrote

> **My strongest current preparation is in machine learning, reproducible pipeline development, and biological-data analysis, and I would be excited to extend that preparation toward deeper work on biological modeling and precision medicine applications.**

## If they ask: **“What are your gaps?”**

Say:

> My strongest preparation is computational. I am not already a cancer systems biologist or a formal control theorist. Those are exactly the areas I want to deepen in this PhD while contributing immediately on the machine-learning, data, and evaluation side.

---

# 9. COVER LETTER — WHY KTH / THE ENVIRONMENT

## What I wrote

> **KTH is especially attractive because this project sits in a strong interdisciplinary environment connecting machine learning, systems modeling, and translational biological research.**

## If they ask: **“Why does that matter to you?”**

Say:

> Because I want the computational model to stay connected to the biological question and to experimental evidence. This project brings those pieces together rather than making the machine-learning work an isolated exercise.

### What we later learned that makes this sentence concrete

- **Matthieu / DCS:** modeling + dynamics + control.
- **Avlant / SciLifeLab / KI:** cancer biology + mechanistically informed deep learning.
- broader project: **in silico + in vitro** validation.

---

## What I wrote

> **I am looking for a PhD setting where strong computational work is directly connected to important biomedical questions, and where collaboration across technical and life-science domains is treated as central research practice.**

## If they ask: **“Why collaboration?”**

Say:

> Because I do not expect one person or one model to answer the whole biological question. I want to work where the computational assumptions can be challenged by people who understand the biology and where the biological questions can shape what we build computationally.

---

# 10. CV PROFILE — IF THEY QUOTE IT BACK TO ME

## CV says

> **Graduate researcher focused on deep learning and computational biology, with hands-on experience in neural network-based approaches to biological sequence and structure data.**

## If they ask: **“What hands-on neural-network work?”**

Say:

> My direct RNN/LSTM implementation comes from DSCI640 Neural Networks, where I worked with recurrent connections, forward and backward propagation, time-series prediction, and LSTM memory cells. In the biological projects, ISTE780 also compared neural-style RNA prediction baselines.

**Important:** BIO614 itself is **Nussinov + thermodynamics**, not an LSTM paper.

**Proof:** [RNN slides](https://drive.google.com/file/d/1E3V3M-cL8DdqpYRgkMLVzS5yDvbtjzJE/view?usp=drivesdk) · [LSTM assignment](https://drive.google.com/file/d/1K8zJDmrcyVUy3Yi6EPbn1XpIC8VxIWnP/view?usp=drivesdk) · [ISTE780](https://drive.google.com/file/d/1VvE4oNsAx6lFlppTv0VjI_GTGDsbkN-v/view?usp=drivesdk)

---

## CV says

> **RNA secondary structure prediction with thermodynamic deep learning enhancements (BIO614)**

## If they ask exactly what that means

Say:

> BIO614 combined Nussinov dynamic programming with thermodynamic information from Turner parameters and ViennaRNA/RNAfold. I would phrase the CV wording more carefully today: that manuscript itself is not a deep-learning paper. My deep-learning work is supported separately by Neural Networks coursework and related projects.

Do not try to defend an imprecise phrase by inventing an implementation.

---

## CV says

> **RNA-seq differential-expression analysis (BIO550)**

Say:

> I worked on a murine DRG RNA-seq reanalysis after sciatic nerve injury, including preprocessing, QC, differential expression with DESeq2, and interpretation of the gene-expression results.

**Proof:** [BIOL550 repo](https://github.com/pzg8794/BIOL550-Project_Paper)

---

## CV says

> **fairness-aware ML applied to bioinformatics diagnostics (ISTE-780)**

Say:

> I built a common evaluation framework for RNA prediction methods and checked whether performance differed systematically by RNA type, GC content, and sequence length. I treat that as methodological fairness at the sequence level, not demographic clinical fairness.

**Proof:** [ISTE780](https://drive.google.com/file/d/1VvE4oNsAx6lFlppTv0VjI_GTGDsbkN-v/view?usp=drivesdk)

---

## CV says

> **Current Graduate Assistant work deepens expertise in neural architectures, uncertainty quantification, and structured experimental methodology.**

Say:

> My GA work compares contextual, adversarial, and neural bandit methods under changing network conditions. The important transferable skills are uncertainty-aware decisions, predictive context, controlled evaluation, and understanding what happens when the environment changes.

**Proof:** [QuantumFaultTolerant](https://github.com/pzg8794/QuantumFaultTolerant) · [DSCI601](https://github.com/pzg8794/DSCI601-Project_Proposal)

---

# 11. RESEARCH & PROFESSIONAL EXPERIENCE — WHAT I ACTUALLY DID

## RIT — Graduate Assistant, Quantum and AI Research

### What I did

- built/evaluated contextual, adversarial, neural bandit methods
- quantum routing + qubit/resource allocation
- stochastic + adversarial conditions
- structured experiment design
- logging + common baselines
- uncertainty + partial feedback + predictive context

### If they ask why this matters for KTH

> The application domain is different, but I already think about evolving state, incomplete context, uncertainty, prediction, and how a decision should change when the environment changes.

**Proof:** [QuantumFaultTolerant](https://github.com/pzg8794/QuantumFaultTolerant) · [DSCI601](https://github.com/pzg8794/DSCI601-Project_Proposal) · [iCMAB integration notes](https://docs.google.com/document/d/19D_XEKoh6HEgOiXioooDyPGoSI1lWsUcKOOCUoHEZkQ/edit?usp=drivesdk)

---

## University of Rochester — NSF Noyce / CS Teacher Candidate

### What I did

- K–12 CS instruction
- computational thinking
- UDL / inclusive pedagogy
- adapting instruction to different learners
- explaining technical ideas clearly

### If they ask why this belongs in a research CV

> It strengthens my ability to communicate technical ideas, collaborate across different backgrounds, and explain complex systems clearly.

**Proof:** [EDE448](https://github.com/pzg8794/EDE448)

---

## BIO614 — RNA Structure Prediction

### What I did

- Nussinov dynamic programming
- thermodynamic MFE information
- Turner parameters
- ViennaRNA / RNAfold
- sensitivity / specificity / MCC
- synthetic + biological RNA structures

### Most important result

**Synthetic motifs worked very well. Realistic tRNA / 5S structures exposed major limitations.**

### If they ask what I learned

> A high metric does not automatically mean the biological structure is right. The model objective and the biological constraints have to match the real structure.

**Proof:** [KTH BIO614 sample](https://drive.google.com/file/d/1x_xLkbu-JGHrqH8gf7DaFwNMtGs-qquZ/view?usp=drivesdk) · [Overleaf](https://www.overleaf.com/project/68a761a470c296440522a537)

---

## BIOL550 — RNA-seq Differential Expression

### What I did

- preprocessing
- QC
- alignment support
- DESeq2
- PCA / distance / dispersion interpretation
- biological/pathway interpretation

### If they ask what I learned

> Upstream data quality and experimental assumptions can completely change the biological conclusion downstream.

**Proof:** [BIOL550 repo](https://github.com/pzg8794/BIOL550-Project_Paper) · [Pipeline diagram](https://github.com/pzg8794/BIOL550-Project_Paper/blob/main/assets_methods/biol550_pipeline_architecture_diagram.svg)

---

## ISTE780 — Equitable Bioinformatics

### What I did

- 20 RNA sequences
- six algorithmic approaches
- Optuna
- five-fold CV
- statistical testing
- disparity analysis by RNA type / GC / length

### If they ask why it matters

> It trained me to look beyond the average result and ask whether the model fails systematically under certain kinds of inputs.

**Proof:** [KTH ISTE780 sample](https://drive.google.com/file/d/1VvE4oNsAx6lFlppTv0VjI_GTGDsbkN-v/view?usp=drivesdk)

---

## VIOME

### What I did

- healthcare / microbiome-oriented data workflows
- preprocessing
- feature engineering
- ML experimentation / evaluation
- AWS environment

### If they ask what this contributes

> It gave me experience with real-world biological and health data where preprocessing and data quality are not clean academic assumptions.

**Boundary:** company code/data are proprietary.

---

## VEDADATA

### What I did

- Python data pipelines
- validation
- statistical diagnostics
- analytics-ready datasets
- AWS / cloud workflows
- data-quality checks

### If they ask what this contributes

> It gave me production discipline around data quality, repeatability, and traceable pipelines.

**Boundary:** company code/data are proprietary.

---

# 12. SELECTED TECHNICAL WRITING — THE JOURNEY

## Big Data Medical Diagnosis

**What it shows:** early interest in medical prediction + data quality + temporal patterns.

Say:

> The importance of that old work is that health-data prediction and data quality were already questions I was interested in very early. I would not describe that old project as modern deep learning.

**Proof:** [Artifact folder](https://github.com/pzg8794/opc-data-mining/tree/main/papers/Data%20Cleaning%20%26%20Processing/Data%20Cleaning/Big%20Data%20Medical%20Diagnosis%20-%20Papers)

---

## Predicting Hospital Readmission Rates — DSCI633

**What I did:** diabetic readmission prediction · cleaning · feature engineering · Decision Tree · Random Forest · Logistic Regression · SVM · evaluation.

Say:

> That project moved the health interest into a modern machine-learning workflow with model comparison and reproducible analysis.

**Proof:** [DSCI633 project](https://drive.google.com/file/d/1R6NLciyevSHcyiBYvHjRX4jF8cGaqJuP/view?usp=drivesdk)

---

## BIO614

**What it added:** molecular structure + thermodynamics + biological validation.

Say:

> That project pushed me from health-data prediction toward modeling actual biological structure and thinking much harder about whether a computational objective matches the biology.

---

## ISTE780

**What it added:** fairness / systematic failure / comparison across conditions.

Say:

> It made the evaluation question more explicit: where does the model work, where does it fail, and does the average hide important differences?

---

## BIOL550

**What it added:** high-throughput molecular data + QC + gene-expression interpretation.

Say:

> It gave me experience with a very different biological data type and reinforced how important preprocessing and experimental context are.

---

## DSCI601 / GA

**What it added:** time + context + uncertainty + action.

Say:

> This moved the question from only predicting a result to deciding what to do next when the system is changing and the information is incomplete.

**Proof:** [KTH-submitted DSCI601 sample](https://drive.google.com/file/d/1W2cLgsNpA5gilPmpaiM-dECPiVzjTSPO/view?usp=drivesdk) · [DSCI601](https://github.com/pzg8794/DSCI601-Project_Proposal)

---

# 13. RNN / LSTM / ARIMA — SIMPLE DEFINITIONS

## RNN

**Simple:** a neural network that carries information from previous time steps forward, so the current prediction depends on the current input **and** previous state.

```text
current input + previous state → new state → prediction
```

### Why useful here

> A biological system does not reset between measurements. Its current state depends partly on what happened before.

---

## LSTM

**Simple:** an RNN with gates that help it decide what information to keep, forget, and use over longer sequences.

```text
FORGET → what old information stays?
INPUT  → what new information is stored?
OUTPUT → what memory affects the current state?
```

---

## ARIMA

**Simple:** a statistical time-series model where we specify how previous values and previous errors are used to forecast the next value.

```text
past values + past errors → forecast
```

### Difference

- **ARIMA:** we specify the memory structure.
- **RNN:** the network learns a recurrent state.
- **LSTM:** the RNN also learns what to keep/forget through gates.

---

# 14. THE PERTURBATION CONNECTION WE DISCUSSED

## Avlant’s biological problem

Observed biological time-series data tell us what happened under the observed condition.

The harder question is:

**What will happen under a new drug / perturbation?**

## Our bandit / quantum problem

Observed network behavior tells us what happened under the observed condition.

The harder question is:

**What will happen when conditions change or an attacker perturbs the environment?**

### Simple way to explain the connection

> The biological and quantum domains are completely different, but the methodological question is familiar to me: observations under one condition do not automatically tell us what happens after a perturbation, so the model has to use structure, history, and context to predict or adapt.

---

# 15. WHY RNNs MAKE SENSE FOR THIS PROJECT

From the RNN material we reviewed:

- multiple variables can be predicted together
- future steps can be predicted beyond only `t+1`
- previous time steps influence the current state
- recurrent connections carry information forward
- LSTM helps keep useful longer-term information

### Simple way to say it

> RNNs make sense because the biological variables evolve together through time. The model needs a way to carry information from previous molecular states into the next state instead of treating every time point independently.

---

# 16. IF THEY ASK ABOUT MY GAPS

Say:

> My strongest preparation is in machine learning, data science, reproducible experimentation, sequential decision-making, and computational biology. I have not yet specialized in cancer systems biology or formal control, and those are areas I would expect to deepen during the PhD.

No apology. No exaggeration.

---

# 17. TWO QUESTIONS FOR THEM

### Scientific question

> From your perspective, what is currently the hardest part of the project: learning the biological state and dynamics from the available data, making the model biologically interpretable, or validating the perturbation predictions experimentally?

### First-year question

> What would you expect the doctoral student to own independently during the first six to twelve months, and where would the closest day-to-day collaboration between the computational and biological sides happen?

---

# 18. LAST-MINUTE REMINDERS

If they quote something from the application:

1. **Recognize the exact sentence.**
2. Explain **what I meant in plain English.**
3. Give **one concrete project**.
4. Stop and let them ask deeper.

If I do not know something:

> I have not worked on that exact problem yet. My closest experience is ____. What transfers is ____, and the part I would need to deepen is ____.
