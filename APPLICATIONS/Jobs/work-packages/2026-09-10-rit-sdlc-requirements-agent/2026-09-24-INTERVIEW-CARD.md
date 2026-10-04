# SDLC requirements-agent interview — quick card

**Meeting:** Thursday, September 24, 2026, 3:00–3:30 PM ET, in person at GCI-3700, RIT. Dr. Nidhi Rastogi said she wants to understand my background and assess fit. The industry partner, scope, compensation, hours, work mode, and deliverables are still to be confirmed. [Meeting email](https://mail.google.com/mail/u/0/#all/1a0cc3746764e07f) · [Opportunity record](README.md)

## 🟦 Start — 30 seconds

> It is great to reconnect—you were my first data science instructor. My work now combines data science, software development, and teaching. I focus on understanding a process, organizing its information, and building small improvements we can test. This project interests me because collecting requirements means asking the right questions and turning incomplete information into something stakeholders can verify and developers can use.

## 🟩 Evidence — two examples

**MLADIS.** The [reservation service contract](https://github.com/pzg8794/MLADIS/blob/248a52ce75a7972b9a87bed17185f195b6308b10/docs/architecture/reservations/instructions/api-service-contract.md) documents structured requests, missing-information detection, suggested replies, recommended actions, lifecycle events, and human approval before sending messages. I can explain how that design relates to requirements elicitation: establish what is known, identify gaps, ask a focused follow-up, and preserve the decision trail. **Claim boundary:** this document proves the design contract; do not describe every element as deployed without checking implementation.

**SaNDAI prototype.** The [case-challenge repository](https://github.com/pzg8794/sandai-seminar-operations-demo) shows how I translated an eight-week attendance objective into a strategy, management view, reusable Python calculations, requirement traceability, and a student-facing activity. The [website](https://sandai-seminar-demo-qkpntto5ya-uc.a.run.app/) makes it reviewable. The campaign data are sample data, not live recruitment.

## 🟨 Approach — if asked how I would start

> First I would understand the partner's current requirements process and examine examples of complete and incomplete requirements. Then I would prototype one narrow workflow: capture a request, identify missing details, ask follow-up questions, and produce a source-linked draft for stakeholder approval. I would compare it with the existing process before expanding.

**Remember:** Understand → Extract → Clarify → Validate → Measure.

**Example:** “We need faster reports” is incomplete. Ask which reports, who uses them, the current delay, and an acceptable response time. Then write a requirement that can be tested.

## 🟪 Short answers

**How would you limit unsupported output?** Link each requirement to its source, label assumptions, leave unknown fields open, and obtain stakeholder approval.

**How would you measure value?** Compare against the existing process: missed or unsupported requirements, useful clarification questions, stakeholder corrections, and time to an approved requirement.

**Would you use multiple agents?** Start with the simplest reliable workflow. Split responsibilities only if separate agents improve quality or control.

## 🟧 Ask Nidhi

1. Where does requirements collection currently break down for the partner?
2. What are the inputs and expected outputs—interviews, documents, user stories, acceptance criteria, or something else?
3. What would a successful first month look like? What are the weekly hours, work mode, and appointment structure for Fall and Spring?

## 🟥 If I lose my place

> Let me give you one concrete example.

Return to **MLADIS → missing information → clarification → human approval**.

**Closing line:** I structure the problem, build a testable workflow, and check whether it actually helps.

## Source boundary

- The time and room come from the RIT Calendar event and the RIT email thread linked above.
- Nidhi's original opportunity is a paid industry-partner project designing agents for requirements collection during the SDLC; this does not establish its scope or appointment terms. See the [opportunity record](README.md).
- MLADIS and SaNDAI links above support the project descriptions. The proposed agent workflow and sample answer are interview talking points, not claims that the industry project already uses them.
