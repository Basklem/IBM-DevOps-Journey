# Introduction to Agile Development and Scrum — Notes

## Key Takeaways
- **Agile** is an iterative, feedback-driven approach to delivering value quickly — small increments, frequent customer feedback, constant adjustment (instead of planning a year out).
- The **Agile Manifesto** values individuals/interactions, working software, customer collaboration, and responding to change over processes/tools, documentation, contracts, and rigid plans — the right-side items still matter, just less.
- **Waterfall** (Requirements → Design → Code → Integrate → Test → Deploy) makes change expensive and delays feedback to the very end. **Extreme Programming (XP)** and **Kanban** were early influences that gave Agile its iterative loops, fast feedback, and workflow/WIP visualization.
- Working Agile day-to-day means small batches, **MVPs** for learning (not partial delivery), **BDD** (outside-in) and **TDD** (inside-out) testing, and pair programming. Core rule: build what's needed, not just what was planned.
- **Scrum** is a prescriptive methodology for practicing Agile: fixed-length sprints, three roles (**product owner**, **Scrum master**, **Scrum team**), three artifacts, five events.
- Product owner owns vision/priorities/acceptance; Scrum master coaches and removes impediments (no management authority); the self-organizing Scrum team pulls and delivers the work itself.
- **Scrum vs. Kanban**: fixed sprints vs. continuous flow, velocity vs. cycle time, locked sprint scope vs. continuous change.
- **Conway's Law**: org structure shapes system architecture — teams should be small, autonomous, mission-aligned, and end-to-end responsible for their area.
- Agile only pays off if the *entire* org (including Ops) adopts it — otherwise you get **Water-Scrum-Fall** (Waterfall front/back, iterative middle). Iterating on a fixed plan isn't Agile unless you're deploying, getting real feedback, and responding to change.
- Don't decide everything at the point you know the least (project start) — plan iteratively and re-estimate from each new vantage point.
- Renaming people into Agile roles without training/retooling fails: product owner ≠ product manager, Scrum master ≠ project manager, Scrum team ≠ just devs. The mindset shift has to come from upper management.
- Tools don't make you Agile — mindset first. A Kanban board (e.g., ZenHub) tracks work left to right: New Issues → Icebox → Product Backlog → Sprint Backlog → In Progress → Review/QA → Done (= dev-done, not yet accepted).
- A good user story: **As a [role], I need [function], so that [value]** — plus assumptions and Gherkin (Given/When/Then) acceptance criteria — and follows **INVEST**. Anything too big for one sprint becomes an epic.
- **Story points** are abstract, relative estimates (effort + complexity + uncertainty) on a loose Fibonacci scale — agree on what a "medium" is, size everything else against it. Never map points to wall-clock time.
- The product backlog is a ranked list of unimplemented stories — only the top needs precise ranking and full detail. **Backlog refinement** happens every sprint: triage new issues, rank, and keep ~2 sprints' worth sprint-ready.
- **Technical debt** (refactoring, environments, patches — work the customer doesn't perceive as value) should be labeled and paid down a bit every sprint.
- **Sprint planning**: the PO presents the goal, the dev team builds the sprint backlog by pulling top stories and stopping at their **velocity** — which is per-team and never comparable across teams.
- Daily execution: one story per person at a time, pulled strictly in priority order. The **daily stand-up** is a strict 15-minute sync (not a status meeting) around three questions — yesterday, today, blockers.
- **Burndown charts** track points remaining vs. time to forecast whether a sprint will land. The **sprint review** is a stakeholder demo where feedback becomes new backlog items. The **sprint retrospective** (no PO) reflects on what to keep, stop, and change.
- Closing a sprint: never silently roll unfinished work forward — close the story (even if incomplete) so **velocity** stays accurate, then write a new story for the remainder.
- Track **actionable metrics** (mean lead time, release frequency, change failure rate, MTTR), not vanity metrics. Watch for Scrum anti-patterns: no/multiple product owners, oversized or non-dedicated teams, siloed or non-self-managing teams.

---

## Notes

### Module 1: Introduction to Agile and Scrum

#### Section 1: Introduction to Agile Philosophy

**Agile Principles**
- **Agile**: an iterative approach to project management — plan in small increments, get customer feedback, adjust continuously (not a year-long plan).
- Defining chain: adaptive planning → evolutionary development → **early delivery** → continuous improvement → responsiveness to change. Early delivery is the key differentiator — iterating without shipping to the customer isn't Agile.
- **Agile Manifesto** — we value:
  - Individuals and interactions *over* processes and tools
  - Working software *over* comprehensive documentation
  - Customer collaboration *over* contract negotiation
  - Responding to change *over* following a plan
  - The right-side items still matter — Agile just values the left side *more*.
- Agile teams are small, co-located, cross-functional, self-organizing, self-managing.
- **Key takeaway**: build what is needed, not what was planned — needs change, so replan instead of sticking to the original.

**Methodologies Overview**
- **Waterfall**: sequential phases (Requirements → Design → Code → Integrate → Test → Deploy) with hard entrance/exit criteria — very difficult to go back once you've moved on ("waterfall" = can't swim upstream).
  - Problems: no provision for change, no intermediate delivery, costly late-stage mistakes, long lead times, siloed teams unaware of their impact on each other, and Ops (who knows the code least) is stuck running it in production.
- **Extreme Programming (XP)**: Kent Beck, 1996; one of the first Agile methods. Nested iteration loops (release in months → weeks → days → daily stand-ups → hours → minutes → seconds) get progressively faster feedback.
  - XP values: simplicity (no over-engineering), communication, feedback, respect (no hierarchy), courage (honest, unpadded estimates).
- **Kanban**: from Japanese manufacturing ("billboard sign") — continuous flow, cards tracking work station to station.
  - Core principles: visualize the workflow, limit work in progress (WIP), manage/enhance the flow, make policies explicit (shared "definition of done"), continuously improve.
  - Agile borrows Kanban boards, WIP limits, and "definition of done" directly from this.

**Working Agile**
- Five practices: small batches, MVPs, BDD, TDD, pair programming.
- **Small batches** (lean manufacturing): batching delays your first inspectable result and delays finding defects. Single-piece flow surfaces defects almost immediately. Smaller batches = faster feedback = less waste.
- **Minimum Viable Product (MVP)**: NOT "phase one" or a first beta — it's the minimal thing built to test a hypothesis and generate learning. Decide to pivot or persevere after each one.
  - Car/skateboard example: delivering a wheel → chassis → car pieces gives the customer exactly what was *planned* but not what they wanted. Delivering a skateboard → steerable skateboard → motorized version (a complete product each time) lets the customer steer the outcome toward what they actually *want*.
- **Behavior Driven Development (BDD)**: tests outside-in, usually at the integration/UI level — does the system behave as the customer expects? Uses Gherkin so devs and stakeholders share one language: "As a [role], I need [function], so that [value]" + Given/When/Then. **BDD = building the right thing.**
- **Test Driven Development (TDD)**: tests inside-out, at the unit level. Workflow: write a failing test (Red) → write just enough code to pass (Green) → refactor (Refactor). **TDD = building the thing right.**
- **Pair Programming**: two programmers, one writes and one reviews/thinks, swapping roles roughly every 20 minutes. Cheaper to catch bugs while writing than in production; also great for mentorship (senior+junior) or knowledge transfer.

#### Section 2: Introduction to Scrum Methodology

**Scrum Overview**
- **Agile is a philosophy** (not prescriptive); **Scrum is a methodology** (prescriptive) for working in an agile fashion.
- **Scrum**: a management framework for incremental product development — small, cross-functional, self-managing teams; structure via roles/rules/artifacts; fixed-length **sprints**; goal is a potentially shippable increment every sprint.
- "Easy to understand, difficult to master" — bring in someone experienced if the team is new to it.
- **Sprint** = one iteration through design/code/test/deploy, with a clear goal. Typical length: two weeks (four is too long; one is a bit too fast).
- Process flow: product backlog → backlog refinement (grooming) → sprint planning (produces the sprint backlog) → two-week sprint with daily stand-up (see Module 3) → shippable increment. Cycle repeats: plan → build → deploy → get feedback → replan.

**The 3 Roles of Scrum**
- **Product Owner**: has the vision, decides pivot/persevere, liaison between team and stakeholders. ("Product manager" is a job title; "product owner" is a Scrum role — not always the same person.) Articulates the vision, is the final arbiter of requirements, continuously reprioritizes/grooms the backlog, and solely decides whether to accept/ship or reject each increment.
- **Scrum Master**: facilitates Scrum, most Scrum-knowledgeable person on the team (especially important on new teams). Coaches, fosters self-organization, shields the team from outside interference. Top daily priority: resolve impediments ("give it to me, I'll fix it" — not "what will *you* do about it"). Enforces timeboxes, tracks empirical data/burndown, and has **no management authority** so the team can confide in them freely.
- **Scrum Team**: cross-functional (devs, testers, BAs, domain experts, ops — not just engineers). Self-organizing/self-managing — nobody assigns work, the team pulls it. Ideal size 7 ± 2 (some say 5 ± 2). Best co-located; if dispersed, keep ≥2 people per time zone. Dedicated, long-term, full-time — not split across projects. Negotiates commitments with the PO one sprint at a time, with full autonomy over *how* to reach them.

**Artifacts, Events, and Benefits**
- **Three artifacts**: product backlog (everything not yet done), sprint backlog (next two weeks' subset), done increment (completed work at sprint end).
- **Five events**: sprint planning → daily stand-up → the sprint → sprint review (demo) → sprint retrospective (reflect and improve — the most important for continuous improvement).
- **Benefits**: higher productivity, better quality (via BDD/TDD), reduced time to market, higher stakeholder satisfaction, better team dynamics, happier employees.
- **Scrum vs. Kanban**: fixed sprints vs. continuous flow; release-at-sprint-end vs. continuous delivery; defined roles vs. none; velocity vs. cycle time; locked sprint scope vs. continuous change. (Scrum teams often still use a Kanban *board* without the full Kanban process.)

#### Section 3: Organizing for Success

**Organizational Impact of Agile**
- Org structure is critical to Agile success — you usually can't just relabel existing teams "Agile"; they may need to be reorganized.
- **Conway's Law** (Melvin Conway, 1968): a system's design mirrors the org's communication structure. (4 teams building a compiler → a 4-pass compiler; UI/app/DB teams → a 3-tier architecture.)
- How teams should be organized: loosely coupled to each other but tightly aligned around one application; own a business-area mission (e.g., order team, accounts team, cart team, not one giant monolith team); end-to-end responsible (build/run/debug in production); long-term, not shuffled between projects.
- **Autonomy** is motivating and fast — decisions happen locally instead of waiting on approval from above.
- **"Wall of Confusion"** (Andrew Clay Shafer): Dev is measured on change, Ops on stability — opposed incentives that stall delivery no matter how "Agile" development is (real example: a February-ready deployment didn't ship until September because of Ops ticketing delays).
- Agile and DevOps goals align closely (faster delivery/time to market, responsiveness/business alignment, quality/productivity) — adopting DevOps helps Ops become just as agile as Dev.

**Mistaking Iterative Development for Agile**
- Common pitfall: **Water-Scrum-Fall** — a "fuzzy front end" of Waterfall-style upfront planning, an iterative middle that never deploys or gets real feedback, and a slow "last mile" deployment because it's the first time anything's been integrated.
- What Agile is **not**: not just an iterative/mini-Waterfall lifecycle; not just developers working in sprints (the team must be cross-functional); there is no "Agile project manager" role — command-and-control isn't Agile, and self-managed teams assign their own work.
- Bottom line: iterating without deploying, getting real feedback, and responding to change is just iterative development — not Agile.

### Module 2: Agile Planning

#### Section 1: Planning to be Agile

**Destination Unknown**
- Upfront planning is why deadlines get missed: you know the *least* at the start of a project, yet that's when traditional planning decides everything.
- "Field of penguins" analogy: you can only plot a few steps from your current vantage point before the terrain shifts — plot a course, advance, re-plot.
- **Core rule: don't decide everything at the point you know the least.** Plan for what you know now; adjust as you learn more.
- Iterative planning gives more accurate estimates — near-100% accuracy for the next two weeks vs. ~50% three months out, so commit short and re-estimate often.

**Agile Roles and the Need for Training**
- Simply *relabeling* existing people/teams into Agile roles (product manager → product owner, project manager → Scrum master, dev team → Scrum team — see Module 1, Section 2 for how these actually differ) fails without real training and reorganization.
- Without training, people fall back on old habits — e.g., a former project manager turning a Kanban board into a Gantt chart.
- The Agile mindset has to come from upper management: ask "what will you deliver in the next two weeks" instead of "what will you deliver by end of year."

**Kanban and Agile Planning Tools**
- Tools don't make you Agile — mindset and process come first; tools only support it.
- Epics and stories are enough to describe plans — tasks/subtasks veer into micromanaging.
- Course tool: **ZenHub** (GitHub plugin adding a Kanban board). Uses GitHub issues directly (no second system to keep in sync), gives one up-to-date source of truth, and has customizable pipelines.
- **ZenHub's default pipelines** (left → right):
  1. **New Issues** — the inbox; triage quickly during refinement.
  2. **Icebox** — cold storage for someday items.
  3. **Product Backlog** — everything not yet done, not yet in a sprint.
  4. **Sprint Backlog** — next two weeks' work (the only pipeline devs need to focus on).
  5. **In Progress** — actively worked, self-assigned.
  6. **Review/QA** — PR open, being reviewed.
  7. **Done** — code merged = *developer* done, not yet PO-accepted (that happens at sprint review).

#### Section 2: User Stories

**Creating Good User Stories**
- A **user story** is a piece of business value deliverable within a done increment — captures *who* it's for, *what* they need, and *why* (the business value), unlike an old-style flat "requirement."
- Contains: business value (who/what/why), assumptions/details, and acceptance criteria (definition of done).
- Template: **As a [role], I need [function], so that [business value].**
- Acceptance criteria prevent "that's not what I wanted" arguments at sprint review — use **Gherkin**: **Given** (precondition) / **When** (trigger) / **Then** (testable result).
  - Example: "As a marketing manager, I need a list of customer names and emails, so that I can notify them of promotions." *Given* 100 customers, 90 opted in, *When* I request the list, *Then* I should see 90 emails.
- **INVEST** (Bill Wake) — good stories are: **I**ndependent, **N**egotiable, **V**aluable, **E**stimable, **S**mall (fits one sprint), **T**estable.
- **Epics** = ideas too large for one sprint, made up of smaller stories — anything you can't estimate or fit in a sprint becomes an epic.

**Effectively Using Story Points**
- **Story points**: an abstract, *relative* estimate of difficulty — effort + complexity + uncertainty. Don't fight the abstractness.
- Humans are bad at estimating wall-clock time, so estimate in T-shirt sizes → Fibonacci numbers instead: 3 = small, 5 = medium, 8 = large, 13 = XL (don't go much further).
- Agree on what a **medium (5)** is first, then size everything else relative to it.
- Keep stories small (a couple of days); break anything that hits 21 into smaller stories (track with an epic if it spans sprints).
- **Anti-pattern**: mapping points directly to days ("a 1 is one day...") — a classic ex-PM habit. Never do this; keep it relative.

**Building the Product Backlog**
- **Product backlog** = a *ranked* list of all unimplemented stories.
- Only the top (next sprint or two) needs precise ranking and full detail; lower items can stay fuzzy.
- Converting requirements → stories (hit-counter example): each one-liner requirement becomes "As a [role], I need [function], so that [value]" — naming who benefits and why is what enables ranking later.
- New stories start in New Issues and get triaged (see Backlog Refinement below) into the backlog or icebox; MVP thinking applies even to the first increment (e.g., ship without persistence first).

#### Section 3: The Planning Process

**Backlog Refinement: Getting Started**
- **Refinement** = rank the backlog, break large stories into sprint-sized ones, and make top stories detailed enough to pick up and start.
- Attendees: **product owner** (owns the stories), **Scrum master** (assists), dev team *optionally* (just a lead/architect for technical questions — not the whole team).
- Product owners who say "everything's important" still have to rank — there's only one #1.
- Do the detail work here, not in sprint planning.
- **New issue triage** first (empty the inbox every meeting): each issue goes to → **product backlog** (doing it soon), → **icebox** (good idea, not now), or → **reject** (not the direction of the product).
- Target state: **sprint-ready** — full role/function/value template, assumptions, and Gherkin acceptance criteria.

**Backlog Refinement: Finishing Up**
- **Labels** visualize the board — keep to a few meaningful colors (bug, enhancement, help wanted, question, wontfix, invalid + a custom **technical debt** label in yellow).
- **Technical debt** = work the customer doesn't perceive as value (refactoring, environment upkeep, DB migrations, patching vulnerable libraries). It accumulates naturally — label it, make it visible, and pay some down **every sprint**.
- Refine every sprint (weekly if requirements come in fast); keep **at least two sprints' worth** of refined stories as a buffer. Time spent refining is time saved in planning.

**Sprint Planning**
- Sprint planning decides what goes into the next sprint, producing the **sprint backlog**.
- Attendees: product owner, Scrum master, full cross-functional dev team — **no stakeholders**.
- Every sprint needs a **goal** (from the PO) that the team can rally around and use mid-sprint as a sanity check ("am I off on a tangent?").
- Mechanics (a dev-team activity): pull top stories → confirm/assign story points (the team commits, so the team sizes — "planning poker" is one technique) → verify each story is self-sufficient → stop at the team's **velocity**.
- **Velocity** = story points completed per sprint; it improves over time and is **never comparable across teams** (each team's "medium" is relative to itself).
- Responsibility split: PO presents the goal; the dev team builds the plan.

### Module 3: Daily Execution

#### Section 1: Executing the Plan

**Workflow for Daily Plan Execution**
- Pull the next-highest-priority item you're skilled for — strictly in priority order, not favorites.
- Assign it to yourself and move it to **In Progress** so everyone can see who's working on what.
- **One story per person at a time** — you can only ship 100% of one finished thing, not 50% of two. (Exception: pick up something new while genuinely blocked.)
- Finish → open a PR → move to **Review/QA** → merge → move to **Done** → repeat from the top of the sprint backlog.

**The Daily Stand-Up**
- Same time/place every day, strictly **timeboxed to 15 minutes** (standing up helps enforce it). Also called the "daily scrum" — **not a status meeting**.
- Three questions: what did I do yesterday, what will I do today, am I blocked?
- Attendance: Scrum master always attends (to unblock people); full dev team attends; product owner is optional and doesn't drill the team.
- If blocked, the Scrum master's top priority is unblocking you; pick up another item in the meantime if it'll take a while.
- **Tabled topics**: anything off-script gets parked by the Scrum master and discussed after the meeting — keeps the 15-minute box intact.

#### Section 2: Completing the Sprint

**Using Burndown Charts**
- A **burndown chart** plots story points completed vs. remaining over time for a sprint (or any milestone).
- Vertical = points remaining, horizontal = days (weekends marked — teams shouldn't burn down on weekends).
- Plots an "optimal" straight line to zero alongside actual progress, so the team can forecast whether they'll hit the sprint goal and course-correct if they fall behind. A self-monitoring tool for the team, not primarily a management report.

**The Sprint Review**
- Demo time — live demonstrations for anyone who wants to attend (PO, Scrum master, devs, stakeholders, customers).
- The PO checks each story against its acceptance criteria to accept it; accepted stories move **Done → Closed**.
- Feedback becomes new backlog items — seeing a working demo sparks ideas stakeholders wouldn't have had during upfront planning. One of Agile's biggest advantages over Waterfall.
- **Rejected stories** follow the same close-and-rewrite pattern as unfinished sprint work (see "Getting Ready for the Next Sprint") — never left dangling or silently redone next sprint.

**The Sprint Retrospective**
- Reflects on the sprint's health — team and process. **Attendees**: Scrum master + dev team only — the PO is deliberately excluded so the team can speak freely.
- Three questions: what went well (keep), what didn't (stop), what should change?
- The Scrum master documents proposed changes and ensures some are actually acted on — not a gripe session. Goal: continuous, incremental improvement.

#### Section 3: Measuring Success

**Using Measurements Effectively**
- You can't improve what you don't measure. Avoid **vanity metrics** (e.g., "10,000 hits") that don't tell you what to do next; use **actionable metrics** — set a baseline, set a goal, track progress sprint over sprint.
- **Top four actionable metrics**: **mean lead time** (idea → delivered), **release frequency**, **change failure rate**, and **mean time to recovery (MTTR)** — since failures are inevitable, recovery speed matters more than avoiding failure entirely.
- Other examples: time to market, product availability, deploy/release time, % of defects caught in testing vs. production, feedback-loop speed.

**Getting Ready for the Next Sprint**
- End-of-sprint checklist: move **Done → Closed**, then close the sprint milestone so it's credited toward velocity.
- **Untouched stories** (never started): move to the top of the product backlog rather than assuming they're still top priority — don't auto-roll into the next sprint.
- **Unfinished stories** (partially worked): never move as-is — re-size to reflect actual points completed, close the original (labeled unfinished) so velocity stays accurate, then write a new story for the remainder.
- Create the next sprint milestone (now or at the next planning meeting). **Golden rule: always preserve velocity accuracy** — credit points completed, never silently carry work forward.

**Agile Anti-Patterns and Health Check**
- **Anti-patterns to avoid**: no real product owner (or too many); teams too large (keep under ~10, aim 5±2 or 7±2); non-dedicated teams (split across projects); teams too geographically dispersed without ≥2 people per time zone; siloed teams (needing tickets from other teams); teams that aren't self-managing.
- **Health check** for a healthy team: everyone accountable; short sprints (1–2 weeks); ordered product backlog; visible sprint backlog; sprint planning actually happens; stand-ups drive real replanning; a done increment every sprint; stakeholders actively give feedback at reviews; backlog updated from review feedback; PO/team/Scrum master stay aligned and act on retrospective learnings.
