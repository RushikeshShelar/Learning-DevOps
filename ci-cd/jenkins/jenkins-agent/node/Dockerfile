FROM jenkins/inbound-agent:alpine

USER root

RUN apk add --no-cache \
    nodejs \
    npm \
    docker-cli \
    openssh \
    git \
    curl

USER jenkins
