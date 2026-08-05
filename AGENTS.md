# RESEARCH Agent Notes

This file applies to the entire `RESEARCH/` tree.

## Account Access And Thread Handoff

Before reporting that an account, mailbox, calendar, Drive file, portal, or
application is unavailable, follow this routing process:

1. Read `AGENTS.private.md` when it exists. It is a machine-local access map
   and is intentionally ignored by Git. Never commit, upload, quote, or copy
   its private account details into public repository files.
2. Use the purpose-built connector first for Google Calendar, Google Drive,
   Gmail, or GitHub when it is connected to the required account and supports
   the operation.
3. If a connector is disconnected, scoped to the wrong Google account, or
   cannot reach the requested resource, use the already signed-in browser
   session documented in `AGENTS.private.md`. Do not inspect cookies, local
   storage, passwords, tokens, or browser credential stores.
4. When the user identifies the in-app Browser or an existing tab, claim the
   exact open tab instead of opening a duplicate. Confirm the visible account
   badge before reading or acting. Gmail paths such as `/u/0` and `/u/1` are
   session positions, not reliable account identities.
5. Treat the RIT Google Calendar as the consolidated planning calendar. An
   official invitation may remain on another institutional calendar; when a
   reminder copy is needed, create a private RIT event that names the official
   source and does not invite external attendees again.
   Apple Calendar should display the RIT Google calendar directly. Do not copy
   events into iCloud as a synchronization workaround. Keep only one enabled
   display source for each Google calendar, refresh after changes, and verify
   macOS Calendar notifications are enabled before claiming reminders will
   appear on the Mac. Other Apple devices require separate verification.
6. Keep account numbers, balances, medical details, identity documents,
   credentials, private message bodies, and family information out of public
   Git. Record only public-safe status, deadline, conflict, source class, and
   next action. Family-account access is request-specific and must not create a
   recurring watch unless the user explicitly asks for one.
7. After browser work, close intermediate, duplicate, login, download, and
   stale portal tabs. Keep only a page the user must review or a live handoff
   that a later task must continue.

Account-specific addresses, browser profiles, mounted Drive paths, and the
verified routing table belong only in `AGENTS.private.md`. The public-safe
email queues remain under `APPLICATIONS/Jobs/`.

## REQUIRED: Meeting Preparation Kit And Calendar Block

Every externally scheduled meeting, interview, recruiter screen, advising
session, information session, medical or administrative appointment, and
registered event must have both of the following before it is treated as ready:

1. A public-safe preparation kit under `PREPARATION/` that identifies the
   purpose, evidence or materials, likely questions, questions to ask, and the
   required follow-up.
2. A separate RIT Google Calendar event titled `PREP: <event name>` with at
   least 30 minutes of protected preparation time. Use at least 45 minutes for
   interviews, advising meetings, and other high-stakes conversations.

The preparation block must finish before the event begins. Travel does not
count toward the minimum unless at least 30 minutes remain protected for actual
review before travel starts. When an event is rescheduled or canceled, move or
remove its preparation block and update the kit in the same pass. Preparation
blocks do not recursively require preparation blocks of their own.

If no conflict-free preparation time exists, flag the schedule as unresolved
instead of claiming the event is ready. Keep private medical, family, identity,
and account details out of Git; use a public-safe checklist and retain exact
details only in the private calendar or secure source.

## FORBIDDEN: DO NOT DELETE GIT REPOSITORIES

Every agent must read and follow [`REPOSITORY_SAFETY.md`](./REPOSITORY_SAFETY.md).
Deleting a local clone, remote repository, `.git` directory, Git history,
worktree, branch, tag, or remote is forbidden. Do not re-clone over a repository
or use destructive cleanup commands against a repository.

If a repository appears duplicated, stale, damaged, disconnected, or misplaced,
preserve it, document its absolute path and Git state, and propose a
non-destructive repair. No cleanup request authorizes repository deletion unless
the user explicitly revokes the safety policy and identifies the exact
repository and operation.

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

- Never delete a Git repository or its `.git` metadata. The full mandatory
  policy is in `REPOSITORY_SAFETY.md`.
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
