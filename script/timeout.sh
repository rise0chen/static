#!/bin/bash
cmd=$1
timeout=$2
echo $cmd|bash &
pid=$!
sleep $timeout
kill -9 $pid &>/dev/null
echo "Timeout!!!"
