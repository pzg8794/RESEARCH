# ICNP Review Classification And A+C-First Revision Roadmap

Updated: 2026-08-04

## Decision Summary

ICNP 2026 submission #330 received a final rejection with three reviewer
recommendations: one Weak Accept, one Reject, and one Weak Reject. The reviews
do not indicate that the entire research direction failed.

The correct revision strategy is:

1. **Reviewer A is the accepted core.** This expert reviewer considered the
   manuscript weakly acceptable and validated the evaluation design,
   cross-testbed evidence, and capacity-paradox finding.
2. **Reviewer C is the conversion checklist.** Although this reviewer selected
   Weak Reject, the review recognized the matched-evaluation problem and the
   controlled grid as a genuine methodology contribution. Most requested
   additions are concrete and testable.
3. **Reviewer B is a secondary risk audit.** B's concerns remain important,
   especially where they overlap with C, but B does not control the first
   revision pass.

This means two reviewers recognized the paper's central evaluation value. The
fastest path is to preserve that value, make it easier to understand and
reproduce, and then strengthen physical grounding and scale evidence.

## Difficulty Scale

| Level | Meaning | Typical effort estimate |
| --- | --- | --- |
| Low | Writing, reorganization, or a table/diagram built from existing evidence | One focused work session |
| Low-Medium | Precise technical documentation derived from code, configs, or logs | One to three focused sessions |
| Medium | Literature grounding, parameter justification, or advisor-validated reframing | Two to four focused sessions |
| High | New experiment design, implementation, execution, diagnosis, and validation | One to three weeks depending on code and compute readiness |

The estimates describe technical effort, not fixed calendar promises.

## Reviewer Classification

| Reviewer | Recommendation / expertise | What is already working | Feedback categories | Difficulty | Revision role |
| --- | --- | --- | --- | --- | --- |
| A | Weak Accept / Expert | Comprehensive evaluation design; explicit policy-allocator-capacity factorization; validation across external testbeds; capacity paradox as a useful insight | Contribution positioning; narrative compression; reducing policy/table overload | Low to Medium | **Anchor. Preserve these strengths and make them the paper's visible spine.** |
| C | Weak Reject / No familiarity | The matched-evaluation problem is real; the controlled grid is a genuine evaluation-methodology contribution | Reproducibility; algorithm specification; context definition; allocator-policy semantics; threat grounding; topology scale | Low to High by item | **Primary conversion target. Complete the concrete checklist in stages.** |
| B | Reject / Expert | Benchmarking bandit methods for quantum routing is interesting | System-model clarity; algorithm definition; physical mapping; topology realism; theoretical or real-world support | Medium to High | **Secondary risk audit. Resolve overlaps with C first, then inspect remaining B-only risks.** |

## Feedback Categories By Difficulty

| Category | Reviewers | What must change | Difficulty | Completion evidence |
| --- | --- | --- | --- | --- |
| Accepted evaluation contribution | A, C | Preserve the matched policy-allocator-capacity design, cross-testbed validation, and capacity paradox; do not bury or remove them | Low | Contribution paragraph names no more than three central claims and each maps to one main figure or table |
| Contribution positioning | A | State clearly that the primary novelty is a controlled evaluation methodology and the evidence it reveals, not an unsupported claim of a new bandit family | Low | Abstract, introduction, contributions, and conclusion use the same contribution statement |
| Narrative compression | A | Reduce the number of visible variants and detailed tables in the main story; move supporting detail to appendix without deleting validated evidence | Low-Medium | A nonexpert reader can state the problem, method, and three findings after reading the abstract and introduction |
| Joint algorithm specification | C, B | Add one end-to-end algorithm showing context construction, path selection, allocation, feedback, replay, and policy update | Low-Medium | `Algorithm 1` or equivalent pseudocode can be followed without reading source code |
| Context and hyperparameter specification | C, B | Define every context feature, vector dimension, normalization, missing-value behavior, training cadence, pursuit settings, and NeuralUCB/TS settings | Low-Medium | One context-feature table and one reproducibility/configuration table trace to code or configs |
| Allocator-policy relationship | C, B | Explain whether allocation occurs before, after, or jointly with route choice and how it changes the action space or feedback distribution | Low | One interface diagram plus a short contract table identifies inputs, outputs, and update order |
| Threat-to-physics mapping | C, B | Map each controlled regime to plausible quantum-network failures or adversaries; justify parameters or label them explicitly as controlled stress tests | Medium | One threat-mapping table has a physical interpretation, parameter rationale, source, and claim boundary for every regime |
| Claim calibration | C, B | Remove or soften deployment-scale language until the scale evidence supports it | Low | Abstract, discussion, and conclusion contain no deployment claim stronger than the validated testbeds support |
| Medium-scale generalization | C, B | Add at least one primary topology with approximately 15-20 nodes and 10 or more candidate paths | High | Reproducible configuration, logs, plots, and comparison with the current small topology are archived |
| Large-topology diagnosis | C, B | Explain the approximately 44.1 percent efficiency result on the 100-node testbed | High | Ablations separate convergence horizon, context/state size, routing diversity, allocator effects, and replay capacity |

## Execution Order

### Phase 0: Protect The Accepted Core

- [ ] Freeze the current validated results, figures, tables, logs, and configs.
- [ ] Create a claim-to-evidence map for the evaluation framework,
  cross-testbed validation, and capacity paradox.
- [ ] Do not delete a model variant, result, figure, or table. Relocation and
  compression require traceable preservation in the appendix or audit notes.

**Exit test:** every strength recognized by Reviewer A remains traceable to
validated evidence.

### Phase 1: Reviewer A Plus The Easy Reviewer C Items

- [ ] Rewrite the contribution statement around controlled evaluation and no
  more than three central findings.
- [ ] Simplify the main-body narrative and move detailed variants or tables to
  supporting material.
- [ ] Add a joint decision-loop algorithm or pseudocode block.
- [ ] Add the complete context-feature and hyperparameter tables.
- [ ] Add an allocator-policy interface diagram and execution-order table.

**Difficulty:** Low to Medium.

**Exit test:** the paper is understandable, reproducible at the interface
level, and directly answers every non-scale request from Reviewers A and C.

### Phase 2: Reviewer C Grounding

- [ ] Add the threat-to-physical-failure mapping table with sources.
- [ ] Justify the five regimes and their parameters, or explicitly classify
  them as controlled stress tests rather than literal physical models.
- [ ] Calibrate real-world and deployment language to the evidence.
- [ ] Ask the quantum-network coauthors to validate the physical mappings and
  claim boundaries.

**Difficulty:** Medium.

**Exit test:** each threat regime has a defensible role, physical analogue,
parameter rationale, and stated limitation.

### Phase 3: Reviewer C Scale Evidence

- [ ] Add a 15-20 node primary topology with at least 10 candidate paths.
- [ ] Compare learning curves, efficiency, regret, allocator behavior, and
  replay-capacity sensitivity with the current small topology.
- [ ] Diagnose the 100-node efficiency compression near 44.1 percent through
  controlled ablations.
- [ ] Report what transfers across scales and what does not.

**Difficulty:** High.

**Exit test:** the manuscript supports a bounded generalization claim with a
reproducible medium-scale experiment and a documented explanation of the
100-node result.

### Phase 4: Reviewer B Risk Audit

- [ ] Map every B concern to the artifacts completed for A and C.
- [ ] Identify any B-only issue that remains after Phases 1-3.
- [ ] Ask coauthors whether the remaining item is required for the next venue
  or should be stated as a limitation and future-work boundary.

**Exit test:** B's review has been considered fully, but it has not displaced
the A+C-first revision strategy.

## First Work Session

The next paper session should produce these four artifacts before any new
experiment is started:

1. A two-sentence contribution statement.
2. A one-page joint decision-loop pseudocode draft.
3. A context and hyperparameter inventory derived from the implementation.
4. An allocator-policy interface diagram or table.

These changes directly preserve Reviewer A's Weak Accept and address the
lowest-cost, highest-value requests from Reviewer C.

## Thesis Connection

The current DSCI 601 proposal already defines clinical decision workflows and
quantum-network routing as two testbeds for one fairness-aware bandit
framework. The proposed DSCI 602 plan is therefore a scope consolidation:

- use the quantum manuscript revision as the primary technical implementation;
- retain the clinical testbed as the fairness and transfer comparison;
- align the shared algorithm, context, fairness, and evaluation artifacts;
- document course, assistantship, and coauthor responsibilities separately.

This is not a proposal to double-count work. It is a proposal to organize the
remaining work around one coherent research contribution with explicit
milestones and approval.

## Retargeting Options

| Rank | Venue | Verified deadline | Fit and decision |
| --- | --- | --- | --- |
| 1 | [IEEE Network: Quantum Communications and Networking Series 5](https://www.comsoc.org/publications/magazines/ieee-network/cfp/quantum-communications-and-networking-series-5) | August 20, 2026 | Excellent scope match for intelligent quantum networks, routing, resource allocation, simulators, and performance evaluation. This is a magazine series, not a conference. Submit only if the A+C interface, grounding, and presentation work is complete and all coauthors approve by the August 19 go/no-go review. |
| 2 | [ICNC 2027: Quantum Networking and AI for Computing and Control](https://www.conf-icnc.org/2027/cfp.html) | August 15, 2026 | Strongest currently open conference-track match, but the deadline is too close to the scheduled A+C work. Do not rush it unless the coauthors already have a submission-ready revision before August 13. |
| 3 | [IEEE CCWC 2027](https://ieee-ccwc.org/call-for-papers/) | November 6, 2026 | Broader and weaker topical match, but it accepts regular and work-in-progress papers and leaves time to complete Reviewer C's grounding and scale work. Use as a conference fallback after advisor review. |
| 4 | [IEEE Transactions on Networking](https://www.comsoc.org/publications/journals/ieee-tnet/policies-guidelines) | Rolling | Best archival path after the complete A+C revision and B risk audit. Typical maximum is 16 pages. Do not submit concurrently with any conference, symposium, workshop, or journal. |

### Current Recommendation

Use the August 19 IEEE Network review as a real quality gate, not a forced
deadline. If the A+C evidence is not ready, skip both August venues and complete
the Reviewer C scale work for the November conference fallback or the rolling
Transactions path. The paper should move because the revision is defensible,
not because a portal is about to close.

## Sources

- Authenticated ICNP review page: [submission #330](https://icnp26.hotcrp.com/paper/330#r330A)
- Quantum manuscript repository: [pzg8794/QuantumFaultTolerant](https://github.com/pzg8794/QuantumFaultTolerant)
- DSCI 601 repository: [pzg8794/DSCI601](https://github.com/pzg8794/DSCI601)
- Current thesis draft: [rough draft report](https://github.com/pzg8794/DSCI601-Project_Proposal/blob/main/rough_draft_report/rough_draft_report.pdf)
- Conditional near-term venue: [IEEE Network, Quantum Communications and Networking Series 5](https://www.comsoc.org/publications/magazines/ieee-network/cfp/quantum-communications-and-networking-series-5)
- Rolling journal path: [IEEE/ACM Transactions on Networking policies and guidelines](https://www.comsoc.org/publications/journals/ieee-tnet/policies-guidelines)

## Source Boundary

This public-safe record summarizes reviewer themes and metadata. It does not
copy private reviewer text. The authenticated HotCRP page and decision email
remain the source of truth.
