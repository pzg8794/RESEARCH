# Research Statement Draft — UW Information Science

Status: **DRAFT — NOT SUBMITTED**
Official range: **1,000–2,000 words**

## Reliable decisions when evidence is incomplete

My research asks how artificial-intelligence and data systems should make decisions when evidence is incomplete, delayed, noisy, outdated, or uneven across people and institutions. These conditions are common in high-stakes settings. Clinical records may omit relevant context, scientific findings may be unevenly represented in retrieval systems, and an apparently strong model may fail differently for groups whose evidence is sparse or poorly captured. In those settings, aggregate accuracy is not enough. A technically useful system must also be evaluated for calibration, reliability, latency, abstention or clarification behavior, and differences in who is repeatedly missed.

I approach this problem as both a computational and an information problem. Algorithms determine how evidence is ranked, combined, or acted upon, but information practices determine what evidence exists, whose observations are recorded, and whether outputs can be interpreted and challenged. My goal is to develop reproducible methods for studying that complete decision path. I want to identify when an AI-supported decision is trustworthy, when the system should ask for more information or defer, and how reliability changes across evidence conditions and populations.

## Preparation and current work

My preparation combines computer engineering, computer science, data science, software and data systems, healthcare machine learning, and inclusive computer-science education. I completed an M.S. in Computer Science at Rochester Institute of Technology and am completing an M.S. in Data Science there in December 2026. In industry, I developed Python machine-learning workflows for healthcare use cases at VIOME and designed Python data pipelines, validation workflows, AWS processes, and analytics-ready datasets at VEDADATA. Those experiences taught me that model behavior cannot be separated from ingestion, cleaning, validation, documentation, and operational use.

My current graduate research develops a shared simulation and evaluation framework for sequential resource allocation. The thesis, *Fairness-Aware Bandits for Network Routing in Quantum and Clinical Settings*, compares algorithms that repeatedly choose among possible actions, observe feedback, and improve later choices. I study utility, reliability, latency, robustness, and group- or flow-level disparities when contextual information is incomplete, delayed, noisy, or uneven. Quantum-network routing provides a constrained computational testbed in which path selection and qubit resources must be allocated under changing conditions. A clinical decision simulation provides a distinct high-stakes setting for testing whether useful context improves decisions and whether fairness-aware policies can reduce disparities without discarding useful performance.

I do not treat the two domains as ethically interchangeable. Their shared research object is the decision structure: allocating scarce resources from partial feedback while preserving traceable evaluation. Building this work has required reusable policy interfaces, structured logging, controlled stochastic and adversarial experiments, comparison-ready datasets, and careful separation of evidence from inference. It has also shown me the limits of a purely algorithmic view. Missing context is not always random. It can be produced by institutional processes, accessibility barriers, and historical differences in whose information is collected or treated as credible.

My concurrent M.S. in Teaching Computer Science K–12 and advanced certificate in disability and inclusive practices at the University of Rochester have sharpened that insight. Teaching preparation has made accessibility, explanation, and learner agency part of how I evaluate systems. If a person cannot access an interface, understand an output, communicate uncertainty, or challenge a mistaken recommendation, the system's technical performance does not describe its full quality.

## Proposed research agenda

At UW, I want to study evidence-aware AI decision support in health and scientific-information settings. The smallest coherent agenda has three connected questions.

First, how does the quality and distribution of available evidence affect model and retrieval reliability? I would construct controlled evidence conditions in which relevant information is missing, delayed, outdated, or unevenly represented. I would then compare pipelines using measures such as task utility, calibration, robustness, abstention, clarification requests, and subgroup disparity. The objective is not simply to show that less information reduces performance. It is to identify which kinds of evidence loss create systematic failure, which evaluation measures reveal that failure, and when a system should stop pretending to know.

Second, how should a decision-support pipeline respond when its evidence is weak? Possible responses include retrieving additional material, requesting clarification, surfacing competing interpretations, abstaining, or routing the case to human review. I am interested in policies that allocate limited attention to these options rather than always generating a single answer. My current bandit work provides a foundation for comparing adaptive decision policies, while information-science research provides the concepts needed to define useful evidence, human oversight, and institutional consequences.

Third, how do accessibility and presentation affect downstream decision quality? Scientific and health information may technically exist while remaining inaccessible to people using assistive technologies or to readers without specialized training. I want to test whether alternative evidence presentations change comprehension, error detection, confidence, and appropriate reliance in human-AI decisions. This question should remain computationally concrete: accessibility conditions would be part of the experimental design, not a general statement of values.

I would begin with public or appropriately governed datasets and reproducible simulations rather than claim clinical deployment. The first phase would establish baselines and controlled evidence-degradation procedures. The second would compare decision and retrieval strategies. The third would introduce human-centered evaluation where scientifically and ethically appropriate. At each stage, I would document provenance, separate source facts from model inference, and preserve the ability to diagnose which layer failed.

## Why UW Information Science

UW Information Science is a strong disciplinary home because the program can support the computational, institutional, and human parts of this agenda without reducing one to the other. Lucy Lu Wang's work on NLP, scientific-text understanding, clinical decisions, accessibility, and AI reliability is closely aligned with my interest in evidence-aware scientific and health-information systems. I am particularly interested in contributing reproducible evaluation of uncertainty, missing evidence, and unequal failure across information conditions.

Tanu Mitra's work in responsible AI, safety, evaluation, epistemic alignment, and AI in health offers a complementary foundation for asking when an output is reliable within real human and institutional contexts. My background in computational experiments and data systems could contribute measurable evaluations while her research environment would help me connect model behavior to how people produce, interpret, and contest information.

Wanda Pratt's work in personal and mental-health informatics provides the health-system and human-impact perspective needed to keep this research grounded in the burdens experienced by patients and caregivers. Her work makes it possible to examine not only whether a system predicts well, but whether information support actually reduces burden and helps people make better decisions. Amy Ko's research in critical and liberatory computing education is also relevant to my secondary interest in how people learn to question and improve AI systems, though I would keep the doctoral research centered on reliable high-stakes information support.

Together, this faculty cluster supports a coherent path: computational reliability, responsible evaluation, health-information practice, and accessibility. I would not arrive with a finished method or a claim that one framework solves every domain. I would bring a clear problem, strong implementation and evaluation habits, and a willingness to refine the questions through collaboration.

## Intended contribution

My long-term goal is to become a faculty researcher and educator who builds rigorous decision-support systems and makes the knowledge needed to test them more accessible. I want my doctoral work to produce methods, datasets, and evaluation practices that help researchers and institutions recognize when an AI system is missing important evidence and who bears the cost of that failure.

The central principle is practical: understand the information process before automating it, establish a baseline before changing it, use the simplest reliable method, and expand only when evidence supports doing so. At UW, I hope to turn that principle into a focused research program on reliable and equitable AI decision support under incomplete evidence.

## Source anchors

- `COMMON_DOSSIER.md`
- `PREPARATION/shared-career-evidence.md`
- `RESEARCH-STATEMENT-PLAN.md`
- `FACULTY-FIT.md`
- `PREPARATION/research/2026-08-10-dsci602-scope-consolidation/advisor-decision-memo.md`
