# 🧩 GitHub Actions: Jobs

This document focuses on **Jobs** in GitHub Actions — the core building blocks of a workflow. Jobs group steps and control the **execution environment**, **parallelism**, **dependencies**, and **execution logic**.

---

## 🏗️ What is a Job?

A **job** is a collection of **steps** that execute on the same runner environment. Jobs can run in **parallel** or **sequentially**, depending on how you configure their dependencies.

Each job:
- Runs in a fresh virtual machine (runner) unless otherwise specified.
- Has its own environment, context, and permissions.
- Contains a list of **steps** that execute commands or reusable actions.

---

## 🧬 Anatomy of a Job

```yaml
jobs:
  build:
    name: Build App
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Install dependencies
        run: npm install

      - name: Build
        run: npm run build
```

### Key Fields

| Field             | Description                                                      |
| ----------------- | ---------------------------------------------------------------- |
| `name`            | (Optional) A friendly name for the job                           |
| `runs-on`         | The runner environment (e.g., `ubuntu-latest`, `windows-latest`) |
| `steps`           | A list of shell commands or actions to run                       |
| `needs`           | Used to make jobs run after other jobs                           |
| `if`              | Conditional execution of a job                                   |
| `env`             | Environment variables scoped to the job                          |
| `timeout-minutes` | Timeout limit for the job                                        |
| `strategy`        | Used for matrix builds (described in the workflow doc)           |

---

## ⚙️ Runner Environments

Jobs need to specify where they will run:

```yaml
runs-on: ubuntu-latest  # Can also use macos-latest or windows-latest
```

Self-hosted runners can be used for specialized hardware or tighter control.

---

## 🔁 Running Jobs in Parallel

By default, all jobs run **in parallel**, unless you explicitly set dependencies:

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps: [...]

  lint:
    runs-on: ubuntu-latest
    steps: [...]

  test:
    runs-on: ubuntu-latest
    steps: [...]
```

All 3 jobs will run simultaneously if there are enough runners available.

---

## 🔗 Dependent Jobs (Sequential Execution)

You can specify dependencies using the `needs:` keyword.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps: [...]

  test:
    runs-on: ubuntu-latest
    needs: build
    steps: [...]

  deploy:
    runs-on: ubuntu-latest
    needs: [test]
    steps: [...]
```

Here, `test` runs only after `build` is successful, and `deploy` only after `test`.

---

## ✅ Conditional Job Execution

Jobs can also have `if` conditions to control when they run:

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
    steps: [...]
```

This ensures deployment only happens on `push` to the `main` branch.

---

## 🔐 Job-scoped Environment Variables

You can define variables that apply only within the job:

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    env:
      NODE_ENV: test
    steps:
      - run: echo $NODE_ENV
```

---

## 🛠️ Example: Multi-Job Workflow (Build → Test → Deploy)

```yaml
name: CI/CD Pipeline

on: push

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm install
      - run: npm run build

  test:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - uses: actions/checkout@v4
      - run: npm test

  deploy:
    runs-on: ubuntu-latest
    needs: test
    if: github.ref == 'refs/heads/main'
    steps:
      - run: echo "Deploying to production..."
```