---
name: m365-evidence
description: Gather privacy-conscious, read-only Microsoft 365 evidence from ScalePad and, when needed, a direct tenant connection. Use to support identity and access, license fit, adoption, service health, security, commercial, or QBR decisions.
---

# Microsoft 365 Evidence

Collect decision-relevant Microsoft 365 evidence with minimum necessary access, preferring native ScalePad objects before an optional direct tenant connection. Default to administrative telemetry and configuration state, not user communications or document content.

Use `/saas-evidence` instead when the question is about ScalePad SaaS Manager's cross-app discovery, app lifecycle, approval, or native license inventory. Microsoft 365 evidence remains the direct tenant-administration view; do not silently combine the two populations.

## Why this evidence matters

Microsoft 365 is often a central identity, collaboration, and licensing platform for the client. License and activity evidence can clarify adoption and investment fit; authentication, roles, and policy evidence can expose access decisions; service health can explain disruption. Use the smallest administrative view needed for those decisions, never as employee surveillance or a proxy for productivity.

## Verify the tenant

Require one exact ScalePad client UUID. A verified Microsoft tenant ID is required only before querying Microsoft directly; prefer a native integration mapping, approved tenant GUID, or authoritative tenant record. A display name or email domain may confirm the match but must not be the sole key when multiple tenants or domains exist.

Resolve the review window, timezone, and evidence question. Keep separate tenants, subsidiaries, and delegated administration relationships explicit.

## Prefer native ScalePad records

Use the live native contracts first:

- `scalepad_query_contacts` for client-scoped contacts and any returned Microsoft 365-derived assignment, activity, or authentication enrichment.
- `/saas-evidence` for native SaaS license inventory, contact assignments, and SaaS Manager usage. Its discoverable `query_saas_licenses.list_contact_licenses` operation can expose supported activity and authentication fields when available.
- `scalepad_query_software` only for installed-software questions with Lifecycle Manager access; do not use its Core SaaS fallback as tenant-administration evidence.

Filter by the exact ScalePad client UUID and inspect the live returned fields before claiming MFA, activity, or license coverage. Do not fail merely because no direct Microsoft connector is available; return the native evidence and state which tenant-native controls or reports remain unknown.

## Discover the remaining Microsoft contract

Only when ScalePad lacks material detail or freshness, inspect any connected Microsoft account, tenant, tools, permissions, operations, fields, report periods, pagination, retention, and throttling advertised on this turn. Do not assume Microsoft Graph scopes or admin roles that are not exposed.

Use the least-privileged read operation that answers the question. Start with aggregates and administrative metadata. Do not read mailbox bodies, Teams conversations, SharePoint or OneDrive document contents, calendar details, or other user content unless the user explicitly requests that exact content, it is necessary, and the live authorization permits it.

Record report generation time, data latency, period, filters, pages, suppressed values, and permission failures. Microsoft reports may lag current tenant state.

## Gather only relevant evidence

Depending on the request and live capabilities, inspect:

- tenant identity, verified domains, subscriptions, and service plans;
- licensed, unlicensed, disabled, guest, member, and service accounts;
- license assignment, availability, and supported activity or adoption reports;
- privileged roles, identity protection, authentication registration, and conditional-access posture;
- security or compliance posture with its scoring model and report date;
- service-health incidents and advisories relevant to the review period;
- product usage trends at the least identifying level that supports the decision;
- configuration or lifecycle evidence linked to a current roadmap question.

Avoid collecting user-level detail when an aggregate answers the question. Never use administrative telemetry to rank employee performance or infer intent.

## Preserve Microsoft semantics

Distinguish:

- assigned license from enabled service plan and observed activity;
- inactive from disabled, guest, service, shared, newly created, or outside the report window;
- authentication registered, capable, required, and enforced;
- a configured policy from a policy that applies to the relevant population;
- secure-score movement from actual risk reduction;
- service advisory from confirmed tenant impact;
- missing report data from confirmed absence of activity or control;
- current configuration from delayed reporting data.

Compare trends only when report definitions, populations, licenses, periods, and scoring methods are sufficiently consistent. Do not invent benchmarks, savings, risk percentages, or compliance conclusions.

## Return the evidence slice

### Coverage

ScalePad native coverage, verified tenant ID when direct access is used, connected account, permissions, reports, periods, sync freshness, latency, pagination, suppressed values, and failed reads.

### Findings

Direct observations with tenant-native IDs, report dates, field definitions, confidence, and returned links when available.

### Existing records

Relevant tenant, domain, subscription, service-plan, user-population, policy, role, incident, and report IDs.

### Decisions

Questions suggested by the evidence; leave security, technology, licensing, and roadmap decisions to the consuming review skill.

### Proposed changes

Potential follow-through for downstream review; do not execute it.

### Unresolved inputs

Missing tenant mapping, permissions, report coverage, population definitions, source authority, or privacy approval.

This skill is read-only. Never change users, groups, roles, licenses, domains, policies, devices, mail, files, calendars, Teams content, security settings, or ScalePad records; never send messages or invitations.
