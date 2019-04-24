#!/bin/sh
cmd=$1

while true
do
	sleep 10
	ps -ef | grep $cmd | grep -v "grep" | grep -v "restart"
	if [ "$?" -eq 1 ]
	then
		echo "process has been restarted!"
		$cmd
	else
		echo "process already started!"
	fi
done
