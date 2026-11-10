---
name: qbr
description: Route a QBR request to the smallest available ScalePad skill for discovery, preparation, decision-making, application, or follow-up. Use when the user asks for QBR help but has not named a specific stage.
---

# QBR Router

Choose the smallest workflow that completes the user's current QBR job. This skill routes work; it does not duplicate specialist analysis or mutate records.

## Establish the request

Resolve the current stage from the user's words and available context:

- **Prepare:** gather evidence and produce a reviewed plan.
- **Find the path:** the account is messy, the objective is unclear, or several investigations may be needed.
- **Make decisions:** facts exist, but material choices remain unresolved.
- **Review one domain:** the user asks specifically about roadmap, service, security, technology, commercial, or client context.
- **Review connected evidence:** the user asks what a PSA, RMM, or Microsoft 365 connection can contribute.
- **Tell the story:** evidence is complete and needs a client-facing narrative.
- **Apply:** the user has reviewed a plan and wants ScalePad records changed.
- **Follow up:** a QBR occurred and decisions, owners, and next steps must be captured.

If the client or period is ambiguous and the next skill cannot resolve it safely, ask one concise question. Do not turn optional refinements into blockers.

## Route through available skills

When `load_skill` is advertised, inspect the skills available to the user on this turn. Use the live contract and pass the selected slash command plus relevant variables. Never assume an unavailable skill can be loaded.

Do not reload a skill already completed for the current request unless new evidence materially changes its scope. Preserve its result by stable IDs and a compact handoff so routing cannot loop.

Prefer this routing:

| Need | Skill |
| --- | --- |
| Routine evidence-backed preparation | `/qbr-prep` |
| Ambiguous or complex QBR path | `/qbr-wayfinder` |
| Unresolved judgment calls | `/qbr-grill` |
| Connected-system discovery and source coverage | `/connected-systems-review` |
| PSA tickets, projects, agreements, and service evidence | `/psa-evidence` |
| RMM device, monitoring, alert, and patch evidence | `/rmm-evidence` |
| Microsoft 365 identity, licensing, service-health, and posture evidence | `/m365-evidence` |
| ScalePad SaaS licenses, assignments, app usage, lifecycle, and approval evidence | `/saas-evidence` |
| Client documents and relationship context | `/client-context-review` |
| Goals, initiatives, roadmap, and tasks | `/roadmap-review` |
| Tickets, incidents, and support patterns | `/service-review` |
| Security, compliance, controls, and risk | `/security-review` |
| Assets, software, lifecycle, and technical estate | `/technology-review` |
| Agreements, renewals, licensing, and budget | `/commercial-review` |
| Executive narrative and decision agenda | `/qbr-story` |
| Approved native ScalePad writes | `/qbr-apply` |
| Post-meeting decisions and actions | `/qbr-follow-up` |

Pass stable scope when known: `client_id`, `client_name`, `review_period_start`, `review_period_end`, `planning_horizon_end`, `timezone`, `linked_organization_id`, verified external source IDs, `source_focus`, and IDs or links for prior evidence. Do not pass large copied payloads when a stable record ID or context pointer will do.

If the best specialist is unavailable, use the closest available read tools for a narrow fallback and disclose the missing coverage. Do not substitute an unrelated write tool.

## Safety boundary

All routes are read-only except `/qbr-apply`. Loading `/qbr-apply` does not grant write approval: that skill must reconcile records, preview the exact batch, and receive explicit approval.

Never infer permission to send invitations, publish or share deliverables, create PSA tickets, archive, or delete records.

## Finish

Report the route selected, resolved client and period, any specialist that could not be loaded, and the resulting artifact or next decision. Do not continue into another stage unless it is needed to complete the user's request.
