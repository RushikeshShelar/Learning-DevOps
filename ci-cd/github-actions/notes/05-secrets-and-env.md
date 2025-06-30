# GitHub Actions: Secrets & Environment Variables 🔐
When working with CI/CD pipelines, you'll often need to provide secure values like API keys, credentials, tokens, and configuration parameters. GitHub Actions provides robust support for securely managing **secrets**, defining **environment variables**, and using **environments** such as `staging`, `production`, etc.

---

## 🔐 1. GitHub Secrets

### 📌 What are Secrets?

**Secrets** are encrypted environment variables stored in your GitHub repository or organization. They are used to store sensitive data like:

- SSH private keys
- API keys
- Access tokens
- Database credentials

These secrets are not visible in logs and cannot be accessed by pull requests from forks (unless explicitly allowed).

### 📁 Where are Secrets Defined?

- **Repository-level:** Go to **Repo Settings → Secrets and Variables → Actions**
- **Organization-level:** Go to **Org Settings → Secrets**
- **Environment-level:** (more below)

### ✅ Usage in Workflow:

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Use Secret
        run: echo "Using secret!"
        env:
          API_KEY: ${{ secrets.MY_SECRET }}
```

> ⚠️ Tip: Never echo secrets directly in logs. They will be masked by GitHub, but it’s a bad practice.

---

## 🌍 2. Environment Variables

### 💡 What are Environment Variables?

Environment variables are dynamic values available during the workflow run, used to store config like:

- App versions
- File paths
- Feature flags

They can be declared:
- Globally (for the job)
- Step-wise
- In the shell script
- In `.env` files (in combination with custom workflows)

### ✅ Declare globally in a job:

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    env:
      NODE_ENV: production
      PORT: 8080
    steps:
      - run: echo $NODE_ENV
```

### ✅ Declare inside a single step:

```yaml
- name: Set local env
  run: echo "ENV=$NODE_ENV"
  env:
    NODE_ENV: development
```

---

## 🏞️ 3. GitHub Environments

### 📌 What are Environments?

**Environments** like `development`, `staging`, and `production` allow you to define **context-specific secrets**, **deployment protection rules**, and **approvals** before workflows can proceed.

Each environment can:
- Have its own secrets
- Require manual approvals before execution
- Define wait timers or protection rules

This is useful for setting up deployment workflows that promote code through multiple stages safely.

### ✅ Defining Environment in Workflow:

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - name: Deploy App
        run: ./deploy.sh
```

Go to:
`Settings → Environments → New Environment → "production"` to define secrets and protection rules.

---

## 📦 Combining All Together

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: staging
    env:
      ENV_NAME: staging
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Use secret
        run: echo "Connecting to $API_URL"
        env:
          API_URL: ${{ secrets.API_URL }}
```