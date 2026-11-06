---
title: "A cloud saving is only a saving if you can still recover"
summary: "Cloud costs and recovery expectations belong in the same conversation. A smaller bill is only one part of the result."
topic: "Operations & FinOps"
takeaway: "Review a proposed saving against the service’s recovery needs. Make the compromise explicit, agree who owns it and check that the recovery path still works."
draft: false
publicationMonth: "2026-07"
order: 2
sketch: "recovery"
---

## Start with what the service needs

A cloud bill gives you a useful place to start looking for waste. It does not explain which resources are carrying an operational responsibility that is easy to overlook.

An apparently quiet environment might be part of a recovery plan. A backup policy might exist because a particular customer obligation requires it. Equally, either could be an expensive arrangement that nobody has revisited for years.

I would want to understand the responsibility before deciding whether the cost is justified. That gives engineering, operations and the business something more useful to discuss than whether a resource looks underused.

## Put the expectations on the table

Two recovery questions help establish the context: how long can the business tolerate the service being unavailable, and how much recent data can it afford to lose?

These correspond to recovery time and recovery point objectives. Microsoft’s [disaster recovery guidance](https://learn.microsoft.com/en-us/azure/well-architected/reliability/disaster-recovery) connects those objectives to business impact and calls for tested recovery plans covering the system and its dependencies.

The practical step is to make sure the people proposing a saving and the people responsible for the service are working from the same expectations. Otherwise, they may be evaluating two different versions of the problem.

## Name the compromise

I find it more useful to describe a cost proposal as a decision with consequences. What becomes cheaper, what work changes and what must remain true for the proposal to be acceptable?

For example, imagine a team considering a smaller standby environment. The useful discussion would include the work needed to bring it into service, who can perform that work and what the team would need to demonstrate before relying on it. This is an illustrative decision, not an account of a particular deployment.

A short comparison can keep the discussion grounded:

| Question                      | What the decision needs                                            |
| ----------------------------- | ------------------------------------------------------------------ |
| What expense are we reducing? | A clear account of the recurring cost and the reason it exists.    |
| What responsibility changes?  | The operational work, dependency or risk affected by the proposal. |
| How will we judge the result? | Cost evidence alongside agreed service and recovery checks.        |
| Who carries it forward?       | A team with the context and authority to maintain the choice.      |

## Keep the check after the saving

A forecast can make a proposal worth trying. The result still needs to be checked after the change.

That includes whether the expected saving appeared and whether the team can still carry out the operational work the design assumes. If the arrangement needs additional manual steps, those steps belong in the assessment too. They use time and need an owner even when they do not appear as a separate line on the cloud bill.

The right balance will differ by workload. Some services can tolerate a longer interruption. Others justify a greater investment in readiness. I would be comfortable with either outcome when the requirement is understood, the compromise is deliberate and the people running the service can explain it.

That makes FinOps part of an ongoing engineering conversation. The useful result is a service whose cost and operational commitments make sense together.
