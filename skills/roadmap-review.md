---
name: roadmap-review
description: Review one client's ScalePad goals, initiatives, tasks, assessments, dependencies, and prior roadmap commitments for a QBR. Use to recommend a coherent rolling plan without creating duplicate records. Read-only.
---

# Roadmap Review

Assess whether the client's roadmap connects business outcomes to a small, credible set of initiatives and owned follow-through.

## Resolve scope

Resolve one exact client, review period, and planning horizon. The planning horizon is normally the next 12 months; the review period is the interval whose progress is being assessed. Use verified IDs and never fuzzy-match records for proposed reuse.

## Discover and read

Use currently advertised ScalePad tools. Prefer direct reads for goals, initiatives, the client plan, insights, tasks, meetings, assessments, deliverables, and users. Use detail reads for specific IDs when available. Use `search_operations` plus `execute_read` only after discovering the live contract. Never call `execute_write`.

Read the previous QBR or roadmap deliverable when available, then the current native records. This preserves continuity and exposes carry-forward work.

## Evaluate the plan

### Goals

Aim for one to three active, prioritized client outcomes, not an arbitrary quota. A useful goal is client-linked, expressed in business language, meaningful within the planning horizon, measurable enough to know whether it improved, and owned by a stakeholder when known.

Flag goals that are duplicates, internal MSP activities, vague themes, unmeasurable aspirations, stale, or disconnected from current evidence.

### Initiatives

Use three to five strategic initiatives across the rolling 12-month roadmap as a planning heuristic, not a hard limit. Usually only one to three should be active or decision-ready in the current quarter.

Every initiative should support a business goal, name the expected outcome, have a credible quarter or sequence, expose dependencies, and distinguish proposed from approved. Carry unfinished work forward when it is still valid instead of recreating it.

### Tasks

Create no task quota. A task is warranted only for a discrete committed action with a clear owner, due date when known, sufficient context, and links to its initiative or meeting. Recommendations awaiting a client decision are not yet commitments.

### Evidence and sequencing

Map assessments, service patterns, security risks, asset lifecycle, agreements, budget, and prior decisions to the goals they support. Identify blockers, conflicting schedules, orphaned tasks, initiatives without outcomes, and decisions that must precede execution.

## Reconcile before proposing

Match by approved record ID or a unique same-client record. Treat ambiguous matches as unresolved. Recommend reusing or updating an existing record when it represents the same work, preserving fields outside the proposed change.

Separate:

- evidence of progress;
- an inference about priority;
- a recommendation;
- a client or user decision;
- an approved commitment.

## Return the evidence slice

### Coverage

Sources, date ranges, record counts, and missing or failed reads.

### Findings

Progress, stalled work, duplication, gaps, dependencies, and business implications with confidence and evidence IDs.

### Existing records

Goals, initiatives, tasks, assessments, meetings, and deliverables that should be reused or referenced.

### Decisions

The smallest set of roadmap choices needed now, with a recommendation and trade-off for each.

### Proposed changes

Exact creates, updates, links, or no-change recommendations for `/qbr-prep`; do not write them.

### Unresolved inputs

Material owners, schedules, statuses, budget choices, or client intent that cannot be inferred safely.
