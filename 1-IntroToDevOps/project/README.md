**Note on authorship:** This project's code and pipeline were built with Claude (Anthropic). I'm still early in my DevOps/software engineering journey, so I leaned on Claude to help generate the code, workflow config, and this write-up — while I directed the project scope and pipeline requirements, and worked through the setup and debugging myself (including fixing a path mismatch that kept the workflow from triggering). I plan to rely on it less as I build up more hands-on experience through this certificate.

# Course 1 Project — Tiny Unit Converter + CI Pipeline

**Course:** Introduction to DevOps (Course 1 of 15, IBM DevOps and Software Engineering)

## Why this project

Course 1 is concept-heavy — plan, code, build, test, release, deploy, operate,
monitor — rather than hands-on labs. Instead of trying to force a big app,
this project keeps the *code* deliberately small (a unit converter CLI) and
puts the actual learning into the **pipeline** wrapped around it.

## What I learned

- The core DevOps loop: every change should be automatically **linted** and
  **tested** before it's trusted, without a human manually running commands.
- Automation isn't about the app being complex — it's about making *any*
  app's feedback loop fast and reliable.
- CI is the foundation everything else (CD, monitoring, rollback) builds on
  top of, which is why this project stops at "lint + test on every push"
  rather than trying to also deploy anywhere.

## What it does

A CLI tool that converts between:
- Celsius ↔ Fahrenheit
- Miles ↔ Kilometers
- Pounds ↔ Kilograms

```bash
cd app
pip install -r requirements.txt
python converter.py c2f 100
# 100.0 -> 212.00
```

## The pipeline

On every push or pull request touching this project, GitHub Actions:
1. Checks out the repo
2. Installs dependencies
3. Runs `ruff` (lint check)
4. Runs the `pytest` suite

See [`.github/workflows/ci.yml`](.github/workflows/ci.yml) — note this file
needs to live at the **repo root** `.github/workflows/`, not nested here;
GitHub only picks up workflow files from that top-level path. It's included
in this folder for documentation purposes, but the working copy needs to be
moved to `<repo-root>/.github/workflows/ci.yml`.

## What I'd do differently

- Add a coverage report step once I've learned more about test strategy
  later in the certificate.
- Revisit this once I hit the CI/CD-specific course — likely add a badge to
  this README showing pipeline status.
