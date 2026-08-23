# KTH PhD Interview Preparation - Deep Learning for Biological Systems

**Interview:** Monday, 2026-08-24, 13:00 Stockholm / 07:00 New York  
**Format:** Zoom, 20 minutes  
**Interviewers:** Matthieu Raphael Barreau (KTH Decision and Control Systems) and Avlant Nilsson (Karolinska Institutet / SciLifeLab)  
**Position:** Doctoral student in deep learning for biological systems, KTH School of Electrical Engineering and Computer Science  
**KTH reference:** PA-2026-1420  

> **Purpose of this document:** Be ready to explain the application clearly, defend every major claim honestly, connect prior work to the actual KTH project, and leave the interviewers wanting a longer technical conversation.
>
> This is a public-safe preparation kit. It intentionally omits the private Zoom link, meeting ID, private email text, travel details, and private academic-record files.

---

## 1. The 20-minute objective

This is not enough time for a comprehensive oral examination. The invitation says the purpose is to further evaluate the application and fit after the applications were reviewed. The KTH advertisement gives a useful scorecard: independence, collaboration, professionalism, ability to analyze complex problems, biological-systems interest/experience, research ability, communication, deep-learning experience, study results, and prior specialization in machine learning, control theory, or mathematics.

### What they are most likely trying to decide

1. **Is the technical depth behind the CV real?**
2. **Can Piter explain research compactly and accurately?**
3. **Does he understand what this project actually is - biological dynamics and cell-cell interactions, not generic biomedical classification?**
4. **Can his ML/data-science background grow into scientific machine learning, dynamical systems, and control?**
5. **Does he have enough biological grounding to collaborate productively with cancer/systems-biology researchers?**
6. **Is he intellectually honest about the boundary between completed work, exploratory work, and future interests?**
7. **Would these supervisors want to work with him for four years?**

### Likely interview shape - inference, not a confirmed agenda

- **1-2 min:** greetings and context
- **2-3 min:** "Tell us about yourself" / motivation
- **10-12 min:** research, technical depth, fit, and application validation
- **3-4 min:** candidate questions / next steps

**Implication:** Answers should usually be **30-75 seconds**, not five-minute lectures. Give the core answer, then stop and let them probe.

---

## 2. The project in one sentence

**Develop scientifically meaningful deep-learning/dynamical models of cancer cell-cell interactions, validate them with in silico and in vitro evidence, build digital twins of those interactions, and use the models to identify interventions that can steer pathological cellular systems toward healthier states.**

Official posting: <https://www.kth.se/lediga-jobb/928557?l=en>

### The project is NOT merely

- cancer classification;
- static prediction from tabular biomarkers;
- a generic deep-learning benchmark;
- a pure bioinformatics sequence-analysis project;
- or a fairness project.

Those experiences are useful evidence, but the research target is **dynamic, mechanistic, interacting biological systems and intervention**.

---

## 3. Why the supervisory team matters

### Matthieu Barreau - modeling, dynamics, scientific ML, control

Matthieu is an Assistant Professor in KTH Decision and Control Systems and a WASP Fellow. His KTH profile emphasizes dynamical systems, robust control, optimization, Physics-Informed Neural Networks, model fidelity, sparse/noisy measurements, and digital-twin thinking. He is also examiner/course responsible for **Scientific Machine Learning for Modeling and Control of Dynamical Systems (FEL3751)**.

Useful mental model: **Matthieu may be asking whether Piter can move from "train a model" to "learn a trustworthy dynamical model that respects structure and can eventually be controlled."**

Sources:
- <https://www.kth.se/profile/barreau>
- <https://www.kth.se/kurs-pm/FEL3751?l=en>

### Avlant Nilsson - mechanistic cancer AI, molecular networks, multiomics

Avlant Nilsson is an Assistant Professor at Karolinska Institutet and a DDLS Fellow/group leader at SciLifeLab. His group develops **mechanistically / biologically informed neural models of cancer**, integrating prior molecular interaction networks with transcriptomics, proteomics, metabolomics, perturbations, and time-resolved data. The group aims to understand signaling, gene regulation, metabolism, drug response/resistance, and tumor-microenvironment interactions, particularly cancer-stroma interactions.

A particularly relevant 2026 direction uses biologically informed recurrent neural networks trained on phosphoproteomic time series to predict dynamic drug responses, including zero-shot perturbation responses.

Useful mental model: **Avlant may be asking whether Piter understands why biology cannot simply be treated as an arbitrary feature matrix, and whether he can reason about mechanisms, networks, perturbations, and experimental validation.**

Sources:
- <https://www.scilifelab.se/researchers/avlant-nilsson/>
- <https://www.scilifelab.se/career/doctoral-phd-student-position-in-deep-learning-modeling-of-cancer/>
- <https://publications-affiliated.scilifelab.se/publication/53deef8658d14591b6b08382650120d7>

### Other proposed supervisors - know them, even though they are not in this 20-minute interview

**Alexandre Proutiere, Professor, KTH DCS:** probability, optimization, machine learning, reinforcement learning, data-efficient decision-making. This is a natural connection to Piter's bandit/sequential-decision experience.  
<https://www.kth.se/profile/alepro/>

**Anna Herland, Professor, KTH/SciLifeLab:** microphysiological and organ-on-chip systems, cell-cell interactions, patient-relevant in vitro models, sensing, and drug-development platforms. Her role helps explain the project's **in vitro validation** dimension.  
<https://www.kth.se/profile/aherland?l=en>

### The key bridge

The team itself spans the project:

**biological mechanism + deep learning + dynamical systems/control + experimental validation.**

That is the interdisciplinary identity Piter should demonstrate.

---

## 4. What KTH actually received from this application

Canonical packet record:
`APPLICATIONS/PhD/review-by-application/05-kth-deep-learning-biological-systems/`

Submitted packet included:

- tailored KTH CV;
- tailored cover letter;
- BIO614/BIO630 RNA-structure project proposal;
- ISTE780 fairness-aware bioinformatics manuscript;
- DSCI601 fairness-aware bandits / clinical-and-quantum decision-systems manuscript;
- two optional Varbi responses.

Packet status:
`APPLICATIONS/PhD/application-materials/2026-07-31-kth-deep-learning-biological-systems-packet-status.md`

### What the cover letter promised

The application positioned Piter around:

- machine learning + mathematical modeling + biological inference;
- precision-medicine motivation;
- reproducible ML workflows;
- careful evaluation and data quality;
- high-dimensional/noisy biological data;
- biological interpretation rather than predictive accuracy alone;
- cell-cell interactions, biological dynamics, and healthier system states;
- a desire to grow deeper into biological modeling.

### Optional answer 1 - core message

Interest in the convergence of **deep learning + biological systems + precision medicine**, especially cell-cell interactions and biologically meaningful system dynamics.

### Optional answer 2 - core contribution

**Reproducible ML workflows + disciplined data analysis + noisy/high-dimensional biological data + transparent reporting + computational perspective bridging ML and computational biology.**

### Important packet-version note

The repository records later CV-quality improvements after the May submission. Do **not** assume every later canonical CV sentence was seen by KTH. For interview preparation, the May-submitted KTH PDF and packet record are the relevant evidence.

---

## 5. Opening answer - 60 to 75 seconds

Do not memorize every word. Memorize the **arc**.

> Thank you for the opportunity. My background is in computer science and data science, and over the last few years I have been moving deliberately toward computational biology and scientific machine learning. At RIT I am completing my master's in Data Science, where my application-facing GPA is 3.9, and I also work as a Graduate Assistant on AI and quantum research, focusing heavily on reproducible evaluation and learning under uncertainty. My biological-computing work includes RNA secondary-structure modeling using dynamic programming and thermodynamic information, high-throughput sequencing and RNA-seq analysis, and a fairness-aware bioinformatics project. What attracts me to this PhD is that it goes beyond static prediction: the goal is to model interacting biological systems, connect those models to mechanisms and experiments, and eventually use them to reason about intervention. The combination of deep learning, dynamical systems and control, and cancer biology is exactly the direction in which I want to develop as a researcher.

### What this answer accomplishes

- establishes CS/data-science foundation;
- establishes biological trajectory without pretending to be a cancer biologist;
- mentions current AI research without hijacking the interview with quantum;
- gives a precise reason for wanting **this** PhD;
- creates openings for them to ask about RNA, deep learning, bandits, uncertainty, or biology.

---

## 6. "Why this PhD?" - 45 to 60 seconds

> What attracts me is that this is not simply a prediction problem. The project is trying to learn biologically meaningful dynamics of interacting cells, validate those models experimentally, and ultimately reason about how to perturb a pathological system toward a healthier state. That requires machine learning, but also system identification, mechanistic constraints, uncertainty, and control. My current strengths are machine learning, reproducible experimentation, sequential decision-making, and biological-data analysis. I see this PhD as the place where those strengths can converge while I deepen the areas I have not yet specialized in, particularly cancer systems biology and formal control of biological systems.

**Key phrase:** *"I am not looking for biology as just another dataset; I am interested in models whose internal structure and predicted interventions mean something biologically."*

---

## 7. Your three strongest research stories

### Story A - RNA structure: the best "real research" story

**Project:** RNA Secondary Structure Prediction and Visualization: Implementing the Nussinov Algorithm with MFE Enhancements.

What was actually done:

- classical Nussinov dynamic programming;
- thermodynamic MFE information using ViennaRNA/RNAfold and Turner parameters;
- environmental/energy corrections;
- validation using sensitivity, specificity, MCC and energetic comparisons;
- biological and synthetic RNA structures;
- reproducible visualization and benchmarking.

#### The most valuable part: it failed in an informative way

Simple synthetic positive controls such as the hairpin and mini-helix could be recovered extremely well, but realistic tRNA-Phe and 5S rRNA structures exposed severe limitations. The model favored nested/long-distance base-pair maximization and lacked explicit treatment of multiloops, junctions, pseudoknots and richer topology. High specificity did not mean biologically correct folding; sensitivity on those biological examples was effectively zero.

That is a **better PhD interview story than claiming >90% accuracy**.

#### 60-second explanation

> I started from Nussinov dynamic programming and added thermodynamic information from ViennaRNA and Turner parameters. On simple synthetic motifs the approach could recover the intended structures very well, which was useful as a positive control. But when I moved to realistic tRNA and 5S rRNA, the model failed despite superficially strong metrics such as specificity. It was maximizing a simplified objective and missing important topology such as multiloops and junctions. The main lesson for me was that biological validity cannot be inferred from one aggregate metric, and adding more scoring terms does not automatically make a model mechanistic. That is actually one reason the KTH project interests me: I want to work on models where biological structure is part of the model design and validation.

**If Matthieu hears this:** it shows model mismatch, objective design, validation discipline.  
**If Avlant hears this:** it shows respect for biological mechanism and that you learned from failure.

---

### Story B - ISTE780: fairness-aware bioinformatics

What the submitted manuscript actually did:

- an exploratory RNA fairness methodology study;
- final dataset of 20 sequences, including tRNA/rRNA/miRNA/synthetic and fairness-augmentation sequences;
- comparisons across Enhanced Nussinov, EnergyMin, ML-feature, Transformer-style, graph-neural, and k-mer logistic baselines;
- Optuna-driven optimization;
- five-fold cross-validation and statistical testing;
- fairness-style grouping by **sequence type, GC-content bin, and length bin**;
- post-processing calibration and disparate-impact monitoring.

#### Safe framing

> I was asking a methodological question: if an algorithm performs differently across meaningful classes of biological inputs, can we audit that systematically rather than hide it in aggregate performance? I adapted group-disparity tools to sequence characteristics such as type, GC content and length. I treat that as exploratory methodological work, not evidence that I measured human demographic fairness or demonstrated a clinical health-equity effect.

This distinction matters. The submitted manuscript uses strong clinical/equity motivation, but the experiment itself is **sequence-level**, not a human clinical cohort.

---

### Story C - DSCI601 / GA: sequential decisions under uncertainty

Submitted sample title:
**Fairness-Aware Bandits for Network Routing in Quantum & Clinical Settings via Multi-Armed, Contextual, and Informative Contextual Decision Spectra**.

The manuscript includes Piter Garcia with Daniel Krutz and Travis Desell; describe authorship/contribution accurately if asked.

Core technical idea:

- bandit feedback / partial observability;
- non-contextual vs contextual policies;
- missing, delayed or noisy context;
- non-stationarity;
- utility vs disparity tradeoffs;
- evaluation across quantum routing and a **synthetic clinical simulation**.

#### Safe framing for this KTH interview

> The part most relevant to KTH is not the quantum domain itself; it is learning and decision-making under partial information. I have been working with sequential policies where the system observes incomplete context, chooses an action, receives only partial feedback, and must remain robust to changing conditions. That has trained me to think about uncertainty, state information, intervention, and evaluation over time - concepts that I think transfer naturally to dynamical biological systems, while the biology and formal control setting here are much richer.

**Never imply the clinical results came from real patients.** The manuscript explicitly describes an embedded synthetic clinical environment.

---

## 8. Deep-learning experience - answer this carefully

The KTH advertisement explicitly values deep-learning experience, so this is likely to be probed.

### Strong, defensible evidence

- RIT graduate **Neural Networks** coursework; current academic requirements show the course completed with an A.
- Graduate AI/quantum research involving learning algorithms, uncertainty and reproducible evaluation.
- PyTorch/TensorFlow/Keras familiarity listed in the submitted CV.
- ISTE780 explored neural baselines in a bioinformatics evaluation framework.
- Industry experience at VIOME in healthcare AI / microbiome data pipelines.

### Important honesty boundary

The submitted BIO614 RNA paper itself is primarily **dynamic programming + thermodynamic modeling**. The paper text we recovered does **not** substantiate the submitted CV's stronger LSTM-extension wording.

If asked directly:

> My strongest validated biological project in the submitted writing sample is not a deep-learning paper; it is a hybrid algorithmic and thermodynamic RNA-modeling project. My formal deep-learning foundation comes from my neural-networks coursework and broader ML work, with exploratory neural components in other projects. One reason I am applying for this PhD is precisely to bring those streams together at a much deeper research level.

If there is actual LSTM code you personally implemented and can explain line-by-line, describe it. If not, do **not** invent details to defend a CV sentence.

---

## 9. Technical concepts to be able to explain without notes

### 9.1 Cell-cell interactions / tumor microenvironment

Cancer cells do not operate in isolation. Tumor behavior can depend on communication with stromal cells, immune cells, vascular cells and other surrounding components. Cells exchange ligands and other signals; reciprocal signaling can create feedback loops that stabilize a pathological state.

**Interview-level explanation:**

> A cell-cell interaction model should represent not only each cell's internal state but how one cell's secreted signals or surface interactions change the state-transition dynamics of another. In cancer, reciprocal signaling between tumor and stromal cells can create self-reinforcing loops, so a useful model should help identify which interactions are causal enough to perturb.

### 9.2 Cancer-promoting equilibrium / attractor

Think of a cellular state as a point in a high-dimensional dynamical system. Feedback between signaling, gene regulation, metabolism and intercellular communication can stabilize an undesirable state or attractor.

You do not need to claim every biological system has a mathematically proven equilibrium. Use the language as a modeling objective:

> The challenge is to learn enough of the dynamics to identify persistent cancer-promoting states and then test whether a perturbation can move the system toward a healthier basin or response regime.

### 9.3 Digital twin in this project

A digital twin is **not just a trained predictor**.

A useful formulation is:

> A computational model of a specific biological interaction system that is calibrated and validated against experimental observations, can reproduce relevant state evolution, and can be queried under interventions that have not yet been run experimentally. For this project I would expect the twin to evolve iteratively as in vitro evidence falsifies or refines the model.

### 9.4 System identification

System identification infers a dynamical model from observed inputs, states/outputs and perturbations.

Conceptually:

`x_(t+1) = f_theta(x_t, u_t, G) + epsilon`

where:

- `x_t` = molecular/cellular state;
- `u_t` = intervention/perturbation;
- `G` = known biological interaction structure/prior;
- `f_theta` = learned dynamics;
- `epsilon` = unmodeled effects/noise.

### 9.5 Control

After learning a sufficiently reliable dynamics model, the next question becomes: **which perturbation should be applied, when, and under what constraints to reach a desired state?**

Do not pretend to be a control theorist. A strong answer is:

> My sequential-decision work gives me intuition for choosing actions under uncertainty, but I see formal control theory as an area I would need to deepen. That is one of the reasons working in DCS with this supervisory team is attractive.

### 9.6 Biologically informed / mechanistic deep learning

Instead of a fully unconstrained network, encode known biological structure into the architecture, connectivity, loss, state representation or constraints.

Examples relevant to Nilsson's work:

- molecular interaction graph constrains allowed information flow;
- recurrent dynamics update molecular states over time;
- known signaling/gene-regulatory/metabolic interactions provide priors;
- perturbation/time-series data train the propagator;
- predictions can be traced back to interpretable molecular paths.

**Why it matters:** interpretability, sample efficiency, stronger inductive bias and potentially better out-of-distribution behavior.

**Caveat:** biological prior knowledge is incomplete and can be wrong. A good model should not become incapable of discovering missing interactions. Mention residual/learnable flexibility and uncertainty if probed.

### 9.7 Multiomics

Transcriptomics, proteomics, phosphoproteomics and metabolomics observe different layers of the cell. Integration is hard because the layers differ in scale, missingness, measurement noise, temporal resolution and causal proximity.

Strong answer:

> I would not treat multiomics integration as concatenating feature matrices. I would want the representation to respect which measurements correspond to which biological processes and how those layers interact over time.

### 9.8 In silico + in vitro validation

A strong loop is:

1. train/calibrate computational model on existing observations;
2. predict response to a perturbation;
3. test perturbation in vitro;
4. compare predicted and observed state trajectories;
5. analyze failure, uncertainty and identifiability;
6. update model or experimental design;
7. repeat.

That closed loop is central to why the project is scientifically interesting.

---

## 10. Likely questions and answer targets

### "Tell us about yourself."

Use the 60-75 second opening. End at the KTH convergence.

### "Why are you interested in this project?"

Say: dynamic/mechanistic + intervention + experimental validation; not generic healthcare AI.

### "Why KTH / why our groups?"

> The supervisory combination is unusually aligned with the problem. DCS brings scientific ML, system identification, control and learning theory; Avlant's group brings mechanistically informed cancer models and multiomics; Anna Herland's work brings experimentally grounded in vitro platforms. I am specifically looking for an environment where the computational model is challenged by biological evidence rather than evaluated only on a benchmark.

### "What is your strongest research project?"

Lead with BIO614 **if the question is biological modeling**, or DSCI601/GA **if the question is ML/sequential decision-making**.

### "Tell us about something that failed."

Use BIO614 tRNA/5S failure. Explain why high specificity was misleading and what model assumption failed.

### "What is your deep-learning experience?"

Separate formal DL training/broader ML research from the Nussinov paper. Do not relabel classical DP as deep learning.

### "You have done quantum research. Why cancer biology now?"

> Quantum networking is one application domain for my current research, not the scientific question I want to spend my PhD on. What transfers is the methodology: learning under uncertainty, partial observability, sequential decisions, distribution shift and rigorous evaluation. My biological coursework and projects have made me increasingly interested in applying that computational discipline to systems where the scientific mechanism and human-health relevance are central. This KTH project is where those trajectories genuinely meet.

### "What does fairness have to do with this project?"

> Fairness is not the central research question of this KTH position. What I carry from that work is evaluation discipline: checking whether aggregate performance hides systematic failure across meaningful subgroups or conditions. In the RNA study those groups were sequence characteristics, not human demographic cohorts. If I joined this project, I would first solve the scientific modeling problem the project defines and use robust subgroup/condition evaluation where biologically appropriate.

### "How would you model cell-cell interactions?"

A reasonable research-process answer, not a claim about their chosen architecture:

1. define cell states and measurable outputs;
2. encode prior intracellular/intercellular interaction networks;
3. use perturbation/time-series data to learn state transitions;
4. compare structured recurrent/graph models with less constrained baselines;
5. quantify uncertainty and identifiability;
6. validate predicted interventions in vitro;
7. iteratively refine the model.

### "How would you validate a digital twin?"

Do not say accuracy alone. Discuss:

- held-out conditions/cell lines;
- held-out perturbations;
- time-series trajectories;
- intervention response;
- biological plausibility/mechanistic consistency;
- calibration/uncertainty;
- comparison to simpler baselines;
- reproducibility across experimental batches;
- prospective in vitro validation.

### "How do you work with noisy, high-dimensional biological data?"

Say:

- QC before modeling;
- understand batch/missingness/confounders;
- avoid leakage;
- dimensional structure/regularization;
- baseline-first evaluation;
- cross-validation that respects biological grouping;
- ablation studies;
- uncertainty/calibration;
- inspect failures, not only means.

### "How independent are you as a researcher?"

Give one concrete example: question -> design -> implementation -> validation -> failure/iteration -> technical writing. BIO614 or DSCI601 works. Clearly state what **you** did versus collaborators/advisors.

### "How do you collaborate across disciplines?"

Best theme: ask domain experts what assumptions are scientifically meaningful; expose model assumptions; keep reproducible artifacts; treat disagreement as something to test. Avoid claiming biological expertise you do not have.

### "Why another PhD / why now?" or "You already have multiple degrees."

> My previous degrees gave me breadth in computing and data science, but I am now at the point where I want sustained research depth around one scientific problem. I do not see the PhD as another credential. I see it as the training environment for becoming an independent researcher in scientific machine learning for biological and clinical systems.

### "What are your weaknesses for this project?"

> I am not entering as a cancer biologist or as someone already specialized in formal control theory. My strongest preparation is in machine learning, data science, reproducible experimentation, sequential decision-making and computational biology. I would need to deepen cancer systems biology and control theory substantially. I view that as a training gap, not something to hide, and the project is compelling precisely because the supervisory environment covers those areas.

That answer is much stronger than pretending there is no gap.

---

## 11. Application claims to defend carefully

| Application/CV idea | What the evidence supports | Safe interview wording |
| --- | --- | --- |
| "Deep learning for biological sequence/structure" | Strong ML/DL training plus biological modeling; submitted BIO614 paper itself is mainly Nussinov + thermodynamics | Separate DL foundation from the validated BIO614 method; do not call Nussinov a neural model |
| ">90% accuracy on synthetic motifs" | Some simple synthetic controls performed perfectly/highly; other synthetic and realistic biological examples were much weaker | Say simple positive controls performed very well, but realistic structures exposed major limitations |
| "LSTM/neural scoring extension" | Appears in submitted CV; not supported by the BIO614 paper text recovered for this prep | Discuss only if you can explain the actual implementation and results; otherwise call it exploratory and distinguish it from validated paper results |
| fairness across "demographic proxies" | ISTE780 grouped sequences by type, GC bin and length bin | Explicitly say these were biological input groups, not human demographic groups |
| clinical bandit results | DSCI601 uses an embedded **synthetic clinical environment** | Never describe those numbers as patient outcomes or clinical validation |
| publications/research output | Several are course manuscripts, technical reports, proposals and works in progress | Say manuscript, technical report, course project, submitted/under review only when that status is verified |
| control theory | Sequential-decision/bandit background gives adjacent experience | Say control is an area to deepen; do not claim formal control-theory specialization |
| GPA | Submitted CV used 3.9; current RIT requirements support strong study results | Say 3.9 in normal interview conversation to match the application; discuss more precise report values only if directly asked |
| course numbering | Project/file labels include BIO614/BIO630 and current requirements highlight BIOL650 High Throughput Sequencing Analysis | Prefer project/course **names** over reciting course numbers from memory |

### Rule for any difficult CV question

Use this pattern:

> **"The precise version of that claim is..."**

Then give the narrower, defensible statement. Clarifying a broad CV bullet is better than trying to defend wording that is too compressed.

---

## 12. Questions to ask them

Because the meeting is only 20 minutes, plan **two**. Ask one if time is tight.

### Best question 1 - research architecture

> How do you envision the first-year balance between methodological development in scientific machine learning/control at DCS and the biological and experimental work with the Nilsson and Herland groups?

Why it is good: shows you understand the project is genuinely cross-lab and that you are thinking about how the PhD operates.

### Best question 2 - scientific bottleneck

> What data and in vitro systems are already available for the cell-cell interaction and digital-twin work, and where do you currently see the biggest methodological bottleneck - model structure, identifiability, multiomic integration, or experimental validation?

Why it is good: invites them to talk science and gives you information that matters if there is a second interview.

### Strong alternative - success criterion

> What would you consider a strong first research milestone for the doctoral student in the first six to twelve months?

Do not use the limited first-interview question time on salary, vacation, relocation benefits or generic KTH facts unless they explicitly open that topic.

---

## 13. How to answer when you do not know

Never bluff.

Use:

> I have not worked directly with that method, so I do not want to overstate my experience. My current understanding is ____. If I were approaching it in this project, I would start by ____ because ____. I would then validate that assumption by ____.

This still demonstrates research reasoning.

Especially safe areas to admit as learning goals:

- pancreatic-cancer-specific biology;
- stromal signaling details;
- advanced control theory;
- specific in vitro platforms;
- particular Nilsson-group architecture details you have not implemented.

---

## 14. Communication behavior for the 20 minutes

### Do

- answer the question asked first;
- use **I** for your contribution and **we** for collaborative work;
- give one concrete example instead of four vague projects;
- say what failed and what you learned;
- connect technical details back to biological meaning;
- pause after 45-75 seconds and let them probe;
- sound curious, not rehearsed;
- show that you are teachable without sounding passive.

### Do not

- dump your entire CV;
- make quantum the center of the conversation;
- sell fairness as the core of their project;
- describe course projects as published research;
- call synthetic experiments clinical validation;
- use jargon you cannot define;
- pretend to know cancer biology or control theory at expert level;
- give a five-minute answer in a 20-minute interview.

---

## 15. Zoom presence

- Join/test the connection before the interview; be fully ready at least 10 minutes before start.
- Camera at eye level.
- Front lighting; avoid a bright window behind you.
- Quiet environment and stable internet.
- Headphones if they improve audio reliability.
- Solid professional shirt; blazer is optional. No tie is required.
- Have water nearby.
- Keep this document open, but do not read answers from the screen.
- Keep a tiny one-screen cheat sheet with only:
  1. opening arc;
  2. BIO614 failure lesson;
  3. deep-learning honesty boundary;
  4. digital twin definition;
  5. two questions to ask.

---

## 16. Tonight's preparation order

### Pass 1 - 20 minutes: know the project

Read sections 2, 3 and 9. Be able to explain:

- cell-cell interactions;
- cancer-promoting states;
- digital twins;
- biologically informed neural networks;
- system identification;
- control/intervention;
- in silico vs in vitro validation.

### Pass 2 - 20 minutes: know your own evidence

Read sections 4, 7, 8 and 11. Then explain aloud:

1. BIO614 in 60 seconds;
2. BIO614 failure in 60 seconds;
3. DSCI601 relevance in 45 seconds;
4. ISTE780 fairness boundaries in 30 seconds;
5. your actual deep-learning preparation in 45 seconds.

### Pass 3 - 15 minutes: interview answers

Say aloud, without reading:

- Tell us about yourself.
- Why this PhD?
- Why KTH / why these supervisors?
- What is your strongest research project?
- What do you still need to learn?

### Pass 4 - 10 minutes: questions and close

Memorize the **idea**, not wording, of your two questions.

---

## 17. Tomorrow-morning 15-minute drill

1. **3 min:** say opening twice.
2. **3 min:** BIO614 failure story once, slowly.
3. **3 min:** define digital twin + biologically informed neural net + system identification.
4. **3 min:** answer "What is your deep-learning experience?" without overclaiming.
5. **3 min:** say the two questions you will ask them.

Then stop studying. The goal is clarity and responsiveness, not cramming.

---

## 18. If the interview becomes unexpectedly technical

### If Matthieu pushes on mathematical modeling

Think in terms of:

- state variables;
- dynamics;
- model structure/prior;
- identifiability;
- noisy/partial observations;
- stability / long-horizon behavior;
- interventions;
- uncertainty;
- validation outside training conditions.

A useful generic form is:

`x_(t+1) = f_theta(x_t, u_t, G) + epsilon`

Then explain what the variables mean biologically rather than trying to perform control-theory theater.

### If Avlant pushes on biology

Think in terms of:

- signaling;
- gene regulation;
- metabolism;
- tumor microenvironment;
- cancer-stroma feedback;
- perturbation data;
- transcriptomics/proteomics/phosphoproteomics/metabolomics;
- biological interaction networks;
- experimentally testable predictions.

If you do not know a pathway or assay, say so and reason from the system level.

### If either pushes on deep learning

Be ready to discuss:

- why recurrent models make sense for state dynamics;
- graph/network priors;
- overfitting in high-dimensional small-sample biology;
- regularization;
- train/validation leakage;
- distribution shift;
- calibration and uncertainty;
- ablations and simpler baselines;
- why mechanistic priors can improve interpretability but may also encode incomplete knowledge.

---

## 19. Final mental positioning

Do **not** try to present yourself as a finished cancer systems biologist.

Present yourself as:

> **A mature computational researcher with a strong CS/data-science foundation, real experience analyzing biological data and algorithmic failure, disciplined reproducible evaluation, and growing expertise in learning under uncertainty - now deliberately seeking doctoral depth in mechanistically informed deep learning and control of biological systems.**

That is credible, useful to this team, and consistent with the submitted application.

### The sentence to remember if nerves hit

> **"My strength is rigorous computational modeling and evaluation; what excites me about this PhD is learning to make those models biologically structured, dynamically meaningful, and experimentally testable."**

---

## 20. After the interview

Record immediately:

- questions they asked;
- where they probed deeply;
- anything they corrected or emphasized;
- data/model/lab details they revealed;
- next-stage timing;
- any requested material;
- names of additional collaborators mentioned;
- what answer you want to improve before a second interview.

Then send a brief thank-you/follow-up only if appropriate to the conversation and next-step instructions.

---

## Verified source anchors

### KTH / supervisor sources

- KTH vacancy: <https://www.kth.se/lediga-jobb/928557?l=en>
- KTH DCS machine learning: <https://www.kth.se/dcs/research/machine-learning>
- KTH optimization and control: <https://www.kth.se/dcs/research/optimization-and-con>
- Matthieu Barreau: <https://www.kth.se/profile/barreau>
- Scientific ML course FEL3751: <https://www.kth.se/kurs-pm/FEL3751?l=en>
- Avlant Nilsson / SciLifeLab: <https://www.scilifelab.se/researchers/avlant-nilsson/>
- Avlant-group 2026 PhD description: <https://www.scilifelab.se/career/doctoral-phd-student-position-in-deep-learning-modeling-of-cancer/>
- 2026 biologically informed phosphoproteomic time-series work: <https://publications-affiliated.scilifelab.se/publication/53deef8658d14591b6b08382650120d7>
- Alexandre Proutiere: <https://www.kth.se/profile/alepro/>
- Anna Herland: <https://www.kth.se/profile/aherland?l=en>

### Application evidence inside RESEARCH

- `APPLICATIONS/PhD/review-by-application/05-kth-deep-learning-biological-systems/README.md`
- `APPLICATIONS/PhD/review-by-application/05-kth-deep-learning-biological-systems/2026-07-31-kth-deep-learning-biological-systems-cover-letter.txt`
- `APPLICATIONS/PhD/application-materials/2026-07-31-kth-deep-learning-biological-systems-packet-status.md`
- `MASTER_RESEARCH_INDEX.md`

**Prepared:** 2026-08-23 for the 2026-08-24 KTH interview.
