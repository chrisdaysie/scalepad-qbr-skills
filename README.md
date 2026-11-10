# ScalePad QBR Skill Kit

> **Turn scattered client evidence into a clear, decision-ready QBR.**
>
> Eighteen composable skills connecting client context, roadmaps, service delivery, security, technology lifecycle, commercial evidence, native SaaS Manager data, and optional PSA, RMM, and Microsoft 365 sources—adapted around MSP customer success best practices.

| | |
| --- | --- |
| **Author** | Chris Day · CEO, ScalePad |
| **Release** | 1.0.0 · 10 November 2026 |
| **Designed for** | Third-party agents using ScalePad MCP tools |
| **Write boundary** | `/qbr-apply` only, after explicit approval |

Each skill is self-contained. Install the full set for composition, or install only the scenarios a user needs. `/qbr` is the front door; `/qbr-apply` is the only skill allowed to mutate records.

## Why this kit exists

Most QBR automation can collect data. The harder problem is preserving what the data means and turning it into a small number of defensible client decisions. This kit gives an agent that semantic layer: source adapters qualify evidence, domain reviews interpret it, QBR skills build the client story, and only an approved apply step changes native records.

| Layer | Semantic value | Typical output |
| --- | --- | --- |
| Source evidence | Establishes what was observed, where, when, and with what coverage | Qualified facts, source IDs, freshness, and gaps |
| Domain review | Explains why the evidence matters to the client's business | Implications, trade-offs, and decision questions |
| QBR preparation and story | Connects prior priorities, delivered value, present state, and next choices | Executive narrative, agenda, and proposed records |
| Approved application | Preserves the reviewed meaning in native ScalePad objects | Goals, initiatives, tasks, links, meeting records, and draft deliverables |

The record shapes are deliberate: goals are durable client outcomes, initiatives are strategic changes, tasks are committed actions, and deliverables communicate the story. Observations, inferences, recommendations, decisions, and commitments remain distinct so an agent does not turn a signal into a promise.

## Quick start

1. Import the exact skill list from `skill-kit.json`, or add each listed Markdown file using its frontmatter `name` as the slash command.
2. Connect the ScalePad MCP tools for the current user.
3. Make the skills that may collaborate available to the user on the same turn.
4. Start with `/qbr` for routing or invoke a specialist directly.

The kit standardizes on `/qbr-prep` and a portable `load_skill` handoff pattern.

See [INSTALL.md](INSTALL.md) for manifest-based GitHub import, manual host layouts, verification, and update guidance.

### GitHub import identity

`skill-kit.json` is the machine-readable source of truth for the kit ID, version, entry points, and exact install list. Skill descriptions and instructions remain canonical in their Markdown files. `entryPoints` identifies recommended starting commands; every listed skill remains directly invokable when the host supports it.

A GitHub importer should identify this kit by GitHub repository ID plus manifest `id`, scoped to the provider and host. It should keep the current repository URL for display, resolve the requested ref to one immutable commit SHA before preview, fetch the manifest and every listed skill from that same SHA, and install that buffered set atomically after approval. Repository renames or transfers retain identity; forks receive a new repository ID and therefore a distinct identity.

## Use with agentic tools

The slash command is the portable skill name, not a requirement that every host display commands the same way. Invoke `/qbr`, `$qbr`, or the host's equivalent named-skill action.

| Host pattern | Install | Compose and run |
| --- | --- | --- |
| **Skill-native host** | Import `skill-kit.json` when supported; otherwise upload each manifest-listed file as one skill using its frontmatter `name`. | Make collaborating skills available to the user on the same turn. Start with `/qbr`; when supported, a composing skill may call the live `load_skill` contract with another slash command and compact variables. |
| **Agent Skills-style host** | Place each manifest-listed file at `<skills-root>/<name>/SKILL.md`. The Markdown body needs no rewrite. | Install the full suite for routing or only the required specialists. Use the host's named-skill invocation; if it has no `load_skill`, let the coordinator open the selected specialist instructions directly. |
| **Prompt, rules, or custom-assistant host** | Attach the smallest relevant skill files as instructions or knowledge. | Start with a specialist such as `/qbr-prep` or `/saas-evidence`; do not attach all 18 files to every request. Composition is manual unless the host can retrieve another instruction file. |
| **SDK or workflow orchestrator** | Register each file as a named instruction resource and expose the authenticated ScalePad MCP tools in the same run. | Resolve the requested skill, pass stable IDs and dates, and implement human approval immediately before `/qbr-apply` can reach write tools. |

Regardless of host:

- Expose the live ScalePad MCP tools and let the skill discover their current contracts.
- Pass a verified `client_id`, explicit review period, and timezone whenever available.
- Keep specialist skills read-only and isolate write access to `/qbr-apply`.
- Load only skills that can change the answer; unavailable optional skills reduce coverage rather than invalidating the review.
- Preserve the returned source IDs, links, timestamps, and unknowns through every handoff.

## Repository layout

```text
.
├── AGENTS.md
├── INSTALL.md
├── README.md
├── skill-kit.json
├── scripts/
│   └── validate-skills.py
└── skills/
    ├── qbr.md
    ├── qbr-prep.md
    ├── qbr-apply.md
    └── ...15 focused skills
```

`AGENTS.md` governs future maintenance. It is not uploaded as a runtime skill.

## How the skills fit together

```text
/qbr
 ├─ unclear path ───────────────> /qbr-wayfinder
 ├─ unresolved decisions ───────> /qbr-grill
 ├─ focused evidence ───────────> specialist reviews
 └─ routine preparation ────────> /qbr-prep
                                      │
                               /qbr-story
                                      │
                            reviewed plan only
                                      │
                                /qbr-apply

completed meeting ─────────────> /qbr-follow-up ──> /qbr-apply

connected and native sources
 └─ /connected-systems-review
     ├─ /psa-evidence ─────────┐
     ├─ /rmm-evidence ─────────┤
     ├─ /m365-evidence ────────┼─> specialist reviews ─> /qbr-prep
     └─ /saas-evidence ────────┘
```

The arrows describe possible handoffs, not a mandatory sequence. Load only the smallest set needed for the user's request.

## Skill catalog

| Skill | Use it when | Writes? |
| --- | --- | --- |
| [`/qbr`](skills/qbr.md) | The user wants QBR help but has not named the stage | No |
| [`/qbr-wayfinder`](skills/qbr-wayfinder.md) | The account story or investigation path is unclear | No |
| [`/qbr-grill`](skills/qbr-grill.md) | Facts exist but user judgment still blocks the plan | No |
| [`/qbr-prep`](skills/qbr-prep.md) | A complete evidence-backed QBR plan is needed | No |
| [`/connected-systems-review`](skills/connected-systems-review.md) | The agent must establish which native or direct sources can support the client story | No |
| [`/psa-evidence`](skills/psa-evidence.md) | Service friction, delivered work, documented scope, or follow-through needs evidence | No |
| [`/rmm-evidence`](skills/rmm-evidence.md) | Lifecycle exposure, resilience, monitoring coverage, or remediation needs evidence | No |
| [`/m365-evidence`](skills/m365-evidence.md) | Identity and access, license fit, adoption, or service disruption needs evidence | No |
| [`/saas-evidence`](skills/saas-evidence.md) | App utilization, license optimization, shadow IT, or shadow AI governance needs evidence | No |
| [`/client-context-review`](skills/client-context-review.md) | Documentation, stakeholders, prior decisions, and relationship context matter | No |
| [`/roadmap-review`](skills/roadmap-review.md) | Goals, initiatives, tasks, dependencies, and carry-forward work need review | No |
| [`/service-review`](skills/service-review.md) | Tickets, incidents, SLA evidence, or recurring service patterns need analysis | No |
| [`/security-review`](skills/security-review.md) | Security posture, controls, compliance, incidents, or accepted risks matter | No |
| [`/technology-review`](skills/technology-review.md) | Hardware, software, SaaS, warranty, or lifecycle evidence may affect the plan | No |
| [`/commercial-review`](skills/commercial-review.md) | Agreements, renewals, licensing, scope, estimates, or budget timing matter | No |
| [`/qbr-story`](skills/qbr-story.md) | Completed evidence needs a client-facing narrative and decision agenda | No |
| [`/qbr-follow-up`](skills/qbr-follow-up.md) | A completed meeting must become a decision log and proposed follow-through | No |
| [`/qbr-apply`](skills/qbr-apply.md) | A reviewed plan should be previewed and applied to ScalePad records | **Yes, after approval** |

## Composition contract

A skill-capable host may expose `load_skill` so one skill can load another by slash command with compact variables. The target skill must be available to the user on that turn.

Every composing skill follows the same rules:

- Inspect the live `load_skill` contract and current skill availability.
- Load only relevant specialists; optional skills never become hidden dependencies.
- Pass stable record IDs and compact context instead of copied raw payloads.
- Do not reload a completed skill unless new evidence materially changes its scope.
- Fall back to the narrowest supported read-only review and disclose reduced coverage when a specialist is unavailable.
- Never substitute an unrelated write operation for a missing capability.

## Source precedence

ScalePad is the aggregation layer. Evidence skills do not require a direct provider connector when native ScalePad objects already answer the question.

1. **Prefer native ScalePad records** with sufficient coverage and freshness.
2. **Use a direct provider connection** only for material source-native detail, configuration, or fresher state that ScalePad does not expose.
3. **Report the remaining gap** instead of failing the whole review or inventing a fallback.

| Evidence lane | Why it matters | Native ScalePad first | Direct provider adds |
| --- | --- | --- | --- |
| PSA | Recurring service friction, delivered value, documented scope, and follow-through | Tickets, agreements, linked initiatives and tasks | Deeper notes, projects, time, CSAT, or source-current state |
| RMM | Lifecycle and resilience risk, monitoring blind spots, and remediation evidence | Hardware, software, lifecycle, source lineage and available summaries | Live alerts, patch policy, monitoring and agent state |
| Microsoft 365 | Identity and access posture, license fit, adoption, and service-disruption context | Contacts, license assignments, supported activity and authentication enrichment, SaaS records | Tenant configuration, roles, policies, service health and source reports |
| SaaS Manager | Observed app utilization, license optimization, shadow IT, and shadow AI governance | Native license inventory, assignments, app utilization, lifecycle and approval data | No separate connector required; missing native operations remain an explicit gap |

Provider absence therefore reduces coverage; it does not erase useful evidence already aggregated by ScalePad.

Useful shared variables are:

| Variable | Meaning |
| --- | --- |
| `client_id` | Verified ScalePad client UUID |
| `client_name` | Display name for confirmation, never the sole write key |
| `review_period_start` | Beginning of the evidence period |
| `review_period_end` | End of the evidence period |
| `planning_horizon_end` | End of the forward roadmap, normally 12 months |
| `timezone` | Client or meeting timezone |
| `linked_organization_id` | Verified linked Lexful organization, when relevant |
| `psa_company_id` | Verified PSA company or client identifier |
| `rmm_client_id` | Verified RMM client, organization, or site identifier |
| `m365_tenant_id` | Verified Microsoft tenant GUID |
| `source_focus` | Narrow evidence question for a connected source |
| `previous_qbr_id` | Prior QBR meeting or deliverable ID |
| `evidence_limit` | Optional bound for focused retrieval |

Use the variables supported by the live skill and tool contracts; do not invent missing fields.

## Common specialist output

Specialist reviews return the same compact evidence envelope so `/qbr-prep` can synthesize them without rereading everything:

- **Coverage:** sources checked, unavailable, partial, and not applicable.
- **Findings:** observation, business implication, confidence, and evidence IDs or links.
- **Existing records:** native records that should be reused or referenced.
- **Decisions:** choices or approvals suggested by the evidence.
- **Proposed changes:** reuse, update, create, link, or no-change proposals—never executed by a review skill.
- **Unresolved inputs:** only material choices the user or client must make.

Every material statement should remain identifiable as an observation, inference, recommendation, or unknown.

Connected and native source adapters return this same envelope, but they stop at qualified observations and suggested questions. Domain reviews remain responsible for business interpretation and recommendations.

## Planning defaults

These are review heuristics, not quotas:

- One to three active client goals expressed as business outcomes.
- Three to five meaningful initiatives across a rolling 12-month roadmap.
- One to three active or decision-ready initiatives in the current quarter.
- No target task count: create a task only for a committed, owned action.
- One curated draft QBR deliverable rather than a data dump.
- Two or three consequential decisions or acknowledged deferrals.

Carry valid unfinished work forward. Reuse native records when they represent the same work, and keep proposals separate from approvals and commitments.

## Safety model

- Resolve one exact client and preserve tenant boundaries.
- Never fuzzy-match a record for a write.
- Discover live ScalePad operations and schemas before promising an action.
- Prefer native operations over raw API operations when both support the approved change.
- Treat `execute_write` as the commit point, never as a dry run.
- `/qbr-apply` must reconcile existing records, preview the exact batch, and wait for explicit approval.
- A material batch change requires a new preview.
- Read back every write and reconcile uncertain results before retrying.
- Stop dependent actions after a failed prerequisite.

The kit does not send invitations, publish or share deliverables, create PSA tickets, archive records, or delete records.

## Validate changes

Run the dependency-free validator before committing:

```bash
python3 scripts/validate-skills.py
```

It checks the manifest schema and exact install list, safe paths, command/frontmatter alignment, unique commands and paths, entry points, version parity, slash-command references, unfinished placeholders, and README catalog links. It does not replace a semantic review of safety or methodology.

## Example entry points

- “Prepare ACME's QBR for last quarter.” → `/qbr-prep`
- “This account is messy; figure out what we should review first.” → `/qbr-wayfinder`
- “Review their ticket history for patterns worth discussing.” → `/service-review`
- “What connected systems can contribute evidence for this client?” → `/connected-systems-review`
- “Pull trustworthy PSA, RMM, or Microsoft 365 evidence.” → the matching source adapter
- “Show observed SaaS utilization, license optimization opportunities, and shadow AI candidates for this client.” → `/saas-evidence`
- “Build the executive security portion of the QBR.” → `/security-review`
- “Help me decide which roadmap items make the cut.” → `/qbr-grill`
- “Turn these completed reviews into the client story.” → `/qbr-story`
- “Capture what we decided in today's meeting.” → `/qbr-follow-up`
- “Apply this reviewed plan to ScalePad.” → `/qbr-apply`, followed by its write preview and explicit approval.

## Inspiration

Thanks to [Matt Pocock](https://github.com/mattpocock/skills) for publicly sharing the composable skill patterns that inspired parts of `/qbr-wayfinder` and `/qbr-grill`. This kit is an independent adaptation built around MSP customer success practices and ScalePad workflows.

## Changelog

### 1.0.0 · 10 November 2026

- Initial release of the 18-skill ScalePad QBR Skill Kit.
- Includes semantic QBR preparation, specialist reviews, storytelling, follow-up, and an explicitly approved native ScalePad apply step.
- Includes read-only PSA, RMM, Microsoft 365, and SaaS evidence adapters that prefer ScalePad's aggregated records and preserve source meaning.
- Supports portable composition through the live `load_skill` contract when a host exposes it.
- Includes a validated `skill-kit.json` for deterministic, commit-pinned installation.
- Includes a host-neutral installation and update guide.
