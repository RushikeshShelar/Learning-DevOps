# DevOps Bash Scripting Industry Conventions (MNC Level)

Author: Rushikesh Shelar  
Maintainer: Self
Date: 2025-06-11

---

## 📌 1. Shebang Rule

```bash
#!/bin/bash
```
- Always absolute path.
- Mandatory at top of every script.
- Avoid using `#!/usr/bin/env bash` unless required for cross-platform portability.

## 📌 2. Script Metadata Header
```bash
####################
# Author: Rushikesh
# Date: 11/06/2025
# Purpose: Outputs the Node Health
# Usage: ./node-health.sh
# Dependencies: awk, grep, pgrep, coreutils
# OS: Linux (Tested on Ubuntu 22.04 LTS)
# Version: v1.1
####################
```
Include:
- Author
- Date
- Purpose
- Usage
- Dependencies
- OS compatibility
- Version

## 📌 3. Strict Mode Best Practice
```bash
set -x # Debug Mode 
set -e # Exit when Erro
set -o pipefail # Exit if any command in the pipe fails
 
set -euo pipefail # Single command for all Strict Mode
```

| Flag        | Purpose                            |
| ----------- | ---------------------------------- |
| -e          | Exit on any error                  |
| -u          | Exit on unset variable             |
| -o pipefail | Fail pipeline if any command fails |

- Helps prevent silent failures.
- Safer for production-level scripting.
- ✅ Avoid `set -x` in production; use only during debugging.

## 📌 4. Echo Headers for Readable Output
```bash

echo "----- Disk Usage -----"
df -h

echo "----- Memory Usage -----"
free -g

echo "----- CPU Cores -----"
nproc
```
- Helps humans understand the output.
- Easier to debug via logs.

## 📌 5. File Naming Conventions
| Rule                            | Example                    |
| ------------------------------- | -------------------------- |
| Lowercase                       | `backup-database.sh`       |
| Use hyphens `-`                 | `rotate-logs-weekly.sh`    |
| No spaces or special characters | `node-health.sh`           |
| Use extensions                  | `.sh`                      |
| Use timestamps in outputs       | `backup-2025-06-11.sql.gz` |
| Use ISO date format             | `YYYY-MM-DD`               |


## Example Script:
```bash
#!/bin/bash

####################
# Author: Rushikesh
# Date: YYYY-MM-DD
# Purpose: Describe purpose here
# Usage: ./script.sh
# Dependencies: awk, grep, jq, curl
# OS: Linux (Ubuntu 22.04 LTS)
# Version: v1.0
####################

set -euo pipefail

log_file="script_$(date +%F_%T).log"
log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$log_file"; }

main() {
  log "Script Started"
  
  echo "Disk Usage:"
  df -h | tee -a "$log_file"
  
  echo "Memory Usage:"
  free -g | tee -a "$log_file"
  
  echo "CPU Core Count:"
  nproc | tee -a "$log_file"
  
  echo "VSCode Process IDs:"
  pgrep -f vscode || log "No vscode processes found."
  
  log "Script Completed"
}

main "$@"
```
