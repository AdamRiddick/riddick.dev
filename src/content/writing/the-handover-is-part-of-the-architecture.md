---
title: "The handover is part of the architecture"
summary: "A system needs to remain understandable, operable and changeable after the person who shaped it has moved on."
topic: "Technical leadership"
takeaway: "Treat the team’s ability to own the system as part of the design. Share the reasoning, make responsibilities clear and test whether someone else can take the next decision."
draft: false
publicationMonth: "2026-09"
order: 1
sketch: "handover"
---

## The question after go-live

A system is in production. The main flows work, the team has a backlog and the project is beginning to look complete. Then somebody asks why one service owns a particular piece of data, or whether an integration can be changed without affecting another product.

If the useful answer lives with one person, part of the system is still difficult to hand over.

I think that is worth considering well before the end of a project. The team’s ability to understand and change what has been built should influence the design, alongside the requirements that are easier to put on a diagram.

## Leave the reasoning with the decision

A diagram can show that two components communicate. It rarely explains why a direct dependency was acceptable, which alternative was rejected or what would need to change before that choice should be revisited.

Those details matter when the next engineer comes to make a change. Without them, a reasonable compromise can look like an obvious mistake. Equally, a constraint that no longer applies can continue shaping the system because nobody is confident enough to question it.

Michael Nygard’s [original description of architecture decision records](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) is a useful starting point: keep the context and consequences close to the decision. I would keep the record small enough for someone to read while working through a real change.

The record does not need to reproduce every discussion. It needs to preserve what another person would need to make a sound judgement.

## Make ownership usable

Naming a team is a start. It still leaves some practical questions unanswered: who reviews a change that crosses a boundary, who responds when a dependency fails, and who can decide that an earlier compromise has become too expensive?

It helps to work through those questions with the people who will own the service. A responsibility that only exists in the architect’s explanation is unlikely to be clear during an incident.

Charity Majors makes the case for [thinking about ownership at team level](https://charity.wtf/p/in-praise-of-normal-engineers). The useful implication here is that the surrounding practices should help the team act together. Knowledge sharing, reviews and operational responsibilities deserve attention alongside the code.

There will still be specialists. The aim is to make their expertise available to the team without making every ordinary decision depend on their presence.

## Use the next change as a test

A handover meeting can confirm that information was presented. A small, real change can reveal whether the information is usable.

Ask someone who did not make the original decision to explain the boundary, propose a change and identify what they would check before releasing it. Give them access to the material the team would normally use. Notice where they need an explanation that has never been written down or discussed beyond a small group.

This should be a collaborative exercise. If the route through the system is difficult to explain, that is useful feedback on the design and its supporting context. It is not a test of whether somebody was paying attention in the meeting.

Some gaps will call for a clearer explanation. Others may point to an unnecessary dependency, unclear authority or a design that is harder to operate than it first appeared.

## A few questions worth leaving behind

Before calling the work complete, I would want the team to be able to answer:

- Which constraints shaped the current design, and which might change?
- Where can we make a change independently, and where do we need to coordinate?
- What would tell us that the system is failing to do its job?
- Who can make the next decision, and what evidence should they use?

The depth of the answers should fit the system. A small internal tool does not need the same supporting material as a service used across several products.

For me, seeing work through includes making the next change easier for the people who will be there to make it. A handover becomes more useful when it confirms an ownership model that the team has already been practising.
