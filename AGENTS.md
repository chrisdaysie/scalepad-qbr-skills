# Repository Agent Guide

This repository contains portable, single-file skills for third-party agents using ScalePad MCP tools. Keep runtime instructions in `skills/`; keep maintainer guidance here.

## Repository map

- `README.md` — user-facing installation, routing, and safety guide.
- `INSTALL.md` — operational GitHub import, manual installation, verification, and update guide.
- `skill-kit.json` — authoritative kit identity, version, entry points, and exact install list.
- `skills/*.md` — standalone runtime skills uploaded to the agent platform.
- `scripts/validate-skills.py` — dependency-free structural validation.

Do not add generated bundles, copied API documentation, example payload dumps, or provider-specific packaging unless a real consumer requires them.

## Skill format

Every file under `skills/` must:

- Be a self-contained Markdown skill with YAML frontmatter.
- Use only `name` and `description` frontmatter fields unless a target platform requires another portable field.
- Use a lowercase hyphenated `name` matching the filename exactly.
- Have a discriminating description that says what the skill does and when to use it.
- Contain only guidance that changes the agent's decisions; do not restate generic agent behavior.
- Remain useful when optional sibling skills are unavailable.

Preserve the author byline in the root README unless instructed to change it. Do not invent a license or copyright policy.

## Composition contract

`/qbr` is the router. `/connected-systems-review` coordinates optional source adapters. `/qbr-prep` synthesizes evidence. Specialist reviews provide focused interpretation. `/qbr-apply` is the only writer.

When a skill composes another skill:

- Use the live `load_skill` contract.
- Confirm the referenced slash command is available to the user on that turn.
- Pass stable IDs and compact variables instead of copied raw payloads.
- Do not reload a completed branch unless new evidence materially changes its scope.
- Fall back to the smallest supported read-only review and disclose reduced coverage.
- Never make an optional sibling a hidden hard dependency.

Use the shared variables and specialist evidence envelope documented in `README.md`. When adding or renaming a skill, update the catalog, workflow, cross-references, and examples there.

Keep `skill-kit.json` bidirectionally complete: every listed path must exist and every `skills/*.md` file must be listed. Commands and paths are unique; commands match the filename and frontmatter name; entry points name listed commands. Keep manifest paths canonical, relative, directly under `skills/`, and free of symlinks. The manifest does not duplicate skill descriptions or instructions.

Keep the README's host guidance capability-based and portable. Document exact vendor paths or invocation syntax only when verified against that host's current contract; do not make a particular agent platform a hidden dependency.

Keep `INSTALL.md` operational and host-neutral. It may explain verified capability patterns and the commit-pinned import contract, but it must not duplicate skill prompts or imply that installation grants write approval.

## ScalePad MCP rules

- Discover the tools and live operation contracts available to the current user before promising an action.
- Prefer advertised direct read tools for common records.
- Use `search_operations` for uncommon operations, then invoke only the returned operation and fields.
- Prefer native ScalePad operations over raw API operations when both support the intended write.
- Resolve one exact client and preserve tenant boundaries.
- Never fuzzy-match a record for a write.
- Preserve distinctions among missing, unknown, empty, zero, and false.
- Preserve fields outside an approved partial change.

Do not freeze a remembered MCP schema into these files. Tool names may be mentioned as preferred live discoveries, but the skill must still inspect the contract available on the turn.

## Connected-source adapters

`psa-evidence.md`, `rmm-evidence.md`, and `m365-evidence.md` qualify evidence that may already be aggregated into ScalePad and may optionally be enriched from a provider connection. `saas-evidence.md` qualifies native ScalePad SaaS licensing and utilization evidence. None replaces the domain review skills that interpret it.

- Keep every adapter optional and read-only.
- Explain why the evidence matters and which client or MSP decision it can support; do not return a technically complete data dump without decision context.
- Prefer native ScalePad objects with sufficient coverage and freshness before requiring a direct provider connector. A missing connector is a coverage note, not an automatic failure.
- Use `scalepad_query_tickets` and `scalepad_query_agreements` for PSA-originated evidence; `scalepad_query_hardware` and `scalepad_query_software` for RMM-originated evidence; and `scalepad_query_contacts` plus discoverable SaaS-license operations for Microsoft 365-derived evidence when their live contracts expose the required fields.
- Use a provider connector only to close a material detail, configuration, or freshness gap. Preserve which source supplied every finding.
- Verify external client, company, site, or tenant IDs through a native mapping or approved authoritative identifier; never fuzzy-match names.
- Discover the live connector account, tools, schemas, permissions, filters, enums, pagination, retention, and timestamps.
- Retrieve aggregates and metadata before sensitive detail; use the minimum data needed for the question.
- Preserve provider-native states, populations, time windows, policy definitions, and source authority.
- Report partial, stale, suppressed, unavailable, and failed coverage explicitly.
- Return the shared evidence envelope with observations and suggested questions, not domain conclusions.
- Do not add operational writes, device actions, Microsoft administration, or PSA mutation to an evidence adapter.

For `saas-evidence.md`, preserve the source-backed split between `query_saas_licenses` and `query_saas_utilization`. Discover both through `search_operations`; do not invent a direct SaaS tool. Make its decision value explicit: utilization, license optimization, shadow IT, and shadow AI governance. License assignments are not app usage, discovered AI is not proof of misuse or exposure, app metadata is not client compliance, and `scalepad_query_software` is not a SaaS Manager fallback. Never assign licenses or create enrollment tokens from the evidence skill.

When adding another source adapter, wire it only to domain skills that can legitimately interpret its evidence and update the README routing map.

## Releases

Version the kit as a whole in `skill-kit.json`; keep the README release row and changelog aligned. Do not add versions or dates to individual skills.

- **Patch:** compatible wording, methodology, safety, or bug corrections.
- **Minor:** a new skill or backward-compatible composition/output capability.
- **Major:** removed or renamed slash commands, incompatible variables, or a breaking composition/output contract.

For every release, update the README Release row and add a dated entry to its Changelog section in the same change. Do not add separate release files unless a real publishing workflow requires them.

## Method and record shape

Treat the planning numbers as heuristics, never quotas:

- One to three active client business goals.
- Three to five meaningful initiatives across a rolling 12-month roadmap.
- One to three active or decision-ready initiatives in the current quarter.
- No task quota; tasks represent committed, owned actions.
- One curated draft deliverable and two or three consequential decisions.

Maintain these boundaries:

- Goals describe client outcomes.
- Initiatives describe strategic change requiring sequencing, investment, or a decision.
- Tasks describe committed execution.
- Deliverables explain progress, value, risk, roadmap, and decisions.
- Operational evidence supports the story; it is not the story by itself.

Keep estimates, proposals, approved budgets, commitments, and actuals separate. Compare assessment or trend data only when the population, period, and method are sufficiently comparable.

## Write safety

All skills except `qbr-apply.md` are read-only.

`qbr-apply.md` must always:

1. Resolve the exact client and current records.
2. Discover the live write contract.
3. Reconcile reuse, update, create, and link candidates.
4. Preview the exact bounded batch.
5. Wait for explicit approval.
6. Apply dependencies before dependents.
7. Read back every write and reconcile uncertainty before retrying.

The suite does not send invitations, publish or share content, create PSA tickets, archive records, or delete records. Do not broaden that authority while editing an unrelated skill.

## Validation

Run before handoff:

```bash
python3 scripts/validate-skills.py
```

Also review changed instructions for semantic safety: the validator checks structure and references, not whether a workflow makes good decisions.
