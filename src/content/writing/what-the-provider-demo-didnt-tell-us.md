---
title: "What the provider demo didn’t tell us"
summary: "An implementation expected to take weeks took months. The gap was in what our company had agreed to own, and what the platform actually provided."
topic: "Technical leadership"
takeaway: "Before signing, walk through the workflows you need under the commercial model you’re buying. Make clear who supplies, builds and runs each part before agreeing a launch date."
draft: false
publicationMonth: "2026-11"
order: 6
sketch: "provider"
---

On one project, we chose a platform that we understood would cover the workflow end to end. We expected the implementation to take a couple of weeks. When engineering got into the detail, we found that our company would act as the merchant of record and that we still had to build the software to manage that arrangement. What we’d planned as a short integration became months of work.

The question I’d ask before making that decision again is simple. Can the provider show us the full workflow under the arrangement we’re about to buy, and point out where our work starts? We’d understood the scope of the platform one way when we planned the launch. The engineers had to work with a different scope once implementation began.

## The work that came back to us

There were two responsibilities to make clear. The first was who would act as the merchant of record for the transactions. The second was who would provide the software to manage the arrangement. In our case, both sat with our company. The second was the part the engineering team had to build, and it hadn’t been allowed for in the original estimate.

Another provider covered the functionality we needed. That would have reduced the amount we had to build and given us a better chance of getting to market sooner. We’d still have needed to integrate the platform and verify that it worked for us. The difference was whether the launch depended on our team delivering a substantial piece of software first.

Engineering hadn’t been involved early enough to test that assumption. I’d bring them in while the shortlist and terms were still open, with product and commercial colleagues in the same conversation. Product can say which workflows customers need at launch. Commercial can confirm what’s included in the offer. Engineering can work out what remains to build and run. The estimate depends on all three answers.

## What the delay cost

The extra build took engineering time. The launch also missed early sales windows, and the income forecast against those windows didn’t materialise. Those are different effects of the same decision. One is the cost of delivering work the team hadn’t planned. The other is the commercial effect of being ready after the dates the forecast depended on.

That distinction matters when comparing providers. If a date can move without much consequence, building a missing capability may be a reasonable trade. It might give the team useful control over a workflow they expect to change. If the date is tied to a sales window, the same piece of work can change the case for buying the platform. I’d want that dependency visible before anyone uses the delivery estimate in a forecast.

## What I’d ask to see before signing

I’d give each shortlisted provider the same representative workflow and ask them to run it under the proposed terms. Start with what the customer needs to do and follow it through to the point where the people operating the service can see that it’s complete. Include one awkward case that matters to the business. A walkthrough can be narrow and still tell you a great deal, provided it includes the step most likely to leave you with work you haven’t estimated.

For each step I’d write down what the provider can show, what our team would have to build or configure, and who would own it in production. If a feature depends on a different commercial arrangement or the provider can only describe how it might work, I’d keep that as an open question in the estimate. A short technical trial can be worth the time if it resolves a question that could move the launch by months.

On this project, I’d have started with the merchant-of-record workflow. If both providers could show where their responsibility ended and ours began, we could have compared the cost and timing of the work still on our side before committing to a date.
