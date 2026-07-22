# Introduction to Software Engineering — Notes

## Key Takeaways
- **Software engineering** = applying scientific/engineering principles to systematically gather requirements and design, build, and test software; it's broader in scope than **software development**, which focuses on implementing specific functionality.
- The mid-1960s–mid-1980s **software crisis** (over budget, late, buggy, unscalable code) is what pushed the industry from ad hoc coding toward a real engineering discipline — including the rise of **CASE** tools.
- Titles (engineer/developer/programmer) are used inconsistently across companies and countries — in some places "engineer" is a formally regulated title (ethics codes, licensing); in the US it's mostly informal. The common thread: engineering implies the *full lifecycle* (design → build → maintain → evolve) and system-level thinking, not just writing code.
- The **SDLC** (Software Development Life Cycle) is the standard framework for building high-quality software predictably — six phases (**planning, design, development, testing, deployment, maintenance**), each discrete with its own deliverables. Originally linear (**Waterfall**), now commonly run iteratively.
- Planning produces the **SRS** (Software Requirements Specification); design produces a **design document**; both are key gate deliverables before coding starts.
- Testing has four common levels — **unit → integration → system → user acceptance (UAT)** — and releases progress through **alpha → beta → GA** audiences.
- **Requirement gathering** is a 6-step process: identify stakeholders → set goals & objectives → elicit → document → confirm → prioritize. It can produce up to three documents: **SRS** (most common), **URS** (user stories), and **SysRS** (whole-system requirements, broader than SRS).
- Requirements split into four categories: **functional, external/UI, system features, non-functional**.
- Three common development methodologies: **Waterfall** and the **V-shape model** are both sequential (upfront planning, hard to change once underway); **Agile** is iterative (short sprints, changing requirements handled easily, but harder to budget/scope upfront). Agile is the most widely used today.
- Software **version numbers** track release/update history — often 2–4 dot-separated number sets; **semantic versioning** = major.minor.patch.build. Check version numbers first when troubleshooting compatibility issues.
- Testing splits into three types — **functional, non-functional, regression** — layered across four levels: **unit → integration → system → acceptance**.
- Documentation splits into **product** (what the software does — requirements, design, technical, QA, user docs) vs. **process** (how to do a task, often detailed further in an **SOP**). Keep it updated during maintenance.
- Common project roles: **project manager/Scrum master, stakeholder, architect, UX designer, developer, tester/QA, SRE/Ops, product manager/owner, technical writer** — names vary by org/methodology, and in practice these roles work best tightly collaborating rather than handing work off in sequence.

---

## Notes

### Module 1: The Software Development Lifecycle

#### Section 1: Overview of Software Engineering

**What is Software Engineering?**
- **Software engineering**: the application of scientific principles to design and create software — a systematic approach to gathering/analyzing business requirements, then designing, building, and testing software to meet them.
- History: computing began in the late 1950s with software engineering as an undefined discipline; it became a formal field in the 1960s as methods shifted from ad hoc programming toward standardized practices.
- The **software crisis** (mid-1960s–mid-1980s): rising demand for complex software outpaced immature development processes — projects ran over budget and behind schedule, produced unmanageable/buggy code, and often didn't scale from small systems to large ones. (Some of this still happens today, just far less often.)
- The fix was treating software development as a real engineering discipline, plus the mid-1980s rise of **CASE** (Computer-Aided Software Engineering) tools, spanning six categories: business analysis/modeling, development tools (e.g., debuggers), verification & validation, configuration management, metrics/measurement, and project management.
- **Software engineer vs. software developer**: often used interchangeably, but engineers typically have broader knowledge, take a systematic/big-picture approach, and build entire systems on larger-scale projects; developers tend to work more creatively on specific functionality within a system.
- SE responsibilities: designing, building, and maintaining software systems; writing and testing code; consulting with stakeholders (clients, vendors, security specialists, other team members).
- Modern development is typically guided by the **SDLC**, covered next.

**Insider's Viewpoint: What is Software Engineering?**
- *(Practitioner opinions, not a formal definition — useful for context on how the term is actually used in industry.)*
- Software engineering spans many specializations: front end, back end, security, mobile, test, full stack, DevOps, cloud, data, ML.
- Common theme across the practitioners: it's the *full lifecycle* — design/architecture, implementation, and ongoing maintenance/evolution — not just writing code; several described it as a creative, end-to-end process starting well before code is written and continuing after deployment.
- Consensus on engineer vs. developer: "engineer" implies a longer time horizon and broader responsibility (system design, architecture, data flow), while "developer" is more narrowly scoped to building features/apps from an assigned task.
- Title usage varies a lot by company and country — in the US, "engineer/developer/programmer" are often interchangeable and inconsistently gatekept; in Canada, "engineer" is a regulated title requiring specific ethics training, similar to civil/mechanical engineering.

**Introduction to the SDLC**
- **SDLC (Software Development Life Cycle)**: a systematic process for developing high-quality software within a predictable timeframe/budget, aimed at meeting the client's business requirements.
- Defines discrete phases (each with its own process and deliverables) in a planning → design → development cycle that can be run iteratively.
- History: took shape in the mid-1960s as growing software complexity demanded a more deliberate approach; originally used the linear **Waterfall method**, later adapted toward iterative approaches to handle shifting requirements.
- **Key advantages**: replaces ad hoc development with a repeatable process (lower risk, higher efficiency); discrete, well-defined phases so teams know what to work on and when; better communication between customers, stakeholders, and the dev team; supports iteration to incorporate new requirements; catches problems early (in design, not mid-coding); clearly defined roles reduce conflict and overlap.

**Phases of the SDLC**
- Six phases: **Planning → Design → Development → Testing → Deployment → Maintenance**. Each is discrete (no task overlap between phases); names/count can vary by organization.
- **Planning**: requirements are gathered, analyzed, documented, and prioritized. Considerations: users, purpose, data in/out, legal/regulatory compliance, risk, QA needs, resource allocation, scheduling. Costs are estimated against time constraints; teams and roles are proposed. **Prototypes** (small-scale replicas used to gather feedback and test basic design ideas) may be built here — though they can occur at any phase whenever requirements need clarifying. Output: the **SRS** (Software Requirements Specification), which must be understood and approved by all stakeholders.
- **Design**: SRS requirements are turned into software architecture by the team, reviewed by stakeholders. Prototypes here are more like preliminary mock-ups for demonstration. Output: the **design document**, used to drive development.
- **Development** (aka building/implementation): coding starts once the design document is done; project planners assign coding tasks from it. Involves specific tools, languages, stacks, and org coding standards.
- **Testing**: code is tested (manually, automated, or hybrid) for stability, security, and conformance to the SRS. Bugs are reported, tracked, fixed, and retested. Levels: **unit → integration → system → acceptance**.
- **Deployment**: the application is released to production. Often staged — first to a **UAT** (User Acceptance Testing) environment, then to production after customer sign-off. Applies to websites, app stores, or internal distribution servers.
- **Maintenance**: post-deployment — surfaces missed bugs, UI issues, and requirements gaps; identifies enhancements. High-priority bugs get fixed immediately; others feed into a future release, restarting the cycle.

**Building Quality Software**
- Six common SE processes: **requirements gathering, design, coding for quality, testing, releases, documenting.**
- **Requirements gathering** → the **SRS**, which may include use cases describing business needs/user flows. Requirements fall into four categories: functional, external/UI, system features, non-functional.
- **Design**: translates requirements into an implementable structure. The technical lead breaks requirements into components (behaviors, boundaries, interactions) that define the system architecture — covering system functions, performance, security, platform characteristics, business rules, application logic, API design, UI, and database design.
- **Coding for quality**: quality code is maintainable, readable, testable, secure, defect-free, clean, consistent, documented, and efficient. Practices: follow coding standards/conventions/patterns, use **linters** to catch programmatic/stylistic errors, and comment code for others.
- **Testing**: verifies the software matches requirements and is bug-free, ensuring reliability, security, performance, and efficiency. Levels: **unit** (developer-run, smallest isolated component) → **integration** (once components are combined) → **system** (full product) → **user acceptance/UAT** (aka beta testing, run by the intended end user). Types: functional, non-functional, regression.
- **Releases** progress through three audiences: **alpha** (first working version, select stakeholders, likely buggy/incomplete, design may still change) → **beta**/limited release (external stakeholders, real-world testing, should meet all functional requirements) → **GA** (general availability, stable version, all users).
- **Documentation**: **system documentation** for technical users (README files, inline comments, architecture/design docs, verification info, maintenance guides) vs. **user documentation** for non-technical end-users (user guides, instructional videos/manuals, online/inline help).

**Requirements**
- **Requirement gathering** = a six-step process: identify stakeholders → establish goals & objectives → elicit requirements → document → analyze/confirm → prioritize.
- **Stakeholders** typically come from the requesting organization — decision-makers, end-users, sysadmins, engineering, marketing, sales, customer support. Aim for a representative from every affected group.
- **Goals** = broad, long-term, achievable outcomes (customer + business goals). **Objectives** = specific, actionable, measurable steps that achieve those goals.
- Eliciting (via surveys, questionnaires, interviews), documenting, and confirming are usually done iteratively together. Confirmed requirements must be analyzed for consistency/clarity/completeness, then approved by stakeholders.
- **Prioritization** uses labels like "must-have," "highly desired," "nice to have," ideally ordered within each category.
- Requirement gathering can produce up to three documents:
  - **SRS (Software Requirements Specification)** — the most common. Captures the functionalities the software should perform plus performance benchmarks/service levels. Contains: a purpose statement (intended use, audience, scope), constraints/assumptions/dependencies, and requirements sorted into four categories — **functional** (what the software does), **external/UI** (behavior toward users, other hardware/software), **system features** (a required subset of functional requirements), and **non-functional** (performance, safety, security, quality standards).
  - **URS (User Requirements Specification)** — business need and end-user expectations, written as user stories/use cases answering *who*, *what function*, and *why*. UAT determines if these are met. Often folded directly into the SRS rather than kept separate.
  - **SysRS (System Requirements Specification)** — broader than the SRS; covers the entire system, not just the software. Includes system capabilities, interfaces, user characteristics, policy/regulation/personnel/performance/security requirements, system acceptance criteria, and hardware expectations. Most software projects only produce an SRS, not a full SysRS.

#### Section 2: The Software Building Process and Associated Roles

**Software Development Methodologies**
- Three common approaches: **Waterfall**, **V-shape model**, **Agile**.
- **Waterfall**: sequential — each phase's output feeds the next, all planning done upfront, customer doesn't see the product until testing. Major releases repeat this whole cycle, so releases are years apart.
- **V-shape model**: also sequential, shaped like a V. Descending the left side (**verification**): planning → system design → architecture design → module design, bottoming out at coding. Ascending the right side (**validation**): unit → integration → system → acceptance testing — each validation phase corresponds to a verification phase, with tests written on the left and executed on the right.
- **Agile**: iterative — short sprints (1–4 weeks) instead of one long linear pass; unit testing happens every sprint; ends in a **sprint demo**/feedback stage instead of a maintenance phase, then repeats. After several sprints, an **MVP** is built to validate assumptions with stakeholders. Grounded in the same four Agile Manifesto values covered in the Agile/Scrum course.
- **Pros/cons**: Waterfall and V-shape are both easy to understand and make budgeting/resourcing easier (planned upfront), but both are rigid — hard to accommodate changed or overlooked requirements once underway (V-shape is even more rigid than Waterfall, though its early test-planning saves time later). Agile handles changing requirements well since planning resets every sprint, but upfront budgeting/scheduling is harder since full scope isn't defined upfront. Agile is the most widely used approach today.

**Software Versions**
- Version numbers track a program's release/update/patch history — useful for both users and developers, and the first thing to check when troubleshooting compatibility issues.
- Typically 2–4 dot-separated number sets. First release is often **1.0**; a beta/testing build can be below 1 (e.g., 0.9). Some projects version by date instead (e.g., Ubuntu 18.04.2 = April 2018, with the third number marking an incremental update).
- **Semantic versioning** (not universal, but common): **major.minor.patch.build** — major = new release/big changes, minor = smaller changes, patch = bug fixes, build = build number/date/minor tweaks.
- Version info is usually in a program's About/Help menu.
- Compatibility between old and new versions is a common problem; some software is **backwards compatible** (older files/programs still work on newer versions).

**Software Testing**
- **Software testing**: integrating quality checks throughout the SDLC to confirm the software meets requirements and is error-free. Built around **test cases** (steps, inputs, data, expected outputs), always written after requirements are finalized.
- Three testing **types**:
  - **Functional**: black-box (no view of source/internals); tests inputs/outputs of the system under test (SUT) against functional requirements; confirms usability, accessibility, and graceful handling of user errors/edge cases.
  - **Non-functional**: tests performance, security, scalability, availability — behavior under stress/concurrent load, cross-OS consistency, disaster recovery, and whether docs match actual behavior.
  - **Regression** (aka maintenance testing): confirms a recent change (e.g., a bug fix) didn't break existing functionality; run after requirement changes or defect fixes. Test-case selection favors areas with frequent defects, heavily used functionality, recent changes, complexity, or flaky (inconsistently passing) history.
- Four testing **levels** (each at a different SDLC stage, to avoid overlap): **unit** (dev-run, function-level, catches construction errors before integration) → **integration** (black-box; tests already-unit-tested modules once combined, catching interaction/communication bugs, logic mismatches, poor exception handling) → **system** (full integrated product, both functional and non-functional, run in a staging environment resembling production) → **acceptance** (formal sign-off against user needs/business processes, usually run by the customer/stakeholders during maintenance).

**Software Documentation**
- **Documentation**: written, video, or graphical material describing what the software is and how to use it — spans the entire SDLC and targets varied audiences (end users, devs, QA, sysadmins, other stakeholders).
- Two categories: **product documentation** (what the product does) vs. **process documentation** (how to complete a task; should define the quality requirements for doing that task right).
- Five types of product documentation: **requirements** (written during planning, for the dev team — includes the SRS/SysRS/user acceptance specs), **design** (written by architects/dev team — conceptual + technical design docs), **technical** (code comments, working papers, engineers' implementation notes), **QA** (test plans, test data, scenarios, cases, strategies, and traceability matrices mapping test cases to requirements), and **user** (FAQs, install/help guides, tutorials, manuals).
- **SOPs** (Standard Operating Procedures) go with process documentation but in much greater, org-specific detail (e.g., a company's exact steps for merging code, beyond generic dev knowledge) — as a flowchart, hierarchical outline, or step-by-step list.
- Documentation must be kept current (e.g., updating docs when a UI changes) — this happens during the maintenance phase and should be reviewed periodically for accuracy.

**Roles in Software Engineering Projects / Insiders' Viewpoint**
- Common roles (names vary by methodology/company; not every project has every one):
  - **Project manager** (Waterfall) / **Scrum master** (Agile): the PM owns planning, scheduling, budgeting, resourcing, execution, and communication; the Scrum master instead focuses on team/individual success and facilitating communication, per Agile's people-over-process value — not on upfront planning.
  - **Stakeholder**: who the product is built for (customer, end-users, decision-makers, sysadmins, other key personnel) — defines requirements, gives clarifying feedback, sometimes joins beta/acceptance testing.
  - **System/software/solution architect**: designs and communicates the architecture — the software's internal structure and technical characteristics — providing technical support across the SDLC.
  - **UX designer**: balances intuitive design with meeting requirements; defines how the software behaves and communicates from the user's perspective.
  - **Developer**: writes the code, implementing the architecture (design doc), requirements (SRS), and UX specs together.
  - **Tester/QA engineer**: writes and runs test cases to find bugs/deficiencies and feeds them back to developers.
  - **Site reliability engineer (SRE)/Ops engineer**: bridges dev and ops — tracks and runs incident meetings, automates systems/processes, troubleshoots, and owns reliability.
  - **Product manager/owner**: holds the product vision, understands client/end-user needs deeply, and leads development toward the value stakeholders want.
  - **Technical writer/information developer**: translates technical material into end-user-facing docs (manuals, reports, white papers, press releases) — helping both end-users and the customer's ability to give useful feedback.
- What practitioners added beyond the formal role list (**Insiders' Viewpoint**):
  - In practice, the product manager often *also* runs Scrum-master-style duties — daily stand-ups, ticket tracking (e.g., JIRA), unblocking engineers, stakeholder updates — even without a formally separate Scrum master title. Project/program managers were highlighted as increasingly important as systems grow larger and more complex.
  - Engineers commonly split informally (or formally, depending on the company) into architecture/big-picture-focused vs. hands-on coding-focused, and further into specialized tracks like DevOps/infrastructure vs. QA/CI-CD automation.
  - Multiple practitioners emphasized that **close, embedded collaboration beats hand-offs** — regular check-ins, shared brainstorming, and cross-role group chats work better than a waterfall-style relay between roles.
  - Typical UX workflow: UX designers hand off specs (e.g., via Figma) that engineers implement, spanning from early sketches through mockups and iteration; separate **UX researchers** are brought in to interview real users/customers for direct feedback.
  - Typical review loop: code goes to a tech lead/senior engineer for review, then to QA for testing; if QA finds something broken, they write up a test plan or detailed bug report so the developer knows exactly what to fix, and the cycle repeats until QA confirms it's resolved.
  - Engineers said they interact most with product managers/owners (sometimes literally an internal customer) for direction and trade-off discussions, and regularly with SREs/sysadmins (deployment/running the software) and dedicated test engineers (end-to-end, automated, integration testing).
  - Overall theme: as systems get more complex, an engineer is never working in isolation — success depends as much on communicating directly with the team as on writing code.
