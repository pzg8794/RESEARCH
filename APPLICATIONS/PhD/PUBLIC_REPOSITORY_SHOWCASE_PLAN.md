# Public Repository Showcase Plan (PhD Applications)

This document defines which GitHub repositories should be public, private-but-referenced, or de-emphasized for graduate applications.

## Goal

Present a focused, high-quality repository set that shows research depth, reproducibility, and technical writing quality.

## Priority Showcase Repositories

Current visibility was checked through GitHub CLI on 2026-05-26. Use [GITHUB_REPO_REGISTRY.md](./GITHUB_REPO_REGISTRY.md) for the broader linked repo list.

| Priority | Repository | Primary role in applications | Current visibility | Target visibility | Current recommendation |
|---|---|---|---|---|---|
| P0 | [pzg8794/RESEARCH](https://github.com/pzg8794/RESEARCH) | Portfolio anchor: artifact index, statements, application framing | Public | Public | Keep public and curated |
| P0 | [pzg8794/pzg8794](https://github.com/pzg8794/pzg8794) | GitHub profile README for PhD applications and public research identity | Public | Public | Keep aligned with RESEARCH and CV links |
| P0 | [pzg8794/quantum_project_hub](https://github.com/pzg8794/quantum_project_hub) | Project/testbed navigation for quantum-routing tracks | Public | Public | Keep public and up to date |
| P1 | [pzg8794/CV_Piter-Garcia](https://github.com/pzg8794/CV_Piter-Garcia) | Current CV/resume source and profile operations | Public | Public or private after review | Keep public only if process transparency is desired |
| P1 | [pzg8794/QuantumFaultTolerant](https://github.com/pzg8794/QuantumFaultTolerant) | Paper workflow quality: manuscript ops, venue prep, validation evidence | Private | Private until public-safe | Do not make public until manuscript/adviser/venue constraints are cleared |
| P1 | [pzg8794/quantum_project](https://github.com/pzg8794/quantum_project) | Core framework and multi-testbed implementation evidence | Private | Private until cleaned | Use public-safe summaries in RESEARCH unless repo is sanitized |
| P2 | [pzg8794/CV_Piter-Garcia-UOR-2025-](https://github.com/pzg8794/CV_Piter-Garcia-UOR-2025-) | Teaching-facing UofR/Warner resume redesign | Private | Private | Reference only as teaching-resume history |

## Repositories To De-Emphasize In Applications

- `pzg8794/GA-Work` (personal superproject): keep for internal coordination, but do not center this in application narratives.
- `pzg8794/CV_Piter-Garcia-UOR-2025-` (private teaching resume): reference for teaching-facing CV history, but do not expose raw contents.
- Legacy coursework or utility repositories that do not support current research identity.

## Application-Facing Quality Bar

For each public showcase repo:

1. README explains problem scope, contribution, and how to run/inspect outputs.
2. Repository has clear structure and no sensitive/private files.
3. Documentation reflects current state (not stale placeholders).
4. At least one reproducibility path is documented (commands, notebooks, or validation logs).
5. Main branch is clean and uses meaningful commit messages.

## Suggested Candidate Ordering On GitHub Profile

1. RESEARCH
2. pzg8794 profile README
3. quantum_project_hub
4. CV_Piter-Garcia
5. Public-safe teaching or BIOL/DSCI repo, depending on the target application

Private repos such as `QuantumFaultTolerant`, `quantum_project`, and `CV_Piter-Garcia-UOR-2025-` should not be pinned unless they are made public and sanitized.

## Maintenance Cadence

- Weekly: quick README and broken-link check for P0 repos.
- Before each application submission: verify pinned repos and top-level docs.
- After major project updates: add concise changelog note in the affected repo.

## Decision Record

- 2026-05-25: Initial public-repo showcase plan created to separate application-facing repositories from personal coordination repositories.
- 2026-05-26: GitHub audit linked the public CV repo, private UofR teaching-resume repo, GitHub profile README repo, and application-facing evidence repos through [GITHUB_REPO_REGISTRY.md](./GITHUB_REPO_REGISTRY.md); current visibility was corrected for private quantum/CV repos.
