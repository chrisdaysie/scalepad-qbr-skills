---
name: psa-evidence
description: Gather read-only PSA-originated evidence from ScalePad and, when needed, a connected PSA. Use to explain recurring service friction, delivered work, documented scope, and follow-through in service, roadmap, commercial, or QBR review.
---

# PSA Evidence

Collect trustworthy PSA-originated operational evidence, preferring native ScalePad objects before an optional direct PSA connection. Qualify the data and return stable source records; leave business interpretation to the consuming review skill.

## Why this evidence matters

PSA evidence connects day-to-day service with the client story. Tickets and incidents can expose recurring friction or improvement, agreements establish documented scope, and projects and commitments show delivered value and unfinished follow-through. Use those signals to decide whether an issue needs operational correction, a client decision, roadmap work, or commercial clarification—not to grade the relationship by ticket volume.

## Verify identity and scope

Require one exact ScalePad client UUID and review period. A PSA company or client ID is required only before querying a direct PSA connector; prefer a native integration mapping or approved external ID. Never query or combine companies by fuzzy name.

Confirm timezone and business-hours context before calculating response, resolution, or SLA claims. When a comparison period is requested, use explicit comparable dates.

## Prefer native ScalePad records

Use the live native contracts first:

- `scalepad_query_tickets` for client-scoped tickets and available owner, contact, contract, board, category, timeline, SLA, status, priority, impact, and severity evidence.
- `scalepad_query_agreements` for agreements, summaries, expiry state, and line items when exposed.
- `scalepad_query_initiatives` and `scalepad_query_tasks` for linked PSA tickets and QBR commitments when relevant.

Filter by the exact client UUID and period before paging. Use summaries or counts when they answer the question, and fetch individual records only for credible patterns or high-impact events. Preserve each record's source lineage and sync timestamp when returned.

Do not fail merely because no direct PSA connector is available. Report which requested fields are answered by ScalePad and which remain unavailable.

## Discover the remaining PSA contract

Only when ScalePad lacks material detail or freshness, inspect any connected PSA account, operations, fields, filters, enums, pagination, retention, and permissions available on this turn. Do not assume a specific PSA product or common field name.

Prefer indexed server-side filters for company ID, date range, status, type, project, or priority. Start with summaries and metadata; retrieve full ticket notes, descriptions, or communications only for targeted material records. Never expose credentials, secrets, unrelated personal data, or cross-client content.

Record query filters, pages retrieved, total-count semantics, failures, and fields absent from the live contract. A page of results is not a period total.

## Gather only relevant evidence

Depending on the request and live capabilities, inspect:

- tickets, incidents, problems, requests, escalations, and reopen history;
- priority, category, source, site, affected service, and root cause;
- response, resolution, waiting, and SLA timestamps with their calendars;
- major-incident timelines and post-incident actions;
- projects, milestones, blockers, scope, status, and completion evidence;
- agreements, covered services, renewal dates, and material scope boundaries;
- CSAT responses and sample size;
- linked contacts, assets, configuration items, or client commitments when relevant.

Do not retrieve every ticket body to discover patterns. Aggregate on reliable fields first, then inspect representative or high-impact records that could change the conclusion.

## Preserve meaning

Do not equate ticket volume with satisfaction, relationship health, technician performance, or value. Distinguish:

- opened, closed, merged, cancelled, and reopened tickets;
- first response from automated acknowledgement;
- resolution time from elapsed time and client-wait time;
- SLA target, measured result, exclusion, and breach;
- incident trigger, root cause, and unresolved investigation;
- project activity, completed outcome, and invoiced work;
- agreement scope from a proposal, estimate, or informal promise;
- CSAT trend from a small or biased sample.

Preserve provider-native statuses and definitions. Normalize labels only in the explanation, never by rewriting the source value.

## Return the evidence slice

### Coverage

ScalePad native coverage, optional PSA provider and account, verified external company ID when used, period, timezone, sources, filters, pagination, retention, permissions, sync freshness, and failed reads.

### Findings

Direct observations with source record IDs, timestamps, field definitions, confidence, and enough context for a downstream review.

### Existing records

Relevant ticket, incident, problem, project, agreement, CSAT, contact, and commitment IDs or links.

### Decisions

Questions suggested by the evidence; do not decide roadmap priority, client health, or commercial action inside this adapter.

### Proposed changes

Potential follow-through for the consuming review skill; do not create or update records.

### Unresolved inputs

Missing mappings, definitions, calendars, permissions, source fields, or ambiguous records.

This skill is read-only. Never create or modify tickets, projects, time entries, notes, contacts, agreements, workflows, or notifications.
