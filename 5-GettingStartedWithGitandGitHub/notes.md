# Getting Started with Git and GitHub — Notes

## Key Takeaways
- **Version control** tracks changes to source code/files over time, letting you recover old versions and collaborate cleanly; **Git** is a free, open-source (GNU GPL) **distributed version control system (DVCS)** — every developer holds a full local copy of the project history and syncs changes to a remote to share them.
- Git was created in 2005 by **Linus Torvalds** to replace BitKeeper for Linux kernel development, designed around non-linear/distributed development, compatibility with existing systems, efficient handling of large projects, cryptographic authentication of history, and pluggable merge strategies.
- **GitHub** is the most popular web-hosted service for Git repositories (alternatives: GitLab, Bitbucket, Beanstalk); it's owned by a Microsoft subsidiary and offers free, professional, and enterprise tiers.
- Core Git/GitHub terms: **repository** (versioned project storage), **fork** (a copy of a repo), **pull request** (proposed changes submitted for review before merging), **working directory** (local files tied to a repo), **commit** (a snapshot of changes plus a description), **branch** (independent line of development), **merge** (combining branch changes, typically into main), **clone** (local copy of a remote repo), **SSH** (protocol for secure remote login).
- A GitHub **repository** contains code plus supporting artifacts (README, license) and can be public or private; its tabs cover **Code** (source files), **Issues** (tracking/planning), **Pull Requests** (review before merge), **Projects** (planning tools), **Wiki/Security/Insights** (advanced/external-facing), and **Settings** (name/access control). An **organization** is a group of accounts owning shared repos, managed by one or more owners with admin rights.
- Hands-on basics: create a repo (name, description, visibility, optional README init); edit files via the browser's pencil-icon editor; create new files with Add File > Create New File; upload local files with Add File > Upload files — all changes are saved via a **commit** with a commit message.
- All files in a GitHub repo live on a **branch**; the **main branch** holds the definitive, deployable code. New branches start as exact copies of their source branch and hold whatever changes you make from there, so multiple branches can be worked on in parallel before merging their tips together.
- A **commit** saves changes with a descriptive message and signals the code is stable; good commit-message practice: no trailing period, keep the summary under 50 characters, use the extended description field for detail, and write in active voice.
- A **pull request** proposes committed changes for review before merging — GitHub opens one automatically if you change a branch you don't own, and merges are only possible after someone (the author or an assigned reviewer) approves. The main branch stays the only deployed code; once a branch's work is fully merged, delete it as obsolete.

---

## Notes

### Module 1: Git and GitHub Fundamentals

#### Section 1: Getting Started with Git and GitHub

**Overview of Git and GitHub**
- **Version control system**: tracks changes to source code (or any files — images, docs, etc.), making it easy to recover older versions and collaborate without conflicting edits.
- **Git**: free, open-source (GNU GPL) **distributed version control system (DVCS)** — anyone can hold a full local copy of a project and sync changes to a remote server to share them; this distributed model is a big reason for its popularity. Git also supports branching strategies like **feature branching**.
- **GitHub** is one of the most popular web-hosted services for Git repos (others: GitLab, Bitbucket, Beanstalk); Git itself can be used purely via command line, without any web interface.
- Key terms introduced: **SSH** (secure remote login protocol), **repository** (versioned project folder), **fork** (copy of a repo), **pull request** (request to review/approve changes before they're finalized), **working directory** (local files tied to a repo), **commit** (snapshot of project state + change description), **branch** (independent line of development), **merge** (combining branch changes, typically feature → main), **clone** (local copy of a remote repo).

**Introduction to GitHub**
- History: Linux development relied on the free **BitKeeper** system until it went for-fee in 2005, prompting **Linus Torvalds** to build a replacement — Git. Design goals: strong non-linear development support (Linux patches arrived at ~6.7/sec), distributed development (full local history per developer), compatibility with existing systems, efficient handling of large projects, cryptographic authentication of history (ensures distributed copies stay identical), and pluggable merge strategies for complex integration cases.
- Git is a distributed VCS focused on tracking source code, coordinating among programmers, and supporting non-linear workflows. In practice, a **main branch** holds deployable code while teams integrate finished work continuously and develop separately on other branches between releases; Git also supports centralized administration with access-level controls per team.
- Git can be used locally (command line, GitHub Desktop) or through a browser via GitHub.
- **GitHub**: online hosting service for Git repositories, owned by a Microsoft subsidiary, with free/professional/enterprise accounts (100M+ repositories as of August 2019).
- **Repository**: a data structure for storing documents (including source code) that tracks and maintains version control.
- **GitLab** (mentioned as a comparison): a complete DevOps platform built around Git repos, adding code review/commenting, branching/merging, and built-in CI/CD.

**GitHub Repositories**
- Signing up: pick a username, enter email, choose a password, verify you're human (puzzle), select the free personal account plan, optionally skip the work/experience questions, then confirm via the verification email.
- After signup, GitHub offers starting points: create a repository, create an **organization**, or take the intro course. An **organization** is a collection of user accounts that owns repositories, managed by one or more owners with admin privileges.
- A **repository** is the heart of a Git project — holds code and related artifacts like a **README** (describes the project's purpose) and a **license** (defines usage terms). Repos can be **public** (searchable/visible to everyone) or **private** (visible only to permitted accounts).
- Repository tabs: **Code** (source files — where README/license live if nothing else has been added), **Issues** (tracks/plans open work items), **Pull Requests** (mechanism for proposing reviewed changes before merging to main), **Projects** (planning/management tools — core of GitHub's collaborative features), **Wiki / Security / Insights** (more advanced, community-facing tools), **Settings** (rename repo, control access, other personalization).

**GitHub - Getting Started**
- Creating a repo: click **+** > **New Repository**, provide a name, optional description, choose visibility (public/private), and optionally initialize with a README, then click Create Repository.
- Editing files in-browser: click the pencil icon to open the online editor, make changes, then scroll to the Commit changes section, add a commit message (and optional description), and click Commit changes to save.
- Creating a new file: **Add File > Create New File**, provide a filename (e.g., `firstpython.py`), add code/comments, then commit the change.
- Editing an existing file: open the file, click the pencil icon, edit, and commit.
- Uploading local files: **Add File > Upload files**, choose files from your system, wait for upload, then click Commit Changes.

#### Section 2: Branches with GitHub

**GitHub Branches**
- All files in GitHub live on a **branch**. The **main branch** (created by default, though any branch can serve this role) holds the definitive, deployable version of the code. To make changes, create a new branch with a descriptive name — it starts as an exact copy of the source branch, and your edits then accumulate there. Create one via the branch dropdown (default "Main") > enter a new branch name > **Create Branch**.
- Simple branching flow: start from a common base, branch off to develop new features (multiple branches can be in progress simultaneously), then merge each branch's tip together — e.g., two feature branches merging into a combined branch.
- Editing a file on a branch: select the file, click the pencil icon, make changes, and **commit**. A commit signals the developer considers the code a stable checkpoint for the feature(s) being built, and requires a descriptive commit message. You can commit directly to the current branch or create a new branch at commit time.
- Commit message best practices: no trailing period, keep the summary under 50 characters (use the extended description field for detail), and write in active voice.
- A **pull request** initiates merging by making committed changes available for review — it can follow any commit, even unfinished code, and requires approval (by the author or an assigned reviewer) before merging. GitHub auto-creates a pull request if you change a branch you don't own; since logs are immutable, who approved a merge is always traceable. To open one: **Pull requests > New pull request**, select the branch to compare, review the diff, add a title/description, and **Create pull request**.
- Merging: the main branch is meant to hold only released code, so branch changes aren't live until they're committed, pulled, reviewed, approved, and merged back in. To merge, click **Merge pull request**, then **Confirm merge**. Once a branch's work is fully merged, it's obsolete and should be deleted.
