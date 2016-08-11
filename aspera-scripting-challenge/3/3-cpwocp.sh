#!/bin/bash

# Title:		
# Aspera Scripting Challenge 2
#
# Description:
# Write a script that can copy a file, without using cp .  The script will take two command
# line parameters: source file and destination file. Describe the performance implications of
# the approach that you took and compare it to other methods of copying a file.
#
# Author:		ike dean iad1046@gmail.com 	

MINPARAMS=2

if [ $# -lt "$MINPARAMS" ]
then
     echo "Usage:    ./scriptname source destination"
	exit 1
else
     echo "copying $1 $2"

	cmd="rsync $1 $2"
	res=$(eval $cmd)

	if [ $? -ne 0 ]
	then
		echo "Copy failed ... see error above"
	else
		echo "Copy complete"
	fi

fi

exit 0



