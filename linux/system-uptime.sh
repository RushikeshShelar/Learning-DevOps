#!/bin/bash
show_uptime(){
    local uptime=$(uptime -p | cut -c4-)
    local since=$(uptime -s)
    echo "System Uptime: $uptime"
    echo "Since: $since"
    echo "Current Time: $(date +'%Y-%m-%d %H:%M:%S')"
}
show_uptime