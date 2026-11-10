---
name: qbr-grill
description: Resolve the judgment calls blocking a QBR by asking one high-leverage question at a time, after independently checking available facts. Use for roadmap priorities, risk acceptance, ownership, sequencing, or scope decisions. Read-only.
---

# QBR Grill

Turn unresolved QBR choices into a short decision path. Investigate facts independently; ask the user only for decisions that require their judgment.

## Start with the decision tree

Accept unresolved inputs from `/qbr-wayfinder`, `/qbr-prep`, or the user's request. For each candidate decision, record:

- the decision to make;
- why it matters now;
- viable options;
- evidence already known;
- missing facts;
- dependent decisions or proposed records;
- the default recommendation and its trade-off.

Remove questions that are merely factual, cosmetic, duplicated, or irrelevant to the requested outcome.

## Resolve facts before asking

Use available read tools or load a relevant available specialist through the live `load_skill` contract. Pass the exact client, review period, and stable evidence pointers. Never ask the user to look up something the connected systems can answer.

Do not reload a completed specialist or return to an earlier skill merely to restate its result. New evidence must materially change the decision before a branch is reopened.

Do not invent status, ownership, dates, budgets, risk tolerance, or client intent. Distinguish missing evidence from a genuine decision.

## Ask one question at a time

Choose the unblocked question that resolves the most downstream uncertainty. Include only enough context to decide.

Use this shape:

> ❓ **[Short decision title]**
>
> [One precise question with only the context needed to answer it.]
>
> ➡️ **Recommendation:** Yes — [recommended answer and why].
>
> ⚖️ **Trade-off:** [most important consequence].
>
> **Agree?**

Word the question so a simple “yes” accepts the recommendation. Offer alternatives only when they are genuinely viable. End with “Agree?” and wait; never place another question beneath it.

When the user answers clearly, begin the next response with:

> ✅ **Settled:** [short statement of the decision].
>
> **Next:**

Then present the next single decision in the same format. If the user rejects the recommendation but provides a clear alternative, settle their decision without arguing. If their answer changes the tree but is ambiguous, ask one focused follow-up instead of declaring it settled.

Do not ask a batch of questions, and do not reopen settled decisions unless new evidence materially changes them. When no frontier remains, acknowledge the final decision and say that all material decisions are settled; do not print an empty “Next.”

After each answer:

1. Acknowledge the settled decision in one line and record its rationale.
2. Mark which downstream questions are now unblocked or obsolete.
3. Resolve any newly factual questions with tools.
4. Ask the next highest-leverage decision.

## Guardrails

This skill never writes records. Agreement on a decision is not approval to apply it in ScalePad. Financial estimates remain proposals until the user confirms them as commitments. Security risks require an explicit owner and disposition; silence is not acceptance.

If the user delegates a decision, use the stated constraints and document the assumption. If no safe recommendation exists, say exactly what evidence is missing.

## Completion and handoff

Finish when no unresolved user decision materially blocks the QBR narrative or proposed record set. Return a decision ledger containing:

- decision and rationale;
- chosen option;
- decision owner;
- affected goals, initiatives, tasks, risks, or deliverables;
- evidence IDs or links;
- remaining non-blocking unknowns.

Load `/qbr-prep` or `/qbr-wayfinder` only when it is available and needed to continue the user's requested workflow. Otherwise return the ledger as the handoff.
