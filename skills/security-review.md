---
name: security-review
description: Review one client's ScalePad and available connected security evidence for a QBR, including assessments, controls, compliance, incidents, accepted risks, and remediation. Produces decision-ready findings without changing records. Read-only.
---

# Security Review

Translate security evidence into visible risk, measurable progress, and explicit client decisions. Avoid fear-based language, tool-centric reporting, and unsupported precision.

## Resolve scope and authority

Resolve one exact ScalePad client, review period, and planning horizon. Use verified IDs and preserve tenant boundaries.

When ControlMap or another connected security system is relevant, verify the exact client or organization linkage before reading its evidence. Do not join records by fuzzy client name. State which system is authoritative for each assessment, control, compliance status, incident, or risk.

## Discover the live read surface

Prefer advertised direct reads for assessments, insights, goals, initiatives, tasks, meetings, notes, deliverables, tickets, software, and client records. Use connected security tools only when available and client-scoped. Use `search_operations` plus `execute_read` for uncommon ScalePad reads only after discovering the exact contract. Never call `execute_write`.

When endpoint, Microsoft tenant, or SaaS governance posture is material, consume completed `/rmm-evidence`, `/m365-evidence`, or `/saas-evidence` slices. If needed and available, load the relevant adapter through the live `load_skill` contract using verified IDs and the narrow security question. Do not treat app approval, certification, or compliance-gap metadata as a risk or compliance conclusion until this review evaluates its business context.

Record source freshness, assessment version, template or framework, scoring scale, evidence date, pagination, and failed sources.

## Assess the evidence

Look for:

- changes in material risks, control coverage, compliance obligations, or maturity;
- remediation completed during the period and the business exposure it changed;
- top active risks, overdue gaps, expiring evidence, exceptions, and dependencies;
- incidents or near misses and the status of their specific follow-up actions;
- unmanaged SaaS or AI usage where ownership, approval, data handling, or policy remains unclear;
- risks explicitly accepted, transferred, avoided, or scheduled for mitigation;
- roadmap items without an owner, target state, decision, or evidence of progress;
- decisions affecting insurance, contracts, regulation, resilience, or client growth.

Compare scores only when the assessment version, scope, population, and scoring method are sufficiently like-for-like. If they changed, describe the underlying controls or findings instead of claiming a trend. Never invent a benchmark, probability, financial loss, risk reduction percentage, or red, amber, or green rating.

Separate a missing control, missing evidence, stale evidence, failed test, and accepted exception; they are not equivalent.

## Build the executive view

Use a compact past-present-future structure:

- **Past:** what was remediated or measurably improved.
- **Present:** the three to five most consequential active risks or obligations.
- **Future:** the decisions, investment, ownership, or risk acceptance needed next.

Keep detailed control evidence as drill-down material. Translate technical findings into business consequences while retaining the source record.

Every material risk should have a proposed disposition and owner. Security silence is not risk acceptance. A decision log entry should capture the decision, decision maker, context, alternatives, residual risk, review date, and supporting evidence when known.

Use the same escalation test as the roadmap:

- a business-level security outcome may be a goal;
- a multi-step remediation or governance program may be an initiative;
- an approved discrete follow-up may be a task;
- a proposal awaiting risk or budget approval remains a decision, not a commitment.

## Return the evidence slice

### Coverage

Systems, assessment versions, frameworks, periods, freshness, completeness, and missing evidence.

### Findings

Observation, business implication, disposition, confidence, and evidence IDs or links.

### Existing records

Relevant assessments, risks, controls, goals, initiatives, tasks, tickets, meetings, and deliverables.

### Decisions

The smallest set of decision-ready risk, policy, budget, or priority choices with recommended options and trade-offs.

### Proposed changes

Potential record reuse, updates, creates, or links for `/qbr-prep`; do not write them.

### Unresolved inputs

Material ownership, risk tolerance, compliance scope, budget, or linkage questions that cannot be resolved from evidence.
