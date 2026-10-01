# IBM Dev Day: Bob in Action and Hackathon

## Confirmed event

- **Host:** IBM SkillsBuild
- **When:** Thursday, August 27, 2026, 11:00 AM-2:30 PM EDT
- **Format:** Virtual
- **Handshake:** https://rochester.joinhandshake.com/stu/events/1980103
- **Official event:** https://ibmdevday-bob.bemyapp.com/
- **Dev Day:** Thursday, August 27, 2026, 10:00 AM-2:30 PM EDT
  (hackathon enablement begins at 10:00 AM; main program begins at 11:00 AM)
- **Hackathon:** Friday-Sunday, August 28-30, 2026
- **Status:** Registered through Handshake on August 17 and directly through
  IBM/BeMyApp on August 18, 2026. Hackathon participation was selected; the
  completed registration returned to the authenticated event page.

## Why this fits

The event aligns with Piter's software-engineering, AI, data-workflow, and
responsible-evaluation background. It offers current exposure to an AI-assisted
development workflow without implying prior production experience with IBM Bob.

## Preparation checklist

1. Review IBM Bob's published event description and note the modernization,
   validation, and governance claims to test during the demonstration.
2. Prepare a small, non-sensitive repository or toy workflow if the hackathon
   requires hands-on participation.
3. Ask how the tool documents changes, evaluates correctness, handles privacy,
   and supports human review.
4. Record reusable lessons for research, teaching, and future applications.

## Competition direction: MLADIS inquiry-agent workflow

Build a sanitized, Bob-assisted developer workflow around the existing MLADIS
short-term-rental inquiry system. The competition submission should be about
how Bob helps developers safely build, test, validate, and maintain the agent,
not merely about presenting a rental chatbot.

### Demonstration workflow

1. Ingest a synthetic rental inquiry and extract dates, occupancy, preferences,
   and special requests.
2. Check sample availability and policy data, then prepare a response or quote
   for human review.
3. Track approval, booking, payment-authorization, and follow-up states.
4. Use Bob to trace requirements to implementation, generate and run tests,
   detect missing or contradictory transaction states, validate documentation,
   and prepare a reproducible release handoff.
5. Compare the workflow before and after Bob using elapsed time, manual steps,
   errors caught, and rework avoided.

### Guardrails

- Use only synthetic guest, property, booking, and payment data.
- Do not expose private MLADIS records, credentials, payment details, identity
  information, production logs, or browsing history.
- Preserve the existing repository and Git history; use a bounded hackathon
  branch or sanitized sample project.
- Verify the current payment implementation before describing it. Do not claim
  that separate stay and deposit holds are complete without working evidence.
