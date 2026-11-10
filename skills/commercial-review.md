---
name: commercial-review
description: Review one client's agreements, renewals, scope, licensing, proposals, budget timing, and commercial dependencies for a QBR. Use to surface decisions without confusing estimates, approvals, commitments, and actual spend. Read-only.
---

# Commercial Review

Identify commercial dates, scope constraints, licensing signals, and investment decisions that materially shape the QBR and roadmap.

## Resolve scope

Resolve one exact client, review period, planning horizon, and currency context. Use verified client and record IDs. Never merge agreements or financial evidence by fuzzy organization name.

## Discover the live read surface

Prefer advertised direct reads for agreements, software, SaaS licenses and management, goals, initiatives, tasks, meetings, notes, deliverables, and client records. Use connected documentation only when the exact client linkage is verified. Use `search_operations` plus `execute_read` for uncommon reads after discovering the live contract. Never call `execute_write`.

When source evidence is material, consume a completed `/psa-evidence` slice for agreements, projects, or service scope; `/m365-evidence` for direct Microsoft licensing or supported adoption signals; and `/saas-evidence` for ScalePad SaaS license inventory or tracked app usage. If needed and available, load the relevant adapter through the live `load_skill` contract using verified IDs. Never elevate estimates, assignments, tracked usage, or free entitlements into commitments, purchased seats, or actual spend.

Record source authority, effective dates, renewal dates, billing cadence, currency, tax treatment when relevant, coverage, and freshness.

## Review commercial evidence

Look for:

- renewals, notice windows, expirations, or price changes inside the planning horizon;
- agreement scope that enables, limits, or conflicts with proposed work;
- proposals or roadmap estimates awaiting a decision;
- licensing waste, under-adoption, overlapping SaaS tools, overage, or ownership gaps supported by source data;
- budget timing and dependencies that affect roadmap sequencing;
- commitments from prior QBRs that lack an approved commercial path;
- client value delivered that should be visible before a renewal decision.

Keep these states explicit and separate:

- **Estimate:** an indicative amount or range.
- **Proposal:** an offer awaiting acceptance.
- **Approved budget:** permission to plan spending, not proof of purchase.
- **Commitment:** an accepted contractual or purchase obligation.
- **Actual:** an incurred, invoiced, or paid amount from an authoritative source.

Do not calculate ROI, savings, forecast, or total contract value without sufficient inputs and stated assumptions. Do not treat assigned licenses as active usage or a roadmap estimate as committed spend.

## Translate evidence into decisions

Connect each commercial signal to a client outcome, deadline, and roadmap dependency. Recommend the smallest decision needed now: approve, defer, obtain a quote, confirm scope, choose a cadence, assign an owner, or acknowledge that no action is needed.

Financial proposals remain separate from operational commitments until explicitly approved. Undecided purchases do not become tasks phrased as if they will occur.

## Return the evidence slice

### Coverage

Sources, date and currency scope, authoritative records, incomplete data, and assumptions.

### Findings

Observation, commercial or business implication, timing, confidence, and evidence IDs or links.

### Existing records

Relevant agreements, licenses, goals, initiatives, tasks, meetings, proposals, and deliverables.

### Decisions

Decision-ready renewal, scope, licensing, or investment choices with recommendation and trade-off.

### Proposed changes

Potential roadmap or follow-through changes for `/qbr-prep`; do not execute them.

### Unresolved inputs

Material currency, cadence, price, approval, scope, ownership, or source-authority questions.
