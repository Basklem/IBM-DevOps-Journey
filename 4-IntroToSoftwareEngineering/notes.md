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
