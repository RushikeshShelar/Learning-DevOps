# 🧩 GitHub Actions: Workflows

GitHub Actions enables powerful CI/CD and automation capabilities through **workflows** – the backbone of any automated pipeline. This document explores what workflows are, how they’re structured, common triggers, real-world use cases, and best practices.

---

## ✅ What is a Workflow?

A **workflow** is a YAML configuration file that defines a set of instructions to **automate tasks** such as:

- Running unit tests
- Building applications
- Deploying to cloud services
- Running scheduled jobs (cron)
- Sending notifications or alerts

Workflows reside in the `.github/workflows/` directory of your GitHub repository and can contain **multiple jobs and steps**.

---

## 🧱 Workflow File Structure

A basic workflow file includes the following sections:

```yaml
name: Node CI

on:                             # Trigger
  push:
    branches: [main]

jobs:                           # One or more jobs
  build:
    runs-on: ubuntu-latest      # Runner/Environment
    steps:
      - uses: actions/checkout@v4
      - name: Install Dependencies
        run: npm install
      - name: Run Tests
        run: npm test
```

### Breakdown:
- `name`: Optional display name of the workflow
- `on`: Defines **when** the workflow runs (event-based)
- `jobs`: Defines **what** should happen when the workflow is triggered
- `runs-on`: Specifies the runner environment (e.g., `ubuntu-latest`)
- `steps`: Individual units inside a job (each is a shell command or action)

---

## 🚀 Trigger Types (`on` block)

Workflows are initiated by events that occur in your GitHub repository. Some popular **trigger types** include:

### 🔹 Push / Pull Request

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
```
Triggered when changes are pushed or PRs are opened/updated.

### 🔹 Manual Trigger (`workflow_dispatch`)

```yaml
on:
  workflow_dispatch:
```
Allows you to **run workflows manually** from the GitHub Actions UI.

### 🔹 Scheduled Runs (`schedule`)

```yaml
on:
  schedule:
    - cron: '0 0 * * *'  # Runs every day at midnight UTC
```
Useful for regular jobs like nightly builds or cleanup tasks.

### 🔹 Repository Events

```yaml
on:
  issues:
    types: [opened]
  release:
    types: [published]
```
Trigger workflows when issues are opened or releases are published.

---

## 🏭 Industry Use Cases

| Industry         | Use Case                                           |
| ---------------- | -------------------------------------------------- |
| SaaS             | Auto-deploy backend on push to `main`              |
| E-Commerce       | Run tests + bundle frontend with every PR          |
| Open Source      | Lint and test PRs, auto-assign reviewers           |
| DevOps           | Publish Docker images to ECR or Docker Hub         |
| Data Engineering | Scheduled ETL workflow triggered every night       |
| Mobile Dev       | Build and upload APK/IPA to TestFlight or Firebase |

---
## 🔍 Example: Separate CI & CD Workflows

```yaml
# .github/workflows/ci.yml
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps: ...

# .github/workflows/deploy.yml
on:
  workflow_run:
    workflows: ["CI"]
    types: [completed]
jobs:
  deploy:
    runs-on: ubuntu-latest
    if: ${{ github.event.workflow_run.conclusion == 'success' }}
    steps: ...
```
