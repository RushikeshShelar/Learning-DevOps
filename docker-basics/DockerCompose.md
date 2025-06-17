# Docker Compose

## What is Docker Compose?

Docker Compose is a **tool for defining and running multi-container Docker applications**. It uses a YAML file to configure all your application’s services, networks, and volumes in a single file called `docker-compose.yml`.

Instead of running `docker run` for each container, Docker Compose allows you to **define your entire stack once and start everything with a single command**.

---

## Why is Docker Compose Needed?

- Simplifies multi-container orchestration (e.g. frontend + backend + database).
- Improves local development and CI/CD workflows.
- Avoids manual container linking and port management.
- Encapsulates service configuration in a single source of truth (`docker-compose.yml`).

---

## How Does Docker Compose Work?

Docker Compose works in **three main steps**:

1. **Define services** in `docker-compose.yml`.
2. **Run `docker-compose up`** to start and build services.
3. **Manage containers** using `docker-compose` CLI commands.

---

## Example: Simple `docker-compose.yml` File

```yaml
version: '3.8'

services:
  web:
    image: nginx
    ports:
      - "8080:80"

  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD: example
```

### Running the Compose File

```bash
docker-compose up
```

- Add `-d` to run in detached mode:
  ```bash
  docker-compose up -d
  ```

- To stop and remove:
  ```bash
  docker-compose down
  ```

---

## Docker Compose File Structure

---

### ✅ `version` and `name` Top-Level Elements

#### `version`
Specifies the syntax version of the Compose file.
```yaml
version: '3.8'
```

#### `name`
Optional project name (defaults to directory name). Can be overridden via:
```bash
docker-compose -p myproject up
```

---

### ✅ `services` Top-Level Element

Defines the containers that make up your application.

#### Example:
```yaml
services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=development
    depends_on:
      - db

  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD: secret
```

#### Common `services` attributes:

| Attribute       | Description                                     |
|----------------|-------------------------------------------------|
| `image`         | Use an existing Docker image                    |
| `build`         | Build from Dockerfile                          |
| `ports`         | Map host:container ports                        |
| `environment`   | Set env variables                              |
| `volumes`       | Mount host paths or named volumes               |
| `depends_on`    | Define service dependencies                     |
| `command`       | Override default command                        |
| `restart`       | Restart policy (`always`, `on-failure`, etc.)  |
| `networks`      | Attach to one or more networks                  |

---

### ✅ `networks` Top-Level Element

Used to define and configure custom networks.

#### Example:
```yaml
networks:
  app-net:
    driver: bridge
```

#### Connecting Services:
```yaml
services:
  app:
    networks:
      - app-net
  db:
    networks:
      - app-net
```

#### Common `networks` attributes:

| Attribute   | Description                          |
|------------|--------------------------------------|
| `driver`    | Network driver (`bridge`, `overlay`) |
| `ipam`      | IP address management                |
| `external`  | Use an existing network              |

---

### ✅ `volumes` Top-Level Element

Defines named volumes for data persistence.

#### Example:
```yaml
volumes:
  db-data:
```

#### Using Volumes in Services:
```yaml
services:
  db:
    image: postgres
    volumes:
      - db-data:/var/lib/postgresql/data
```

#### Common `volumes` attributes:

| Attribute   | Description                      |
|------------|----------------------------------|
| `driver`    | Volume driver (default: local)   |
| `external`  | Use pre-existing volume          |
| `driver_opts` | Custom volume options          |

---

### ✅ `configs` Top-Level Element

Used to store non-sensitive configuration data.

#### Example:
```yaml
configs:
  my-config:
    file: ./my-config.txt

services:
  app:
    image: nginx
    configs:
      - source: my-config
        target: /etc/nginx/conf.d/my-config.txt
```

---

### ✅ `secrets` Top-Level Element

Used to manage sensitive data like API keys, passwords, etc.

> ⚠️ Requires Docker Swarm mode

#### Example:
```yaml
secrets:
  db-password:
    file: ./db-password.txt

services:
  db:
    image: mysql
    secrets:
      - db-password
```

---

## Summary: Compose File Elements

| Element   | Purpose                                  |
|-----------|------------------------------------------|
| `version` | Defines compose file format version      |
| `services`| Defines containers and configurations     |
| `networks`| Creates and connects virtual networks     |
| `volumes` | Manages persistent data volumes          |
| `configs` | Adds config files to containers           |
| `secrets` | Provides secure access to sensitive data |

---

## Key Docker Compose Commands

| Command                        | Description                                 |
|--------------------------------|---------------------------------------------|
| `docker-compose up`            | Start and run services                      |
| `docker-compose up -d`         | Run services in the background              |
| `docker-compose down`          | Stop and remove services                    |
| `docker-compose build`         | Build or rebuild services                   |
| `docker-compose logs`          | View logs of services                       |
| `docker-compose exec <svc>`    | Run a command inside a running container    |
| `docker-compose ps`            | List running services and ports             |


---

> 🛠️ **Tip:** Use `.env` files with Compose to manage environment variables cleanly across services.

---
