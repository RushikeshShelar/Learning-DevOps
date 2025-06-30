FROM openjdk:17-slim
USER root
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    docker-cli \
    docker-compose \
    openssh \
    curl \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -d /home/jenkins -s /bin/bash jenkins
WORKDIR /home/jenkins

USER jenkins