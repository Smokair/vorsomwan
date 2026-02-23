#!/bin/bash
clear
echo $(date)
echo "Computer Name: " $HOSTNAME
echo "System Info: "
uname -a
echo "Operating System"
cat /etc/os-release | grep PRETTY_NAME
cat /etc/os-release | grep VERSION_ID
echo "CPU: "
lscpu | grep "Model name: " | sed -r 's/Model name: \s(1,)//g'
echo "Total RAM:"
cat /proc/meminfo | grep "MemTotal"
echo "Storage devices: "
df -h
echo "IP Addresses: "
hostname -I
echo "Created by"
whoami

