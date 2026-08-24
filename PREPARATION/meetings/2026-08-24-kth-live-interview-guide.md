# KTH LIVE INTERVIEW GUIDE — WHAT I MEANT, WHY IT FITS, AND HOW I DEFEND IT

**Interview:** Aug. 24, 2026 · 07:00 New York / 13:00 Stockholm  
**Interviewers:** Matthieu Barreau + Avlant Nilsson  
**Position:** Doctoral student in deep learning for biological systems

> Keep this open during the interview. This is not a paper and not a script. It is a reminder of **what I meant when I wrote the application, why I was genuinely excited about it, what work backs it up, and what I can point to if they ask.**

**Application:** [folder](../../APPLICATIONS/PhD/review-by-application/05-kth-deep-learning-biological-systems/) · [submitted CV](../../APPLICATIONS/PhD/review-by-application/05-kth-deep-learning-biological-systems/2026-07-31-kth-deep-learning-biological-systems-cv.pdf)

---

# 1. THE PART THAT MADE THIS FEEL LIKE *MY* PHD

## The scientific question that clicked for me

The question underneath this project is basically:

> **Can we learn the state and dynamics of a complex biological system well enough to understand what is happening, predict what will happen when it is perturbed, and use that knowledge to identify a better intervention?**

That is why I got excited.

It is not just **“use deep learning on cancer data.”** It is the same kind of question I keep circling in my own work:

- What is the **state of the system now**?
- What **history/context** produced that state?
- What information is **missing, noisy, or uncertain**?
- What happens when the environment is **changed or perturbed**?
- Can the model predict what happens **next**, not just describe what already happened?
- Can that prediction help us choose a **better action/intervention**?

That is the thread connecting a lot of what I already do — even though the domains are different.

### If they ask, “Why are you so interested in this question?”

> I think this is where several directions I have been moving toward finally meet. I have been pulling my computational work toward health for years — medical diagnosis, hospital readmission, healthcare data, RNA structure, RNA-seq — and at the same time my machine-learning work has increasingly focused on context, sequence, uncertainty, changing conditions, and what happens next. What excited me here is that the biological problem itself needs all of those things. It is not only prediction; it is understanding an evolving system well enough to reason about what happens when you perturb it.

That is much closer to **why I actually want this PhD** than “I like deep learning.”

---

## Why the work feels connected to me

### BIO614 taught me: a model can look good and still be biologically wrong

I had simple synthetic RNA structures where the approach looked very strong.

Then realistic tRNA / 5S structures exposed the problem:

- high-looking specificity was not enough;
- the model was missing important topology / multiloop structure;
- the objective was simpler than the biology.

That changed how I think about biological modeling.

> **A good score is not enough if the model is not representing what actually matters biologically.**

That is exactly why “biologically meaningful inference” and “mechanistic understanding” in the KTH project matter to me.

**Proof:** [BIO614 KTH writing sample](https://drive.google.com/file/d/1x_xLkbu-JGHrqH8gf7DaFwNMtGs-qquZ/view?usp=drivesdk) · [Overleaf](https://www.overleaf.com/project/68a761a470c296440522a537)

---

### BIOL550 moved me into real high-dimensional molecular data

RNA-seq made the upstream side of biological modeling very concrete:

- preprocessing;
- QC;
- alignment evidence;
- differential expression;
- PCA / distance / dispersion;
- biological interpretation.

The lesson I carry into this project:

> **If the data and biological assumptions are weak, a sophisticated downstream model does not rescue the science.**

**Proof:** [BIOL550 repo](https://github.com/pzg8794/BIOL550-Project_Paper) · [main paper](https://github.com/pzg8794/BIOL550-Project_Paper/blob/main/main.tex) · [pipeline diagram](https://github.com/pzg8794/BIOL550-Project_Paper/blob/main/assets_methods/biol550_pipeline_architecture_diagram.svg)

---

### RNN/LSTM work made the “state over time” idea familiar

The part that clicked while reviewing DSCI 640:

**a system does not reset at every measurement.**

RNN idea:

```text
current input + previous state -> new state -> prediction
```

That is why RNNs feel natural for this project:

- signaling changes over time;
- gene regulation changes over time;
- metabolism changes over time;
- each current molecular state partly reflects what happened before;
- perturbations can push the trajectory somewhere different.

LSTM adds the idea of **learning what information to keep, forget, and expose**.

**Proof:** [RNN lecture](https://drive.google.com/file/d/1E3V3M-cL8DdqpYRgkMLVzS5yDvbtjzJE/view?usp=drivesdk) · [memory cells](https://drive.google.com/file/d/1ELmiTOTOreE9lQgGg-4Qs3-1PsLjAXRY/view?usp=drivesdk) · [LSTM implementation assignment](https://drive.google.com/file/d/1K8zJDmrcyVUy3Yi6EPbn1XpIC8VxIWnP/view?usp=drivesdk)

---

### Bandit / GA work made perturbation + changing conditions feel familiar

My quantum work is obviously not cancer biology.

The connection is the question underneath it:

- current observation is not always enough;
- context can be incomplete / noisy;
- conditions change;
- an attack or other perturbation can invalidate what worked before;
- the system has to decide using uncertainty and partial feedback.

That is why Avlant’s perturbation work immediately felt familiar conceptually.

**Their setting:** observed molecular trajectory does not automatically tell you the response to a new drug perturbation.  
**My setting:** observed network behavior does not automatically tell you how the policy behaves after attack / changing conditions.

Different science. Same instinct:

> **Do not assume the observed past tells you the changed future. Model the evolving state and test what happens when conditions change.**

**Proof:** [QuantumFaultTolerant](https://github.com/pzg8794/QuantumFaultTolerant) · [DSCI601](https://github.com/pzg8794/DSCI601-Project_Proposal)

---

## Why the environment feels unusually right

This is the other part we got excited about: **the environment itself mirrors the scientific question.**

### Matthieu

He brings the side I want to deepen:

- dynamical systems;
- state / system identification;
- model fidelity;
- uncertainty / robustness;
- control;
- digital-twin thinking.

So with him the question becomes:

> **Do we understand the dynamics well enough to trust the model and eventually use it to guide intervention?**

### Avlant

He brings the biological / mechanistic side:

- signaling;
- gene regulation;
- metabolism;
- molecular interaction networks;
- RNN-based biological modeling;
- time-series / perturbation;
- drug response;
- cancer.

So with him the question becomes:

> **Does the model actually represent enough of the biology to predict how molecular state changes under perturbation?**

### KTH + SciLifeLab + KI

This is what I meant in the cover letter by wanting an interdisciplinary environment.

I do **not** want to do machine learning where biology is simply handed to me as a feature matrix and the job ends at AUC.

I want:

> **computation + biological mechanism + experimental reality**

That is what makes this environment different for me.

### If they ask, “Why this environment specifically?”

> Because the environment matches the question. Matthieu’s side brings dynamics, model fidelity and control. Avlant’s side brings mechanistic cancer biology and perturbation. And the SciLifeLab/KI connection means the computational model stays connected to biological and experimental work. That is exactly the kind of environment I was trying to describe in the cover letter — one where I do not have to separate the computational question from the biological one.

---

# 2. APPLICATION QUESTION 1 — WHY THIS POSITION?

## What I wrote in the application

> **I am interested in this project because it combines deep learning, biological systems, and precision-medicine questions in a way that requires both strong modeling and careful scientific interpretation. The focus on cell-cell interactions and biologically meaningful system dynamics is especially compelling to me.**

## What I was really saying

This answer was already pointing at the exact things we later dug into more deeply:

**deep learning**  
→ not just because it is modern ML, but because the project needs a model that can represent complex nonlinear state.

**biological systems**  
→ not a single isolated measurement; signaling, regulation, metabolism, cell interactions all influence one another.

**precision medicine**  
→ the point is eventually to understand which perturbation/intervention makes sense for a particular biological state, not only classify disease.

**strong modeling + careful scientific interpretation**  
→ exactly the lesson from BIO614: the model can score well and still miss the biology.

**cell-cell interactions + system dynamics**  
→ this is what made the project feel like more than another biomedical ML application. It is about how the system evolves.

### If they point to this answer and ask, “Why did you write this?”

> Because this is where my work has been heading. I started with health-prediction questions years ago, then moved closer to the biology through RNA structure and RNA-seq, while my ML work kept moving toward context, sequence, uncertainty and changing conditions. When I saw that this project was about cell interactions and biological dynamics — not just classifying a sample — it clicked. It brings together the computational questions I already think about with the health and biological direction I have been deliberately moving toward.

### If they ask, “What do you mean by biologically meaningful system dynamics?”

> I mean that the current state of the cell should not be treated as if it appeared from nowhere. It comes from what happened before and from the interaction of signaling, gene regulation, metabolism and other cells. The part that excites me is learning that evolving state well enough to predict how it changes when the system is perturbed.

### If they ask, “Why precision medicine?”

> Because for me the useful endpoint is not only saying what state the system is in. It is understanding enough about that state and its dynamics to make a better prediction about which intervention could change the outcome.

### Work I can point to immediately

- **BIO614** → biological structure + model mismatch + interpretation
- **BIOL550** → noisy/high-dimensional molecular data + QC
- **DSCI640** → RNN/LSTM state over time
- **GA / DSCI601** → context + uncertainty + prediction under changing conditions

**Links:** [BIO614](https://drive.google.com/file/d/1x_xLkbu-JGHrqH8gf7DaFwNMtGs-qquZ/view?usp=drivesdk) · [BIOL550](https://github.com/pzg8794/BIOL550-Project_Paper) · [LSTM assignment](https://drive.google.com/file/d/1K8zJDmrcyVUy3Yi6EPbn1XpIC8VxIWnP/view?usp=drivesdk) · [DSCI601](https://github.com/pzg8794/DSCI601-Project_Proposal)

---

# 3. APPLICATION QUESTION 2 — WHAT CAN I CONTRIBUTE?

## What I wrote in the application

> **I can contribute reproducible machine-learning workflows, strong data-analysis practice, and experience working with noisy, high-dimensional biological data. I would bring disciplined evaluation, transparent reporting, and a computational perspective shaped by both ML research and computational biology work.**

## What I meant by that

I was not claiming to arrive as a finished cancer systems biologist.

I was saying I already bring a strong computational/research-engineering base that is useful immediately:

- I know how to turn an experiment into a reproducible pipeline;
- I am comfortable with messy/high-dimensional data;
- I compare models rather than falling in love with one;
- I pay attention to failure cases;
- I am used to uncertainty and partial information;
- I document what I did so someone else can challenge it.

### If they ask, “What can you contribute from day one?”

> On day one, my strongest contribution would be on the computational side: coding, reproducible experimentation, model evaluation, high-dimensional data analysis and careful comparison of methods. I also already have enough computational-biology experience to understand why QC, biological structure and interpretation matter. The cancer-systems-biology and formal-control depth are the parts I would be building with the group.

### If they ask, “What do you mean by reproducible workflows?”

> I mean I should be able to trace the result from the raw/prepared data through preprocessing, model settings, baselines, metrics, logs and final analysis. If a result only exists because one notebook happened to run once, I do not consider that strong research evidence.

**Examples:**

- GA → common testbeds, logging, algorithm comparison
- ISTE780 → common evaluation framework, Optuna, CV, statistics
- BIOL550 → preprocessing/QC through DE analysis
- BIO614 → controlled comparison across synthetic + biological examples

### If they ask, “What high-dimensional biological data?”

> BIOL550 is the strongest academic example because it involved RNA-seq data and the full analysis/QC story. BIO614 and ISTE780 gave me sequence/structure data experience, and VIOME gave me industry exposure to healthcare and microbiome-oriented data workflows.

### If they ask, “What does fairness-aware work add here?”

> The biggest transfer is the evaluation habit: do not let one aggregate score hide where the model systematically fails. In ISTE780 I looked across RNA type, GC-content bins and length bins. I treat that as sequence-level methodological fairness, not demographic clinical fairness.

**Links:** [ISTE780](https://drive.google.com/file/d/1VvE4oNsAx6lFlppTv0VjI_GTGDsbkN-v/view?usp=drivesdk) · [BIOL550](https://github.com/pzg8794/BIOL550-Project_Paper) · [QuantumFaultTolerant](https://github.com/pzg8794/QuantumFaultTolerant)

---

# 4. COVER LETTER — “MACHINE LEARNING, MATHEMATICAL MODELING, AND BIOLOGICALLY MEANINGFUL INFERENCE”

## What I wrote

> **I am drawn to this project because it combines machine learning, mathematical modeling, and biologically meaningful inference in a way that could directly support precision medicine.**

### If they ask what I meant

> I meant that I do not want the model to be useful only because it predicts well. I want its representation of the system to tell us something biologically meaningful about why the state changes and what could happen under intervention. That is what makes this more interesting to me than a normal classification problem.

### Why this now feels even more concrete

When I applied, I already knew the project description emphasized the themes.

After reading the team’s work more deeply, I could see the pieces more clearly:

- **Matthieu** → dynamical models, state, model fidelity, control
- **Avlant** → mechanistic neural models, signaling/regulation/metabolism, perturbation

### If they ask, “Did you only discover that after applying?”

> The interest was already there — that is why those words are in the cover letter and short answers. What the deeper reading did was make the fit much more concrete. I could see exactly how the two sides of the supervisory environment line up with the questions I was already trying to describe.

---

# 5. COVER LETTER — “UNCERTAINTY, DATA QUALITY, AND SCIENTIFIC INTERPRETATION”

## What I wrote

> **My goal is to contribute to research that builds strong computational models for complex biological systems while remaining careful about uncertainty, data quality, and the scientific interpretation of results.**

### Why uncertainty matters to me

My bandit work made this practical:

- estimates have different confidence;
- partial context matters;
- the best action can change when the environment changes;
- uncertainty affects exploration vs exploitation.

> I do not want a model to act as though every prediction is equally trustworthy.

### Why data quality matters to me

BIOL550:

> poor upstream QC / preprocessing can contaminate the entire downstream biological conclusion.

### Why scientific interpretation matters to me

BIO614:

> a model can look strong on one metric and still be wrong about the biology.

That is probably the strongest concrete example I can give.

---

# 6. COVER LETTER — “CAREFUL MODELING RATHER THAN PREDICTIVE ACCURACY ALONE”

## What I wrote

> **That experience has made me especially motivated by questions where meaningful biological insight depends on careful modeling rather than predictive accuracy alone.**

### If they ask “What experience?”

Go straight to BIO614:

> On simple synthetic RNA motifs, the model looked very strong. But on realistic tRNA and 5S structures, it failed to recover the biology because the objective and topology were too simple. That was a very useful lesson for me: a strong metric does not guarantee a biologically meaningful model.

### Why that points toward this PhD

> This project is attractive because the biological structure is not an afterthought. The whole point is to build a model whose dynamics and perturbation predictions remain meaningful in the biology.

---

# 7. COVER LETTER — “COMPLEX INTERACTIONS, HETEROGENEOUS DATA, AND UNCERTAIN STRUCTURE”

## What I wrote

> **I am particularly interested in problems where machine learning must represent complex interactions, heterogeneous data, and uncertain structure without losing scientific usefulness.**

### What that means here

The interactions are not abstract anymore:

- signaling;
- gene regulation;
- metabolism;
- cell-cell communication;
- perturbations / drug response.

### If they ask why that interests me

> Because those processes are not independent features. They influence one another and evolve together. That makes the problem much closer to learning the state of a system than simply fitting a predictor to a table.

This is where RNNs become a natural bridge.

---

# 8. COVER LETTER — “CELL-CELL INTERACTIONS, BIOLOGICAL DYNAMICS, AND HEALTHIER SYSTEM STATES”

## What I wrote

> **The focus on modeling cell-cell interactions, biological dynamics, and healthier system states is compelling because it requires both methodological rigor and strong interdisciplinary reasoning.**

### Why this sentence matters

This was already in the application **before** we did the deeper interviewer/paper reading.

So if they ask about it, I can genuinely say:

> That was one of the parts of the project description that caught me immediately. I was already interested in dynamic systems and decision-making under changing conditions, and here the state is biological and the intervention has a potential health consequence. That combination is exactly what I want to grow into.

### “Healthier system states” in plain language

> I mean understanding a cancer-promoting or pathological state well enough to predict what perturbation could move the system toward a healthier response. I am interested in the modeling problem behind that — not claiming I have already solved the biological-control problem myself.

---

# 9. COVER LETTER — WHY THE ENVIRONMENT

## What I wrote

> **KTH is especially attractive because this project sits in a strong interdisciplinary environment connecting machine learning, systems modeling, and translational biological research.**

> **I am looking for a PhD setting where strong computational work is directly connected to important biomedical questions, and where collaboration across technical and life-science domains is treated as central research practice.**

### If they ask, “Why does that matter to you?”

> Because I do not want to build the computational model in isolation and then hand it over to biology at the end. I want the biological question to shape the model from the beginning, and I want experimental evidence to be able to challenge what the model thinks it has learned.

### Why this particular team makes sense to me

**Matthieu** → dynamics / control / model fidelity  
**Avlant** → mechanism / cancer biology / perturbation  
**SciLifeLab / KI / KTH** → computational + experimental life-science environment

> That combination is almost exactly the environment I was trying to describe in the letter before I knew the details as deeply as I do now.

---

# 10. MY RESEARCH JOURNEY — IF THEY ASK “HOW DID YOU END UP HERE?”

This is not six unrelated projects.

It is a direction that kept getting more biological and more dynamic.

```text
Big Data Medical Diagnosis
health + prediction + data quality
        ↓
Hospital Readmission ML
modern clinical ML workflow
        ↓
BIO614 RNA Structure
biological structure + mechanism + model failure
        ↓
ISTE780
where does the model fail across conditions/groups?
        ↓
BIOL550 RNA-seq
high-dimensional molecular data + QC + interpretation
        ↓
RNN / LSTM
history + state + temporal evolution
        ↓
Bandits / GA
context + uncertainty + changed conditions + action
        ↓
KTH
biological dynamics + perturbation + intervention
```

### Natural answer

> I did not start by saying I wanted to build cancer RNNs. The direction developed over time. I was interested in medical prediction very early, then modern clinical ML, then moved closer to the biological mechanisms through RNA structure and RNA-seq. At the same time my ML work kept becoming more sequential and uncertainty-aware. This project feels like the point where those two directions finally meet.

---

# 11. RESEARCH / PROFESSIONAL EXPERIENCE — IF THEY ASK “WHAT DID YOU ACTUALLY DO?”

## RIT Graduate Assistant — Quantum + AI

**What I did:**

- multi-armed / contextual / adversarial / neural bandit evaluation;
- quantum routing / resource allocation;
- uncertainty-aware exploration;
- changing / adversarial environments;
- predictive context;
- reproducible multi-testbed evaluation;
- manuscript-level technical analysis.

**How it transfers:**

> state/context + uncertainty + changing conditions + action + feedback.

**Proof:** [QuantumFaultTolerant](https://github.com/pzg8794/QuantumFaultTolerant) · [DSCI601](https://github.com/pzg8794/DSCI601-Project_Proposal)

---

## BIO614 — RNA Structure

**What I did:**

- Nussinov dynamic programming;
- MFE / Turner parameters / ViennaRNA;
- environmental / energy corrections;
- synthetic + biological RNA validation;
- sensitivity / specificity / MCC;
- structure visualization;
- failure analysis.

**What I learned:**

> biological validity != one strong metric.

**Proof:** [KTH writing sample](https://drive.google.com/file/d/1x_xLkbu-JGHrqH8gf7DaFwNMtGs-qquZ/view?usp=drivesdk)

### CV wording warning

If they quote **“thermodynamic deep learning enhancements”**:

> The BIO614 manuscript itself was Nussinov plus thermodynamic modeling. My RNN/LSTM implementation came from my Neural Networks coursework. The CV compressed those two strands too much.

---

## BIOL550 — RNA-seq

**What I did:**

- preprocessing / QC;
- alignment evidence;
- DESeq2 differential expression;
- PCA / distance / dispersion interpretation;
- biological / pathway interpretation.

**Proof:** [repo](https://github.com/pzg8794/BIOL550-Project_Paper) · [pipeline](https://github.com/pzg8794/BIOL550-Project_Paper/blob/main/assets_methods/biol550_pipeline_architecture_diagram.svg)

---

## ISTE780 — Equitable Bioinformatics

**What I did:**

- RNA structure methods comparison;
- 20-sequence final dataset;
- six method families;
- Optuna;
- five-fold CV;
- statistical tests;
- sequence-level disparity auditing.

**Groups actually used:** RNA type · GC-content bin · length bin.

**NOT:** human demographic fairness.

**Proof:** [KTH writing sample](https://drive.google.com/file/d/1VvE4oNsAx6lFlppTv0VjI_GTGDsbkN-v/view?usp=drivesdk)

---

## DSCI640 — RNN / LSTM

**What I implemented / worked with:**

- Jordan recurrence;
- Elman recurrence;
- recurrent forward pass;
- recurrent backpropagation / BPTT;
- time-series prediction;
- LSTM node / gates.

**Proof:** [RNN lecture](https://drive.google.com/file/d/1E3V3M-cL8DdqpYRgkMLVzS5yDvbtjzJE/view?usp=drivesdk) · [LSTM assignment](https://drive.google.com/file/d/1K8zJDmrcyVUy3Yi6EPbn1XpIC8VxIWnP/view?usp=drivesdk)

---

## VIOME

**What I can defend:** healthcare / microbiome-oriented data workflows, preprocessing, feature engineering, ML experimentation/evaluation, AWS context.

**Boundary:** proprietary employer work; do not pretend there is a public repo proving production details.

---

## VEDADATA

**What I can defend:** Python data pipelines, ingestion, preprocessing/validation, statistical diagnostics, analytics-ready data, AWS / traceable quality checks.

**Boundary:** proprietary employer code.

---

# 12. SELECTED TECHNICAL WRITING — THE JOURNEY THEY SAW ON THE CV

## Big Data Medical Diagnosis

**Why it matters in the story:** I was already trying to connect computation, prediction, and health years ago.

**Do not oversell it as modern deep learning.**

**Proof:** [artifact folder](https://github.com/pzg8794/opc-data-mining/tree/main/papers/Data%20Cleaning%20%26%20Processing/Data%20Cleaning/Big%20Data%20Medical%20Diagnosis%20-%20Papers)

---

## Predicting Hospital Readmission Rates — DSCI633

**What:** diabetic readmission prediction · feature engineering · model comparison · evaluation.

**Methods:** Decision Tree · Random Forest · Logistic Regression · SVM.

**Proof:** [project PDF](https://drive.google.com/file/d/1R6NLciyevSHcyiBYvHjRX4jF8cGaqJuP/view?usp=drivesdk)

---

## BIO614 Final Project

**What:** RNA structure + thermodynamic modeling + rigorous validation + biological failure analysis.

**Proof:** [writing sample](https://drive.google.com/file/d/1x_xLkbu-JGHrqH8gf7DaFwNMtGs-qquZ/view?usp=drivesdk)

---

## Equitable Bioinformatics — ISTE780

**What:** fairness-style evaluation of RNA prediction methods across sequence conditions.

**Proof:** [writing sample](https://drive.google.com/file/d/1VvE4oNsAx6lFlppTv0VjI_GTGDsbkN-v/view?usp=drivesdk)

---

## BIOL550 — Differential Gene Expression

**What:** reproducible bulk RNA-seq pipeline + DESeq2 + QC + biological interpretation.

**Proof:** [repo](https://github.com/pzg8794/BIOL550-Project_Paper)

---

## DSCI601 — Fairness-Aware Bandits

**What:** sequential decision-making under partial feedback, context, uncertainty, non-stationarity, with quantum and **synthetic clinical** settings.

**Proof:** [KTH writing sample](https://drive.google.com/file/d/1W2cLgsNpA5gilPmpaiM-dECPiVzjTSPO/view?usp=drivesdk) · [repo](https://github.com/pzg8794/DSCI601-Project_Proposal)

---

# 13. RNN / LSTM / ARIMA — QUICK DEFINITIONS IF THEY COME UP

## RNN

**Simple:** neural network for sequential data that carries a learned state from previous time steps.

```text
x(t) + h(t-1) -> RNN -> h(t) -> prediction
```

**Why here:** molecular state now partly depends on molecular state before.

---

## LSTM

**Simple:** RNN with gated memory that learns what to keep, forget, and expose.

```text
FORGET -> what old info stays?
INPUT  -> what new info enters?
OUTPUT -> what memory affects the current state?
```

---

## ARIMA

**Simple:** statistical forecasting model where we specify how past values / errors enter the forecast.

**Our current iCPursuit:** ARIMA -> predicted context -> bandit decision.

### Difference I should remember

**ARIMA:** we specify the memory structure.  
**RNN:** network learns a recurrent state.  
**LSTM:** RNN with gated longer-term memory.

---

# 14. IF THEY ASK ABOUT MY GAPS

Do not apologize for them.

> My strongest preparation is on the computational side — machine learning, neural networks, reproducible experimentation, sequential decision-making and computational-biology data analysis. I am not already a cancer systems biologist or a formal control theorist. Those are precisely the areas I want to deepen here.

---

# 15. QUESTIONS I WANT TO ASK THEM

## Best one

> Because the project sits between DCS and the biological/experimental side, what do you currently see as the hardest scientific bottleneck: learning the underlying state and dynamics from the available data, making the model sufficiently identifiable and biologically interpretable, or experimentally validating the intervention predictions?

## Second

> What would you want the doctoral student to own independently during the first six to twelve months, and where do you expect the closest day-to-day collaboration between DCS and the biological team?

---

# 16. IF I FREEZE — COME BACK TO THIS

**WHY I WANT IT:**  
I have been moving my computing toward **human health + deeper biology**, and this project combines **dynamic modeling + biological mechanism + perturbation + intervention**.

**WHY I FIT:**  
RNA structure · RNA-seq · RNN/LSTM · uncertainty · sequential decisions · reproducible experiments.

**WHY THIS TEAM:**  
Matthieu = dynamics/control.  
Avlant = mechanism/cancer/perturbation.  
SciLifeLab/KI/KTH = computation connected to experimental biology.

**WHAT I DO NOT CLAIM:**  
I am not already a cancer systems biologist or control theorist. I am coming in with the computational foundation and biological trajectory to grow into exactly that intersection.
