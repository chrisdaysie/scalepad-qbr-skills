---
name: rmm-evidence
description: Gather read-only RMM-originated evidence from ScalePad and, when needed, a connected RMM. Use to expose lifecycle and resilience risk, monitoring blind spots, and remediation evidence for technology, security, service, or QBR review.
---

# RMM Evidence

Collect RMM-originated evidence without turning observation into remediation, preferring native ScalePad objects before an optional direct RMM connection. Preserve the monitored population, timestamps, exclusions, and source-native meaning.

## Why this evidence matters

RMM evidence shows whether the managed technology estate is visible, supportable, current, and resilient. It can uncover concentrated lifecycle exposure, missing monitoring, recurring operational weakness, or evidence that an approved remediation worked. Use telemetry to frame business consequence and the next decision; an alert or stale agent is not business impact by itself.

## Verify identity and population

Require one exact ScalePad client UUID. A direct RMM client, organization, or site mapping is required only before querying the provider connector; prefer a native integration link or approved external ID. Never combine clients or sites by fuzzy name.

Resolve the review window and the device population relevant to the question. State whether the source includes all managed devices, selected sites, active agents, servers only, workstations only, or another filtered population.

## Prefer native ScalePad records

Use the live native contracts first:

- `scalepad_query_hardware` for aggregated device inventory, source lineage, lifecycle, replacement, warranty, type, site, and available device summaries.
- `scalepad_query_software` for installed-software inventory, products, lifecycle summaries, and affected devices. With Lifecycle Manager access this is installed software; without it, the tool may fall back to Core SaaS data, which is not equivalent.
- `backup_radar_query_health` when advertised and backup health is relevant; do not infer backup status from a generic RMM field when a dedicated source exists.

Filter by the exact client UUID and relevant device type or source before pagination. Prefer device and software summaries, then inspect only material records. Preserve integration source, sync freshness, and coverage signals.

Do not fail merely because no direct RMM connector is available. Use ScalePad's aggregate for the evidence it contains and disclose missing live-alert, patch-policy, monitoring, or agent-state detail.

## Discover the remaining RMM contract

Only when ScalePad lacks material detail or freshness, inspect any connected RMM account, operations, fields, filters, timestamps, enums, pagination, retention, and permissions available on this turn. Do not assume a vendor schema or that a familiar field is current telemetry.

Prefer server-side filters by verified client or site ID, device status, platform, policy, and date. Read aggregate or summary data first, then inspect only devices or alerts material to the finding.

Record the connector sync time, each observation's timestamp, pages retrieved, result limits, and failed sources. RMM data can be stale even when the connector responds successfully.

## Gather only relevant evidence

Depending on the request and live capabilities, inspect:

- enrolled and recently seen devices by type, site, platform, and critical role;
- agent check-in freshness, orphaned agents, duplicate records, and monitoring gaps;
- operating-system version, supportability, age, and end-of-support evidence;
- patch policy scope, scan freshness, approval state, maintenance window, failures, exclusions, and reboot state;
- active and historical alerts, recurrence, flapping, suppression, severity, and affected services;
- monitoring policy coverage and changes that affect comparability;
- endpoint security, encryption, backup, or configuration posture only when the RMM is an authoritative source for that field;
- evidence of improvement after an approved remediation.

## Preserve telemetry meaning

Distinguish:

- offline from stale, retired, intentionally disconnected, or outside the connector population;
- noncompliant from not assessed, not applicable, excluded, pending scan, or pending reboot;
- an alert from an incident and alert count from business impact;
- configured monitoring from tested monitoring;
- installed security tooling from healthy, current, and policy-compliant tooling;
- missing telemetry from a confirmed disabled control;
- device inventory from lifecycle-scoped or integration-scoped records.

Do not compare patch or alert trends across changed policies, thresholds, populations, or maintenance windows without disclosing the change.

## Return the evidence slice

### Coverage

ScalePad native coverage, optional RMM provider and account, verified external client and site IDs when used, population, time window, sync freshness, filters, pagination, permissions, and missing telemetry.

### Findings

Direct observations with device, policy, or alert IDs; timestamps; provider-native states; confidence; and source links when returned.

### Existing records

Relevant client, site, device, policy, alert, check, and remediation-history IDs.

### Decisions

Questions suggested by the evidence; leave roadmap, risk, and service decisions to the consuming review skill.

### Proposed changes

Potential investigation or follow-through for downstream review; do not execute it.

### Unresolved inputs

Ambiguous mappings, population gaps, stale telemetry, changed policies, missing permissions, or unclear source authority.

This skill is read-only. Never run scripts or commands, deploy software, patch or reboot devices, isolate endpoints, acknowledge alerts, change monitors, edit policies, or mutate ScalePad records.
