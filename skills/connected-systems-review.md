---
name: connected-systems-review
description: Discover connected PSA, RMM, Microsoft 365, and available ScalePad SaaS Manager sources for one exact client, verify mappings and coverage, and load read-only evidence adapters. Use before a QBR when source availability or authority is unclear.
---

# Connected Systems Review

Build a trustworthy map of connected and native evidence available for one ScalePad client. Verify connections and identity before delegating focused reads; do not crawl every available source by default.

## Why aggregation matters

A useful QBR connects service demand, technology health, identity and adoption, SaaS usage, and commercial scope to client decisions. ScalePad's client-linked records can support that view without requiring direct access to every provider; provider connectors should add only material depth or freshness. Connector availability is not itself evidence of client health.

## Resolve the request

Resolve one exact ScalePad client, review period, planning horizon, and evidence question. Prefer an approved client UUID or current ScalePad context. If the client or period remains ambiguous, ask one concise question.

Identify which evidence lanes could change the answer:

- PSA for service, incidents, projects, agreements, and operational commitments.
- RMM for managed-device, monitoring, patch, and endpoint telemetry.
- Microsoft 365 for tenant identity, licensing, adoption, service health, and security posture.
- ScalePad SaaS Manager for native SaaS license inventory, assignments, app usage, lifecycle, approval, and compliance metadata.

Do not load a source merely because it is connected.

## Prefer ScalePad's aggregate

Before requiring a direct provider connector, inspect the native ScalePad records already available for the exact client:

- `scalepad_query_tickets` and `scalepad_query_agreements` for PSA-originated service and contract evidence.
- `scalepad_query_hardware` and `scalepad_query_software` for RMM-originated estate and installed-software evidence.
- `scalepad_query_contacts` plus discoverable `query_saas_licenses` operations for Microsoft 365-derived contact, license-assignment, activity, and supported authentication posture.
- `/saas-evidence` for ScalePad SaaS license inventory and SaaS Manager utilization.
- A targeted client summary section when it is cheaper than several independent reads and reports its failed or incomplete sources.

Use a direct PSA, RMM, or Microsoft 365 connection only when it provides material detail, freshness, or source-native state that ScalePad does not expose. A missing direct connector is a coverage limitation, not a reason to discard useful native evidence or fail the whole review.

## Discover live connections

Inspect the native tools, optional connectors, schemas, permissions, and authentication state advertised on this turn. Do not infer a provider, product, tenant, or capability from a remembered connector name.

For each relevant source, record:

- connector and provider when advertised;
- connected account, tenant, company, or workspace ID;
- operations and fields actually available;
- granted read scope and material permission gaps;
- latest successful sync or telemetry timestamp when exposed;
- pagination, retention, and result limits;
- errors or partial availability.

Availability is not proof of complete coverage. Native ScalePad aggregation may be partial or delayed; direct provider access may be narrower than its product UI.

## Verify client mappings

Carry the ScalePad client UUID throughout. Native ScalePad reads require no second company mapping. Match a direct external source only through, in order:

1. A verified native integration mapping.
2. An approved external company, client, or tenant ID already linked to the ScalePad client.
3. A unique exact identifier confirmed from authoritative records, such as a Microsoft tenant GUID.

Never join systems by fuzzy client, company, site, or domain name. Display names and verified domains may confirm a mapping but must not be the sole key when multiple candidates exist. If a source mapping is ambiguous, show the candidates and skip that source until reviewed.

## Load evidence adapters

When `load_skill` is advertised, inspect the skills available to the user on this turn and use its live contract:

- Load `/psa-evidence` for relevant PSA evidence.
- Load `/rmm-evidence` for relevant RMM evidence.
- Load `/m365-evidence` for relevant Microsoft 365 evidence.
- Load `/saas-evidence` for relevant native ScalePad SaaS licensing or utilization evidence.

Pass only supported variables, normally `client_id`, `client_name`, `review_period_start`, `review_period_end`, `planning_horizon_end`, `timezone`, the verified external source ID, and `source_focus`.

Load independent adapters only when their evidence could affect the requested narrative or decision. Do not reload a completed adapter unless new evidence changes its scope. If an adapter is unavailable, perform only the smallest equivalent read supported by the live connector and disclose reduced coverage.

## Reconcile sources

Prefer a native ScalePad object when it answers the question with sufficient coverage and freshness. Use the provider system for fields it alone owns or when newer source-native state could change the conclusion. Common candidates are the PSA for service transaction state, the RMM for current endpoint telemetry, Microsoft 365 for current tenant configuration, ScalePad SaaS Manager for its tracked license and app-usage records, and ScalePad for aggregated and native QBR records; verify rather than assume these roles.

Preserve contradictions, timestamps, and source IDs. Do not silently merge different populations, time windows, definitions, or statuses. Prefer stable record pointers over copied payloads and retrieve sensitive detail only when it is necessary to explain a material finding.

## Return the connection map

### Coverage

Native and direct sources considered, available, connected, mapped, unavailable, partial, stale, or not relevant.

### Source map

For each source: verified external ID, mapping evidence, live capabilities, permissions, freshness, authoritative fields, and limitations.

### Findings

Material cross-source observations, contradictions, confidence, and evidence IDs or links.

### Existing records

Stable external and ScalePad source-record IDs needed by downstream reviews.

### Decisions

Only mapping, scope, or source-authority choices that genuinely require user judgment.

### Proposed changes

Potential downstream review or ScalePad record proposals; do not execute them.

### Unresolved inputs

Ambiguous mappings, missing permissions, retention gaps, or source limitations that could change the conclusion.

This skill is read-only. Never create tickets, run device actions, change Microsoft 365 state, or mutate ScalePad records.
