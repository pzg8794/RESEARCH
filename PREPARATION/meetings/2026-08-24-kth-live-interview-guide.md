# KTH LIVE INTERVIEW DASHBOARD — KEEP THIS OPEN

**Interview:** Aug 24, 2026 · **07:00 New York / 13:00 Stockholm**  
**Interviewers:** **Matthieu Barreau** + **Avlant Nilsson**  
**Position:** Deep Learning for Biological Systems · PA-2026-1420

> **DO NOT READ THIS PAGE. SCAN IT.**  
> **Bold words = talking cues.** Arrows = thought flow. Links = proof only if needed.

**Application:** [CV](../../APPLICATIONS/PhD/review-by-application/05-kth-deep-learning-biological-systems/2026-07-31-kth-deep-learning-biological-systems-cv.pdf) · [Application folder](../../APPLICATIONS/PhD/review-by-application/05-kth-deep-learning-biological-systems/) · [Detailed prep](./2026-08-24-kth-interviewer-focus-matthieu-avlant.md)

---

# 1. WHY IS THIS THE RIGHT FIT?

## QUESTION

**How do complex biological systems change over time — and how do we predict what happens when we perturb them?**

Think:

**STATE → DYNAMICS → PERTURBATION → RESPONSE → INTERVENTION**

This connects directly to what attracted me in the application:

- **“machine learning + mathematical modeling + biologically meaningful inference”**
- **“uncertainty, data quality, scientific interpretation”**
- **“complex interactions, heterogeneous data, uncertain structure”**
- **“cell-cell interactions, biological dynamics, healthier system states”**

### If they ask WHY THIS PROJECT

**Prediction alone is not enough**  
→ **learn dynamics**  
→ **respect biology/mechanism**  
→ **predict perturbation response**  
→ **support better intervention / precision medicine**

**One rescue sentence:**  
> What attracted me from the beginning was that this is not just a prediction problem; it is a biological dynamics and intervention problem.

---

## MY WORK

**Medical prediction**  
↓  
**Hospital readmission ML**  
↓  
**RNA structure + biological constraints**  
↓  
**RNA fairness / failure analysis**  
↓  
**RNA-seq / high-dimensional molecular data**  
↓  
**RNN/LSTM temporal modeling**  
↓  
**Bandits: context + uncertainty + prediction + intervention**  
↓  
**KTH: dynamic biological systems + perturbation**

### The bridge

**My recurring question:**  
> What information describes the system now, what has changed, what happens next, and what should we do when the system is uncertain or perturbed?

---

## ENVIRONMENT

### MATTHIEU

**dynamics · state · model mismatch · uncertainty · control · digital twins**

Think:

**Can the model represent the system well enough to justify intervention?**

### AVLANT

**signaling · gene regulation · metabolism · RNNs · perturbations · cancer · mechanism**

Think:

**Can the model learn how molecular state evolves and predict response under perturbation?**

### KTH + SciLifeLab + KI

**machine learning + biological mechanism + experiments + translation**

### Why the environment fits

**I do not want biology as “just another dataset.”**  
I want:

**COMPUTATION ↔ BIOLOGY ↔ EXPERIMENTAL VALIDATION**

---

# 2. COVER LETTER → WHAT I MEANT / WHAT I NOW SEE MORE CLEARLY

## “machine learning, mathematical modeling, and biologically meaningful inference”

**Then:** model biology carefully, not accuracy-only.  
**Now I can point to:**

- **Matthieu:** dynamical/system models + model fidelity
- **Avlant:** biologically constrained neural networks
- **Project:** unified cancer-cell model

---

## “uncertainty, data quality, and scientific interpretation”

**My evidence:**

- **BIO614:** strong-looking metrics ≠ correct biology
- **BIOL550:** QC/preprocessing affects biological conclusion
- **GA:** uncertainty + partial information + distribution change

---

## “careful modeling rather than predictive accuracy alone”

**BIO614 taught this directly:**

**synthetic success → realistic RNA failure → mechanism/topology mattered**

**Use if Avlant asks about biological meaning.**

---

## “complex interactions, heterogeneous data, and uncertain structure”

**Application idea**  
→ now more concrete through **signaling + gene regulation + metabolism + perturbation**.

**Do NOT claim:** “I already knew their exact architecture.”  
**Do say:** deeper reading showed how literally the project matched what I had already described.

---

## “cell-cell interactions, biological dynamics, and healthier system states”

**This was already in my cover letter.**

Now connect it to:

**cell interactions → evolving state → pathological equilibrium / behavior → perturb → healthier response**

---

## “interdisciplinary environment connecting machine learning, systems modeling, and translational biological research”

Now visible as:

**Matthieu / KTH DCS**  
+ **Avlant / KI / SciLifeLab**  
+ **experimental / biological collaborators**

**Rescue sentence:**  
> The deeper reading did not create the fit; it made the fit I described in the application much more concrete.

---

# 3. SUBMITTED SHORT ANSWERS — ANCHORS

## Q1 — WHY INTERESTED?

**Submitted:**  
> I am interested in this project because it combines deep learning, biological systems, and precision-medicine questions in a way that requires both strong modeling and careful scientific interpretation. The focus on cell-cell interactions and biologically meaningful system dynamics is especially compelling to me.

### SCAN CUES

**deep learning**  
+ **biological systems**  
+ **precision medicine**  
+ **strong modeling**  
+ **scientific interpretation**  
+ **cell-cell interactions**  
+ **system dynamics**

### If asked now

**Why?**  
→ not static prediction  
→ **dynamic state**  
→ **perturbation**  
→ **mechanism**  
→ **intervention**

---

## Q2 — WHAT CAN I CONTRIBUTE?

**Submitted:**  
> I can contribute reproducible machine-learning workflows, strong data-analysis practice, and experience working with noisy, high-dimensional biological data. I would bring disciplined evaluation, transparent reporting, and a computational perspective shaped by both ML research and computational biology work.

### SCAN CUES

**reproducible ML**  
**coding / data analysis**  
**noisy high-dimensional data**  
**evaluation discipline**  
**transparent reporting**  
**ML + computational biology bridge**

### Evidence to mention

- **BIO614** → validation + biological failure
- **BIOL550** → RNA-seq + QC
- **ISTE780** → comparative evaluation
- **GA** → structured experiments + uncertainty

---

# 4. TELL US ABOUT YOURSELF

### SAY THE ARC — NOT THE CV

**CS + Data Science**  
→ **ML / research engineering**  
→ **computational biology**  
→ **RNA structure + RNA-seq**  
→ **sequential learning / uncertainty**  
→ **want dynamic mechanistic biology**

### End on KTH

**deep learning + dynamics + cancer biology + intervention**

**Stop. Let them choose what to probe.**

---

# 5. RESEARCH / EXPERIENCE — FAST DEFENSE CARDS

## RIT GA — Quantum + AI

**What:** contextual / neural / adversarial bandits · routing · uncertainty · partial feedback · predictive context  
**Transfer:** **state/context → estimate → action → feedback → update**  
**KTH link:** temporal state + uncertainty + perturbation/intervention

**Proof:** [QuantumFaultTolerant](https://github.com/pzg8794/QuantumFaultTolerant) · [DSCI601](https://github.com/pzg8794/DSCI601-Project_Proposal) · [GA notes](https://drive.google.com/file/d/1Og91TkKAUk2euKtJtea5eAe1BjzzykdY/view?usp=drivesdk)

---

## BIO614 — RNA STRUCTURE

**What:** Nussinov DP + MFE + Turner + ViennaRNA · synthetic + real RNA · sensitivity/specificity/MCC  
**Big lesson:** **good metric ≠ biologically correct structure**  
**Failure:** tRNA / 5S → multiloops / topology missing  
**KTH link:** **structure/mechanism must constrain model**

**Proof:** [KTH sample](https://drive.google.com/file/d/1x_xLkbu-JGHrqH8gf7DaFwNMtGs-qquZ/view?usp=drivesdk) · [Overleaf](https://www.overleaf.com/project/68a761a470c296440522a537)

### If they mention the CV “deep learning enhancements” wording

**DO NOT DEFEND THE BAD PHRASE.**

Say simply:

> BIO614 itself was Nussinov plus thermodynamic modeling. My RNN/LSTM implementation came from Neural Networks coursework; the CV compressed those strands together too much.

---

## BIOL550 — RNA-SEQ

**What:** preprocessing · QC · alignment support · DESeq2 · PCA/distance/dispersion · biological interpretation  
**Big lesson:** **upstream data quality changes downstream biology**  
**KTH link:** noisy high-dimensional molecular data

**Proof:** [Repo](https://github.com/pzg8794/BIOL550-Project_Paper) · [Paper](https://github.com/pzg8794/BIOL550-Project_Paper/blob/main/main.tex) · [Pipeline](https://github.com/pzg8794/BIOL550-Project_Paper/blob/main/assets_methods/biol550_pipeline_architecture_diagram.svg)

---

## ISTE-780 — EQUITABLE BIOINFORMATICS

**What:** 20 RNA sequences · 6 methods · Optuna · CV · statistical tests · disparity auditing  
**Groups:** **RNA type · GC bin · length bin**  
**NOT:** human demographic groups  
**Big lesson:** **aggregate score can hide systematic failure**

**Proof:** [KTH sample](https://drive.google.com/file/d/1VvE4oNsAx6lFlppTv0VjI_GTGDsbkN-v/view?usp=drivesdk) · [Overleaf](https://www.overleaf.com/project/687b2ee4bacc2838e411460b)

---

## DSCI 640 — RNN / LSTM

**What I actually implemented:**

**Jordan + Elman recurrence**  
**forward pass**  
**BPTT / backward pass**  
**time-series prediction**  
**LSTM node + gates**

**Proof:** [RNN slides](https://drive.google.com/file/d/1E3V3M-cL8DdqpYRgkMLVzS5yDvbtjzJE/view?usp=drivesdk) · [Memory cells](https://drive.google.com/file/d/1ELmiTOTOreE9lQgGg-4Qs3-1PsLjAXRY/view?usp=drivesdk) · [LSTM assignment](https://drive.google.com/file/d/1K8zJDmrcyVUy3Yi6EPbn1XpIC8VxIWnP/view?usp=drivesdk)

---

## DSCI 633 — HOSPITAL READMISSION

**What:** diabetic readmission · data cleaning · feature engineering · Decision Tree / Random Forest / Logistic Regression / SVM · evaluation  
**Journey role:** **modern clinical ML workflow**

**Proof:** [Project PDF](https://drive.google.com/file/d/1R6NLciyevSHcyiBYvHjRX4jF8cGaqJuP/view?usp=drivesdk)

---

## BIG DATA MEDICAL DIAGNOSIS — EARLY WORK

**What:** medical-data quality · symptoms · temporal patterns · prediction/recommendation ideas  
**Journey role:** **health / diagnosis interest goes back years**  
**Do NOT oversell:** old work ≠ modern deep learning

**Proof:** [Artifact folder](https://github.com/pzg8794/opc-data-mining/tree/main/papers/Data%20Cleaning%20%26%20Processing/Data%20Cleaning/Big%20Data%20Medical%20Diagnosis%20-%20Papers) · [Paper 1](https://github.com/pzg8794/opc-data-mining/blob/main/papers/Data%20Cleaning%20%26%20Processing/Data%20Cleaning/Big%20Data%20Medical%20Diagnosis%20-%20Papers/Big%20Data%20Medical%20Diagnosis%20-%20Paper1/report.tex)

---

## VIOME

**What:** healthcare / microbiome data · preprocessing · feature engineering · ML experimentation · AWS  
**Use for:** **real-world noisy biological/health data**  
**Boundary:** proprietary code; do not claim ownership of VIOME biological models

**Context:** [Career evidence](../shared-career-evidence.md)

---

## VEDADATA

**What:** Python data pipelines · validation · statistical diagnostics · AWS · data quality  
**Use for:** **production data discipline**  
**Boundary:** proprietary code

**Context:** [Career evidence](../shared-career-evidence.md)

---

## UofR / NOYCE

**What:** K–12 CS · UDL · inclusion · communication across backgrounds  
**Use for:** **communication + collaboration + teaching complex ideas**

**Proof:** [EDE448](https://github.com/pzg8794/EDE448) · [Portfolio](https://github.com/pzg8794/EDE448-Communication_and_Behavioral_Support_Portfolio)

---

# 6. RESEARCH JOURNEY — ONE LOOK

```text
MEDICAL DIAGNOSIS / DATA QUALITY
            ↓
HOSPITAL READMISSION ML
            ↓
RNA STRUCTURE + BIOLOGICAL CONSTRAINTS
            ↓
FAIRNESS / FAILURE ANALYSIS
            ↓
RNA-SEQ + HIGH-DIMENSIONAL MOLECULAR DATA
            ↓
RNN / LSTM TEMPORAL MODELING
            ↓
BANDITS: CONTEXT + UNCERTAINTY + PREDICTION + ACTION
            ↓
KTH: BIOLOGICAL DYNAMICS + PERTURBATION + INTERVENTION
```

### If asked “HOW DID YOU GET HERE?”

**Health interest**  
→ **better ML**  
→ **deeper biological data**  
→ **mechanism + failure**  
→ **time / context / uncertainty**  
→ **dynamic biological intervention**

That is enough. **Do not narrate every project unless they ask.**

---

# 7. RNN / LSTM / ARIMA — EMERGENCY GLANCE

## RNN

**current input + previous state → new state → prediction**

```text
x(t) + h(t-1) → [RNN] → h(t) → prediction
```

**WHY:** sequence / time / history matters

---

## LSTM

**RNN + gated memory**

```text
FORGET → what old info matters?
INPUT  → what new info enters?
OUTPUT → what memory is exposed?
```

**c(t)** = longer-term cell memory  
**h(t)** = current hidden/output state

---

## ARIMA

**specified past values + past errors → forecast**

```text
x(t), previous errors → ARIMA → x_hat(t+1)
```

### REMEMBER

**ARIMA:** WE specify memory structure.  
**RNN:** NETWORK learns recurrent state.  
**LSTM:** RNN learns what to keep / forget through gates.

### OUR WORK

**iCPursuit:** ARIMA forecast → predicted context → bandit  
**original iCMAB direction:** EXAMM-RNN → future context/reward → bandit  
**KTH:** molecular history → recurrent biological state → future response under perturbation

---

# 8. THE PERTURBATION CONNECTION

### AVLANT

**observed phosphoproteomic trajectory**  
≠ automatically know **response under a new drug perturbation**

### OUR BANDIT WORK

**observed network performance**  
≠ automatically know **behavior after attack / changed conditions**

### COMMON COMPUTATIONAL QUESTION

**What happens when the environment changes?**

history  
→ learn/use state  
→ predict changed response  
→ adapt decision

**Domains are different. Methodological instinct is familiar.**

---

# 9. IF MATTHIEU ASKS...

## “What do you mean by dynamics?”

**state changes over time**  
**current state depends on previous state + input/perturbation**

```text
x(t+1) = f(x(t), u(t))
```

---

## “What about model mismatch?”

Go to **BIO614**:

**objective worked on synthetic motifs**  
→ **failed on realistic topology**  
→ model assumptions did not match biology

---

## “What about uncertainty?”

Go to **bandits**:

**partial feedback · confidence · exploration/exploitation · non-stationarity**

---

## “Control experience?”

**Do not bluff.**

**I have sequential decision / intervention reasoning.**  
**Formal control + system identification = area I want to deepen.**

---

# 10. IF AVLANT ASKS...

## “Why RNNs?”

**biological state evolves**  
**history matters**  
**multiple interacting variables**  
**multi-step prediction**  
**feedback / recurrence**

---

## “Why biological constraints?”

**less arbitrary model**  
**known interactions matter**  
**better interpretability**  
**more plausible perturbation predictions**

Caution: wrong priors can create **model mismatch**.

---

## “Biology experience?”

**BIO614** → RNA structure / thermodynamics  
**BIOL550** → RNA-seq / DE / QC  
**VIOME** → biological/health data pipeline context

Then stop.

---

# 11. GAPS — SAY THEM CLEANLY

**NOT yet:** cancer systems biologist  
**NOT yet:** formal control theorist

**YES:** ML · neural networks · reproducible experiments · sequential decisions · uncertainty · computational biology · molecular-data analysis

### If needed

> My strongest preparation is on the computational side. Cancer systems biology and formal control are exactly the areas I want to deepen in the PhD.

---

# 12. QUESTIONS FOR THEM

## BEST QUESTION

**Hardest bottleneck right now?**

- **learning state/dynamics?**
- **biological interpretability / identifiability?**
- **experimental validation of perturbation predictions?**

## SECOND

**First 6–12 months:**

- what should **I own independently?**
- where is the closest **DCS ↔ biology collaboration?**

---

# 13. TWO RESCUE LINES

### I do not know exact thing

> I have not worked on that exact problem yet. My closest experience is ___; what transfers is ___; the part I would need to deepen is ___.

### They want more depth

> I can go one level deeper into the implementation if useful.

---

# 14. LAST 10-SECOND RESET

**WHY:** health + dynamic biological modeling  
**MATTHIEU:** state · dynamics · mismatch · uncertainty · control  
**AVLANT:** mechanism · RNN · perturbation · validation  
**ME:** RNA · RNA-seq · RNN/LSTM · bandits · reproducibility  
**GAP:** cancer biology + formal control = learn  
**ASK:** bottleneck? / first-year ownership?
