---
name: client-context-review
description: Review one client's documentation, stakeholders, prior meetings, decisions, agreements, and linked Lexful context for QBR preparation. Use to establish business context and continuity before roadmap or executive synthesis. Read-only.
---

# Client Context Review

Build a compact, evidence-backed view of who the client is, what matters to them, and what has already been promised or decided.

## Scope and identity

Resolve one exact ScalePad client and review period. Prefer a verified client ID or a unique exact result from the advertised client query tool. Never combine records from similar names.

If a linked Lexful organization is relevant, resolve it by an approved stable ID or verified exact linkage. Keep tenant boundaries intact and disclose when the linkage cannot be confirmed.

## Discover the live read surface

Use tools advertised on this turn. Prefer direct ScalePad reads for clients, contacts, users, meetings, notes, agreements, goals, initiatives, tasks, and deliverables. Use `search_operations` plus `execute_read` only for a relevant uncommon read whose live contract has been discovered. Never call `execute_write`.

For Lexful, use only available organization-scoped knowledge or document reads. Do not broaden a client review into workspace-wide discovery.

## Review progressively

Start with identifiers and the newest high-value context rather than reading everything:

1. Client profile, tier, lifecycle stage, primary contacts, and decision makers.
2. Previous QBR or executive deliverable and its recorded decisions.
3. Recent meeting notes, account plans, strategy documents, and open commitments.
4. Agreements or scope boundaries that materially constrain the plan.
5. Linked documentation needed to explain current goals or risks.

Prefer authoritative, current records. When sources disagree, retain both, identify their dates and owners, and do not silently choose one.

## Extract what matters

Look for:

- business priorities, growth plans, constraints, and risk appetite;
- stakeholders, decision rights, preferred communication, and ownership gaps;
- prior promises, approvals, deferrals, accepted risks, and unresolved asks;
- service boundaries, renewal timing, or dependencies that shape recommendations;
- changes since the last review that should alter the narrative or roadmap;
- missing or stale context that could make a recommendation unsafe.

Treat meeting notes and informal documents as evidence, not automatic truth. Separate direct observations, reasonable inferences, recommendations, and unknowns.

## Return the evidence slice

Produce:

### Coverage

Sources checked, date range, linked systems, unavailable sources, and freshness concerns.

### Findings

For each material finding: observation, business implication, confidence, and evidence IDs or links.

### Existing records

Relevant client, contact, meeting, agreement, goal, initiative, task, and deliverable IDs.

### Decisions

Confirmed decisions and unresolved choices, with owners where known.

### Proposed changes

Potential corrections or follow-through for `/qbr-prep`; do not mutate anything.

### Unresolved inputs

Only material gaps that cannot be answered by available tools.

Keep the result concise and pass stable pointers instead of copied documents.
