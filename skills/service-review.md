---
name: service-review
description: Review one ScalePad client's tickets, incidents, SLA evidence, recurring issues, and service-delivery trends for a QBR. Use to find business-impacting patterns and post-incident follow-through without treating ticket volume as client health. Read-only.
---

# Service Review

Turn service records into a concise view of business impact, recurring friction, and improvement opportunities. Do not make the QBR a ticket report.

## Resolve scope

Resolve one exact client and one review period. Use a verified ScalePad client ID or a unique exact match. When trend claims matter, select a comparable prior period and state its dates. Never merge data across clients.

## Discover the live read contract

Prefer advertised direct tools for tickets, clients, meetings, notes, tasks, goals, initiatives, deliverables, and users. Use `search_operations` plus `execute_read` only for an uncommon read after discovering its exact operation and fields. Never call `execute_write`.

When PSA-originated evidence could materially improve the review, use a completed `/psa-evidence` slice or load that available skill through the live `load_skill` contract with the exact ScalePad client and period. It should prefer native ScalePad tickets and agreements before requiring a direct PSA connector. Use `/rmm-evidence` only for relevant monitoring or endpoint telemetry. Do not duplicate source discovery already completed by `/connected-systems-review`.

Record filters, pagination, result limits, failed sources, and whether the ticket source is complete. A partial page is not a period total.

## Analyze service evidence

Look for material patterns rather than individual noise:

- repeated categories, symptoms, affected services, users, sites, or root causes;
- high-impact incidents, outages, escalations, or business disruption;
- long-running, reopened, bounced, or repeatedly reclassified work;
- recurring demand that signals a training, standards, lifecycle, capacity, or automation problem;
- measurable improvement after a remediation, project, or operating change;
- commitments from prior incident reviews that remain open;
- scope, intake, communication, or ownership breakdowns.

Use ticket logs, monitoring evidence, and communication records for incident timelines rather than memory. When a root cause is unknown, say so and identify the investigation plan; do not substitute the triggering symptom.

Do not infer user satisfaction, relationship health, technician quality, SLA compliance, or business impact from ticket count alone. Do not treat low volume as proof of health. SLA or response-time claims require the relevant source fields and comparable definitions.

## Translate activity into decisions

For each material pattern, state:

1. What happened and how often, with evidence IDs.
2. The client consequence or risk.
3. Whether the pattern is improving, stable, or worsening on comparable evidence.
4. The smallest sensible response.

Use this escalation test:

- **Goal:** the issue affects a client business outcome over the planning horizon.
- **Initiative:** resolving it needs coordinated work, investment, sequencing, or a client decision.
- **Task:** a discrete action is already committed, with an owner and due date when known.
- **Operational follow-through only:** normal service work that does not belong on the strategic roadmap.

Post-incident actions must be specific and owned. Generic actions such as “improve monitoring” are not ready for task creation.

## Return the evidence slice

### Coverage

Period, comparison period, sources, filters, completeness, and unavailable metrics.

### Findings

Observation, business implication, trend, confidence, and ticket or incident IDs for every material pattern.

### Existing records

Related goals, initiatives, tasks, meetings, deliverables, and prior incident actions.

### Decisions

Proposed client or MSP decisions, recommended option, trade-off, and owner when known.

### Proposed changes

Potential reuse, updates, creates, or links for `/qbr-prep`; do not execute them.

### Unresolved inputs

Only facts or choices that could materially change the conclusion and cannot be resolved from available records.
