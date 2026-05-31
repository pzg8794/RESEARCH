# ICT Defense Notes — NTNU PhD Quantum Compiler Technologies

**Application:** 5878636 — PhD Candidate in Quantum Compiler Technologies (NTNU, Job 298925)  
**Date created:** 2026-05-30  
**Purpose:** Interview/screening talking points for three ICT-level skill entries that may prompt follow-up questions.

---

## 1. LLVM / MLIR compiler backend framework

**Declared level:** Good (knowledge + practical familiarity)  
**Honest scope:** Study-level and application-review; not production compiler-pass authoring.

**How to defend:**

> "My LLVM/MLIR familiarity comes from purposefully studying the IR architecture as it applies to quantum compilation pipelines — specifically the MLIR Quantum Dialect (QSSA/QIR work), how LLVM's pass infrastructure maps to gate optimization and decomposition, and how TAFFO's VRA-based precision selection operates at the LLVM IR level. I reviewed this in depth while preparing my SPQR-focused research proposal. I understand the pass manager, IR transformation pipeline, and how quantum gates are lowered to classical hardware backends. My hands-on experience is at the analysis and study level rather than production pass implementation — but that understanding is exactly what I need to start contributing to the SPQR codebase under supervision."

**Anchor evidence:** The project outline itself names MLIR Quantum Dialect explicitly and discusses compiler-assisted QEC code selection — you studied it enough to produce a credible 8-section research proposal.

---

## 2. Qiskit / Cirq — gate-based quantum computing

**Declared level:** Good/Proficient  
**Honest scope:** This is your strongest ICT entry — you have active experimental code.

**How to defend:**

> "This is the area where I have the most concrete implementation experience. In my GA role at RIT, I've built and tested gate-level quantum circuits for quantum network path optimization and fault-tolerant routing research. I've used Qiskit's circuit, transpiler, and noise simulation APIs to run parameterized experiments under stochastic conditions, and I've implemented stabilizer-circuit concepts for error correction simulation using Stim-compatible pipelines. The `QuantumFaultTolerant` and `quantum_project_hub` repositories on my GitHub contain this work. I can speak to gate decomposition, unitary simulation, circuit optimization passes, and the difference between Qiskit's Aer simulator and hardware-target compilation."

**Anchor evidence:** GitHub repos `pzg8794/QuantumFaultTolerant` and `pzg8794/quantum_project_hub`.

---

## 3. TAFFO / Precimonious — approximate computing, precision tuning

**Declared level:** Familiarity with  
**Honest scope:** Deep reading + research proposal work; no production TAFFO plugin authoring.

**How to defend:**

> "I was deliberate in writing 'familiarity with' rather than 'proficient.' I have read the TAFFO papers including Prof. Cherubin's work on compiler-assisted dynamic precision tuning, and I understand the Value Range Analysis mechanism, how TAFFO propagates type annotations through LLVM IR, and how it performs mixed-precision substitution for floating-point operations. I've analyzed how this methodology could extend to QEC code selection — specifically using a VRA-style pass to select between code families based on estimated resource bounds and qubit budget constraints. That analysis forms the basis of my project outline. I have not written a TAFFO plugin, but I understand the framework well enough to contribute to the SPQR codebase under supervision from day one, which is the appropriate level for a PhD candidate entering this position."

**Key framing:** The SPQR position *is the research* — no applicant is expected to have already extended TAFFO to quantum. You are applying to do exactly that.

---

## General interview posture

- Distinguish clearly between tools you've **used actively** (Qiskit, Cirq), tools you've **studied deeply for this proposal** (LLVM/MLIR, TAFFO/Precimonious), and new capabilities you expect to develop **as the PhD research itself**.
- Entries are written at honest levels; do not inflate under pressure.
- If asked about compiler design coursework: point to your MS CS at RIT (2015), which included compiler design and algorithm analysis coursework, plus the self-directed MLIR/TAFFO study for this proposal.
- If asked about the quantum paper under review: describe the research problem and methodology but do not name the venue or exact title (double-blind review active).
