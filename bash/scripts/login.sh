#!/bin/bash

allowed_users=("rushi" "admin" "devops")

if [[ -z "$1" ]]; then
    echo "Enter Username: \n"
    read username
else
    username="$1"
fi
	
result="FAILURE"
found=false

for user in "${allowed_users[@]}"; do
	if [[ "$1" == "$user" || "$username" == "$user" ]]; then
		found=true
		break
	fi
done

if $found; then
	result="SUCCESS"
	echo "$username Logged In!"	
else
    echo "Idk you! Type 'help' for instructions."
fi

datetime=$(date "+%Y-%m-%d %H:%M:%S")

log_text="[$datetime] User: $username - $result"

echo $log_text >> login.logs
