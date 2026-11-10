---
name: qbr-apply
description: Apply a reviewed QBR plan to native ScalePad records for one exact client and period. Use after qbr-prep or when the user supplies a reviewed plan. Requires a write preview and explicit approval; excludes invitations, publishing, sharing, PSA tickets, archival, and deletion.
---

# QBR Apply

Apply a reviewed QBR plan to native ScalePad records. The input may be a `/qbr-prep` handoff or a user-provided plan. Treat the plan as approved intent, not approval to write.

## Establish the target

Resolve exactly one ScalePad client and one QBR period. Carry the resolved client UUID through every read and write.

Prefer, in order:

1. A client UUID explicitly accepted in the handoff.
2. The current ScalePad page's client UUID.
3. A unique exact result from the advertised client query tool.

Validate that every supplied record ID belongs to that client. Never use fuzzy name matching for a write. If the client, period, or intended mutations remain ambiguous, ask one concise question.

The QBR period provides context only. Do not derive task due dates, meeting dates, initiative schedules, financial values, owners, or statuses from it unless the reviewed plan explicitly specifies them.

Check a linked Lexful organization read-only when the handoff includes its ID, the user requests cross-system validation, or a proposed action depends on that linkage. A missing unrelated Lexful connection does not block ScalePad work.

## Discover the live MCP contract

Use the tools and schemas advertised for this user on this turn. Do not assume a remembered tool or operation is available.

For common reads, prefer these direct tools when advertised:

- `scalepad_query_clients`
- `scalepad_query_goals`
- `scalepad_query_initiatives`
- `scalepad_query_tasks`
- `scalepad_query_meetings`
- `scalepad_query_deliverables`
- `scalepad_query_users`

Use the client query tool's `get_client_summary` operation only when broad context is still needed. Select only the required sections; omitting `sections` loads every section. A reviewed handoff normally needs targeted duplicate and state checks instead of another broad review.

Use `search_operations` for writes and uncommon reads. Search using action-and-resource terms or exact operation names. Comma-separate known exact names to load several contracts together. The search returns at most five matches; follow `next_offset` only when required.

Preserve each returned `operation_id`, `execution_tool`, `parameters`, and `prerequisite_tools`. Example identifiers are placeholders. Never guess an operation or field.

When both a native operation and an `api.*` operation perform the work, prefer the native operation. Native operations add ScalePad-specific validation, batching, partial-update behavior, rich-text handling, and result hydration. Use `api.*` only when no native operation supports the approved action or field.

For `execute_read` and `execute_write`, encode the discovered argument object as the `arguments_json` string required by the live schema. Supply no undiscovered fields. `execute_write` is the commit point, not a dry run or confirmation screen.

Independent reads may run together. Keep dependent writes sequential.

## Check the plan's shape

Use these as review heuristics, not quotas. Do not manufacture records to meet a number or silently rewrite an approved exception.

### Goals

Prefer one to three active, prioritized client goals for a planning period. A goal should:

- Belong to the exact client.
- Describe a business outcome, measurable risk reduction, or obligation.
- Have a target period and one to three observable outcomes when known.
- Identify the accountable client stakeholder when supported and known.
- Be advanced by at least one initiative.

Technical work such as deploying a firewall is normally an initiative. The goal is the client result it enables, such as reducing material insurance exceptions before renewal.

### Initiatives

Use a rolling 12-month roadmap as the normal horizon. Three to five meaningful initiatives across that horizon is a useful default; one to three active or decision-ready initiatives in the current quarter is a useful review signal.

An initiative should represent a meaningful change requiring sequencing, investment, or a client decision. It should have a business justification, target timing, allowed priority and status values, and either a linked goal or an explicit risk, compliance, lifecycle, or contractual reason.

Carry valid unfinished initiatives forward. Routine service work, tickets, tiny recommendations, and product-led ideas without client justification do not become roadmap initiatives.

### Tasks

There is no target task count. Create one task per committed next action only when it has:

- A clear verb-led title.
- One accountable owner.
- A due date.
- Enough context to complete it.
- A link to the relevant goal, initiative, or meeting when supported.

Recommendations awaiting a client decision remain decision items. Do not turn every QBR bullet into a task or use tasks as a second project plan. If the client owns an action but only internal ScalePad users can be assigned, assign the MSP owner responsible for follow-through and identify the client owner in the description.

### Meetings

Reuse an existing scheduled QBR meeting. A meeting record should contain a purposeful title, confirmed local date and timezone, concise agenda, verified attendees, and only the links actually discussed. Do not create a duplicate meeting merely to hold links.

### Deliverables

Create one curated draft deliverable for the review, preferably from the client's approved QBR template. Its narrative should cover:

1. Where the client wanted to go.
2. What changed during the period.
3. What value or risk movement resulted.
4. Where the client stands now.
5. What decisions and actions come next.

A useful default shape is executive overview, goals and progress, material value delivered, important risks, roadmap, proposed versus committed budget, two or three decision items, and named next actions. Assessments, analytics, contracts, assets, and third-party data are supporting evidence, not mandatory sections.

Keep the deliverable unpublished. Do not add a separate Executive Summary section when the live operation supports updating the existing Overview section.

Surface methodology concerns in the preview: excessive record counts, technical goals, unsupported initiatives, missing owners or dates, premature tasks, reusable records, and data-dump deliverables.

## Reconcile current records

Query only the resolved client. Narrow list reads using exact type, title or name, period, schedule, and status where supported. Fetch details only for credible candidates; goal and initiative detail operations can inspect up to ten IDs together when advertised.

A record is reusable only when:

- Its approved record ID matches; or
- It is the sole same-client record of that type with the exact title or name and a compatible period or schedule.

Show multiple candidates for review. If no candidate qualifies, propose a create. Never create a duplicate because an existing candidate is uncertain.

Preserve fields outside the approved change. Before a raw `PUT`, read the current record and provide the complete representation required by the contract. Never replace unknown fields with invented values, empty strings, zero, false, or null.

Fetch allowed statuses, priorities, assignees, meeting types, schedules, currencies, and other enumerated values when unresolved. Do not convert display labels into guessed enum values.

## Preview and approve

Preview one bounded write batch containing:

- Exact client UUID and display name.
- QBR period and timezone.
- Creates, updates, reuses, and links.
- Existing record IDs and returned `web_url` values when available.
- Every changed field as current → proposed.
- Dependency order and discovered write operation IDs.
- Methodology warnings.
- Missing inputs, unsupported actions, and manual work.

Do not synthesize URLs when `web_url` is absent; report the record ID.

Keep proposed financial estimates separate from commitments. Write a financial field only when the exact amount, currency, cadence, and destination field were explicitly approved.

Wait for explicit approval of this batch. Approval of `/qbr-prep` is not write approval. A material change to the client, records, fields, values, dependencies, or operations requires a new preview.

## Apply the approved batch

Apply dependencies in the order established by the plan. Usually:

1. Create or update goals and initiatives.
2. Read back and capture their IDs.
3. Create or update dependent tasks and meetings.
4. Apply relationship links.
5. Create or update the unpublished draft deliverable.

Batch records only when the discovered native schema explicitly supports a collection. Use returned IDs for dependent writes rather than names.

For meetings, require confirmed local date-time, timezone, meeting type when required, and real attendee IDs or emails. Do not call an operation that sends invitations or notifications.

For deliverables, prefer the native create or update operation. Never publish, share, schedule, or send a deliverable.

Do not call operations that send invitations or notifications, publish or share content, create PSA tickets, send reports or test messages, archive, restore, or delete records. When a required write is unavailable, produce a ready-to-enter manual draft and name the missing operation instead of substituting an unrelated tool.

## Verify and report

Read back every created or updated record and verify its client, changed fields, and relationships.

For an uncertain create result, query the target before retrying. Never blindly retry a create. A composite operation may partially succeed; preserve and report a created record even if a later summary, attendee, or link step fails.

After a failed prerequisite, stop dependent writes. Do not delete successful records as an automatic rollback.

Report each item as:

- Created
- Updated
- Already present
- Failed
- Not attempted because a dependency failed
- Uncertain and reconciled
- Manual action required

Include record IDs, returned links, verification results, failures, and remaining manual steps.
