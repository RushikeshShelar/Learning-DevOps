# Use slim base with Java
FROM openjdk:17-slim

USER root
# Install Python and essential tools
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Add Jenkins user
RUN useradd -m -d /home/jenkins -s /bin/bash jenkins

# Switch to Jenkins home
WORKDIR /home/jenkins

# Make Jenkins the user
USER jenkins