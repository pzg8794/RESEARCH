# KTH First-Round Interview — Evidence Debrief and Improvement Plan

**Interview completed:** August 24, 2026  
**Panel present:** Matthieu Barreau, Avlant Nilsson, and Alexandre Proutiere  
**Position:** Doctoral student in deep learning for biological systems  
**Evidence status:** derived from the private interview transcript; the raw transcript is intentionally not committed to this public repository

## Bottom Line

This was not a failed interview. Piter established authentic motivation, relevant computational experience, scientific humility, and willingness to relocate. He also asked a strong project-design question that Avlant explicitly called excellent and that elicited concrete information about the planned data.

The interview did expose three priority gaps under pressure:

1. define cancer technically rather than socially or clinically;
2. explain omics and its use in cancer without searching notes; and
3. distinguish custom neural-network implementation, custom architecture, and custom loss functions using only verified experience.

The broader communication issue was **answer compression**. Several answers began with personal context or a list of projects and metrics before stating the direct answer. For a technical panel, use this sequence:

> **Answer first → one piece of evidence → one lesson or project connection → stop.**

## Verified Interview Outcome

- The panel used a common question sequence for candidates and then opened the discussion.
- Piter confirmed that he could travel to KTH for a second interview.
- The panel said it would confer with Anna Herland and select a shortlist.
- Shortlisted candidates may be invited to KTH within approximately two weeks.
- The second interview would be more technical.
- No shortlist decision or invitation was made during this interview.

## What Worked

### Authentic motivation and persistence

Piter connected his health-system experience to a long-running interest in decision-making from incomplete evidence. The motivation was genuine and memorable.

### Scientific judgment about misleading metrics

The readmission example—high aggregate accuracy with very low positive-class recall—showed that Piter knows a model can look successful while failing on the outcome that matters. The RNA example similarly showed willingness to accept biological failure rather than protect a model.

### Honest boundary-setting

When asked about cancer biology, Piter did not pretend to possess expertise he did not have. That honesty should remain, but it should follow a correct baseline definition rather than replace it.

### Strong question to the panel

Piter asked which interacting system and datasets were committed and what would count as a minimum viable digital twin. Avlant called it an excellent question. The answer disclosed:

- a completed pilot of roughly 100 samples;
- a planned gene-expression dataset of roughly 2,000 ligand-stimulation samples;
- a planned secreted-protein readout of roughly 100 samples;
- use of public cancer-cell-line data; and
- a planned microfluidics integration whose postdoctoral researcher had not yet started.

Treat these as interview observations, not as guarantees beyond what the panel stated.
The panel answered the dataset half of Piter's question but did not define the
minimum viable first-year digital twin; that remains a useful second-round
follow-up.

## Where the Answers Broke Down

| Question | What happened | What to improve |
| --- | --- | --- |
| Why apply / tell us about yourself | The answer was sincere but long and moved through personal history, readmission, RNA, and quantum work before reaching the role. | Lead with the research question and KTH fit; use one personal sentence and two evidence points. |
| Why a PhD now? | The answer explained the health direction but did not clearly state why doctoral training is required now. | Name the transition: from building/evaluating models to mechanistic, experimentally testable research. |
| Thesis elevator pitch | The answer mixed the quantum and clinical scopes, many metrics, bioinformatics results, and a recent scope split. | State one current scope, one problem, one method, one contribution/result, and the exact completion status. |
| Why are you a strong candidate? | Personal commitment came before research capability. | Lead with immediate research contributions; add motivation after the evidence. |
| Research experience | The answer became a chronological list of projects. | Show a research cycle: question, method, result/failure, revision, and what was learned. |
| Long-term goals | The vision was committed but the phrase “until the day I die” was broader than the panel needed. | State a credible direction: interdisciplinary scientific-ML/health research, teaching, and mentorship. |
| What is cancer technically? | Cancer was described mainly as a chronic illness without a cure. That is not a sufficient technical definition, and some cancers can be cured or controlled. | Define abnormal uncontrolled growth, survival, invasion/metastasis, genetic change, heterogeneity, and microenvironmental interaction. |
| What are omics measurements and how are they used in cancer? | Piter recognized the term but could not retrieve a definition and searched notes. | Memorize the molecular layers and connect each measurement to state, pathway, biomarker, and perturbation analysis. |
| Have you customized neural-network training? | The answer described generic losses and feedback but did not identify a verified non-standard loss or a concrete implementation. | Answer the exact boundary: recurrent coursework and assignment evidence are documented; a novel custom loss and exact code ownership require artifact verification. |

### Claim and source corrections before the next interview

- Use **2015** for the Big Data Medical Diagnosis project unless a stronger
  dated source establishes an earlier start; the interview's 2013/2014 answer
  conflicts with the current verified guide.
- The exact “improve human health” prompt came from a related
  KI/SciLifeLab/Nilsson-group opportunity, not the KTH vacancy. The motivation
  still fits this KTH project, but attribute sources accurately.
- Keep the evidence type visible: coursework is not a publication, a group
  RNA-seq project is not solely owned work, a manuscript is not necessarily
  submitted or accepted, and a synthetic clinical environment is not patient
  validation.
- The automated transcript garbles several technical names. Verify any unclear
  term against the recording before citing it as evidence.

## Corrected Answers for the Next Interview

### “What is cancer from a technical perspective?” — 25 seconds

> Cancer is a family of diseases in which genetic and regulatory changes allow abnormal cells to proliferate or survive when they should not, evade normal controls, invade tissue, and sometimes metastasize. It is also a systems problem: tumor cells interact with stromal, immune, and vascular cells, and those signals can stabilize a cancer-promoting state. In this project, the modeling question is which interactions maintain that state and which perturbations can move it toward a healthier response.

### “What are omics measurements, and how can they be used in cancer?” — 30 seconds

> Omics are large-scale measurements of a molecular layer: genomics for DNA, transcriptomics for RNA expression, proteomics or phosphoproteomics for proteins and signaling, and metabolomics for metabolites. In cancer, those layers can characterize cell state, identify pathways or biomarkers, compare responses to perturbations, and help infer communication between tumor and surrounding cells. My verified hands-on experience is transcriptomics and RNA-seq through a group course project, and I would identify my documented contribution if probed; the other layers are areas I am prepared to learn rather than work I should claim as completed.

### “Have you made custom modifications to neural networks?” — 30 seconds

> I need to distinguish implementation work from inventing a novel loss. My documented neural-network evidence is graduate coursework and assignment material covering Elman and Jordan recurrence, recurrent forward and backward propagation, time-series training, and LSTM memory-cell logic. I have not yet verified a research-grade project in which I designed a novel custom loss. A custom loss is the differentiable scalar objective used for training—not the hidden state or backpropagation itself—and it can combine prediction error with justified domain constraints. Before claiming specific code ownership, I would open the submitted assignment and identify exactly what I implemented.

### “Give us the elevator pitch for your current thesis/work.” — 45 seconds

> My program completion is now expected in December 2026, and the thesis remains in progress. Its core question is how context quality affects sequential resource allocation under uncertainty. I compare non-contextual, contextual, and informative contextual bandits in a reproducible quantum-routing evaluation framework. With my advisers, I narrowed the thesis to the quantum domain and separated the synthetic clinical branch. Preliminary predictive-context policies improved over the no-context baseline by 3.74 percentage points internally and 2.83 externally. I am proud of the reusable evaluation framework and of narrowing the scope rather than overstating a two-domain thesis.

Before reusing this answer, verify the current tracker and separate what is
**completed**, **in progress**, **drafted**, and **submitted**.

### “What research experience do you have?” — 45 seconds

> My strongest evidence is not simply the number of projects; it is how I respond when evidence contradicts the initial story. In the readmission study, class-specific recall showed that a high-accuracy model was failing on the outcome of interest, so I changed the interpretation. In RNA-structure modeling, success on simple motifs did not transfer to realistic structures, so I reported the biological limitation instead of presenting the metric as success. In my current research I use reproducible comparisons and controlled factors to study uncertainty and changing conditions. Those experiences taught me to treat failure analysis as part of the research result.

### “Why are you a strong fit?” — 35 seconds

> I can contribute immediately through programming, reproducible experiments, careful baselines, neural-network implementation, biological-data analysis, and reasoning under uncertainty. My readmission and RNA work also show that I question aggregate metrics and revise conclusions when biological evidence disagrees. I am not yet a cancer systems biologist or formal control theorist; those are the two areas I want to deepen in a team that connects computation to experiments.

### “Why a PhD now, and where do you want it to lead?” — 35 seconds

> I already have breadth across computer science, data science, and biological data, but I need sustained depth in cancer systems biology, system identification, and control. A PhD is the right next step because I want to learn to formulate and experimentally test mechanistic models as an independent researcher, not only apply existing tools. Long term, I want to contribute to or lead interdisciplinary computational-biology research and continue teaching and mentoring. I am open about whether that is in academia, a research institute, or R&D; the research function is clear.

## Recovery Pattern for an Unfamiliar Technical Question

Do not search notes while the panel waits. Use this four-part recovery:

1. **State the part you know:** “My understanding is…”
2. **Set the boundary:** “My hands-on experience is in transcriptomics, not all omics layers.”
3. **Reason from first principles:** identify the measured object, model input/output, and validation question.
4. **Invite correction briefly:** “That is how I would approach it; I would want to verify the biological assumption with the team.”

If the term is completely unfamiliar, say so once and pivot to the nearest verified concept. A precise boundary is stronger than a vague answer.

## Reading Plan

### Priority 1 — before any second-round invitation (about 90 minutes)

1. **Cancer fundamentals (15 minutes):** [NCI, “What Is Cancer?”](https://www.cancer.gov/about-cancer/understanding/what-is-cancer). Be able to explain uncontrolled growth, apoptosis/growth controls, invasion, metastasis, genetic change, heterogeneity, and the tumor microenvironment.
2. **Omics map (15 minutes):** [NHGRI, “Multi-Omics Defined”](https://www.genome.gov/sites/default/files/media/files/2022-10/Multi-Omics_Pre-Application_Webinar_2022.pdf). Make a one-line input/meaning/limitation card for genome, transcriptome, proteome/phosphoproteome, and metabolome.
3. **The panel’s modeling language (25 minutes):** [Nilsson et al., LEMBAS](https://www.nature.com/articles/s41467-022-30684-y). Focus on the abstract, model diagram, prior-network-constrained sparse RNN, ligand inputs, transcription-factor outputs, feedback, steady state, loss, and held-out validation.
4. **Own implementation evidence (35 minutes):** reopen the submitted DSCI 640 Programming Assignment 2 artifacts, not just the assignment instructions. Record the dataset, architecture, loss, optimizer, exact personal code changes, evaluation, result, and limitation. If the submitted code cannot verify an implementation claim, retain the coursework-only boundary.

### Priority 2 — over the following week

- Review ligand, receptor, cytokine, transcription factor, gene expression, secreted protein, perturbation, knockout, and tumor-microenvironment vocabulary.
- Distinguish **architecture customization** (network structure), **objective customization** (loss), **training customization** (optimizer/schedule), and **biological constraints** (known edges, signs, sparsity, stability).
- Review why a predictive model is not automatically a digital twin: calibration, dynamics, intervention, uncertainty, and prospective experimental validation are required.
- Read the LEMBAS limitations as carefully as its results: incomplete prior networks, identifiability, data coverage, and steady-state assumptions.
- Practice project-design questions tied to the disclosed data: generalization to unseen ligands, batch effects and biological replicates, high dimensionality relative to sample size, transcriptomic/proteomic integration, falsification, and the minimum in-vitro evidence needed to justify “digital twin.”

## Practice Protocol

### Daily 20-minute drill

1. Draw one question at random.
2. Answer without notes for 30–45 seconds.
3. Listen once and score only three things: direct first sentence, verified evidence, and stopping point.
4. Repeat the answer once, shorter.

### Required flashcards

- cancer;
- tumor microenvironment;
- cell-cell signaling;
- ligand and receptor;
- genomics;
- transcriptomics;
- proteomics and phosphoproteomics;
- metabolomics;
- custom loss versus custom architecture;
- recurrent neural network;
- digital twin;
- system identification and control.

### Mock-interview rule

The mock interviewer should interrupt after 45 seconds, ask “What did **you** implement?”, and then ask one unfamiliar follow-up. This trains concise evidence ownership and recovery under pressure.

If an interviewer answers only half of a compound question, retrieve the other
half politely:

> Thank you—that clarifies the data pipeline. Could I return briefly to the second part: what would you consider the minimum viable digital twin in year one?

## Next-Stage Trigger

If KTH sends a shortlist invitation:

1. record the exact invitation and technical format;
2. update the preparation guide with the dataset details disclosed in this interview;
3. verify the current thesis scope and milestones before rehearsing the elevator pitch;
4. complete at least two technical mocks; and
5. prepare a one-page explanation of a biologically constrained recurrent model, its loss terms, validation plan, and failure modes.

[Return to the one-page interview cheat sheet](2026-08-24-kth-interview-cheat-sheet.md#index) · [Open the full interview guide](2026-08-24-kth-live-interview-guide.md)
