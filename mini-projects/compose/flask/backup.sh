#!/bin/bash
timestamp=$(date +"%Y%m%d_%H%M%S")
backup_dir="./backups"
mkdir -p "$backup_dir"
docker cp $(docker-compose ps -q db):/var/lib/mysql "$backup_dir/mysql_$timestamp"
echo "✅ Backup done: mysql_$timestamp"
