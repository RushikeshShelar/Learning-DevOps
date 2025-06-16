# Container Basics

## Publishing and exposing ports
If you've been following the guides so far, you understand that containers provide isolated processes for each component of your application. Each component - a React frontend, a Python API, and a Postgres database - runs in its own sandbox environment, completely isolated from everything else on your host machine. This isolation is great for security and managing dependencies, but it also means you can’t access them directly. For example, you can’t access the web app in your browser.

That’s where port publishing comes in.

### Publishing ports
Publishing a port provides the ability to break through a little bit of networking isolation by setting up a forwarding rule. As an example, you can indicate that requests on your host’s port `8080` should be forwarded to the container’s port `80`. Publishing ports happens during container creation using the `-p` (or `--publish`) flag with `docker run`. The syntax is:
```bash
 docker run -d -p HOST_PORT:CONTAINER_PORT nginx
```
- `HOST_PORT`: The port number on your host machine where you want to receive traffic
- `CONTAINER_PORT`: The port number within the container that's listening for connections
  
For example, to publish the container's port `80` to host port `8080`:
```bash
 docker run -d -p 8080:80 nginx
```
Now, any traffic sent to port 8080 on your host machine will be forwarded to port 80 within the container.

### Publishing to ephemeral ports
At times, you may want to simply publish the port but don’t care which host port is used. In these cases, you can let Docker pick the port for you. To do so, simply omit the `HOST_PORT` configuration.

For example, the following command will publish the container’s port `80` onto an ephemeral port on the host:
```bash
 docker run -p 80 nginx
```
Once the container is running, using `docker ps` will show you the port that was chosen:
```bash
docker ps
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS          PORTS                    NAMES
a527355c9c53   nginx         "/docker-entrypoint.â¦"   4 seconds ago    Up 3 seconds    0.0.0.0:54772->80/tcp    romantic_williamson
```
In this example, the app is exposed on the host at port 54772.

### Publishing all ports
When creating a container image, the `EXPOSE` instruction is used to indicate the packaged application will use the specified port. These ports aren't published by default.

With the `-P` or `--publish-all` flag, you can automatically publish all exposed ports to ephemeral ports. This is quite useful when you’re trying to avoid port conflicts in development or testing environments.

For example, the following command will publish all of the exposed ports configured by the image:
```bash
docker run -P nginx
```

## Overriding container defaults

### Overriding the network ports
Sometimes you might want to use separate database instances for development and testing purposes. Running these database instances on the same port might conflict. You can use the `-p` option in `docker run` to map container ports to host ports, allowing you to run the multiple instances of the container without any conflict.
```bash
 docker run -d -p HOST_PORT:CONTAINER_PORT postgres
```

### Setting environment variables
This option sets an environment variable `foo` inside the container with the value `bar`.
```bash
docker run -e foo=bar postgres env
```

- TIP
The `.env` file acts as a convenient way to set environment variables for your Docker containers without cluttering your command line with numerous `-e` flags. To use a `.env` file, you can pass `--env-file` option with the `docker run` command.
```bash
docker run --env-file .env postgres env
```

### Restricting the container to consume the resources
You can use the `--memory` and `--cpus` flags with the `docker run` command to restrict how much CPU and memory a container can use. For example, you can set a memory limit for the Python API container, preventing it from consuming excessive resources on your host. Here's the command:
```bash
docker run -e POSTGRES_PASSWORD=secret --memory="512m" --cpus="0.5" postgres
``` 
This command limits container memory usage to 512 MB and defines the CPU quota of 0.5 for half a core.




