#!/bin/bash

# sample.txt
# ip port

while read -r line; do
    nc -z $line
    STATUS=$(echo $?) # $? gives the return code of the last run command
    if [ $STATUS == "0" ]; then
        echo "$line is up"
    else
        echo "$line is down"
    fi
done < sample.txt
