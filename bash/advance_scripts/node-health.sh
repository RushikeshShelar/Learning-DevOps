#!/bin/bash

####################
# Author: Rushikesh
# Date: 11/06/2025
# Purpose: Outputs the Node Health
# Usage: ./node-health.sh
# Dependencies: 
# OS: Linux (Tested on Ubuntu 22.04 LTS)
# Version: v1
####################

set -x #debug mode
set -e # exit script when there is error
set -o pipefail

#set -exo pipefail

df -h

free -g

nproc

ps -ef | grep "vscode" | awk -F" " '{print $2}'
