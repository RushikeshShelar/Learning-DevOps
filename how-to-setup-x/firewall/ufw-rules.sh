#!/bin/bash

# setup-firewall.sh — Best Practices UFW Setup Script

echo "🔐 Setting up UFW with best practices..."

# Exit on error
set -e

# Check if UFW is installed
if ! command -v ufw &> /dev/null
then
    echo "⚠️  UFW not found. Installing..."
    sudo apt update && sudo apt install ufw -y
else
    echo "✅ UFW is already installed."
fi

echo "🚧 Setting default policies..."
sudo ufw default deny incoming
sudo ufw default allow outgoing

echo "✅ Allowing essential ports..."
sudo ufw allow 22/tcp     # SSH
sudo ufw allow 80/tcp     # HTTP
sudo ufw allow 443/tcp    # HTTPS
sudo ufw allow 3000/tcp   # Common local dev port

# Enable Logging
echo "📝 Enabling UFW logging (low level)..."
sudo ufw logging on

# Enable UFW if not already active
echo "🚀 Enabling UFW..."
sudo ufw --force enable

echo "🔍 Current firewall status:"
sudo ufw status verbose

echo "✅ UFW setup complete with secure defaults."
