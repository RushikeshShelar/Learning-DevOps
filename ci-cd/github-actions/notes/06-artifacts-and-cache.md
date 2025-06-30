# 📦 Artifacts & Caching in GitHub Actions

When working with CI/CD pipelines, it's essential to manage **build outputs**, **dependencies**, and **intermediate files** effectively. GitHub Actions provides two powerful mechanisms to help with this:

- **Artifacts** → Share build results or logs between jobs or store them for later download.
- **Cache** → Speed up workflows by reusing dependencies or files between runs.

---

## 📦 1. Artifacts

### 🔍 What are Artifacts?

Artifacts are files or directories that a job uploads at the end of a workflow or passes to another job. They are used to:

- Share test reports or logs
- Store compiled binaries
- Keep screenshots or coverage reports
- Download outputs post-build

> Artifacts are stored per-workflow and are retained by default for 90 days (configurable).

### ✅ Uploading Artifacts

Use the official [`actions/upload-artifact`](https://github.com/actions/upload-artifact) action:

```yaml
- name: Upload Build Output
  uses: actions/upload-artifact@v4
  with:
    name: my-artifact
    path: path/to/build/output/
```

### ✅ Downloading Artifacts (Same Workflow)

Use the [`actions/download-artifact`](https://github.com/actions/download-artifact) action in a later job:

```yaml
- name: Download Build Output
  uses: actions/download-artifact@v4
  with:
    name: my-artifact
    path: ./restored-output/
```

> 📦 Tip: Combine artifacts with job dependencies to pass data from one job to another.

### 🔧 Example: Share test reports between jobs

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: pytest > report.txt
      - uses: actions/upload-artifact@v4
        with:
          name: test-report
          path: report.txt

  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: test-report
      - run: cat test-report/report.txt
```

---

## ⚡ 2. Caching

### 🔍 What is Caching?

Caching helps speed up workflows by saving and restoring files between runs. It’s ideal for:

- Node modules (`node_modules`)
- Python packages (`.venv`, `__pycache__`)
- Build tools like Maven, Gradle, npm, pip, composer, etc.

> Caches are scoped per **branch** by default and can be shared using key strategies.

### ✅ Using Cache

Use the official [`actions/cache`](https://github.com/actions/cache) action:

```yaml
- name: Cache Node Modules
  uses: actions/cache@v4
  with:
    path: node_modules
    key: node-modules-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      node-modules-
```

### 🧠 How It Works

- `key`: Defines the cache lookup key. If found, it's restored.
- `restore-keys`: Fallback keys if the main key is not found.
- `path`: Files or directories to cache.

> ⚠️ Cache is not meant for passing data between jobs (use Artifacts for that).

---

## ⚖️ Artifacts vs Cache

| Feature    | Artifacts                                      | Cache                                      |
| ---------- | ---------------------------------------------- | ------------------------------------------ |
| Purpose    | Share files across jobs or download post-build | Speed up builds by reusing dependencies    |
| Lifespan   | Saved with workflow (default 90 days)          | Reused across workflow runs                |
| Access     | Used for logs, binaries, coverage reports      | Used for package managers, compilers, etc. |
| Cross-job? | ✅ Yes                                          | ❌ No (job-scoped)                          |
| Cross-run? | ❌ No                                           | ✅ Yes                                      |

---

## 🚀 Practical Use Cases

### 🧪 Testing Logs

```yaml
- name: Upload Test Logs
  if: failure()
  uses: actions/upload-artifact@v4
  with:
    name: failed-tests
    path: ./test-output/logs/
```

### ⚡ Cache Python packages

```yaml
- uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
    restore-keys: |
      ${{ runner.os }}-pip-
```