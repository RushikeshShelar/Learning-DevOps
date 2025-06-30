# ⚙️ GitHub Actions – Overview

This folder contains documentation, workflows, and examples related to **GitHub Actions**, GitHub’s built-in automation platform for **CI/CD** and **workflow automation**. Whether you're running tests, building containers, or deploying to cloud platforms, GitHub Actions lets you automate it all – directly from your GitHub repository.

---

## 📌 What is GitHub Actions?

**GitHub Actions** is a powerful automation tool that allows developers to define custom workflows triggered by events such as:

- Code pushes or pull requests
- Issue or comment creation
- Scheduled intervals (cron jobs)
- Manual triggers via the UI (workflow_dispatch)

GitHub Actions integrates seamlessly with your code and version control lifecycle. It enables you to:

- Automate build, test, and deployment pipelines (CI/CD)
- Run linting, formatting, or security checks
- Automate releases, tagging, and publishing packages
- Interact with other services (Slack, AWS, Docker, etc.)

---

## 🧱 Basic Building Blocks

### 🔄[01 - Workflows](./notes/01-workflows.md)

A **workflow** is an automated process defined in a `.yml` file stored in `.github/workflows/`.

Each workflow contains one or more **jobs** and is triggered by a specific **event**.

**Example Workflow File:**

```yaml
name: CI Pipeline

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 18

      - name: Install dependencies
        run: npm install

      - name: Run tests
        run: npm test
```

> 🔹 Workflows are stored in `.github/workflows/*.yml`

---

### ⚙️[02 - Jobs](./notes/02-jobs.md)

A **job** is a collection of steps that run in the same environment (called a **runner**). Jobs can run in **parallel** or **sequentially**, and you can define dependencies between jobs using `needs`.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Building..."

  test:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - run: echo "Running tests..."
```

---

### 🔧[04 - Actions](./notes/04-actions.md)

An **action** is a reusable unit of code that performs a task – like setting up a language, authenticating to a cloud, or sending a Slack message. You can:

- Use **official actions** from GitHub
- Use **third-party actions** from the marketplace
- Write your **own custom actions**

**Example:**

```yaml
- name: Setup Node.js
  uses: actions/setup-node@v4
  with:
    node-version: 18
```

Marketplace: [https://github.com/marketplace/actions](https://github.com/marketplace/actions)

---

### 🔐[05 - Secrets & Environments](./notes/05-secrets-and-env.md)

**Secrets** are used to store sensitive values like API keys, passwords, or access tokens securely. They can be accessed inside workflows via environment variables.

- Add them under **Settings → Secrets and variables → Actions**
- Available as `secrets.SECRET_NAME`

```yaml
- name: Deploy to AWS
  run: aws s3 cp ./dist s3://my-bucket/
  env:
    AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
    AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
```

---

**Environments** in GitHub Actions help manage **deployment-specific variables, secrets, and approval rules**. For example:

- `staging`, `production`, `preview`
- Each can have its own secrets, reviewers, or protection rules.

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - run: echo "Deploying to production..."
```

---

## 🧠 [Additional Concepts](./notes/) 

### ✅ Runners

- GitHub Actions uses **runners** to execute jobs.
- **Hosted runners**: Provided by GitHub (e.g., `ubuntu-latest`, `windows-latest`)
- **Self-hosted runners**: Custom machines that run your workflows (e.g., on-premises, EC2)

### 🔁 Matrix Strategy

Used to run jobs across **multiple environments, versions, or configurations**.

```yaml
strategy:
  matrix:
    node: [16, 18, 20]
```
> 💡 GitHub Actions is powerful yet beginner-friendly. Start small (testing or linting) and gradually evolve your workflows to handle full deployments, security checks, monitoring, and auto-releases.