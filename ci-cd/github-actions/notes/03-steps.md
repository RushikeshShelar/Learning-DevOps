# 🧱 GitHub Actions: Steps

A **Step** is a single task within a **job**. Each step runs in the same virtual environment and can run shell commands or call prebuilt **actions**.

Steps are the most granular unit of execution in a GitHub Actions workflow.

---

## 🔹 What is a Step?

A **step** represents an individual command or action executed as part of a job. It could be:
- A shell command (e.g., `npm install`)
- A built-in or custom GitHub Action (e.g., `actions/checkout@v4`)

All steps within a job share the **same workspace** and **filesystem**.

---

## 🧬 Structure of a Step

Each step has one of two forms:
1. Run a shell command using `run`
2. Use an external action with `uses`

```yaml
jobs:
  example-job:
    runs-on: ubuntu-latest
    steps:
      - name: Run a Shell Command
        run: echo "Hello, World!"

      - name: Use an Action
        uses: actions/checkout@v4
```

---

## 🔑 Common Step Keywords

| Keyword             | Purpose                                  |
| ------------------- | ---------------------------------------- |
| `name`              | Optional display name of the step        |
| `uses`              | Reference to a GitHub Action             |
| `run`               | A shell command or script                |
| `with`              | Parameters to pass to an action          |
| `env`               | Environment variables scoped to the step |
| `if`                | Conditional execution of the step        |
| `continue-on-error` | Don’t fail job if step fails             |

---

## 📦 Using Prebuilt Actions with `uses`

To use a GitHub Action from the marketplace:

```yaml
- name: Checkout repository
  uses: actions/checkout@v4
```

You can also pass inputs to the action:

```yaml
- name: Setup Node.js
  uses: actions/setup-node@v4
  with:
    node-version: 18
```

---

## ⚙️ Running Shell Commands with `run`

You can execute one or multiple shell commands:

```yaml
- name: Install dependencies
  run: |
    npm install
    npm audit fix
```

The default shell on Ubuntu runners is `bash`.

---

## 📁 Shared Workspace Across Steps

All steps in the same job **share the workspace**, meaning:

```yaml
- run: echo "file created" > hello.txt

- run: cat hello.txt  # ✅ This works because file is in same workspace
```

This makes it easy to pass artifacts, intermediate files, or results between steps.

---

## 📌 Setting Environment Variables for a Step

```yaml
- name: Use custom env vars
  run: echo "ENV is $MY_VAR"
  env:
    MY_VAR: dev
```

This `env` only applies to this step.

---

## 🚦 Conditional Step Execution

Like jobs, steps can also have `if` conditions:

```yaml
- name: Run only on main
  if: github.ref == 'refs/heads/main'
  run: echo "Deploying on main branch"
```

---

## ❗ Handling Failures Gracefully

If you don’t want a step to stop the workflow on failure:

```yaml
- name: Try to deploy
  run: ./deploy.sh
  continue-on-error: true
```

Useful for non-critical steps like cleanup or optional testing.

---

## ✅ Example: Combined Step Use

```yaml
jobs:
  node-app:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 18

      - name: Install Dependencies
        run: npm ci

      - name: Run Tests
        run: npm test

      - name: Build App
        run: npm run build
```