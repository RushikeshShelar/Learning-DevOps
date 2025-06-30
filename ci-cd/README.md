# 🚀 CI/CD – Continuous Integration and Continuous Delivery

This folder documents the core concepts, workflows, and tooling around **CI/CD (Continuous Integration and Continuous Delivery/Deployment)**. It also contains practical setups using **GitHub Actions** and **Jenkins**, both widely used automation servers/tools for implementing CI/CD pipelines.

---

## 📌 What is CI/CD?

**CI/CD** is a modern software engineering practice that automates the process of integrating code changes, running tests, and deploying applications. It brings speed, consistency, and reliability to software delivery by reducing manual intervention.

- **Continuous Integration (CI)**: Automatically integrates and tests code changes whenever a developer pushes updates to a shared repository. The goal is to detect bugs early, ensure code correctness, and maintain a healthy codebase.
- **Continuous Delivery (CD)**: Ensures that the integrated code is always in a deployable state. Artifacts are automatically built and tested and can be manually or automatically deployed to staging/production environments.
- **Continuous Deployment (also CD)**: An extension of Continuous Delivery, where every change that passes automated tests is **automatically deployed** to production without human intervention.

---

## 🌍 Where is CI/CD Used?

CI/CD is essential in nearly every modern software delivery workflow:

- **Web and Mobile Applications**: For automatically testing and deploying apps to servers or cloud platforms.
- **Microservices**: To manage builds and deployments across multiple services with independent pipelines.
- **DevOps & SRE**: CI/CD is a core pillar of DevOps practices, allowing quick iteration and reliable operations.
- **Infrastructure as Code (IaC)**: For provisioning and updating infrastructure using tools like Terraform or Ansible.
- **Open Source Projects**: To test pull requests, verify contributions, and generate artifacts across platforms.

---

## ⚙️ How Does CI/CD Work?

The CI/CD pipeline begins when a developer pushes code to a version control system like **GitHub**. That action triggers the pipeline defined in a CI/CD tool (like GitHub Actions or Jenkins), which then goes through several predefined stages such as:

1. **Code Checkout**: The pipeline pulls the latest code from the repository.
2. **Build**: Source code is compiled or packaged (e.g., into Docker images or zip archives).
3. **Test**: Automated tests (unit, integration, E2E) are executed to validate functionality.
4. **Artifact Generation**: Build outputs (e.g., binaries, images) are stored in an artifact store or registry.
5. **Deploy**: The application is deployed to staging, test, or production environments.
6. **Notify/Monitor**: Notifications are sent via Slack, email, or dashboards; monitoring and health checks begin.

> 🔁 The pipeline repeats every time a change is pushed, ensuring fast feedback and reliable delivery.

---

## 🧱 Core Concepts of CI/CD

### 1. **Pipeline**
A series of automated steps that run sequentially or in parallel to validate and deploy changes. Pipelines are defined in YAML files (`.github/workflows/`, `Jenkinsfile`, etc.)

### 2. **Stages (Phases)**
- **Build**: Compile or bundle code, create containers.
- **Test**: Run tests to validate code behavior.
- **Deploy**: Move code to an environment (staging, production).
- **Post**: Cleanup, notify, or log results.

### 3. **Triggers**
Events that initiate the pipeline – such as pushing to a branch, creating a pull request, or on a schedule.

### 4. **Runners/Agents**
Servers that execute the steps defined in the pipeline. GitHub provides hosted runners; Jenkins requires setting up agents.

### 5. **Secrets and Environment Variables**
Used to securely pass credentials, tokens, or config values into pipelines.

### 6. **Artifacts**
Files produced during the pipeline process (e.g., `.jar`, `.zip`, `.html`, Docker image), which can be reused or deployed.

### 7. **Version Control Integration**
CI/CD systems are tightly integrated with Git. Every pipeline run is tied to a specific commit, making it easy to trace changes.


## CI/CD Core Tools
1. [Github Actions](./github-actions/)
2. [Jenkins](./jenkins/)