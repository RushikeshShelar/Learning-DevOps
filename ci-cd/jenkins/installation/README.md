# Installation of Jenkins (using Docker)

## Using Automated Docker Compose
1. Open up a terminal window.
2. Change to the current Folder.
3. Run Docker Compose
```bash
docker-compose up -d
```
or 
```bash
docker compose up -d
```

4. Open up a terminal window.
5. Create a bridge network in Docker using the following docker network create command:
```bash
docker network create jenkins
```
1. In order to execute Docker commands inside Jenkins nodes, download and run the docker:dind Docker image using the following docker run command:
```bash
docker run \
  --name jenkins-docker \
  --restart unless-stopped \
  --detach \
  --privileged \
  --network jenkins \
  --network-alias docker \
  --env DOCKER_TLS_CERTDIR=/certs \
  --volume jenkins-docker-certs:/certs/client \
  --volume jenkins-data:/var/jenkins_home \
  --publish 2376:2375 \
  docker:dind \
  --storage-driver overlay2
```

1. Customize the official Jenkins Docker image, by executing the following two steps:
    a. Create a Dockerfile with the following content:
    ```bash
    FROM jenkins/jenkins:2.504.3-jdk21
    USER root
    RUN apt-get update && apt-get install -y lsb-release ca-certificates curl && \
        install -m 0755 -d /etc/apt/keyrings && \
        curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc && \
        chmod a+r /etc/apt/keyrings/docker.asc && \
        echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] \
        https://download.docker.com/linux/debian $(. /etc/os-release && echo \"$VERSION_CODENAME\") stable" \
        | tee /etc/apt/sources.list.d/docker.list > /dev/null && \
        apt-get update && apt-get install -y docker-ce-cli && \
        apt-get clean && rm -rf /var/lib/apt/lists/*
    USER jenkins
    RUN jenkins-plugin-cli --plugins "blueocean docker-workflow json-path-api"
    ```

    b. Build a new docker image from this Dockerfile, and assign the image a meaningful name, such as "myjenkins-blueocean:2.504.3-1":
    ```bash
    docker build -t myjenkins-blueocean:2.504.3-1 .
    ```
If you have not yet downloaded the official Jenkins Docker image, the above process automatically downloads it for you.

1. Run your own myjenkins-blueocean:2.504.3-1 image as a container in Docker using the following docker run command:
```bash
docker run \
  --name jenkins-blueocean \
  --restart=on-failure \
  --detach \
  --network jenkins \
  --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client \
  --env DOCKER_TLS_VERIFY=1 \
  --publish 8080:8080 \
  --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  myjenkins-blueocean:2.504.3-1 
```