# ⚙️ GitHub Actions: Actions

**Actions** are reusable units of logic that can be shared across workflows and repositories.  
They form the **building blocks** of each `step` inside a `job`.

You can:
- Use **public actions** from the GitHub Marketplace.
- Use **actions from another repo**.
- Define **custom or composite actions** in your own repo.

---

## 🔸 What is a GitHub Action?

A **GitHub Action** is a packaged piece of code that automates a task.  
Think of it like a reusable function that performs a specific job – such as checking out code, setting up a language runtime, or deploying to AWS.

Actions are used inside a `step` using the `uses:` keyword:

```yaml
- name: Checkout code
  uses: actions/checkout@v4
```

---

## 🔹 Types of Actions

### 1️⃣ **Docker Actions**
- Run in a Docker container.
- Used for OS-specific tasks or when dependencies are complex.
- Defined in `action.yml` and include a `Dockerfile`.

### 2️⃣ **JavaScript Actions**
- Run directly on the runner without a container.
- Fast and best for cross-platform logic.

### 3️⃣ **Composite Actions**
- Group multiple shell commands or actions into a single action.
- Useful to reduce duplication.

Example:
```yaml
name: Greet User
description: Greets the user
inputs:
  username:
    required: true
    default: World

runs:
  using: "composite"
  steps:
    - run: echo "Hello, ${{ inputs.username }}!"
```

---

## 🧩 Using Actions in a Workflow

Example using official actions:

```yaml
steps:
  - uses: actions/checkout@v4

  - uses: actions/setup-node@v4
    with:
      node-version: 18
```

You can also reference actions from GitHub or a private repo:

```yaml
uses: owner/repo@v1
uses: ./path/to/action
```

---

## 🎛️ Passing Inputs and Getting Outputs

```yaml
- name: Use Action with Inputs
  uses: some/action@v1
  with:
    token: ${{ secrets.MY_TOKEN }}
    directory: ./build
```

And to use outputs from an action:
```yaml
- id: greet
  uses: my/action@v1

- run: echo "The result was ${{ steps.greet.outputs.result }}"
```

---

## 🧪 Create Your Own Action

To create a custom action:

1. Create a folder: `my-action/`
2. Add `action.yml`:

```yaml
name: 'My Custom Action'
description: 'Says hello'
inputs:
  name:
    required: true
    default: 'World'

runs:
  using: 'composite'
  steps:
    - run: echo "Hello ${{ inputs.name }}!"
```

3. Use in workflow:
```yaml
- uses: ./my-action
  with:
    name: Rushikesh
```

---

## ⚙️ Matrix Strategy (Parallelism in Actions)

**Matrix builds** allow you to run a job multiple times with different inputs (OS, versions, envs, etc).

### 🔄 Use Case: Test app on multiple Node versions

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node: [14, 16, 18]
    steps:
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}

      - run: npm install
      - run: npm test
```

The above runs 3 jobs in parallel, each with a different Node version.

### 💡 You can use matrices for:

- OS variations (`ubuntu-latest`, `windows-latest`, `macos-latest`)
- Language versions
- Environment configs (prod/dev/test)
- Custom toolchains

---
## 🔹 Official & Common Actions

### ✅ `actions/checkout`

Checks out your repository code so future steps can access it.

```yaml
- name: Checkout repo
  uses: actions/checkout@v4
```

Without this, your job won't have access to the code by default.

---

### ✅ `actions/setup-node`

Sets up the required Node.js version in the workflow runner.

```yaml
- name: Set up Node
  uses: actions/setup-node@v4
  with:
    node-version: 18
```

This also supports caching of `node_modules` and `npm`.

---

### ✅ `appleboy/ssh-action`

Allows running shell commands on a **remote server over SSH**.

```yaml
- name: Deploy via SSH
  uses: appleboy/ssh-action@master
  with:
    host: ${{ secrets.SSH_HOST }}
    username: ${{ secrets.SSH_USER }}
    key: ${{ secrets.SSH_PRIVATE_KEY }}
    script: |
      cd /var/www/myapp
      git pull
      pm2 restart myapp
```

Great for deployment or triggering remote jobs.

