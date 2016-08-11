#!/bin/bash
DISK="/media/iqdean/Lexar"
res=`df $DISK | grep / | awk '{ print $5}' | sed 's/%//g'`
ts=$(eval "date +%Y%m%d%H%M%S")
echo "Time: $ts Volume: $DISK  Used: $res% " >> diskmon.log

