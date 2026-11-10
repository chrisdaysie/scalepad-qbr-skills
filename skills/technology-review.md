---
name: technology-review
description: Review one ScalePad client's hardware lifecycle, software, SaaS, warranty, estate concentration, and technical-health evidence for a QBR. Use to identify decision-worthy lifecycle risk and investment timing. Read-only.
---

# Technology Review

Turn the technical estate into a small set of lifecycle, resilience, standardization, and investment signals that matter to the client.

## Resolve scope

Resolve one exact client, review period, and planning horizon. Use a verified ScalePad client ID or a unique exact match. Retain site, source, and device identifiers where they affect the conclusion.

## Discover the live read surface

Prefer advertised direct reads for hardware, software, SaaS licenses and management, agreements, insights, goals, initiatives, tasks, meetings, and deliverables. Use a targeted client summary only when a broad section is genuinely needed. Use `search_operations` plus `execute_read` for uncommon reads only after discovering the live contract. Never call `execute_write`.

When connected or native operational evidence is material, consume completed `/rmm-evidence`, `/m365-evidence`, or `/saas-evidence` slices. If needed and available, load the relevant adapter through the live `load_skill` contract using verified IDs and the narrow technology question. Preserve each adapter's population, freshness, tracking coverage, and source limitations.

Record source systems, last sync, filters, coverage, pagination, and failures. Distinguish lifecycle-scoped hardware from a complete asset inventory.

## Review the estate

Look for:

- warranty, end-of-life, age, capacity, or support deadlines within the planning horizon;
- concentrated exposure by site, role, platform, vendor, or critical workload;
- unsupported or non-standard software and platforms;
- meaningful SaaS license waste, adoption gaps, duplicated or unmanaged apps, and shadow AI requiring ownership or enablement decisions;
- unknown, stale, duplicate, or unsynchronized records that weaken confidence;
- improvements completed since the prior review;
- dependencies between lifecycle work, security, service patterns, agreements, and budget.

Do not label every old device a strategic risk. Prioritize by business criticality, concentration, deadline, replacement lead time, supportability, and consequence. Do not infer usage from license assignment alone or infer inventory completeness from one integration.

## Translate evidence into the roadmap

For each material signal, identify the client consequence, decision window, dependency, and smallest response.

- Use a goal only for a durable client outcome such as resilience, standardization, or workforce readiness.
- Use an initiative for a coordinated refresh, migration, remediation, or optimization program.
- Use a task only for an approved discrete follow-up with ownership.
- Keep routine maintenance and isolated replacement work out of the strategic roadmap unless materially consequential.

Treat cost as unknown unless a source provides it. Keep estimates, approved budgets, purchase commitments, and actual spend distinct.

## Return the evidence slice

### Coverage

Systems, sections, dates, asset population, exclusions, sync freshness, and incomplete sources.

### Findings

Observation, business implication, timing, confidence, and evidence IDs or links.

### Existing records

Related insights, goals, initiatives, tasks, agreements, meetings, and deliverables.

### Decisions

Decision-ready lifecycle or platform choices with recommendation, timing, and trade-off.

### Proposed changes

Potential roadmap and follow-through changes for `/qbr-prep`; do not execute them.

### Unresolved inputs

Material criticality, scope, cost, ownership, timing, or source-coverage questions.
