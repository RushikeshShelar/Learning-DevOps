#!/bin/bash
showuptime(){
local uptime=$(uptime -p | cut -c4-)
local since=$(uptime -s)
cat << EOF
-----
This machine is up for ${uptime}
IT has been running since ${since}
-----
EOF
}
showuptime
