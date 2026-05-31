# ProFellow Search Routine

Updated: 2026-05-27

This note defines the repeatable workflow for turning ProFellow discovery into a usable application queue.

## Goal

Use ProFellow for three things only:

1. find live open calls,
2. surface fully funded doctoral programs and external fellowships,
3. bookmark plausible items before they are either promoted or discarded.

Do not treat ProFellow as the final authority on deadlines, eligibility, or required materials.

## Weekly cadence

Run this search pass at least once per week while active application season is open.

### 1. Check open calls first

- Open the ProFellow open-calls page.
- Capture any live calls that directly match the current strategy.
- Add every relevant call to the queue the same day.
- If a call is already in progress, update its queue status instead of adding a duplicate line.

### 2. Run productive keyword searches

The 2026-05-27 pass showed that ProFellow responds better to discipline-aligned terms than to generic buzzwords.

### Productive search terms from this pass

| Query | Observed ProFellow result count | Use |
| --- | --- | --- |
| `machine learning` | 26 | Best search for doctoral ML opportunities and doctoral fellowships. |
| `bioinformatics` | 24 | Best search for diagnostics-adjacent PhD programs. |
| `computer` | 120 | Useful for wider CS doctoral long-list expansion. |
| `phd` | 200 | Broad doctoral sweep when widening the queue. |
| `doctoral` | 200 | Same use as `phd`; helpful for fellowship-type listings too. |
| `biology` | 83 | Useful when widening computational biology and systems-biology options. |
| `health` | 200 | Broad health-oriented sweep; requires aggressive filtering. |
| `innovation` | 88 | Useful for impact- or venture-oriented fellowships like Mira. |
| `research` | 200 | Broad sweep only; use when deliberately widening the long list. |

### Weak or noisy queries from this pass

| Query | Observed behavior | Guidance |
| --- | --- | --- |
| `ai` | 0 results | Use `machine learning` instead. |
| `data science` | weak / unreliable | Use `computer`, `phd`, or program-specific terms instead. |
| `biomedical informatics` | weak / unreliable | Use `bioinformatics` first, then verify on official pages. |
| `quantum` | 5 | Low-yield on ProFellow; rely more on direct university vacancy pages for quantum PhD searches. |

### 3. Apply a quick triage rule

Promote an item into the working queue only if at least one of these is true:

- It is a live fellowship or open call with a realistic deadline window.
- It is a fully funded PhD directly aligned with machine learning, diagnostics, bioinformatics, biomedical informatics, computational biology, or adjacent CS.
- It is an external doctoral fellowship that could materially fund the final PhD shortlist.

Screen it out if any of these are true:

- It is internship-only and does not support the research / PhD trajectory.
- It is too far outside the active research narrative.
- It duplicates a better official-source tracker already in use.

### 4. Bookmark before closing the tab

- If it survives triage, bookmark it in ProFellow immediately.
- Then add it to the queue with a status such as `Bookmarked` or `Needs official verification`.
- If ProFellow exposes the item only as an article or open-call post and not as a bookmarkable database record, document it manually in the queue.

### 5. Verify externally before promotion

Only move an item into the main PhD roadmap after checking the official page for:

- deadline,
- eligibility,
- funding model,
- required materials,
- and whether the program is genuinely active for the target cycle.

## Queue workflow

Use this status progression whenever possible:

`Found` -> `Bookmarked` -> `Needs official verification` -> `Verified` -> `Packet staged` -> `Applied` or `Paused` or `Screened out`

## Current high-value ProFellow patterns

- ProFellow is currently most useful here for machine learning and bioinformatics doctoral discovery.
- Quantum-specific doctoral searching is still better handled through direct university vacancy pages, especially European institutions.
- Open calls are sparse, so the open-calls page should be checked quickly but should not be the only discovery step.
- The ProFellow fully funded graduate-program articles are useful as long-list sources, but they still need official-page confirmation before any calendar commitment.

## Documentation rule

Every meaningful ProFellow scan should leave behind one or both of the following:

- an updated queue entry in [profellow-opportunity-queue-2026-05-27.md](./profellow-opportunity-queue-2026-05-27.md),
- or a new dated queue file if the next scan materially changes the shortlist.

If the search changes the overall workflow, update this file in the same pass.