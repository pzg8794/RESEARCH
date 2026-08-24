# KTH Interviewer Focus - Matthieu Barreau and Avlant Nilsson

**Interview:** 2026-08-24, 13:00 Stockholm / 07:00 New York  
**Format:** Zoom, 20 minutes  
**Confirmed interviewers:** **Matthieu Raphael Barreau** and **Avlant Nilsson**

> **Priority rule:** For tomorrow's interview, actively prepare only for Matthieu and Avlant. Alexandre Proutiere and Anna Herland are relevant to the broader PhD/supervisory environment, but they are **not listed as participants in this 20-minute meeting** and should not take study time away from the two confirmed interviewers.

---

## 1. Matthieu Raphael Barreau - KTH Decision and Control Systems

### Read first

- KTH profile: <https://www.kth.se/profile/barreau>
- Scientific Machine Learning for Modeling and Control of Dynamical Systems (FEL3751): <https://www.kth.se/kurs-pm/FEL3751?l=en>

### Research themes most relevant to this PhD

- dynamical systems;
- control;
- optimization;
- system identification;
- scientific machine learning;
- physics-informed / structure-informed learning;
- modeling from sparse or noisy measurements;
- digital-twin thinking.

### What he may be evaluating in Piter

- Can Piter move beyond generic predictive ML toward models of **dynamics**?
- Can he reason about state, uncertainty, interventions, model mismatch and validation?
- Does his sequential-decision/bandit background transfer to controlled dynamical systems?
- Is he mathematically and computationally mature enough to deepen into formal control and system identification?
- Can he discuss limitations honestly rather than oversell a model?

### Best personal evidence to connect

1. **BIO614/BIO630 RNA project:** simplified objective worked on synthetic motifs but failed on realistic biological structures - excellent model-mismatch story.
2. **DSCI601 / GA work:** partial observability, sequential decisions, uncertainty, non-stationarity and intervention-like action selection.
3. **Reproducible evaluation:** baselines, validation, logging, distribution shift and failure analysis.

### Mental sentence

> "With Matthieu, show that I think about what the model is learning, how the system evolves, what is observable, what is uncertain, and whether an intervention is actually justified."

---

## 2. Avlant Nilsson - cancer systems biology / mechanistically informed deep learning

### Read first

- SciLifeLab profile: <https://www.scilifelab.se/researchers/avlant-nilsson/>
- Current group/doctoral-position description: <https://www.scilifelab.se/career/doctoral-phd-student-position-in-deep-learning-modeling-of-cancer/>
- Relevant 2026 biologically informed time-series work: <https://publications-affiliated.scilifelab.se/publication/53deef8658d14591b6b08382650120d7>

### Research themes most relevant to this PhD

- mechanistically / biologically informed neural networks;
- cancer signaling;
- gene regulation;
- metabolism;
- molecular interaction networks;
- transcriptomics, proteomics, phosphoproteomics and metabolomics;
- perturbation and time-series data;
- drug response and resistance;
- tumor microenvironment;
- cancer-stroma / cell-cell interactions;
- interpretable models that can generate experimentally testable hypotheses.

### What he may be evaluating in Piter

- Does Piter understand that biological data have **mechanistic structure**, not merely features?
- Can he distinguish a biologically meaningful model from a high-performing black box?
- Does he understand why perturbation and time-series data are valuable for causal/dynamical inference?
- Can he work productively with biological collaborators while openly acknowledging what biology he still needs to learn?
- Can he connect his RNA/bioinformatics experience to a larger systems-biology problem without pretending they are the same problem?

### Best personal evidence to connect

1. **BIO614/BIO630:** biological validity vs aggregate metrics; thermodynamic/structural priors; learning from failure.
2. **High-throughput sequencing / RNA-seq:** practical familiarity with noisy molecular data and QC.
3. **ISTE780:** subgroup/condition evaluation discipline, carefully framed as sequence-level methodological work.
4. **VIOME / biological-data pipeline experience:** real-world biological-data preprocessing context, if asked.

### Mental sentence

> "With Avlant, show that I respect biological mechanism, understand why interactions and perturbations matter, and want computational models whose predictions can be tested experimentally."

---

## 3. Why the pair is important

Tomorrow's interview has a very useful structure:

- **Matthieu:** dynamics, scientific ML, control, modeling rigor.
- **Avlant:** mechanistic cancer biology, multiomics, cell-cell interaction, experimental meaning.

The PhD sits at their intersection.

A strong candidate does **not** need to be a finished expert in both areas. A strong candidate needs to demonstrate:

1. sufficient ML/data-science depth to contribute immediately;
2. enough biological reasoning to engage seriously with the scientific problem;
3. the ability to learn formal dynamical/control methods;
4. intellectual honesty about gaps;
5. evidence of independent research reasoning.

---

## 4. DSCI 640 RNN refresher - use OUR course language

Do **not** learn a new RNN explanation tonight. Refresh from the exact material already used in RIT Neural Networks.

### Slides

1. **Lecture 5 - Recurrent Neural Networks and the RNN Forward Pass**  
   <https://drive.google.com/file/d/1E3V3M-cL8DdqpYRgkMLVzS5yDvbtjzJE/view?usp=drivesdk>  
   Best first refresher. Covers what RNNs are, sequential/temporal data, traditional recurrent architectures, recurrent connections, forward pass and loss functions.

2. **Lecture 6 - RNN Backward Pass, Weight Initialization and Dealing with Numerical Issues**  
   <https://drive.google.com/file/d/1KEBQz-2Z9O373hVoE44ibeh8CwbiT7xd/view?usp=drivesdk>  
   Use only if needed to reactivate backpropagation-through-time intuition, accumulated recurrent deltas, initialization, gradient clipping/scaling/boosting.

3. **Lecture 7 - RNN Memory Cells**  
   <https://drive.google.com/file/d/1ELmiTOTOreE9lQgGg-4Qs3-1PsLjAXRY/view?usp=drivesdk>  
   Most relevant to Avlant's RNN-based architecture. Covers LSTM, GRU, MGU, UGRNN and Delta-RNN. The LSTM material uses the language already familiar from class: **input gate, forget gate, output gate, cell memory, current input, previous cell value, and gated information flow through time**.

### Programming Assignment 2 - what Piter actually implemented

- **PA2 Part 1 - RNN structure + forward pass**  
  <https://drive.google.com/file/d/1K-rD3x05MrIPYisk-9CPL6nnfC0cxQ-2/view?usp=drivesdk>  
  Implemented/filled in `connectNodes`, **Jordan recurrent connections**, **Elman recurrent connections**, `RecurrentNeuralNetwork.forwardPass`, tanh/sigmoid behavior, and loss functions. The assignment used `RecurrentNeuralNetwork.java`, `RecurrentNode.java`, `RecurrentEdge.java`, one-hot encoded sequence data, and Penn Treebank examples.

- **PA2 Part 2 - RNN backward pass**  
  <https://drive.google.com/file/d/1K2b__Ui7lzatv142KabnLKKPPRnbUc_y/view?usp=drivesdk>  
  Implemented recurrent backward propagation in `Edge`, `RecurrentEdge`, `RecurrentNode`, and `RecurrentNeuralNetwork`, plus Xavier/Kaiming initialization and numerical-gradient checking.

- **PA2 Part 3 - time-series RNN training**  
  <https://drive.google.com/file/d/1K8sVVDxkopa7hs3_sSBrHG2Px2pFlMum/view?usp=drivesdk>  
  Extended the recurrent forward/backward path for **time-series prediction**, regression losses, normalization, and batch/minibatch/stochastic gradient descent.

- **PA2 Part 4 - LSTM implementation**  
  <https://drive.google.com/file/d/1K8zJDmrcyVUy3Yi6EPbn1XpIC8VxIWnP/view?usp=drivesdk>  
  **Most important evidence if asked whether Piter has actually coded recurrent memory cells.** The assignment required completing `LSTMNode.java`, including both `propagateForward` and `propagateBackward`, initialization of all weights/biases, and the forget-gate bias. Optional extensions included GRU, MGU, UGRNN or Delta-RNN.

- **Programming Assignment 2 overview / notes**  
  <https://docs.google.com/document/d/121cQHygwY1SxNHgUTwx3FZRoXfhifZAS07AJU55UtSo/edit>  
  Quick text reference to the codebase and required methods.

### Simple definitions and visuals: RNN, LSTM, ARIMA

#### RNN - Recurrent Neural Network

**Simple definition:** A neural network for sequential or temporal data that carries information from previous passes forward through recurrent connections, allowing the current prediction to depend on both the current input and learned information from the past.

```text
x(t-2)      x(t-1)       x(t)
  |           |           |
  v           v           v
[RNN] -----> [RNN] -----> [RNN] -----> prediction
  | h(t-2)     | h(t-1)     | h(t)
  +------------+------------+
        learned memory/state moves forward
```

Mental shorthand:

```text
current input + previous learned state -> new state -> prediction
```

Why it matters here: signaling, gene regulation and metabolism are **evolving interacting processes**. An RNN can carry a learned representation of prior molecular state forward as the system changes.

#### LSTM - Long Short-Term Memory

**Simple definition:** A gated type of RNN designed to preserve useful information over longer sequences by controlling what enters memory, what is kept or forgotten, and what leaves the cell as output.

```text
                         cell memory c(t-1)
                               |
                               v
x(t) + h(t-1) ---> [ FORGET GATE ] --- what old information stays?
        |                    |
        |                    v
        +----------> [ INPUT GATE ] --- what new information enters?
                               |
                               v
                         [ cell c(t) ]
                               |
                               v
                       [ OUTPUT GATE ] --- what information is exposed?
                               |
                               v
                            h(t)
```

Mental shorthand:

```text
FORGET: what old information should I keep/remove?
INPUT:  what new information should I store?
OUTPUT: what part of memory should influence the current output/state?
```

The two states to remember:

```text
c(t) = cell memory       -> longer-term information path
h(t) = hidden/output     -> current recurrent state/output
```

Why LSTM exists: a simple RNN can struggle to preserve useful information across long sequences during training. LSTM provides a gated memory path so important information can survive across more time steps while irrelevant information can be forgotten.

Why it matters here: a biological response at time `t` may depend on molecular events much earlier than `t-1`. LSTM-style memory gives the model a mechanism for carrying selected longer-term signaling/regulatory information forward.

**Our direct evidence:** PA2 Part 4 required implementing `LSTMNode.java`, including both forward and backward propagation, weight/bias initialization and the forget-gate bias.

#### ARIMA - AutoRegressive Integrated Moving Average

**Simple definition:** A statistical time-series forecasting model that predicts future values from a specified number of past values, optional differencing, and past prediction errors.

For the current quantum implementation, **ARIMA(1,0,1)** means approximately:

- **AR(1):** use one previous observed value;
- **I(0):** no differencing;
- **MA(1):** use one previous prediction error.

```text
previous value x(t)
        |
        +------+
               v
          [ ARIMA ] -----> prediction x_hat(t+1)
               ^
               |
        previous error e(t)
```

Mental shorthand:

```text
specified past values + specified past errors -> forecast
```

#### The difference to remember

```text
ARIMA: WE specify how much history enters the forecast.
       x(t), x(t-1), errors -> x_hat(t+1)

RNN:   THE NETWORK learns a state that represents useful history.
       x(t) + h(t-1) -> h(t) -> x_hat(t+1)

LSTM:  AN RNN WITH GATED MEMORY learns what history to keep,
       what to forget, and what to expose as the current state/output.
```

Both ARIMA and recurrent neural networks use temporal information. **ARIMA has an explicit statistical memory structure; RNNs learn a recurrent state representation; LSTM adds gated long-term memory to that recurrent representation.**

Connection to our work:

```text
Current iCPursuitNeuralUCB:
history -> ARIMA forecast -> predicted context -> bandit decision

Original iCMAB direction:
history -> EXAMM-RNN world/controller models -> predicted context/reward -> bandit decision
          (EXAMM can evolve recurrent cell types including gated-memory structures)

KTH/Avlant direction:
molecular history -> biologically constrained RNN state -> future molecular/cellular state under perturbation
```

### What to remember for the interview

The course framing is enough:

- RNNs operate on **sequential/temporal data**.
- Recurrent connections let information from earlier time steps affect later computation.
- Elman/Jordan structures are concrete recurrence patterns already implemented in class.
- Training requires forward propagation through time and backward propagation through those recurrent dependencies.
- LSTM adds **gates** that regulate how information enters memory, is retained/forgotten, and leaves the cell.

Do not claim to have developed a cancer-specific RNN. The defensible statement is stronger and simpler: **Piter has formal graduate RNN training and hands-on implementation experience down to recurrent edges, forward/backward propagation and LSTM memory-cell code.**

---

## 5. What NOT to spend time studying tonight

Do not spend meaningful preparation time memorizing Alexandre Proutiere or Anna Herland biographies for this 20-minute interview. Know only that the broader project environment includes expertise in learning/optimization and experimental/in-vitro systems.

If Matthieu or Avlant mention either person, listen carefully and use that as new information. Do not force those names into an answer to prove you researched the team.

---

## 6. One-line strategy for tomorrow

> **Show Matthieu that you can become a rigorous scientific-ML/control researcher, and show Avlant that you can become a rigorous computational cancer-systems researcher - while giving both evidence that you already know how to build, test, question and explain computational models.**
