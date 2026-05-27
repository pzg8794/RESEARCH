# GitHub Repo Registry for CV, Profile, and Application Evidence

Updated: 2026-05-26

This registry links GitHub repositories that matter for PhD, fellowship, CV, public-profile, and application evidence work back into the RESEARCH repo.

Audit source:

- `gh repo list pzg8794 --limit 200 --json nameWithOwner,url,visibility,description,updatedAt`
- targeted `gh repo view` checks for the CV/profile repositories
- local remotes for the active CV and GitHub-profile checkouts

## CV, Resume, and Profile Repositories

These are the CV/profile repos found on GitHub and now linked from this RESEARCH repo.

| Repository | Visibility on GitHub | Role | Local/source status | RESEARCH action |
| --- | --- | --- | --- | --- |
| [pzg8794/CV_Piter-Garcia](https://github.com/pzg8794/CV_Piter-Garcia) | Public | Current CV/resume source and profile-materials repo. | Local checkout: [CV_Piter-Garcia](<file:///Users/pitergarcia/DataScience/Semester5/Scholarship/CV_Piter-Garcia>); remote checked as `git@github.com:pzg8794/CV_Piter-Garcia.git`. | Treat as canonical CV source; link current PDF/source from [LOCAL_SOURCE_MAP.md](./LOCAL_SOURCE_MAP.md). |
| [pzg8794/CV_Piter-Garcia-UOR-2025-](https://github.com/pzg8794/CV_Piter-Garcia-UOR-2025-) | Private | Teaching-facing UofR/Warner resume redesign and K-12 CS/inclusion resume evidence. | No current local checkout found in the active DataScience tree during this audit; prior work treated it as a resume repo. | Reference as private historical/teaching-resume source; do not publish raw contents without review. |
| [pzg8794/pzg8794](https://github.com/pzg8794/pzg8794) | Public | GitHub profile README for PhD applications and public research identity. | Local checkout: [PHD/pzg8794](<file:///Users/pitergarcia/DataScience/PHD/pzg8794>); remote checked as `https://github.com/pzg8794/pzg8794.git`. | Keep aligned with RESEARCH, ORCID, ResearchGate, website, LinkedIn, and CV links. |
| [pzg8794/RESEARCH](https://github.com/pzg8794/RESEARCH) | Public | Portfolio anchor and cross-repo navigation hub. | Current pushed repo for this registry. | Use this registry as the entry point for GitHub repo navigation. |

## Application-Facing Research and Portfolio Repositories

These are not CV repos, but they are similar application-facing repositories that should be discoverable from RESEARCH.

| Repository | Visibility on GitHub | Application role | RESEARCH action |
| --- | --- | --- | --- |
| [pzg8794/quantum_project_hub](https://github.com/pzg8794/quantum_project_hub) | Public | Public navigation hub for quantum-routing/project testbeds. | Keep in showcase plan and pin/profile candidates. |
| [pzg8794/QuantumFaultTolerant](https://github.com/pzg8794/QuantumFaultTolerant) | Private | Quantum manuscript/research workflow evidence. | Keep private unless sanitized/public-safe; reference only in application planning. |
| [pzg8794/GA-Work](https://github.com/pzg8794/GA-Work) | Private | Personal research superproject with project submodules. | Keep as internal coordination; summarize public-safe outputs in RESEARCH. |
| [pzg8794/quantum_project](https://github.com/pzg8794/quantum_project) | Private | Core quantum/project framework evidence. | Keep private unless cleaned for public showcase. |
| [pzg8794/EXPNeuralUCB](https://github.com/pzg8794/EXPNeuralUCB) | Private | Shareable EXPNeuralUCB testbed package. | Use as technical evidence only after public-safety review. |
| [pzg8794/EQUITAS-Research-Paper.tex](https://github.com/pzg8794/EQUITAS-Research-Paper.tex) | Private | EQUITAS/fairness research paper source. | Reference as private research-writing source; do not expose raw draft. |
| [pzg8794/DSCI601-workspace](https://github.com/pzg8794/DSCI601-workspace) | Public | Data-science coursework/project workspace. | Use as public technical-evidence source if current and clean. |
| [pzg8794/DSCI601-Project_Proposal](https://github.com/pzg8794/DSCI601-Project_Proposal) | Public | DSCI601 project/proposal evidence. | Candidate support for ML/fairness methods. |
| [pzg8794/DSCI601-Project_Proposal_Final](https://github.com/pzg8794/DSCI601-Project_Proposal_Final) | Public | Final DSCI601 proposal evidence. | Candidate support for methods/writing sample review. |
| [pzg8794/BIOL550-Project_Paper](https://github.com/pzg8794/BIOL550-Project_Paper) | Public | Computational biology paper evidence. | Candidate writing/scientific sample for biomedical ML applications. |
| [pzg8794/mouse_group_project_work](https://github.com/pzg8794/mouse_group_project_work) | Public | Public BIOL550 mouse project documentation. | Candidate support for KTH/Uppsala biology/ML applications. |
| [pzg8794/BIOL550-group_project](https://github.com/pzg8794/BIOL550-group_project) | Private | BIOL550 group project working repo. | Reference privately; use sanitized public equivalents when possible. |
| [pzg8794/biol550](https://github.com/pzg8794/biol550) | Private | BIOL550 lab notes, reports, and analysis artifacts. | Reference privately; do not expose raw coursework or sensitive artifacts. |

## Teaching, Inclusion, and Broader-Impact Repositories

These are useful when applications need teaching, equity, inclusion, Noyce/Warner, or broader-impact evidence.

| Repository | Visibility on GitHub | Application role | RESEARCH action |
| --- | --- | --- | --- |
| [pzg8794/ED400-Comprehensive_Teaching_Portfolio](https://github.com/pzg8794/ED400-Comprehensive_Teaching_Portfolio) | Public | Public teaching portfolio evidence. | Candidate broader-impact/teaching link. |
| [pzg8794/ED452B-Innovative-Unit-Plan-Portfolio](https://github.com/pzg8794/ED452B-Innovative-Unit-Plan-Portfolio) | Public | Inclusive CS unit-plan portfolio. | Candidate teaching/inclusion artifact. |
| [pzg8794/ED452C](https://github.com/pzg8794/ED452C) | Public | ED452C course materials and discussion documentation. | Reference when documenting education-research identity. |
| [pzg8794/EDU498](https://github.com/pzg8794/EDU498) | Private | EDU498 literacy/teaching repo documentation. | Reference privately; copy only public-safe synthesis. |
| [pzg8794/teaching-placement](https://github.com/pzg8794/teaching-placement) | Private | Teaching placement evidence. | Keep private; use de-identified summaries only. |
| [pzg8794/EDU442-Bias_Deconstruct-Assignment](https://github.com/pzg8794/EDU442-Bias_Deconstruct-Assignment) | Public | Equity/bias deconstruction assignment. | Candidate broader-impact writing evidence. |
| [pzg8794/edu442-impacting-practice-ai-pd](https://github.com/pzg8794/edu442-impacting-practice-ai-pd) | Public | AI professional-development module for equitable elementary AI use. | Candidate public teaching/AI artifact. |
| [pzg8794/ede498c-integrating-cs-across-curriculum](https://github.com/pzg8794/ede498c-integrating-cs-across-curriculum) | Public | Integrated CS across curriculum evidence. | Candidate public teaching/CS artifact. |

## Not Centered

The GitHub account also contains legacy utilities, old coursework, demos, and unrelated business/application repositories. They are intentionally not centered in the PhD application map unless a future application needs them.

Examples: `Calculator`, `hello-express`, `Mobile-Detect`, `GAPP`, `Project_Progress`, `cleanData`, `cleanedData`, `DBSCAN`, `MLADIS-*`, `lodge-website`, and older private utility repos.

## Follow-Up Checks

- [x] Public CV repo linked.
- [x] Private UofR teaching-resume repo linked.
- [x] GitHub profile README repo linked.
- [x] RESEARCH repo identified as the GitHub navigation hub.
- [ ] Before each application submission, verify visibility again with `gh repo list pzg8794 --limit 200`.
- [ ] Decide whether `pzg8794/CV_Piter-Garcia` should stay public or become private after each CV update.
- [ ] Decide whether any private quantum/project repo should get a sanitized public mirror or a public-safe README excerpt in RESEARCH.
