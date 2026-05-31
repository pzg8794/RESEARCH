# Overleaf Canonical Status

Updated: 2026-05-30

This file records the canonical Overleaf project IDs to use when multiple closely related course projects exist. It exists so packet preparation can rely on stable project names instead of informal memory.

## Canonical records

| Artifact lane | Canonical project | Related project(s) | Evidence | Packet rule |
| --- | --- | --- | --- | --- |
| ISTE780 project paper | `ISTE780-Project_Phase4` -> `https://www.overleaf.com/project/687b2ee4bacc2838e411460b` | `ISTE780-Project_Phase3` -> `https://www.overleaf.com/project/687a7fa9cc5c2aa5f7e0ea47` | Live Overleaf project-list search on 2026-05-30 showed that the alternate link is Phase 3, not another Phase 4. Repo-side derivatives and packet-status files already use the Phase 4 artifact. | Use Phase 4 for all future packet derivatives. Treat Phase 3 as earlier-stage provenance only. |
| IDAI700 portfolio lane | `IDAI700-Research_Portfolio` -> `https://www.overleaf.com/project/6912b8af5f8d972c24f1a3af` | `IDAI700-Research_Paper` -> `https://www.overleaf.com/project/693fcd2283c8d0afc36697e1`; application copy -> `https://www.overleaf.com/project/6a1a8f65770fe8ccfa3ccdee` | Live Overleaf project-list search on 2026-05-30 showed these are distinct titled projects, not duplicate links. Follow-up editor review showed that the research-paper project is the cleaner single-paper packet source, while the portfolio remains the broader narrative bundle. A non-destructive application copy was created on 2026-05-30. | Use `IDAI700-Research_Paper` as the first single-paper responsible-AI sample. Reuse the application copy when a packet-specific edit path is needed. Use `IDAI700-Research_Portfolio` when broader narrative or lived-authority framing is the better fit. |
| DSCI644 phase artifact | `DSCI644-GP-Phase4` -> `https://www.overleaf.com/project/6806e71cd7edd322e0877d31` | `DSCI644-G2-Phase4` -> `https://www.overleaf.com/project/6802fb993030e298f6132ea9`, `DSCI644-Group2-Phase2` -> `https://www.overleaf.com/project/67c5430984aab4778d5519a2`, `DSCI644-Group2-Phase1` -> `https://www.overleaf.com/project/67ad23bdc469f055a6d50e06` | Live Overleaf project-list search on 2026-05-30 captured the exact title for the previously unnamed DSCI644 link. | Keep `DSCI644-GP-Phase4` as the tracked DSCI644 backup sample, but verify authorship and application fit before upload. |
| DSCI633 pipeline | No Overleaf project currently tracked | Drive folder: `https://drive.google.com/drive/u/0/folders/1Z-zMFLS6uAfOCkpysGW8vuaQiezAhG14`; staged repo-side derivative: `application-materials/2026-05-30-dsci633-predicting-hospital-readmission-rates-writing-sample.pdf` | Live Overleaf project-list search on 2026-05-30 returned no `DSCI633` projects. A repo-side application copy was staged on 2026-05-30 from the confirmed V2 report PDF. | Use the staged repo-side derivative when a direct course-report sample is acceptable. A manuscript-style cleanup remains optional follow-up work rather than a gating requirement. |

## What to update after a change

1. Update `OVERLEAF_PAPER_INDEX.md` if canonical project choice or readiness changes.
2. Update `OVERLEAF_DISCOVERY_PLAYBOOK.md` if search terms or visible titles change.
3. Update `MASTER_RESEARCH_INDEX.md` if artifact status changes.
4. Update the relevant `application-materials/` packet-status file if a new derivative is uploaded.
