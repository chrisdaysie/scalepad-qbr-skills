---
name: qbr-follow-up
description: Convert a completed QBR's meeting record, notes, or transcript into a verified decision log, owned follow-up, and read-only handoff for qbr-apply. Use after the meeting; never writes or sends by itself.
---

# QBR Follow-up

Capture what the meeting actually decided and turn it into a clean proposed record set. Do not reinterpret the pre-meeting recommendation as the outcome.

## Resolve the meeting

Resolve one exact client, QBR meeting, date, and timezone. Prefer an approved meeting ID or a unique same-client record. Verify that every note, transcript, attachment, and linked record belongs to that client.

Use the tools advertised on this turn. Prefer direct reads for meetings, notes, deliverables, goals, initiatives, tasks, users, and client records. Use `search_operations` plus `execute_read` only for an uncommon read after discovering its live contract. Never call `execute_write` in this skill.

## Reconcile the outcome

Compare the meeting evidence with the pre-meeting plan and capture:

- decisions approved, rejected, deferred, or left open;
- decision maker, rationale, alternatives, and review date when stated;
- accepted risks and residual exposure;
- changes to goal or initiative priority, scope, status, or timing;
- committed actions, owner, due date, and parent record;
- promises to send information or produce a deliverable;
- contradictions between notes, transcript, and existing records.

Do not infer agreement from silence, attendance, or a recommendation appearing in the deck. Do not invent owners or dates. When sources conflict, show the conflict for review.

## Shape proposed follow-through

Use these rules:

- Update or reuse an existing goal, initiative, or task when it represents the same work.
- Propose a new task only for a discrete commitment, not an undecided recommendation.
- Keep financial estimates separate from accepted purchases or budgets.
- Record deferrals with their reason and revisit point when known.
- Prefer prompt follow-up and short closure windows, but never fabricate a deadline from an operating heuristic.

Prepare a concise client follow-up draft if requested, but do not send, share, invite, or publish anything.

## Return the handoff

### Meeting evidence

Meeting ID, date, attendees when available, sources checked, and coverage gaps.

### Decision log

Decision, disposition, decision maker, rationale, alternatives, residual risk, review date, and evidence pointer.

### Confirmed actions

Action, owner, due date, parent record, dependency, and evidence.

### Record reconciliation

Existing IDs to reuse, exact proposed field changes, new records required, and ambiguous matches.

### Communication draft

Optional concise summary of decisions and next steps, clearly marked unsent.

### Unresolved inputs

Only choices or missing facts that block safe follow-through.

If the user explicitly asks to apply the reviewed outcome and `/qbr-apply` is available, load it through the live `load_skill` contract with this handoff. `/qbr-apply` must still preview the exact batch and receive explicit write approval. Otherwise stop with the read-only handoff.
