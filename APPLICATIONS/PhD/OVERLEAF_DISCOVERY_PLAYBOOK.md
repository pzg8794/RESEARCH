# Overleaf Discovery Playbook for Application Materials

Updated: 2026-05-28

This playbook records how to rapidly find high-value writing samples for PhD and fellowship packets.

## Canonical retrieval order

1. Overleaf first (formal manuscripts and paper-style artifacts).
2. Google Drive second (broader archive, planning, and historical drafts).
3. GitHub third (public-safe mirrors, packet trackers, and sanitized derivatives).

Timing rule:

- Google Drive and GitHub can be treated as interchangeable lookup layers when timing is tight.
- Even when using that shortcut, always anchor navigation from the DataScience root first:
  - [DataScience root Drive folder](https://drive.google.com/drive/folders/1pY_fQ54nHKvFABNRGYAr5bQ3su_tUDAi?usp=sharing)
  - This root lands at semester-level directories where course folders are nested for fast traversal.

## Standard workflow

1. Open Overleaf project list.
2. Use the search box with a course or topic keyword.
3. Capture candidate projects with title, URL, and relevance score.
4. Prefer manuscript-style, methods-heavy, reproducible artifacts.
5. Keep non-destructive behavior: copy project before edits when packaging application-specific versions.
6. Log final chosen artifacts in packet-status files under `application-materials/`.

## Portal CV curation defaults

- Do not blindly mirror every LinkedIn or legacy-CV entry into live application portals.
- Exclude volunteer, pro bono, weak-fit, or user-disliked part-time roles unless the user explicitly asks to include them.
- Prefer the strongest recent research, teaching, tutoring, and directly relevant industry roles when a portal has a short work-history surface.
- Normalize noisy employer branding when it weakens the presentation, for example use `Varsity Tutors` instead of `Varsity Tutors, a Nerdy Company` unless the full legal branding is specifically needed.
- For the University of Rochester teaching placement, use the user-approved title `UofR Warner School Teaching Placement` or an explicit replacement the user requests; keep the placement school as the organization when the form separates role title from organization.
- After each live portal CV edit, reopen the send/preview state, confirm the unwanted entry is absent, and record the retained set in the packet-status file.

## Verified search keywords and results

### BIO614

- `BIO614-FinalProjectProposal` -> `/project/68a761a470c296440522a537` (primary BIO614 manuscript-style evidence)
- `BIO614-Project_Proposal` -> `/project/6801a374fdbab3130b844398`
- `BIO614-Project_Proposal2` -> `/project/680192464bec9fc317edfdd4`
- `BIO614-Project_Proposal` -> `/project/6801835c29fff18f5bc05afb`

Recommendation: use `BIO614-FinalProjectProposal` as the first BIO writing-sample anchor.

### DSCI601

- `Uppsala-2026-Writing-Sample-DSCI601-Clean` -> `/project/6a17c004b31cb222b4ffa75a` (current cleaned application copy)
- `DSCI601-Project_Proposal_Final` -> `/project/69fabc7d791e6b1ee999ff4c`
- `DSCI601-Project_Proposal` -> `/project/69941bd7ee1169df5004fd26`
- `DSCI601-Project_Presentation` -> `/project/69f41fca7e6dfa2926019e62`
- `DSCI601-Project_Rough_Draft` -> `/project/69e84596e393ca9e39437d3f`
- `DSCI601-Architecture_Writeup` -> `/project/69e5a255cb0a1e055a0e270a`
- `DSCI601-Extra` -> `/project/69e10d60d51e14cfab615a2a`

Recommendation: keep the cleaned DSCI601 manuscript copy as core methods/fairness evidence.

### ISTE780

- `ISTE780-Lab5-Report` -> `/project/68945fb950c987645f1ac4ca`
- `ISTE780-Lab4-Report` -> `/project/688b182bb3f4dc2b2916d1e7`
- `ISTE780-Project_Phase4` -> `/project/687b2ee4bacc2838e411460b`
- `ISTE780-Lab3-Report` -> `/project/68730e1b162a9946d16ad890`
- `ISTE780-Project_Phase2` -> `/project/685f6d4e7cfd1be32fb1edc2`
- `ISTE780-Lab2-Report` -> `/project/6862...` (visible in list; capture full ID when selected)

Recommendation: use `ISTE780-Project_Phase4` before lab-only reports when stronger project narrative is needed.

### IDAI700

- `IDAI700-Research_Portfolio` -> `/project/6912b8af5f8d972c24f1a3af` (primary IDAI700 candidate)
- `IDAI700-Reflection9` -> `/project/692aab0f82feceb233d08217`
- `IDAI700-Reflection8` -> `/project/692aaad00c4b289dbb2d69f2`
- `IDAI700-Reflection5` -> `/project/6917f399749fc724f36b5ff2`
- `IDAI700-Unit6-AI_in_Hiring-Reflective_Journal` -> `/project/68fd704cf15f899ed5134bb8`
- `IDAI700-Unit6-Journal` -> `/project/68fc54d09806bccf5b401d7b`
- `IDAI700-Ban_Technology_Journal` -> `/project/68...` (visible in list; capture full ID when selected)

Recommendation: prefer `IDAI700-Research_Portfolio` over short reflections when attaching fairness/ethics evidence.

### BIOL550

- `BIOL550-Project_Paper` -> `/project/69e646218e011fb4b09687b5`
- `BIOL550-Project_Update` -> `/project/69...` (visible in list; capture full ID when selected)

Recommendation: use BIOL550 as companion computational biology evidence with BIO614, not standalone when possible.

### Quantum and GA

- `QuantumPathOptimization` -> `/project/68ea344896594f27b427ca8f`
- `2026_ijcnn_quantum_path_optimization` -> `/project/6945bfa58266e8759ad66f24`
- `QuantumFaultTolerant(draft)` -> `/project/6901745edee2c9a6507815c8`
- `GA-QuantumMAB-ProjectPlan` -> `/project/68ac548ee48df828c5fc8b5a`

Safety rule: for active anonymous submissions, attach anonymous-safe technical reports first; avoid reusing draft manuscript title/identity.

## Multi-sample packaging strategy

For strong applications, target a 2-4 sample packet when allowed:

1. BIO614 primary computational biology manuscript evidence.
2. DSCI601 methods/fairness manuscript evidence.
3. Quantum/GA anonymous-safe technical report (role-dependent).
4. Optional ISTE780 or IDAI700 artifact for computational systems or AI fairness breadth.

## Documentation rule after each submission update

After changing any live portal packet:

1. Update the role-specific packet-status file in `application-materials/`.
2. Record current live attachment filenames and application record ID.
3. Record source project names and whether copies were created before editing.
