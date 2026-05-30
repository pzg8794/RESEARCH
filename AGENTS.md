# RESEARCH Agent Notes

This file applies to the entire `RESEARCH/` tree.

## LOCKED: Canonical GPA Values — DO NOT CHANGE

The following GPA values are locked. No agent, script, or human edit may
change them to any other value for any reason, including rounding, approximation,
or "correction." These are the values the applicant uses in all applications.

| Degree | Institution | GPA |
|---|---|---|
| Dual B.S. Computer Engineering Technology / Electrical Engineering | Farmingdale State College | **3.3** |
| M.S. Computer Science | Rochester Institute of Technology | **3.2** |
| M.S. Data Science | Rochester Institute of Technology | **3.9** |
| M.S. track, Teaching Computer Science K–12 | University of Rochester, Warner School of Education | **4.0** |

**Enforcement rules:**
- Do NOT use approximations like `3.9+`, `~3.9`, or `≈4.0`.
- Do NOT use more decimal places (e.g., `3.93`, `3.23`).
- Do NOT omit a GPA from a CV that already lists it.
- When creating a new CV tex file, copy GPA values exactly from this table.
- If a GPA appears in a motivation letter, cover letter, or any application text, use the same values from this table.

## Application Artifact Rules

- For PhD/fellowship packet building, follow the lookup order in
  `APPLICATIONS/PhD/OVERLEAF_DISCOVERY_PLAYBOOK.md`.
- Canonical CV source files are in `APPLICATIONS/PhD/application-materials/`.
- Always verify GPA values against this file before any CV edit.
- Packet-status files live in `APPLICATIONS/PhD/application-materials/` and
  must be updated after every submission or resubmission.

## Non-Destructive Policy

- Do not delete, overwrite, or rename application materials without explicit
  user instruction.
- Create versioned copies (e.g., `-v2`, `-v3`) rather than overwriting.

## ICT Experience Coverage Rule (ALL AGENTS — MANDATORY)

When filling any application portal ICT/skills section:
1. Pull the full list of required AND preferred technical skills from the job posting.
2. Cross-reference every skill against what is already entered in the ICT section.
3. For any required or preferred skill that is missing, identify the closest
   equivalent from the candidate's actual experience and add it with an
   honest description. Do not fabricate; do use equivalent framing
   (e.g., "gate-based quantum circuit simulation via Qiskit/Cirq" covers
   "gate-based quantum computing" if that is the actual experience).
4. Document the mapping in the application's packet-status file.
5. This rule applies to every portal and every agent — no exceptions.

## Projects / Publications Coverage Rule (ALL AGENTS — MANDATORY)

Before submitting any application with a Projects or Publications section:
1. Enumerate all documented projects from RESEARCH/MASTER_RESEARCH_INDEX.md
   that have a GitHub, Overleaf, or Google Drive source link.
2. Map each to either "Project / research experience" or "Publications /
   scientific productions" in the portal.
3. For anything that fits the application's research area, add it with:
   - Title, brief description, year, and source link
   - Role (sole author, co-author, lead developer, etc.)
4. Update the packet-status file with the final list.
5. This rule applies to every portal and every agent — no exceptions.

## Portfolio Evidence Coverage Rule (ALL AGENTS — MANDATORY)

Before every PhD or fellowship application — especially positions requiring C/C++, systems programming, or industry software experience:
1. Check `RESEARCH/PORTFOLIO/PORTFOLIO_INDEX.md` and `https://github.com/pzg8794/portfolio` for relevant evidence artifacts.
2. For positions requiring C/C++: the `Portafolio Projects/Projects Code/C++` and `CPP_OOP` Drive folders contain direct code evidence (MS CS, RIT 2017). Reference or mirror to the portfolio GitHub repo.
3. For positions requiring industry software experience: the `Work Projects` folder (Qualitrol, TrueInteraction, TiburonLockers) is the primary evidence source.
4. The `Piter Portfolio` Google Doc (Aug 2025, starred) is the canonical current portfolio narrative — open it first for any portfolio summary work.
5. Do NOT use the 2015 academic PDFs in the `Publications` subfolder as primary PhD writing samples; use Overleaf-tracked papers instead (see `APPLICATIONS/PhD/OVERLEAF_PAPER_INDEX.md`).

This portfolio supplements `MASTER_RESEARCH_INDEX.md` — both should be consulted.
