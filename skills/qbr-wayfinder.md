---
name: qbr-wayfinder
description: Map the shortest evidence and decision path for a complex or ambiguous QBR. Use when the account story is unclear, several review branches compete, or qbr-prep would otherwise become an unfocused data trawl. Read-only.
---

# QBR Wayfinder

Turn a foggy QBR request into a small navigable map. Find the next useful frontier instead of loading every possible record.

## Resolve the destination

State the intended outcome in one sentence, such as:

- prepare an executive QBR for one client and period;
- decide the next-quarter roadmap;
- explain a service or security concern;
- capture an approved plan in ScalePad.

Resolve one exact ScalePad client and the relevant review period. Use a verified client ID or a unique exact lookup; never blend similarly named clients. Ask one concise question only if the destination, client, or period cannot be inferred safely.

## Build the QBR map

Maintain this compact working map:

### Destination

The outcome, audience, review period, and planning horizon.

### Decisions so far

Confirmed choices and constraints, each with its source or the user who decided it.

### Evidence map

What is known in each material lane: client context, roadmap, service, security, technology, commercial, and prior QBR commitments. Use stable record IDs or links instead of copied payloads.

### Frontier

Questions that are specific, material, and currently answerable. Order them by how many downstream choices they unlock.

### Fog

Areas that may matter but are not yet specific enough to investigate. Do not turn fog into invented requirements.

### Out of scope

Explicit exclusions that prevent the review from expanding indefinitely.

## Advance one frontier at a time

Facts are the agent's job. Use currently available read tools or load the smallest relevant specialist before asking the user factual questions.

When `load_skill` is available, inspect the skills available on this turn and use the live contract. Use `/connected-systems-review` when source availability or external client mapping is part of the fog. Typical domain branches are `/client-context-review`, `/roadmap-review`, `/service-review`, `/security-review`, `/technology-review`, and `/commercial-review`. Pass the exact client, periods, and stable evidence pointers. If a branch is unavailable, note its coverage gap and continue with supported evidence.

Never reload a completed branch unless new evidence materially changes its scope. A handoff back from `/qbr-prep` or `/qbr-grill` updates this map; it does not restart the route.

Judgment calls are the user's job. When a material decision remains after fact-finding, load `/qbr-grill` if available and pass the decision, viable options, recommendation, evidence, and downstream dependencies. Otherwise ask the single highest-leverage question directly.

After each branch:

1. Add new evidence and confidence.
2. Record decisions or contradictions.
3. Promote newly answerable questions from fog to frontier.
4. Remove questions that no longer affect the destination.
5. Choose the next smallest investigation.

Do not run all branches by default. Stop when additional evidence is unlikely to change the QBR narrative, decisions, or proposed records.

## Handoff

When the map is sufficiently clear, load `/qbr-prep` if available with:

- exact client and period;
- destination and audience;
- decisions so far;
- evidence pointers and specialist findings;
- remaining coverage gaps;
- explicit out-of-scope items.

The handoff is read-only. If `/qbr-prep` is unavailable, return the same map as a ready-to-use preparation brief.

## Completion condition

Finish when there is a credible path to the requested outcome, no material ambiguity blocks the next stage, and every remaining gap is either disclosed, intentionally deferred, or assigned to a specific frontier.
