---
title: "The work between ‘deployed’ and ‘done’"
summary: "A successful deployment is an important milestone. Closing the change takes evidence that it works in practice and that the remaining responsibilities are clear."
topic: "Technical leadership"
takeaway: "Agree what completion needs to mean before release. Verify the outcome in use, make the operating responsibilities workable, and give anything left open an owner and a next decision."
draft: false
publicationMonth: "2026-04"
order: 4
sketch: "completion"
---

## The release has gone through

The deployment has finished. The checks are green, the application is responding and the team can move on to the next thing. There may still be a scheduled job that has not run, a support team waiting for an explanation, or an old integration that nobody has quite agreed to switch off.

Each of those can look small beside the work it took to get the change into production. Together, they affect whether it is ready to become an ordinary part of the service.

I would want the team to agree what evidence closes the change while there is still time to plan for it. Some of that evidence comes from testing before release. Some only becomes available when the change meets real use. Making that distinction early gives the remaining work a place in the delivery plan.

## Check the outcome people needed

Consider an illustrative change to a reporting service. A new background process accepts requests and generates reports. The deployment checks confirm that it starts and accepts a request. Those are useful checks, but the customer still needs to receive a complete, accurate report within the expected time.

If the process accepts work faster than it completes it, the application can appear healthy while customers wait. If a report is generated but never reaches its destination, the processing step has succeeded while the customer’s task remains unfinished.

For this change, I would want to follow the work far enough to see that useful outcome. That could mean checking completion, delivery and failure behaviour through appropriate service telemetry and a controlled verification, without exposing customer report contents in logs.

The same reasoning applies to a migration, an authentication change or a new internal tool. What should become possible, safer or easier because this work exists? The answer helps decide what to observe after deployment. It also prevents a convenient technical signal from quietly becoming the definition of success.

Google’s [guidance on canary releases](https://sre.google/workbook/canarying-releases/) describes evaluating a limited deployment before deciding whether to extend it. That provides an early opportunity to examine a change under real conditions. A short observation window still needs to be considered alongside work that runs less often, such as a scheduled reporting cycle.

## Make the operating work visible

Some of the questions after release belong to engineering. Others need product, support or operations colleagues involved. Who can tell a customer what changed? What should someone do when a report is delayed? Which team can decide whether to pause the new process?

A name on a service catalogue helps, but the people carrying that responsibility also need access, useful signals and a practical route to take action. A runbook that assumes permissions the responding team does not have leaves the responsibility unfinished.

Google’s [reliable product launches chapter](https://sre.google/sre-book/reliable-product-launches/) treats launch preparation as coordination across teams, supported by checks for common risks. The useful idea for a smaller team is to bring the right people into the work early. The amount of process should fit the change.

For the reporting example, that might be a short session with the people who will handle delayed or failed work. Walk through how they would recognise the problem and what they can safely do. If they need an engineer to explain an undocumented step, there is something concrete to improve before the change is closed.

## Give the remaining work a destination

Releases often leave temporary arrangements behind: a feature flag, an extra dashboard, an old processing path or a manual check. Some are sensible protections during a transition. They need a reason to remain and a condition for removal.

I would distinguish between work required to close the current change, a deliberate ongoing responsibility, and an improvement that can be considered later. Without that distinction, the team can end up carrying every loose end as an indefinite promise.

For example, retaining the old reporting path until the new process has completed a representative workload may be reasonable. The plan should say what evidence allows it to be retired, who makes that decision and what happens if the evidence is inconclusive. “Remove after go-live” leaves too much for someone else to reconstruct.

This also matters for recovery. Returning to the previous application version may be possible while undoing data changes is much harder. The response available after a release needs to match the state the system is now in. A recovery plan deserves another look when the change alters those assumptions.

## Agree how to close the change

A small completion record can make the discussion easier. For the illustrative reporting change, it might look like this:

| Question                                   | Evidence to review                                                                                      |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| Is the intended outcome working?           | A representative report completes accurately and reaches its destination within the agreed expectation. |
| Can the team operate it?                   | Delayed and failed work is visible, and the responding team can use the agreed actions.                 |
| Is the response to failure still credible? | The team has checked the recovery options against the current application and data state.               |
| What remains?                              | The old path and temporary checks have a removal condition, or an explicit reason to continue.          |

Those answers should be shaped with the people who need them. They need not become another approval board or a document nobody uses. For a routine, reversible change, existing automated checks and normal service monitoring may already provide enough evidence.

A change that affects stored data, crosses several teams or only shows its behaviour at the end of a business cycle may need more. Agree which risks require waiting for that evidence and which can be accepted with a clear follow-up. A fixed observation period for every release would ignore those differences.

There also needs to be a point at which the delivery team can move on. Normal service ownership should take over explicitly; it should not depend on the original project remaining permanently available. Improvements can stay in the backlog without keeping the whole change open, provided they are not concealing an unmet commitment or an unresolved risk that nobody has accepted.

Before closing the work, I would ask the team to look at what is still being held together by temporary checks, personal knowledge or an expectation that somebody will return to it. Decide which of those needs resolving now, which belongs in normal operation, and which needs a named follow-up. That gives the next team a clearer starting point and the current team a credible place to finish.
