# Introduction to Agile Development and Scrum — Notes

## Key Takeaways
- Agile is an iterative approach to project management/software development that delivers value to customers quickly and adapts based on feedback, rather than planning everything up front.
- The Agile Manifesto values individuals/interactions, working software, customer collaboration, and responding to change over processes/tools, documentation, contracts, and rigid plans (the right-side items still matter, just less).
- Waterfall's phase-gated structure (Requirements → Design → Code → Integrate → Test → Deploy) makes change expensive and delays feedback until the very end.
- Extreme Programming (XP) and Kanban were early influences on Agile, contributing iterative loops, fast feedback, and workflow visualization/WIP limits.
- Working Agile in practice means small batches, MVPs for learning, BDD (outside-in) and TDD (inside-out) testing, and pair programming.
- The key takeaway across all of this: build what is needed, not just what was planned.
- Scrum is a prescriptive methodology for practicing the Agile philosophy — fixed-length sprints, defined roles (product owner, Scrum master, Scrum team), and a repeatable set of artifacts and events.
- The three Scrum roles have distinct jobs: product owner owns vision/priorities/acceptance, Scrum master coaches the team and removes impediments (no management authority), and the self-organizing Scrum team commits to and delivers the work.
- Scrum's three artifacts (product backlog, sprint backlog, done increment) and five events (sprint planning, daily Scrum, the sprint, sprint review, sprint retrospective) form the full cadence of a sprint.
- Scrum and Kanban differ in cadence, release approach, roles, key metrics (velocity vs. cycle time), and tolerance for mid-cycle change — Scrum locks the sprint scope, Kanban allows continuous change.
- Team organization directly shapes system architecture (Conway's Law) — teams should be small, autonomous, mission-aligned, and end-to-end responsible for their business area.
- Agile only delivers its full benefit if the *entire* organization (including Ops) adopts it — otherwise you get "Water-Scrum-Fall": Waterfall planning + iterative middle + a slow, painful final deployment.
- Just iterating on a plan isn't Agile — you're only Agile if you're deploying frequently, getting real customer feedback, and being responsive to change.

---
  
## Notes

### Module 1: Introduction to Agile and Scrum

#### Section 1: Introduction to Agile Philosophy

**Agile Principles**
- Agile = an iterative approach to project management that lets teams be responsive and deliver value to customers quickly. Plan in small increments (not a full year), get customer feedback, adjust as you go.
- Defining characteristics: adaptive planning → evolutionary development → early delivery → continuous improvement → responsiveness to change.
  - Early delivery is a key differentiator — iterating without delivering to the customer isn't actually being Agile.
- Agile Manifesto (4 value statements): we value...
  - Individuals and interactions over processes and tools
  - Working software over comprehensive documentation
  - Customer collaboration over contract negotiation
  - Responding to change over following a plan
  - Important nuance: the items on the right still have value — Agile just values the items on the left *more*. You still use tools, document, negotiate contracts, and plan.
- Agile software development = an iterative approach to software development that conforms to the Agile Manifesto, emphasizing flexibility, interaction, and transparency.
- Agile teams are small, co-located, cross-functional, self-organizing, and self-managing.
- Key takeaway: build what is needed, not what was planned — needs change, and you should replan/respond rather than stick to the original plan.

**Methodologies Overview**
- Waterfall approach: sequential phases — Requirements → Design → Code → Integrate → Test → Deploy — each with entrance/exit criteria; very hard to go back once you move to the next phase (hence "waterfall," like swimming upstream).
  - Problems with Waterfall:
    - No provision for change
    - No intermediate delivery — you don't know if it works until the very end
    - Each step ends when the next begins (info loss/handoff issues at every transition)
    - Mistakes found late are very costly to fix
    - Long lead times between wanting software and delivering it
    - Teams work in silos, unaware of their impact on each other
    - The Ops team, who knows the least about the code, is the one running it in production
- Extreme Programming (XP): introduced by Kent Beck in 1996; one of the first Agile methods. Uses nested iteration loops (release in months → iteration in weeks → acceptance in days → stand-ups daily → pair negotiation in hours → unit testing in minutes → pair programming in seconds) to get progressively faster feedback.
  - XP values: simplicity (don't over-engineer), communication, feedback, respect (no hierarchy, everyone's ideas are valued), courage (honest estimates, no padding).
- Kanban: from Japanese manufacturing ("billboard sign"); about continuous flow, using cards/notes to track work moving station to station.
  - Core Kanban principles: visualize the workflow, limit work in progress (WIP), manage/enhance the flow, make process policies explicit (including a shared definition of "done"), continuously improve.
  - Agile borrows Kanban boards, WIP limits, and "definition of done" directly from this methodology.

**Working Agile**
- Five practices of working Agile: work in small batches, use MVPs, BDD, TDD, pair programming.
- Small batches (from lean manufacturing): batching work (e.g., folding/inserting/sealing/stamping 50 brochures at a time) delays your first inspectable result and delays finding defects (e.g., a typo or bad glue isn't caught until much later). Single-piece flow surfaces defects almost immediately and lets you pivot fast. Lesson: smaller batches = faster feedback = less waste.
- Minimum Viable Product (MVP):
  - NOT "phase one" of a project or a first beta — it's the minimal thing built to test a hypothesis and generate learning, not to deliver a partial product.
  - Decide to pivot or persevere after each MVP.
  - Car/skateboard example: delivering a wheel → chassis → car pieces (feature-slicing without learning) gives the customer exactly what was planned, but not what they actually wanted. Delivering a skateboard → skateboard with steering → motorized version (a complete, if minimal, product each time) lets the customer react and steer the outcome toward what they actually want (they end up wanting a convertible, not the original car).
- Behavior Driven Development (BDD): tests the system from the outside in, usually at the integration/UI level — does the system behave the way the customer expects?
  - Uses Gherkin syntax so devs and stakeholders share one language: "As a [role], I need [function], so that [business value]" followed by Given/When/Then scenarios.
  - BDD = building the right thing.
- Test Driven Development (TDD): tests the system from the inside out, at the unit level.
  - Workflow: write a failing test case (Red) → write just enough code to pass it (Green) → refactor (Refactor). "Red, Green, Refactor."
  - TDD = building the thing right.
- Pair Programming (from XP): two programmers work together — one writes, one reviews/thinks/looks things up — typically swapping roles every ~20 minutes.
  - Cheaper to catch bugs while writing code than in production; results in higher-quality code.
  - Good for pairing senior + junior (mentorship) or someone unfamiliar with the code + someone who knows it (knowledge transfer).

#### Section 2: Introduction to Scrum Methodology

**Scrum Overview**
- Agile vs. Scrum: Agile is a philosophy (not prescriptive); Scrum is a methodology (prescriptive) for working in an agile fashion.
- Scrum = a management framework for incremental product development. Emphasizes small, cross-functional, self-managing teams; provides structure via roles, rules, and artifacts; works in fixed-length increments called sprints; goal is a potentially shippable increment every sprint.
- "Easy to understand, difficult to master" — few rules, but hard to execute well. If the team is new to Scrum, bring in someone experienced to mentor/guide.
- Sprint = one iteration through design/code/test/deploy. Every sprint needs a clear goal. Typical length is two weeks (some do up to four, but that's too long — stay closer to small batches; one week is a bit too fast).
- Scrum process flow: product backlog (everything you might ever want to do) → backlog refinement/grooming (making stories sprint-ready) → sprint planning (produces the smaller sprint backlog) → two-week sprint with daily Scrum/stand-up → shippable increment.
  - Daily stand-up = answer 3 questions: What did you do yesterday? What will you do today? Is anything blocking you?
  - The cycle repeats every sprint: plan → design/code/test → deploy → get customer feedback → feed into next plan.

**The 3 Roles of Scrum**
- Only three roles in Scrum: product owner, Scrum master, Scrum team (aka development team).
- Product Owner:
  - Has the vision; decides to pivot or persevere; represents stakeholder interests (liaison between team and stakeholders/whoever holds the checkbook).
  - Note: "product manager" is a job title, "product owner" is a Scrum role — not always the same person.
  - Articulates the product vision to the whole team, is the final arbiter of requirements/questions, continuously reprioritizes and grooms the product backlog, and solely decides whether to accept/ship or reject each increment (and whether to pivot or persevere).
- Scrum Master:
  - Facilitates the Scrum process; should be the most Scrum-knowledgeable person on the team; more critical to have experienced when the team is new to Scrum.
  - Coaches the team as an Agile coach/mentor, fosters a self-organizing environment, shields the team from external interference (stakeholders/customers should go through the Scrum master, not grab team members directly).
  - Top daily priority: resolve impediments raised in stand-up (unlike a traditional PM who asks "what are you going to do about it," the Scrum master says "give it to me, I'll get it fixed").
  - Enforces timeboxes (15-min stand-up, 2-week sprint, etc.), tracks empirical data/burndown, and should have no management authority over the team (so team members can confide in them without a manager-employee power dynamic).
- Scrum Team:
  - Cross-functional (devs, testers, business analysts, domain experts, ops — not just software engineers).
  - Self-organizing and self-managing: no externally assigned roles, no one assigns work to anyone — the team pulls work off the board and assigns it to themselves.
  - Ideal size: 7 ± 2 people (some say 5 ± 2) — kept small intentionally.
  - Best when co-located; if geographically dispersed, keep at least two people per time zone/geography so no one is isolated.
  - Should be dedicated, long-term, full-time members — not split across multiple projects.
  - Negotiates commitments with the product owner one sprint at a time (not committing months in advance) and has full autonomy over how to reach those commitments — told what to do, not how.

**Artifacts, Events, and Benefits**
- Three Scrum artifacts:
  - Product backlog — everything not yet done; all future requirements/stories (some teams split this further into an icebox/release backlog, but generally treated as one list).
  - Sprint backlog — the subset of stories committed to for the next two weeks.
  - Done increment — the completed product increment at the end of a sprint.
- Five Scrum events:
  1. Sprint planning meeting — product owner, Scrum master, and team plan the sprint and commit to stories.
  2. Daily Scrum/stand-up — daily sync, same time/place, using the 3 standard questions.
  3. The sprint itself — the two-week working period.
  4. Sprint review — demo to stakeholders showing what was completed.
  5. Sprint retrospective — team reflects on what went well, what didn't, and what to change (most important event for continuous improvement).
- Benefits of Scrum: higher productivity (daily sync + visible Kanban board), better quality (continuous testing via BDD/TDD), reduced time to market (small increments shipped sooner), increased stakeholder satisfaction (faster visibility into progress), better team dynamics (transparency, team members help each other), and happier employees (more autonomy/control).
- Scrum vs. Kanban comparison:
  - Cadence: Scrum = fixed-length sprints (~2 weeks); Kanban = continuous flow.
  - Release: Scrum releases at sprint end; Kanban does continuous delivery.
  - Roles: Scrum has defined roles (PO, Scrum master, dev team); Kanban has no prescribed roles (maybe an Agile coach).
  - Key metric: Scrum tracks velocity (work completed per sprint); Kanban tracks cycle time (inception to completion).
  - Change philosophy: Scrum locks sprint scope once committed (avoid mid-sprint changes); Kanban allows changes continuously, anytime.
  - Note: Scrum teams often use a Kanban board for visualizing work, without adopting the full Kanban process.

#### Section 3: Organizing for Success

**Organizational Impact of Agile**
- Organization structure is critical to Agile success — you often can't just take existing teams and declare them "Agile"; teams may need to be reorganized.
- Conway's Law (Melvin Conway, 1968): any organization that designs a system will produce a design whose structure mirrors the organization's communication structure. Example: 4 teams asked to build a compiler will produce a 4-pass compiler; a UI team + app team + database team will produce a 3-tier architecture.
- How teams should be organized:
  - Loosely coupled to each other (minimal dependency between teams) but tightly aligned around building a single application.
  - Each team has its own mission aligned with the business — e.g., for a 50-dev e-commerce app, break into smaller teams (order team, accounts team, shopping cart team, recommendation team) with ownership of a business area, rather than one big monolith team.
  - End-to-end responsibility: teams build it, run it, and debug it in production.
  - Long-term mission — constantly shuffling people between projects kills ownership and hurts business outcomes.
- Autonomy matters: it's motivating (motivated people build better software) and it's fast (decisions happen locally on the team instead of waiting on approval from above), which avoids bottlenecks from handoffs and waiting.
- "Wall of Confusion" (Andrew Clay Shafer): Dev is measured on delivering change; Ops is measured on stability/not changing anything — diametrically opposed incentives. If this divide exists, being "Agile" in development alone won't deliver the expected benefits.
  - Real example given: a team worked in agile sprints starting January, had something ready to deploy by mid-February, but Ops required a ticket and the deployment kept slipping — it didn't actually ship until September. Lesson: if the whole org isn't Agile (especially Ops), the dev team's agility gets bottlenecked.
- Agile and DevOps goals are well aligned: Agile wants faster delivery / DevOps wants faster time to market; Agile wants responsiveness to change / DevOps wants IT tightly aligned with the business; Agile wants higher quality / DevOps wants higher IT productivity. To get the full benefit of Agile, look at adopting DevOps too so Ops is just as agile as Dev.

**Mistaking Iterative Development for Agile**
- Common pitfall: teams claim to be Agile but actually do a "fuzzy front end" (Waterfall-style requirements/design/planning upfront), then iterate only on execution, then hit a "last mile" where deployment takes forever because it's the first time everything's been integrated and Ops has never deployed it before.
- This pattern is called Water-Scrum-Fall — Waterfall on both ends with iterative "Scrum-looking" work sandwiched in the middle. It's not real Agile because there's no deployment/feedback loop happening after each iteration and no pivot-or-persevere decision point.
- What Agile is NOT:
  - Not just an iterative software development lifecycle / "mini Waterfall" — if you're planning everything out upfront, you're not being Agile.
  - Not just developers working in sprints — the team must be cross-functional (devs, testers, business analysts, and ops if doing DevOps), not just software engineers.
  - There is no "Agile project manager" role in the Agile Manifesto — a project manager doing command-and-control isn't Agile; self-managed teams assign work to themselves.
- Bottom line: iterating on a plan without deploying and getting real customer feedback each cycle, and without being responsive to change, is not Agile — it's just iterative development.
