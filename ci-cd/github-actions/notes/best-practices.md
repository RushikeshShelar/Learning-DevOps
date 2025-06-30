# ✅ 07 - Best Practices for GitHub Actions

GitHub Actions is a powerful automation tool. But like any automation system, its effectiveness depends on how well you **structure**, **secure**, and **optimize** your workflows.

This guide highlights best practices across core components of GitHub Actions:

---

## 🧩 1. Workflows

### ✅ Do

- **Split large workflows** into modular workflows based on the purpose: e.g., `ci.yml`, `lint.yml`, `release.yml`.
- **Use reusable workflows** (`workflow_call`) for repeated patterns like build + test + deploy.
- **Name your workflows** and jobs clearly. This helps with readability and debugging.

```yaml
name: CI Pipeline
on: [push, pull_request]
```

### ❌ Avoid

- Long, monolithic workflows doing everything from build to deploy.
- Triggering workflows on every commit if not necessary — use `paths`, `branches`, etc. filters.

---

## ⚙️ 2. Jobs

### ✅ Do

- Use `needs` to define job dependencies rather than repeating steps.
- Use **job matrices** for OS, language, or version compatibility testing.
- Prefer descriptive job names (`name:`) and IDs (`build-backend` over `job1`).

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node: [16, 18, 20]
```

### ❌ Avoid

- Running unrelated jobs in parallel if they depend on the same resources.
- Hard-coding `runs-on` without flexibility — use `matrix` where it adds value.

---

## 🪜 3. Steps

### ✅ Do

- Use **named steps** for clarity in logs and failure debugging.

```yaml
- name: Install dependencies
  run: npm install
```

- Group logically-related steps using `if` conditions.
- Use `continue-on-error: true` for non-blocking steps (e.g., lint warnings).

### ❌ Avoid

- Writing long multiline `run:` scripts in a single step — break them down.
- Adding secrets directly in `run` commands (`echo $SECRET`).

---

## 🧱 4. Actions

### ✅ Do

- Use **official actions** or popular, community-vetted actions.
- Pin actions to a **commit SHA** or specific version — avoid floating `@main`.

```yaml
uses: actions/checkout@v4 # ✅ Safe
uses: actions/setup-node@v4 # ✅ Official and pinned
```

- Create **custom local actions** when logic is repeated across workflows.

### ❌ Avoid

- Blindly using third-party actions without inspecting source/reputation.
- Relying on outdated/unmaintained GitHub Actions.

---

## 🔐 5. Secrets & Environment Variables

### ✅ Do

- Store **secrets** using GitHub's **encrypted Secrets Manager** (`Settings > Secrets`).
- Access secrets using `${{ secrets.MY_SECRET }}` syntax.
- Use **Environments** like `staging`, `production` to gate deployment secrets.

```yaml
jobs:
  deploy:
    environment: production
    env:
      API_KEY: ${{ secrets.PROD_API_KEY }}
```

- Use `env:` block to define global or job-level env variables.

### ❌ Avoid

- Hardcoding sensitive credentials or API keys in the YAML.
- Exposing secrets in logs (`echo $API_KEY`).

---

## 📦 6. Artifacts & Caching

### ✅ Do

- Use `upload-artifact` to share test logs, build outputs, and reports.
- Set `retention-days` for artifacts to avoid storage bloat.

```yaml
- uses: actions/upload-artifact@v4
  with:
    name: test-results
    path: ./results/
    retention-days: 5
```

- Use `actions/cache` to speed up dependencies install (e.g., `node_modules`, `~/.cache/pip`).
- Use `hashFiles()` to invalidate cache when inputs (e.g., lock files) change.

```yaml
key: npm-cache-${{ hashFiles('**/package-lock.json') }}
```

### ❌ Avoid

- Using cache for build artifacts — cache should store **inputs**, not outputs.
- Uploading huge files or entire `.git` directories as artifacts.

---

## 🚀 Additional Tips

- Use `outputs` to pass data between jobs.
- Use `workflow_dispatch` for manual triggers (great for testing).
- Add status badges to your README:

```md
![CI](https://github.com/user/repo/actions/workflows/ci.yml/badge.svg)
```

- Debug with `ACTIONS_STEP_DEBUG=true` or GitHub’s `debug` feature.