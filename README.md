# RESEARCH

This repository is the version-controlled research and PhD application portfolio for Piter Garcia.

## Critical Repository Safety Rule

**Agents, scripts, and collaborators must not delete Git repositories.** Do not
delete local clones, remote repositories, `.git` metadata, worktrees, branches,
tags, remotes, or Git history; do not re-clone over an existing repository; and
do not use destructive cleanup commands in or around this repository. Preserve
duplicates or damaged checkouts and investigate them non-destructively.

Read the mandatory [Repository Safety Policy](./REPOSITORY_SAFETY.md) and
[Agent Notes](./AGENTS.md) before making repository-level changes.

The portfolio tracks research artifacts, technical projects, writing samples, CV materials, application planning, and source-of-truth references across several connected areas:

- Machine learning for adaptive decision-making
- Quantum network routing and resource allocation
- AI-assisted learning and CS education
- Computational biology and RNA-seq analysis
- Inclusive pedagogy and educational access

The living planning source is maintained in Google Drive. This GitHub repository mirrors public-safe summaries, polished artifacts, and application-ready documentation.

## Artifact Discovery Order (Start Here)

When locating research documents, always follow this order:

1. **Overleaf first**: primary source for formal manuscripts, proposal-style papers, and polished LaTeX artifacts.
2. **Google Drive second**: broader planning files, historical drafts, and administrative working copies.
3. **GitHub third**: public-safe mirrors, summaries, and versioned derivatives.

Practical guidance:

- Start by searching Overleaf project titles directly (for example, `BIO614` to find `BIO614-FinalProjectProposal`).
- If multiple similar Overleaf projects appear, resolve the canonical packet source in `APPLICATIONS/PhD/OVERLEAF_CANONICAL_STATUS.md` before packaging a derivative.
- If an item is not in Overleaf, check the Drive source maps in `APPLICATIONS/PhD/LOCAL_SOURCE_MAP.md`.
- Use this repo to find sanitized final references and application trackers after source validation.

---

## Research Narrative

Piter Garcia's research portfolio sits at the intersection of machine learning, quantum network optimization, computational biology, and inclusive CS education. The central application narrative emphasizes **adaptive decision-making systems that support scientific, technical, and educational impact**.

The strongest technical direction is machine learning for quantum network routing and resource allocation, especially contextual and adversarial bandit methods. In parallel, AI and CS education work shows a commitment to translating technical ideas into equitable learning environments. Computational biology work demonstrates scientific computing maturity and ability to write in research formats. Together, these threads support a PhD trajectory focused on machine learning, applied computing, and socially meaningful technical systems.

---

## Core Application Artifacts

| Artifact | Path |
| --- | --- |
| Master Research Index | [`MASTER_RESEARCH_INDEX.md`](./MASTER_RESEARCH_INDEX.md) |
| Community Bridge Reading Path | [`PORTFOLIO/COMMUNITY_BRIDGE_READING_PATH.md`](./PORTFOLIO/COMMUNITY_BRIDGE_READING_PATH.md) |
| TODO / Follow-up Tasks | [`TODO_PHD_RESEARCH.md`](./TODO_PHD_RESEARCH.md) |
| Public Repository Showcase Plan | [`APPLICATIONS/PhD/PUBLIC_REPOSITORY_SHOWCASE_PLAN.md`](./APPLICATIONS/PhD/PUBLIC_REPOSITORY_SHOWCASE_PLAN.md) |
| Statement Theme Library | [`STATEMENTS/statement-theme-library.md`](./STATEMENTS/statement-theme-library.md) |
| PhD and Research Application Roadmap | [`APPLICATIONS/PhD/phd-application-roadmap-2026-2027.md`](./APPLICATIONS/PhD/phd-application-roadmap-2026-2027.md) |
| Fellowship Opportunity Queue | [`APPLICATIONS/Fellowships/profellow-opportunity-queue-2026-05-27.md`](./APPLICATIONS/Fellowships/profellow-opportunity-queue-2026-05-27.md) |
| Fulbright Awards Queue | [`APPLICATIONS/Fellowships/fulbright-awards-queue-2026-05-27.md`](./APPLICATIONS/Fellowships/fulbright-awards-queue-2026-05-27.md) |
| ProFellow Search Routine | [`APPLICATIONS/Fellowships/profellow-search-routine.md`](./APPLICATIONS/Fellowships/profellow-search-routine.md) |
| Job Search Operations | [`APPLICATIONS/Jobs/README.md`](./APPLICATIONS/Jobs/README.md) |
| Job Pipeline | [`APPLICATIONS/Jobs/job-pipeline.md`](./APPLICATIONS/Jobs/job-pipeline.md) |
| RIT Fall 2026 CSCI-739 Audit | [`ADMIN/rit-fall-2026-csci739-audit.md`](./ADMIN/rit-fall-2026-csci739-audit.md) |
| Local PhD/Application Source Map | [`APPLICATIONS/PhD/LOCAL_SOURCE_MAP.md`](./APPLICATIONS/PhD/LOCAL_SOURCE_MAP.md) |
| Overleaf Writing-Sample Discovery Playbook | [`APPLICATIONS/PhD/OVERLEAF_DISCOVERY_PLAYBOOK.md`](./APPLICATIONS/PhD/OVERLEAF_DISCOVERY_PLAYBOOK.md) |
| Writing Sample Shortlists | [`APPLICATIONS/PhD/WRITING_SAMPLE_SHORTLISTS.md`](./APPLICATIONS/PhD/WRITING_SAMPLE_SHORTLISTS.md) |
| Canonical Overleaf Project Status | [`APPLICATIONS/PhD/OVERLEAF_CANONICAL_STATUS.md`](./APPLICATIONS/PhD/OVERLEAF_CANONICAL_STATUS.md) |
| DSCI633 Manuscript Plan | [`PAPERS/Data_Science_and_Machine_Learning/DSCI633_MANUSCRIPT_PLAN.md`](./PAPERS/Data_Science_and_Machine_Learning/DSCI633_MANUSCRIPT_PLAN.md) |
| Academic CV | `CV/current/academic-cv.pdf` *(to be uploaded)* |
| Industry Resume | [`CV/current/industry-resume.pdf`](./CV/current/industry-resume.pdf) |
| Teaching CV | `CV/current/teaching-cv.pdf` *(to be uploaded)* |
| Statement of Purpose (PhD) | `STATEMENTS/statement-of-purpose-phd.md` *(to be drafted)* |
| Writing Sample | `STATEMENTS/writing-sample.pdf` *(to be selected)* |

---

## Repository Structure

```text
RESEARCH/
├── README.md                          # This file
├── MASTER_RESEARCH_INDEX.md           # Central index of all artifacts
├── TODO_PHD_RESEARCH.md               # Actionable follow-up checklist
├── CV/
│   ├── current/                       # Active CV and resume PDFs
│   └── archive/                       # Older versions
├── STATEMENTS/                        # SOP, personal, diversity, teaching statements, reusable theme library
├── PAPERS/
│   ├── AI_and_Education/
│   ├── Data_Science_and_Machine_Learning/
│   ├── Quantum_Computing/
│   │   ├── Quantum_MAB/
│   │   ├── UDRM_Quantum_Path_Optimization/
│   │   ├── iCMAB_EXPNeuralUCB/
│   │   ├── implementation_framework/
│   │   ├── literature/
│   │   └── references/
│   ├── Bioinformatics_Computational_Biology/
│   │   ├── DRG_RNAseq/
│   │   ├── HTSA_reports/
│   │   ├── HTSA_paper/
│   │   └── references/
│   ├── Computer_Graphics/
│   │   └── source/
│   └── CS_Education_and_Pedagogy/
│       ├── inclusion/
│       └── group_lesson_plans/
├── PROJECTS/
│   ├── AI_as_partner/
│   └── AI_Business_Model_Project/
├── PORTFOLIO/
│   ├── COMMUNITY_BRIDGE_READING_PATH.md # Reader-first community-partner sequence
│   └── PORTFOLIO_INDEX.md               # Broader portfolio inventory
├── APPLICATIONS/
│   ├── Fellowships/                 # ProFellow queue, bookmarks, and discovery workflow
│   ├── Jobs/                        # Job pipeline and public-safe communication logs
│   ├── Mira/                        # Mira Fellowship artifacts and staged materials
│   ├── Noyce/
│   └── PhD/                         # PhD planning, deadlines, and public-safe application trackers
├── ADMIN/                             # Non-private admin notes only
└── ARCHIVE/
    └── course_notes/
```

> ⚠️ Private administrative documents (insurance, health, enrollment, financial records) are **never** stored here. They live exclusively in Google Drive under `05_ADMIN_PRIVATE/`.

---

## Priority Ranking for PhD Positioning

1. **Quantum Computing / Quantum Networks / ML Bandits** — strongest technical research thread
2. **AI + CS Education** — strongest teaching and impact thread
3. **Bioinformatics / Computational Biology** — evidence of scientific computing and methods writing
4. **CS Education / Inclusive Pedagogy** — Noyce, Warner, education programs, broader impact
5. **Computer Graphics** — historical technical evidence; not centered unless applying to graphics programs
6. **Administrative / Noyce logistics** — important for applications but not research identity
