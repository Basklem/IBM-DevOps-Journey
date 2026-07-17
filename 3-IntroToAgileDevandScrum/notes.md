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
- Don't decide everything at the point you know the least (the start) — plan iteratively from each new vantage point for far more accurate estimates.
- Renaming people into Agile roles without training fails: product owner ≠ product manager, Scrum master ≠ project manager, and a Scrum team is cross-functional, not just devs. The mindset shift must come from upper management.
- Tools don't make you Agile — mindset first. A Kanban board (e.g., ZenHub on GitHub) tracks work flowing left to right through pipelines: New Issues → Icebox → Product Backlog → Sprint Backlog → In Progress → Review/QA → Done (done = developer done, not product-owner accepted).
- A good user story states who/what/why ("As a [role], I need [function], so that [value]"), includes assumptions and Gherkin (Given/When/Then) acceptance criteria, and follows INVEST; ideas too big for one sprint become epics.
- Story points are abstract, relative sizes (effort + complexity + uncertainty) on a loose Fibonacci scale — agree on what a medium (5) is and compare; never map points to wall-clock time.
- The product backlog is a ranked list of unimplemented stories — only the top needs precise ranking and sprint-ready detail; requirements become stories via the story template, then get triaged into backlog or icebox.
- Backlog refinement happens every sprint: triage new issues to empty the inbox (backlog / icebox / reject), rank by priority, and make top stories sprint-ready (details, assumptions, acceptance criteria, labels) — keep ~two sprints' worth refined.
- Technical debt is work the customer doesn't perceive as value (refactoring, environments, library patches) — label it and pay some down every sprint.
- In sprint planning the PO presents the sprint goal and the dev team builds the sprint backlog: pull top stories, agree on estimates (they're the ones committing), and stop at the team's velocity — which is per-team and never comparable across teams.

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

### Module 2: Agile Planning

#### Section 1: Planning to be Agile

**Destination Unknown**
- Upfront planning is why deadlines get missed: at the start of a project you know the *least*, yet that's when traditional planning decides everything.
- "Navigating the unknown" (field-of-penguins analogy): you can only plot a few steps from your current vantage point, and the terrain keeps shifting (OS patches, package updates, changing requirements) — so plot a course, advance, then re-plot from the new vantage point.
- Core rule: **don't decide everything at the point you know the least.** Plan only for what you know now; as you learn more, adjust the plan.
- Iterative planning gives more accurate estimates: you can predict the next two weeks with near-100% accuracy, but three months out maybe 50% — so commit in short horizons and re-estimate as you go.
- Don't try to be omniscient — plan as you go, and estimates of where you are and how long things will take keep improving.

**Agile Roles and the Need for Training**
- Placing existing people into new Agile roles *without training* leads to failure. Three common (bad) direct mappings:
  - Product manager → product owner: the product manager is typically a business/budget/operations person; the product owner is the *visionary* who leads the team through experiments toward the sprint goal and acts as the conduit between stakeholders and team (translating business requirements into technical goals). Different skill sets — sometimes the same person works, sometimes not (job title vs. Scrum role).
  - Project manager → Scrum master: a project manager is a task manager who keeps everyone marching to a plan and *documents risks* ("what are you going to do to unblock yourself?"); a Scrum master is a coach who keeps the team focused and self-managing and *eliminates impediments* ("let me handle that for you"). Also: nobody assigns work on a Scrum team — the team assigns work to themselves, which is why "how do I know when I've assigned too much work?" is the wrong question entirely.
  - Development team → Scrum team: a dev team is just software engineers; a Scrum team is cross-functional (devs, testers, security, business analysts, ops — whoever is needed to build an increment). You must actually reorganize, not just relabel.
- Without training, people fall back on old habits — e.g., a project manager will try to turn a Kanban board into a Gantt chart because that's all they know.
- Bill Cantor quote: until business leaders stop managing projects with fixed functions, timeframes, and costs (Waterfall-style), they'll struggle to use Agile as designed.
- The Agile mindset must come down from upper management: stop asking "what will you deliver by end of year?" and start asking "what will you do in the next two weeks — how will you delight my customers at the end of the next sprint?"

**Kanban and Agile Planning Tools**
- A tool won't make you Agile — you need the Agile mindset/process first; tools only *support* the process. (Untrained people will make a Kanban board look like a Gantt chart — two totally different things.)
- Many Agile planning tools exist and mostly do the same thing; epics and stories are enough to describe plans — tasks/subtasks veer into micromanaging.
- Course tool: **ZenHub** — a GitHub plugin that adds a Kanban board/project management on top of GitHub. Why it's good:
  - Uses GitHub issues as the stories — developers stay in their normal tool, so there's no second system to update (statuses in separate tools are out of date ~100% of the time).
  - One up-to-date version of the truth; anyone (including management) can open the board and instantly see what's not started, in progress (and by whom), and done.
  - Customizable columns (called *pipelines*), simple or complex as you want — keep it simple.
- Kanban board = at its simplest: things to do, things you're doing, things you've done; move items left → right to show progress. Can literally be a whiteboard with sticky notes.
- ZenHub's default pipelines (workflow left → right):
  1. **New Issues** — the "inbox"; every new issue lands here. Triage it quickly during backlog refinement: move it to another pipeline or reject it, don't let it sit.
  2. **Icebox** — cold storage (unique to ZenHub) for long-term/someday items, so they're not forgotten but don't clutter active pipelines.
  3. **Product Backlog** — everything you ever want to do that isn't done and isn't in a sprint yet.
  4. **Sprint Backlog** — what you're doing in the next two weeks (pulled from the product backlog during sprint planning); the only pipeline developers need to focus on.
  5. **In Progress** — actively being worked; developers assign stories to themselves (avatar shows who's on what).
  6. **Review/QA** — work complete, pull request open; other devs review to make sure it meets the criteria to merge. (GitHub/ZenHub can auto-move PRs here.)
  7. **Done** — code merged; means the *developer* is done, NOT that the product owner has accepted it (acceptance happens at sprint review).
- Flow: new stories come in on the left, a done increment goes out on the right; devs finish a story, then pull the next one from the sprint backlog into In Progress themselves.

#### Section 2: User Stories

**Creating Good User Stories**
- User story = a piece of business value the team can deliver within a done increment. More than an old-style "requirement" ("I need this/that") — it captures *who* it's for, *what* they need, and critically *why* (the business value).
- A good story contains: a description of the business value (who/what/why), any assumptions and details you know (e.g., "we're using a relational database, don't go looking at NoSQL" — anything discussed while writing the story that helps the developer), and acceptance criteria (definition of done).
- Story description template: **As a [role], I need [function], so that [business value].** The role clarifies who benefits (marketing manager? customer? sysadmin?), and the business value is what you'll use later to prioritize the backlog.
- Acceptance criteria matter because you don't want the product owner saying "that's not what I wanted" at sprint review — with an agreed definition of done, the story either has the behavior or it doesn't (if they want something else, that's a *new* story). No arguments.
- Acceptance criteria use **Gherkin** syntax: **Given** (precondition, sets up the scenario) / **When** (the triggering action) / **Then** (the testable, measurable result).
- Example story: "As a marketing manager, I need a list of customer names and emails, so that I can notify them of marketing promotions." Assumptions: we maintain customer emails; customers have opted in. Acceptance: Given 100 customers in the DB and 90 opted in to email promotions, When I request a customer email list, Then I should see 90 (not 100) emails. Stakeholders can confirm it's the behavior they want; developers can confirm it's deliverable.
- **INVEST** (Bill Wake) — good stories are:
  - **I**ndependent — rankable/movable in the backlog on their own (not always possible, but aim for it)
  - **N**egotiable — scope can flex up or down; not too tightly coupled to one exact implementation
  - **V**aluable — clear customer value (vs. pure technical-debt work the customer never sees)
  - **E**stimable — enough info to size it (small/medium/large)
  - **S**mall — must fit within a single sprint
  - **T**estable — you can test the definition of done
- **Epics** = big ideas too large for one sprint. Epics sit above stories in the hierarchy and are made up of smaller stories. Backlog items often *start* as epics and get broken down into sprint-sized stories during refinement — any story you can't estimate or fit in a sprint becomes an epic.

**Effectively Using Story Points**
- Story points = an *abstract, relative* metric estimating the difficulty of implementing a story. The abstractness is the point — don't fight it.
- Three components of the estimate: **effort** (how much work — can be high even for easy/boring tasks), **complexity** (how hard), and **uncertainty** (have you done this before? never-done-before = rate it higher).
- Humans are terrible at estimating wall-clock time ("the only thing that takes 30 minutes is 30 minutes — everything else takes longer"), so don't estimate in time at all. Use T-shirt sizes instead.
- Since you can't add up S/M/L, use Fibonacci numbers — but don't get too granular. Recommended: 3 = small, 5 = medium, 8 = large, 13 = extra large, and not much beyond.
- The team must *agree on what a medium (5) is*, then size everything else relative to it — like estimating building heights: if this building is a 5, the shorter one next to it is a 3, the taller one an 8, the tallest a 13.
- Keep stories small — ideally completable in a couple of days. A 21 won't fit in a sprint: break it into smaller stories (possibly spanning sprints, tracked with an epic).
- **Anti-pattern: equating story points to wall-clock time** ("a 1 is one day, a 3 is three days...") — classic move of an ex-project-manager Scrum master who thinks in Gantt-chart dates. Never do this. A medium might take 2–3 days, sometimes 4 — agree on the fuzziness, keep it relative.

**Building the Product Backlog**
- Product backlog = a *ranked* list of all unimplemented stories (not in a sprint, waiting to be worked).
- Ranking effort is front-loaded: only the top (next sprint or two) needs accurate ranking by business importance; lower items can stay relatively unranked. Same for detail — top stories should be sprint-ready with full detail, bottom stories can stay fuzzy until later refinement.
- Converting requirements → stories (hit-counter service example — a service that counts things):
  - "Need a service for counting things" → As a **user**, I need a service that has a counter, so that I can keep track of how many times something has been done.
  - "Must allow multiple counters" → As a **user**, I need multiple counters, so that I can keep track of several counts at once.
  - "Persist counters across restarts" → As the **service provider**, I need the service to persist the last known count, so that users don't lose their counts after a restart.
  - "Counters can be reset" → As a **system administrator**, I need the ability to reset the counter, so that I can redo counting from the start. (Note the role choice — maybe only sysadmins get to reset.)
  - Each one-liner requirement becomes a story via the "As a / I need / so that" template — making who benefits and the business value explicit is what enables ranking later.
- New stories go into New Issues first (the inbox), then get triaged: prioritize into the product backlog in execution order (core service first → persistence → reset) or defer to the icebox (multiple counters = later). MVP thinking applies — first increment might have no persistence at all.

#### Section 3: The Planning Process

**Backlog Refinement: Getting Started**
- Backlog refinement = rank the backlog in priority order, break large stories into sprint-sized ones, and make sure stories near the top have enough detail that a developer can just pick them up and start.
- Who attends: **product owner** (key person — has the vision and should be creating/owning the stories), **Scrum master** (assists the PO in refining), and the dev team only *optionally* — bring one or two technical people (lead/architect) to answer technical questions; the whole Scrum team attending is a waste of their time.
- Goal: a ranked backlog. Product owners who say "everything's important" still have to pick — there's only one #1, one #2, one #3.
- Do the detail work *here*, not in sprint planning — the more sprint-ready stories are now, the faster planning goes ("you don't want to be doing a lot of typing in the sprint planning meeting").
- **New issue triage** comes first: customers keep filing new issues (e.g., "remove a counter," "deploy to cloud"), so start every refinement meeting by emptying the New Issues column (it's your inbox). Each new issue goes one of three ways:
  - → **Product backlog** — doing it soon (maybe even top of the backlog)
  - → **Icebox** — good idea, not a priority, deal with it in a future sprint
  - → **Reject** — not where the product is going; never doing it
  - Example: "remove a counter" → icebox (we don't even have multiple counters yet); "deploy to cloud" → product backlog, ranked *above* reset.
- Refinement workflow: PO reorders by importance; optionally assign rough story points (nice to know roughly how big the backlog is — the team re-confirms/refines them at sprint planning); split large items, clarify vague ones. Target state: **sprint-ready** stories.
- Making a story sprint-ready = complete the template: role/function/value + assumptions (e.g., need a one-step atomic increment, a way to get current value) + Gherkin acceptance criteria (Given I've incremented the counter to 2, when I call get counter, then it returns 2).
- New stories in ZenHub start unassigned, with no labels, milestones, or estimates — refinement fills these in.

**Backlog Refinement: Finishing Up**
- **Labels** help visualize the work on the board — a few meaningful colors, not too many or they become meaningless. Standard GitHub labels: bug (red = danger), enhancement (cyan), help wanted (green), question, wontfix, invalid. Add a custom **technical debt** label in *yellow* (caution — don't accumulate too much).
- Grooming examples: persistence story gets an assumption ("use Redis, store counter as a name-value pair in a memcache DB — no relational DB needed"; document decisions like this so the developer doesn't have to guess) and acceptance criteria (Given counter = 2 and I restart the service, then it still returns 2 — proves persistence). Reset story gets an implementation hint (POST to `/counters/<name>/reset` — a separate endpoint so only admins can access it) and criteria (Given counter = 5, when I call reset, then get returns 0).
- **Technical debt** = anything you must do that the customer doesn't perceive as value. Examples: code refactoring, setting up/maintaining environments, changing databases (SQL → NoSQL), patching vulnerable libraries and retesting. It builds up naturally (not always your fault — e.g., upstream vulnerabilities), so don't shy away from it: label it, make it visible, and **include some technical debt in every sprint plan** to pay it down.
- "Deploy service to the cloud" labeled technical debt (arguable — availability is value, but customers *expect* availability; it's not a feature they'd recognize).
- Refinement tips:
  - Refine every sprint (weekly if lots of requirements come in). Typical cadence: sprint runs Monday → following Friday; review + retrospective that Friday; refinement the Wednesday *before* sprint end; sprint planning first thing Monday.
  - Keep at least **two sprints' worth of refined stories** in the backlog — buffer if the team finishes early or a refinement meeting gets skipped.
  - Time spent refining is time saved planning.

**Sprint Planning**
- Sprint planning = deciding what stories go in the next sprint (how much can we do in two weeks), producing the **sprint backlog**.
- Who attends: product owner, Scrum master, and the full cross-functional dev team (engineers, testers, ops, BAs). **No stakeholders** — core Scrum roles only.
- Every sprint needs a **goal**, articulated by the product owner (think "what can we get done in two weeks," not "I need the whole thing"). Stories in the sprint should support the goal. Mid-sprint, the goal keeps you on track — "am I off on a tangent? Am I over-engineering? What did we commit to deliver?"
- Mechanics (a *development team* activity): take stories from the top of the product backlog → confirm/assign story points (the team commits, so the team decides size — "planning poker" is one way to reach agreement) → verify each story has enough info for *anyone* on the team to pick it up without mid-sprint questions → move into sprint backlog → **stop when you hit the team's velocity**.
- **Velocity** = number of story points a team completes in a sprint. It changes over time (estimates improve, team gets more competent). Critical: **you cannot compare velocity across teams** — story points are relative to each team's definition of a medium, and teams using bigger numbers aren't doing more work. Velocity is a personal, per-team measure.
- In ZenHub, create a **milestone** (or ZenHub's newer "sprints" feature) for each sprint: short title (shows in dropdowns — e.g., "Sprint 1: single counter"), description = the sprint goal (e.g., "get a single counter working and deployed to the cloud"), and start/end dates (two weeks — one week is too short, 3+ too long).
- Planning flow with the board: open each story → team discusses size and assigns estimate (e.g., base counter service = 8, persistence = 5, cloud deploy = 5) → assign it to the sprint milestone → drag to the sprint backlog; the tool totals the pipeline's points. At team velocity (e.g., 18), stop — don't over-commit. It's not the *number* of stories, it's the point total vs. your track record.
- Responsibility split: product owner presents the sprint goal; the development team creates the sprint plan.
