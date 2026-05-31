# NTNU Quantum Compiler PhD Project Outline (v3 — REVISED)

Position: PhD Candidate in Quantum Compiler Technologies (Job 298925)
Supervisor: Prof. Stefano Cherubin — System Software Group, NTNU IDI
Deadline: 1 June 2026
Project context: SPQR — Smart Precision for Quantum Resilience (NFR)
Target: ≤1500 words / 4 pages

---

## Title
Compiler-Assisted Precision Tuning for QEC Code Optimization in Fault-Tolerant Quantum Workloads

---

## 1. Problem and Motivation

Scalable fault-tolerant quantum computing depends on quantum error correction (QEC) codes that protect logical qubits from physical noise. However, the choice of QEC code family — surface codes, color codes, or low-density parity-check (LDPC) codes — critically determines resource overhead: physical qubit counts, circuit depth, and gate fidelity requirements vary by orders of magnitude across families and across subcircuit types within a single program. Current compilation workflows typically apply a fixed code choice program-wide, without adapting to the varying noise sensitivity, precision requirements, or resource budgets of different subcircuits.

Classical compiler research has directly addressed analogous cost-correctness trade-offs through precision tuning and approximate computing. Tools such as TAFFO (Tuning Assistant for Floating-Point to Fixed-Point Optimization), developed within Prof. Cherubin's research group and its collaborators, demonstrate that compiler-level static analysis can systematically identify where floating-point precision can be reduced with bounded correctness impact — trading computation accuracy for efficiency gains while preserving program-level output guarantees. These same principles have not been systematically transferred to the quantum compiler setting.

The SPQR (Smart Precision for Quantum Resilience) project, sponsored by the NFR Enabling Technologies programme, proposes exactly this transfer: adapting precision tuning and approximate computing techniques to guide QEC code selection within quantum compiler infrastructure. This project outline proposes my doctoral research contribution within SPQR: extending the analytical framework established in classical precision tuning (as exemplified by TAFFO) to develop formal IR-level models and transformation passes for adaptive, subcircuit-granular QEC code optimization.

## 2. Research Questions

1. Which IR abstractions best capture the precision-resource trade-off structure of gate-based logical-qubit circuits, in a form compatible with LLVM/MLIR-based compiler analysis?
2. How can the cost-correctness modeling approach demonstrated in classical precision tuning tools (TAFFO, Precimonious, HiFPTuner) be formally extended to the QEC code selection problem?
3. What static analysis strategies and transformation pass designs minimize physical resource overhead while preserving correctness bounds under target error models?
4. How can compiler-level optimization decisions for QEC code selection be made reproducible, explainable, and generalizable across circuit workload families?

## 3. Methodology

**Phase 1 — Literature and Formal Modeling (Year 1, H1).** Systematically review precision tuning literature (TAFFO and its predecessors) alongside QEC code selection and quantum compiler IR literature. Establish formal cost-correctness trade-off models for representative gate-based circuit families, parameterized by noise model and subcircuit structure. Deliver: formal trade-off model; baseline compilation pipeline reproducing published surface code and color code overhead results.

**Phase 2 — Compiler Pass Design (Year 1 H2 – Year 2 H1).** Prototype analysis and transformation passes in C/C++ within LLVM/MLIR-compatible infrastructure, targeting the MLIR Quantum Dialect or a project-specific IR extension. Passes will implement precision-aware QEC code selection at subcircuit granularity, guided by static analysis of error sensitivity and resource budgets from Phase 1. Engage Politecnico di Milano partner team on joint pass design sessions and shared test suites.

**Phase 3 — Evaluation (Year 2).** Benchmark optimization pipeline against fixed-choice baselines across representative workloads spanning NISQ-adjacent and fault-tolerant circuit families. Primary metrics: physical qubit overhead reduction, gate count, and estimated logical error rate under depolarizing and biased noise models. Secondary metrics: pass runtime and optimization decision interpretability. Submit mid-cycle publication (CGO or QSW target).

**Phase 4 — Validation and Generalization (Year 3).** End-to-end framework finalization, cross-site benchmark validation with Politecnico di Milano, ablation studies isolating individual pass contributions, and generalization to broader workload classes. Deliver open reproducible benchmark suite. Complete thesis.

## 4. Implementation Stack

- **Primary language:** C/C++ for all compiler pass development
- **Compiler infrastructure:** LLVM/MLIR (with TAFFO and the MLIR Quantum Dialect as prior art and design reference points)
- **QEC simulation backends:** Stim (fast stabilizer circuit simulation), FlamingPy / Qiskit Aer for noise modeling and overhead estimation
- **Engineering principles:** Modular pass architecture; version-controlled artifacts; reproducible benchmarks with open release

LLVM/MLIR is the natural infrastructure target because it underpins TAFFO and provides the multi-level IR framework and pass interface conventions on which this project's extensions will be built. The MLIR Quantum Dialect provides an existing IR target point; SSG's JLM compiler (RVSDG-based) offers additional IR design perspective within the group. The candidate is actively developing LLVM/MLIR implementation depth in parallel with this application.

## 5. Expected Contributions

1. **Formal QEC precision-resource trade-off model** — an IR-level cost-correctness model formalizing the TAFFO-style analysis structure for QEC code selection in logical qubit programs
2. **Compiler optimization pass suite** — C/C++ analysis and transformation passes within LLVM/MLIR-compatible infrastructure implementing subcircuit-granular QEC code selection
3. **Reproducible benchmark suite** — versioned evaluation protocol and open benchmark suite for resilience-aware quantum compilation, enabling community replication
4. **Peer-reviewed publications** — targeting SSG's home venues (CGO, PLDI, CC) and quantum software engineering venues (QSW, IEEE Quantum Week)

## 6. Risk and Mitigation

| Risk | Mitigation |
|---|---|
| IR abstraction mismatch with QEC semantics | Start from MLIR Quantum Dialect; consult Politecnico di Milano partner team on IR design choices in Phase 1 |
| Benchmark coverage too narrow | Diversify circuit workload suite across ≥3 QEC code families and ≥2 noise models in Year 1 baseline |
| Metric ambiguity (correctness vs. overhead) | Define primary/secondary objective hierarchy with explicit Pareto trade-off criteria before pass design |
| LLVM/MLIR integration complexity | Stage from minimal prototype to full pipeline; use existing TAFFO pass structure as an implementation reference |
| QEC code selection sensitivity to noise model | Evaluate under multiple noise models; document sensitivity as an independent deliverable |

## 7. Three-Year Progress Plan

**Year 1 (Foundations):** Literature review of TAFFO/precision tuning tools, QEC code families, quantum compiler IR literature. Formal precision-resource model. Baseline pipeline reproducing published overhead results. Initial prototype passes in C/C++. First meeting/visit to Politecnico di Milano.

**Year 2 (Core Development):** Full pass suite implementation. Systematic benchmarking. Mid-cycle publication submission (CGO or QSW). Cross-site workload validation with Politecnico di Milano. IR abstraction refinement from benchmarking feedback.

**Year 3 (Consolidation and Dissemination):** End-to-end framework, broader workload generalization, open benchmark release. Thesis writing. Journal submission and final research stay at Politecnico di Milano.

## 8. Candidate Fit

My MS thesis implemented real-time recognition software in C and C# — systems-level work requiring careful reasoning about computation-correctness trade-offs and precision bounds, the analytical pattern directly applicable to compiler pass design. My current research at RIT on fault-tolerant quantum network optimization involves contextual bandit algorithms and hybrid variable frameworks for adaptive routing under error-sensitivity and capacity constraints, building toward peer-reviewed publication. Both the adaptive routing framework and the proposed compiler work are instances of the same abstract problem: structured optimization over correctness-resource trade-off surfaces under uncertainty. Prof. Cherubin's precision tuning research trajectory, embodied in TAFFO and extended in SPQR, is precisely the computational framework I want to contribute to and extend into the quantum compiler domain. The collaboration with Politecnico di Milano, where the foundational work on compiler-assisted precision tuning was originally developed, adds a dimension to this PhD I find genuinely exciting. I am committed to developing the LLVM/MLIR implementation depth required from the start of the programme.
