---
title: "When the application becomes multi-tenant before the database does"
summary: "A shared application and separate tenant databases can coexist. The important work is making the boundary explicit."
topic: "Architecture"
takeaway: "Choose the application and data boundaries deliberately. Make tenant context, routing and operational responsibility clear across every path, including background work and reporting."
draft: false
publicationMonth: "2026-06"
order: 3
sketch: "tenancy"
---

## Two decisions at different layers

A modernisation programme can bring several products or customer environments behind a shared application while their data remains in separate databases. The application and storage models do not have to change at the same time.

That can be a reasonable stage in a longer transition. It can also be a deliberate operating model. The question I would start with is what the arrangement needs to make explicit for the teams building and running it.

This note considers the design questions in general. It is not a description of a particular employer’s implementation or a complete security design.

## Be precise about what is shared

A statement such as “the platform is multi-tenant” leaves a lot of room for misunderstanding. It helps to describe the boundary at each layer: which application components are shared, where tenant context is established and how the data stores are separated.

Microsoft’s [multitenant storage guidance](https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/approaches/storage-data) describes different approaches to sharing and isolating data. It also highlights operational concerns such as tenant-specific requirements, maintenance, monitoring, reporting and schema changes.

A database-per-tenant arrangement therefore deserves an explicit operating plan as well as an application diagram.

## Follow the request beyond the front door

A useful design review follows a request through the system. Where does the application establish its tenant context? How is the caller’s access checked? How is the correct data destination selected, and what prevents a later component from silently replacing that context?

I would follow the same reasoning through work that does not arrive as an ordinary web request. A scheduled task, an integration or a reporting process still needs a clear account of whose data it can reach and why.

An illustrative review might use this small set of prompts:

- **Context:** where is the tenant established and what makes that information trustworthy?
- **Access:** what checks connect the authenticated caller to that tenant and operation?
- **Routing:** which component is responsible for selecting the destination?
- **Failure:** what happens when context is absent, invalid or inconsistent?
- **Verification:** how will tests demonstrate that one tenant cannot access another tenant’s data?

These are questions to resolve with the implementation and its security requirements. A tenant identifier attached to a request is not, by itself, proof that access is authorised.

## Give the operating model equal attention

Separate databases can make some boundaries easier to describe while creating coordination work elsewhere. Teams still need an approach to schema changes, failures affecting individual tenants and reporting that spans the estate.

I would want the people responsible for those activities involved while the model is being chosen. An architecture that assumes every database can be updated together may be difficult to operate if customer constraints require something else.

The useful record explains which responsibilities are shared, which remain tenant-specific and how the teams will manage the difference.

## Keep the next step open

A hybrid arrangement should be understandable on its own terms. It does not need to be presented as an unfinished version of a supposedly inevitable destination.

If the reasons for retaining separate stores remain valid, the model may continue to fit. If the operational burden changes or customer requirements move, there should be enough context to reassess it.

For me, that is where a modernisation plan earns its place: it gives the teams a clear next step without asking them to pretend the whole estate can change at once.
