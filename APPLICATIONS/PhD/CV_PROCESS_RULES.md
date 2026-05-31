# CV Process Rules — PhD Application Packets

> **This IS the process.** Whenever a new PhD application CV is created or an existing one is updated, follow every rule in this document. Do not improvise — check here first.

---

## 1. Format B — Standard CV Structure

All PhD application CVs use **Format B**. The section order is:

1. `\section{Research Profile}` — 1–2 paragraph narrative (no Research Summary, no Abstract)
2. `\section{Research Interests}` — keyword-style list, position-specific framing
3. `\section{Education}` — degree entries in reverse chronological order
4. `\section{Research and Professional Experience}` — ALL experience in one section (no separate Teaching, no separate Professional Experience)
5. `\section{Selected Technical Writing}` — canonical order (see Section 3)
6. `\section{Awards \& Recognition}` — standard 4 entries (see Section 5)
7. `\section{Technical Competencies}` — not "Technical Skills"
8. `\section{Selected Fit for [Position]}` — always last before `\end{document}`

**Banned section names** (never use these):
- `Research Summary` → use `Research Profile`
- `Research Experience & Projects` → use `Research and Professional Experience`
- `Current Research Experience & Projects` → same
- `Selected Publications & Academic Contributions` → use `Selected Technical Writing`
- `Technical Skills` → use `Technical Competencies`
- Standalone `Teaching & Mentoring Experience` → fold into `Research and Professional Experience`
- Standalone `Professional Experience` → fold into `Research and Professional Experience`

---

## 2. UofR Teaching/Research Entry — Canonical Framing

UofR **always appears in the Research and Professional Experience section** as a dual teaching+research entry. It must **never** be the only entry in a separate "Teaching & Mentoring" section, and must never be omitted from the experience section.

```latex
\entry{University of Rochester, Warner School of Education}{Sep 2024 -- Present}{CS Teacher Candidate \& Education Research (NSF Noyce Scholar)}{Rochester, NY}
\begin{itemize}
  \item Deliver K--12 computer science instruction in active public school placement as part of the NSF Robert Noyce Scholar program, including computational thinking, inclusive pedagogy, and NYS learning standards.
  \item Conduct applied education research on AI-informed and data-driven approaches to improve learning outcomes for neurodivergent students, applying Universal Design for Learning (UDL) and evidence-based adaptive strategies.
  \item Produce lesson artifacts and instructional analyses documenting the intersection of AI, inclusive education, and evidence-based CS pedagogy.
\end{itemize}
```

**Rule**: Position this entry immediately after the RIT Graduate Assistant entry, before computational biology research entries.

---

## 3. Selected Technical Writing — Canonical Order

**Order is locked. Do not reorder. Do not combine items.**

### Non-quantum CVs (6 items):
1. **BDMD** — *Big Data Medical Diagnosis: A Multi-Method Approach* (RIT M.S. Computer Science graduate research, 2015)
2. **PHRR** — *Predicting Hospital Readmission Rates: A Multi-Method ML Analysis* (DSCI-633 Project Report, 2025)
3. **BIO614** — *BIO614-FinalProjectProposal* (Overleaf manuscript, 2026)
4. **ISTE780** — *Equitable Bioinformatics: Enhancing Diagnostic Decision-Making through RNA and Biomarker Data* (ISTE-780 Project Report, 2025)
5. **BIOL550** — *Differential Gene Expression in Murine DRG Neurons Following Sciatic Nerve Injury: An NGS Reanalysis* (BIOL550 Computational Biology Project, 2026)
6. **DSCI601** — *Fairness-Aware Bandits for Clinical Decision Systems* (DSCI-601 Project Proposal, 2025)

### Quantum CVs (7 items — quantum manuscript at position 0):
0. **QuantumPathOptimization** — *Quantum Path Optimization with Fault-Tolerant Routing* (manuscript under review, 2025–2026)
1–6. Same canonical order as above

### Rules:
- **BDMD always first** (not buried in an Education section bullet)
- **BIOL550 is always a standalone entry** — never combined with BIO614 ("BIO614 and companion BIO550...")
- **DSCI601 always uses the clinical diagnostic framing** — "bandit learning with equity constraints applied to high-stakes clinical diagnostic decision-making, addressing demographic disparity in sequential clinical recommendation workflows"
- While the quantum paper is under anonymous double-blind review, do not use the ICNP 2026 venue draft title; use the generic title above

---

## 4. Canonical Writing Sample Descriptions

Exact LaTeX text for each item:

```latex
\item \textit{Big Data Medical Diagnosis: A Multi-Method Approach} (RIT M.S.\ Computer Science graduate research, 2015) --- ensemble and deep learning methods for clinical classification on high-dimensional biomedical data.

\item \textit{Predicting Hospital Readmission Rates: A Multi-Method ML Analysis} (DSCI-633 Project Report, 2025) --- ensemble and regularized regression methods for clinical risk stratification under distribution shift.

\item \textit{BIO614-FinalProjectProposal} (Overleaf manuscript, 2026) --- RNA secondary structure prediction with thermodynamic deep learning enhancements, reproducible benchmarking, and biological interpretation.

\item \textit{Equitable Bioinformatics: Enhancing Diagnostic Decision-Making through RNA and Biomarker Data} (ISTE-780 Project Report, 2025) --- fairness-aware ML for genomic diagnostic algorithms with SHAP-based bias detection and statistical significance testing.

\item \textit{Differential Gene Expression in Murine DRG Neurons Following Sciatic Nerve Injury: An NGS Reanalysis} (BIOL550 Computational Biology Project, 2026) --- reproducible bulk RNA-seq pipeline using DESeq2, QC validation, and pathway-level biological interpretation of nociceptor gene expression.

\item \textit{Fairness-Aware Bandits for Clinical Decision Systems} (DSCI-601 Project Proposal, 2025) --- bandit learning with equity constraints applied to high-stakes clinical diagnostic decision-making, addressing demographic disparity in sequential clinical recommendation workflows.
```

Quantum position 0 item:
```latex
\item \textit{Quantum Path Optimization with Fault-Tolerant Routing} --- manuscript-level analysis of quantum-classical hybrid ML for fault-tolerant routing under noise constraints (under review, 2025--2026).
```

---

## 5. Awards & Recognition — Standard 4 Entries

Every CV that uses Awards & Recognition includes these in this order:

```latex
\section{Awards \& Recognition}
\begin{itemize}
  \item NSF Robert Noyce Teacher Scholarship (2024--2026) --- full funding for M.S. in Teaching Computer Science K--12.
  \item MS International Scholarship (2012--2015) --- MESCYT \& RIT, awarded for academic excellence.
  \item Honorable Mention Technology Award (2012) --- NYS STEP/CSTEP, 2nd place capstone project.
  \item IEEE Alumni Member (2009--Present) --- Member No. 90613000.
\end{itemize}
```

---

## 6. GPA Values — Locked, Never Change

| Degree | Institution | GPA |
|---|---|---|
| B.S. Computer Engineering Technology | Farmingdale State College | **3.3** |
| M.S. Computer Science | RIT | **3.2** |
| M.S. Data Science | RIT | **3.9** |
| M.S. track Teaching CS K–12 | UofR Warner School | **4.0** |

---

## 7. Research Profile Guidance

The **Research Profile** section replaces the old short "Research Summary" paragraph. It should:
- Be 1–2 substantial paragraphs (not a bulleted list)
- Name the NSF Noyce Scholar affiliation in the first sentence
- Connect research background to the specific position being applied for
- End with a sentence about what draws the applicant to this lab/position
- Never include the ICNP 2026 venue draft title while under anonymous review

---

## 8. Research Interests Section

Add a `\section{Research Interests}` after Research Profile. Use a semicolon-separated inline keyword list (not `\begin{itemize}`). Tailor the keywords to the position's focus area.

---

## 9. CV Checklist Before Submission

Before submitting any CV, verify:
- [ ] All 4 GPA values are correct (3.3 / 3.2 / 3.9 / 4.0)
- [ ] UofR entry appears in Research and Professional Experience (not only in Teaching)
- [ ] Selected Technical Writing follows canonical order: BDMD → PHRR → BIO614 → ISTE780 → BIOL550 → DSCI601
- [ ] BIOL550 is a standalone entry (not combined with BIO614)
- [ ] DSCI601 uses clinical diagnostic framing
- [ ] No "Teaching & Mentoring Experience" section exists as a standalone (must be merged)
- [ ] No "Professional Experience" section exists as a standalone (must be merged)
- [ ] Section name is "Technical Competencies" not "Technical Skills"
- [ ] Section name is "Selected Technical Writing" not "Selected Publications..."
- [ ] PDF compiles without errors (`pdflatex -interaction=nonstopmode`)
- [ ] Packet-status file updated in `application-materials/`

---

## 10. Common Mistakes (Do Not Repeat)

These mistakes were found across submitted CVs in the 2025–2026 application cycle and corrected post-submission. Every future CV must be checked for these before submission.

| Mistake | Fix |
|---|---|
| UofR only in Teaching section, not Research/Experience | Add dual teaching+research entry to Research and Professional Experience |
| BIOL550 combined with BIO614 as one bullet | Separate into two standalone entries |
| DSCI601 framed as "quantum routing" or missing clinical context | Always use clinical diagnostic framing |
| BDMD missing from Selected Technical Writing (only in Education bullet) | Add as first item in Selected Technical Writing |
| Old writing order (DSCI601 first, IDAI700 included, combined BIO614+BIO550) | Replace with canonical order: BDMD→PHRR→BIO614→ISTE780→BIOL550→DSCI601 |
| Separate Professional Experience section | Merge into Research and Professional Experience |
| Section named "Technical Skills" | Rename to "Technical Competencies" |
| Section named "Selected Publications & Academic Contributions" | Rename to "Selected Technical Writing" |
| Short "Research Summary" paragraph | Expand to "Research Profile" narrative |
