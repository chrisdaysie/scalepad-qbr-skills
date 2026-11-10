---
name: qbr-prep
description: Prepare an evidence-backed QBR plan for one exact ScalePad client and review period using available ScalePad records, documentation, tickets, prior meetings, and roadmap work. Read-only; produces a structured handoff for qbr-apply and never mutates records.
---

# QBR Prep

Prepare a decision-oriented QBR plan for one exact client. Gather facts, identify patterns, shape a client-facing narrative, and propose native ScalePad record changes. This skill is read-only. Its handoff never grants write approval.

## Resolve scope

Resolve exactly one ScalePad client, one review period, one timezone, and one planning horizon.

Distinguish:

- **Review period:** the completed or current period whose progress and evidence are being assessed.
- **Planning horizon:** normally the next 12 months used to sequence goals and initiatives.

Prefer an approved client UUID or current page context. Otherwise use the advertised client query tool and accept only a unique exact match. Never merge evidence from similarly named clients. If the client or period remains ambiguous, ask one concise question.

When relevant, resolve the linked Lexful organization using its stable ID or an exact verified linkage. Treat documentation as client-scoped evidence and prevent cross-client leakage.

## Compose available skills

This skill is the router and synthesizer, not the expert implementation of every evidence domain.

When `load_skill` is available, inspect which skills are available to the user on this turn. Load only relevant available specialists. Do not assume a skill exists and do not fail merely because an optional skill is absent.

Useful specialist branches include:

- `/connected-systems-review` when connected PSA, RMM, Microsoft 365, or native ScalePad SaaS Manager evidence could materially change the review and source coverage is not already verified. Let it load the smallest relevant source adapters.
- `/psa-evidence`, `/rmm-evidence`, `/m365-evidence`, or `/saas-evidence` directly only when the request is source-specific or the coordinator is unavailable.
- `/client-context-review` for client documentation, account plans, stakeholders, contracts, decisions, and prior meeting notes.
- `/roadmap-review` when goals, initiatives, assessments, budgets, or roadmap recommendations exist. Load this before drafting any roadmap narrative or proposed initiative set.
- `/service-review` when ticket, SLA, incident, recurring-issue, or support-demand evidence is available.
- `/security-review` when security assessments, compliance records, ControlMap evidence, incidents, or accepted risks are material.
- `/technology-review` when hardware lifecycle, software, SaaS, warranty, or estate-health evidence may affect the plan.
- `/commercial-review` when agreements, renewals, licensing, estimates, or budget timing are material.
- `/qbr-story` when a separate narrative specialist is available and the evidence slices are complete.
- `/qbr-grill` when fact-finding is complete but user judgment still blocks the plan.

Use the live `load_skill` contract and pass the selected skill's slash command plus the variables it needs. Prefer these shared variables when supported:

- `client_id`
- `client_name`
- `review_period_start`
- `review_period_end`
- `planning_horizon_end`
- `timezone`
- `linked_organization_id`
- `psa_company_id`
- `rmm_client_id`
- `m365_tenant_id`
- `source_focus`
- `previous_qbr_id`
- `evidence_limit`

Ask each specialist for the same compact result shape:

- `coverage`: sources checked, unavailable, partial, and not applicable.
- `findings`: observation, implication, confidence, and evidence IDs or links.
- `records`: relevant existing records with stable IDs.
- `decisions`: client decisions or approvals suggested by the evidence.
- `proposed_changes`: reuse, update, create, or link proposals without executing them.
- `unresolved_inputs`: choices only the user or client can make.

Collect independent specialist slices in any useful order. Never reload a specialist already completed for the current request unless new evidence changes its scope. Pass context pointers and stable IDs instead of copying large raw payloads between skills. Facts are the agent's job; ask the user only for unresolved decisions.

When a specialist is unavailable, perform the smallest equivalent read-only review directly and record the reduced coverage.

Prefer native ScalePad objects and targeted summaries before requiring direct third-party connectors. ScalePad may already aggregate PSA tickets and agreements, RMM-derived hardware and software, Microsoft 365-derived contacts and licenses, and SaaS Manager usage. Use provider connections only to close material coverage or freshness gaps; their absence must not erase usable native evidence.

## Discover the live data surface

Use the tools and schemas advertised for this user on this turn. Prefer common direct reads when available:

- `scalepad_query_clients`
- `scalepad_query_contacts`
- `scalepad_query_goals`
- `scalepad_query_initiatives`
- `scalepad_query_tasks`
- `scalepad_query_meetings`
- `scalepad_query_deliverables`
- `scalepad_query_tickets`
- `scalepad_query_assessments`
- `scalepad_query_plan`
- `scalepad_query_agreements`
- `scalepad_query_hardware`
- `scalepad_query_software`

Use `search_operations` only for an uncommon read whose contract is not exposed directly. Preserve its returned operation ID, parameters, prerequisites, and coverage limitations. Never use `execute_write` in this skill.

## Gather evidence progressively

Start broad enough to orient, then follow only evidence that can change the QBR narrative or a client decision. Do not exhaustively scrape every accessible record.

### Minimum pass

1. Resolve the exact client and account context.
2. Read the most recent prior QBR deliverable or executive summary when one exists.
3. Read current goals, initiatives, open tasks, and relevant meetings for that client.
4. Review tickets and service evidence for the review period.
5. Use connected-system evidence only when its verified coverage could change a finding, narrative, or decision.
6. Follow documentation, assessment, budget, contract, asset, software, SaaS, security, or backup evidence only when it is relevant to a finding or planned decision.

For broad client context, use `get_client_summary` and request only relevant sections such as `roadmap`, `open_tasks`, `meetings`, `hardware_lifecycle`, `software`, `saas_licenses`, or `saas_management`. Omitting `sections` loads all sections. Preserve its `complete`, `failed_sources`, and `incomplete_sources` signals; availability is not proof of complete coverage.

For the prior deliverable, list the client's deliverables, select the exact newest relevant QBR by ID and date, then inspect it. Prefer its approved narrative and decisions over reconstructing history from unrelated records.

Use narrow filters, the smallest useful page size, and cursors only when another page could change the conclusion. Fetch record details only for credible candidates. Goal and initiative detail operations may inspect up to ten IDs together when advertised.

## Fallback domain pass

When a relevant specialist is unavailable, review only the material lane with the equivalent direct reads:

- **Context:** current priorities, stakeholders, prior decisions, scope, and commitments.
- **Roadmap:** goal alignment, progress, stalled work, dependencies, duplicate carry-forward work, and owned follow-through.
- **Service:** recurring causes, high-impact incidents, unusual demand, and post-incident actions; never equate ticket volume with client health.
- **Security:** material risks, remediation, accepted risk, deadlines, and comparable assessment movement; do not compare changed templates as a trend.
- **Technology:** lifecycle deadlines, concentrated exposure, supportability, standardization, and source freshness; lifecycle data is not necessarily complete inventory.
- **Commercial:** renewals, agreement scope, licensing, and investment timing; keep estimates, proposals, approvals, commitments, and actuals distinct.

Across every lane, preserve contradictions, identify authoritative and current sources, and distinguish client statements from MSP recommendations. Inspect tasks and meetings for unowned commitments, and compare the prior deliverable with current evidence so completed value and repeated undecided recommendations are visible.

## Synthesize the QBR

Label every material statement as one of:

- **Observation:** directly supported by a cited record or document.
- **Inference:** a reasoned interpretation of multiple observations.
- **Recommendation:** proposed MSP action or client decision.
- **Unknown:** missing or partial evidence that could change the conclusion.

Build one narrative arc:

1. Where the client wanted to go.
2. What changed during the review period.
3. What value was delivered or risk changed.
4. Where the client stands now.
5. What decisions and actions come next.

Lead with the client's priorities rather than ticket statistics. Prefer two or three consequential decisions over a long recommendation list. Record contradictions, confidence, and missing coverage.

## Shape proposed records

Use these as review heuristics, not quotas:

- One to three active, prioritized client goals for the planning period.
- Three to five meaningful initiatives across the rolling 12-month roadmap.
- One to three active or decision-ready initiatives for the current quarter.
- No target task count; one task per committed, owned, dated next action.
- One curated draft QBR deliverable, preferably from the approved client template.
- Two or three decision items, with at least one meaningful decision or acknowledged deferral.

Goals express client outcomes. Initiatives express strategic changes. Tasks express execution. The deliverable makes progress, value, risks, and decisions understandable to client leadership.

Flag deviations rather than silently deleting, combining, or inventing records.

## Produce the handoff

Return a self-contained Markdown plan with these sections:

### Scope

- Client name and exact UUID
- Linked organization ID when relevant
- Review period, timezone, and planning horizon
- Previous QBR or deliverable ID

### Evidence coverage

- Sources checked
- Complete, partial, unavailable, and not-applicable sources
- Important contradictions and unknowns

### Executive narrative

- Where we were
- What changed
- Where we are
- What is next

### Goals and roadmap

For every goal and initiative, include existing ID when present, current state, evidence-backed interpretation, proposed state, relationships, and whether to reuse, update, create, or leave unchanged.

### Service, risk, and value signals

Summarize only material patterns with evidence IDs or links and business interpretation.

### Decisions

List two or three proposed client decisions or acknowledged deferrals, including rationale, decision owner, and consequences of delay.

### Follow-through

List proposed tasks and meeting changes with owner, due date, parent record, and evidence. Keep undecided recommendations out of the task list.

### Deliverable outline

Describe the proposed draft QBR deliverable's narrative, sections, supporting evidence, decision items, and approved template ID when known.

### Proposed ScalePad actions

For each action include:

- `action`: reuse, update, create, link, or no change
- `record_type`
- existing `record_id` and returned link when present
- exact proposed fields
- dependency IDs
- supporting evidence IDs or links
- methodology warning, if any
- unresolved required input, if any

### Handoff status

State clearly that the plan is ready for `/qbr-apply` review or name what remains unresolved. This handoff does not authorize writes.

The preparation is complete when every material recommendation has evidence, every proposed record has a clear purpose and relationship, coverage limitations are explicit, and the next agent can preview writes without repeating the research.
