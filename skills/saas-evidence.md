---
name: saas-evidence
description: Gather read-only ScalePad SaaS licensing and app-utilization evidence for one exact client. Use to identify adoption and license optimization opportunities, unmanaged SaaS, shadow IT, and shadow AI governance questions for technology, security, commercial, or QBR review.
---

# SaaS Evidence

Collect decision-relevant SaaS evidence from ScalePad's native license and SaaS Manager operations. Keep purchased or assigned licensing separate from observed app usage, and qualify tracking coverage before drawing conclusions.

## Why this evidence matters

SaaS management explains which applications are observed in use, where adoption or license allocation may be misaligned, and which tools lack understood ownership or approval. That supports cost optimization, tool consolidation, enablement, vendor governance, and the discovery of shadow IT.

Shadow AI is the AI-specific version of that governance gap: an AI-enabled app appears to be used outside a known ownership, approval, or data-handling path. Treat discovery as a reason to confirm business purpose, users, data handling, and policy—not as proof of misuse, data exposure, or noncompliance.

## Resolve scope

Resolve one exact ScalePad client UUID, review period, comparison period when needed, and evidence question. Never query a client by fuzzy name for this work.

Use a maximum requested utilization range of 366 days. Prefer the smallest period and population that can answer the question.

## Discover the live SaaS operations

Inspect the tools and schemas advertised for the authenticated user on this turn. SaaS operations may be absent because of product access, deployment, configuration, or a disabled operation.

The current source registers SaaS through `search_operations`, not a top-level direct MCP tool. Search only for the exact operations needed, then use each returned `operation_id`, `execution_tool`, and parameter contract with `execute_read`. Do not guess a future direct-tool name.

Useful native operations to discover are:

- `query_saas_utilization.get_utilization_summary` for the client summary. It accepts `client_id` and no query parameters.
- `query_saas_utilization.get_app_utilization` for app-level usage in an explicit date range.
- `query_saas_utilization.get_app_lifecycle_timeseries` for daily, weekly, monthly, or quarterly lifecycle buckets.
- `query_saas_utilization.get_app_utilization_with_users` only when per-app user detail is necessary.
- `query_saas_licenses.list_saas_licenses` for client license inventory.
- `query_saas_licenses.get_saas_asset` for one known SaaS asset.
- `query_saas_licenses.list_contact_licenses` for contact assignment and supported activity or authentication enrichment.
- `query_saas_licenses.get_saas_portfolio_summary` for account-wide portfolio totals, not a client-only answer.
- `query_saas_licenses.get_license_summary` for the authenticated partner account's ScalePad license capacity, not client SaaS consumption.

Search accepts only a bounded result page, so request the smallest exact set and follow `next_offset` only when a required match is missing. If the native operations are unavailable, report the missing capability. Do not substitute installed-software data for SaaS utilization.

## Query efficiently

Start with `get_utilization_summary` when a broad usage signal is sufficient. For app-level reads, pass the exact `start_date` and inclusive `end_date`; add paired comparison dates only when a comparable trend is required.

Use server-side filters before paging through apps. The live contract can support app, user, department, category, vendor, approval status, favorite, lifecycle, compliance-gap, missing-framework, and aligned-framework filters. Approval values are `approved`, `not_approved`, or `unreviewed`; lifecycle filters are `discovered` or `dropped_off`.

For shadow AI review, use only an AI classification returned by the live app or timeseries data, then examine approval status, observed users or departments, and any available ownership or compliance metadata. Label the app as a candidate when ownership or policy cannot be established; do not classify every AI app as shadow AI.

Use the base app-utilization operation before the user-enriched operation. Per-app users add an extra query for every app row, so use a small `users_limit` and request them only when a material question cannot be answered at app level.

Use cursor pagination and the smallest useful page size, up to the live maximum of 200. App pagination is best-effort and non-atomic: records may move, repeat, or be skipped while underlying usage changes. Preserve the cursor and coverage limits rather than reporting an unstable crawl as an exact census.

For license inventory, filter by the exact client UUID and relevant product, status, term, or pool fields returned by the live contract. Use portfolio summaries only for account-wide questions. When totals should describe purchased licensing, request the contract's paid-only population; free entitlements, trials, and uncapped-capacity sentinels can otherwise change totals.

With Lifecycle Manager access, contact assignments are returned as contact enrichment. Use `list_contact_licenses` and filter its returned assignments; do not rely on the Core-only `get_contact_license` detail operation.

## Preserve SaaS meaning

Keep these distinctions explicit:

- License inventory is not observed app usage.
- Assigned, available, utilized, suspended, and uncapped capacity are different states.
- An assigned license is not proof of active use.
- A discovered app is not proof of purchase, approval, business necessity, or managed ownership.
- No observed usage may mean no activity, incomplete enrollment, missing agents, retention limits, or unsupported coverage.
- Active time, average time, sessions, unique users, and days active are different measures.
- Approval status is a governance state, not a security verdict.
- App certification or framework metadata is not proof that the client is compliant.
- A compliance gap is source evidence for review, not a complete vendor-risk assessment.
- SaaS inventory is not installed-software coverage, and installed-software results are not a SaaS Manager substitute.

Lifecycle timeseries segments are mutually exclusive and priority ordered. `risky_apps` takes precedence, followed by `unapproved_apps`, `ai_apps`, `other_apps`, and `unused_apps`; do not add those groups to other categories or double-count them.

Compare periods only when tracking coverage, app classification, filters, and date lengths are sufficiently comparable. Never turn usage time into employee-performance scoring or infer user intent.

## Return the evidence slice

### Coverage

Authenticated product access, client UUID, operations found or missing, period, comparison period, enrollment or tracking limitations, filters, pages, cursors, and failed reads.

### Findings

Direct observations with app, asset, contact, product, or vendor IDs; source metrics; period; confidence; and returned links when available.

### Existing records

Relevant SaaS asset, app, contact assignment, category, vendor, department, and source-record IDs.

### Decisions

Questions suggested by the evidence; leave security, technology, commercial, and roadmap conclusions to the consuming review skill.

### Proposed changes

Potential investigation, governance, optimization, or roadmap follow-through for downstream review; do not execute it.

### Unresolved inputs

Missing product access, tracking coverage, enrollment state, mappings, comparison validity, source definitions, or user-level privacy justification.

This skill is read-only. Never assign or unassign licenses, create enrollment tokens, approve or reject apps, change classifications, alter tracking, or mutate ScalePad records. Enrollment tokens are sensitive credentials and are outside this skill.
