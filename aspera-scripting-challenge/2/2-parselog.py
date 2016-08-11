#!/usr/bin/python

'''
Title:		
	Aspera Scripting Challenge 3

Description:
	Write a script to parse aspera.log file

	The script will report:
	1 Total number of ascp  transfers;
	2 Listing of all transfers and their average rate in Mb/s;
	3 PID of transfer(s) with the longest duration;
	4 PID of the transfer(s) sending the most data;
	5 PID of the transfer(s) with the fastest rate.

Author:		ike dean iad1046@gmail.com 	
'''

import re
import numpy as np

mlog = open('aspera.log')

arr = np.empty((0,4), dtype=int)

for line in mlog:
	line = line.rstrip()
	mydata = []
	if re.search('FASP Session Statistics', line) :
		'''print line'''
		mydata.append(int(re.findall('\[([0-9]*)\]', line)[0]))
		mydata.append(int(re.findall(' tx_bytes ([0-9]*) ', line)[0]))
		mydata.append(int(re.findall(' tx_time ([0-9]*)\)', line)[0]))
		''' print mydata '''
		''' compute the avg xfr rate in Mbs '''
		bits = float(mydata[1]*8)
		uSec = float(mydata[2])
		if (uSec > 0) :
			Mbs = float(bits/uSec)
		else :
			Mbs = 0
		''' print('Mbs : %5.2f' % Mbs) '''
		mydata.append(int(Mbs)) 
		arr = np.append(arr, [mydata], axis=0)

'''
array([[6, 7, 8],
       [4, 5, 6],
       [1, 2, 3],
       [1, 2, 3]])
>>> arr.shape
(4, 3)
>>> arr.shape[0]
4 
'''

print('1 Total number of ascp  transfers : %d' % arr.shape[0])

print "2 Listing of all transfers and their average rate in Mb/s"
print "  PID      Mbs"
print arr[:,[0,3]]

''' since PIDs launch sequentially, resulting table ends up being
    sorted by PID in ascending order ...now we can slice and dice it '''

print "3 PID of transfer(s) with the longest duration "

''' sort by Total uS (col=2) in descending order and
    list the top 10 PIDs '''

col = 2

'''  sort descending by col     /----\ '''
arr = arr[np.argsort(arr[:,col])[::-1]]

print "      PID    Total uS"
print arr[:10,[0,2]]

print "4 PID of the transfer(s) sending the most data"

''' sort by Bytes Xfrd (col=1) descending order & dump 1st 10 rows '''

col = 1
arr = arr[np.argsort(arr[:,col])[::-1]]
print "         PID   Bytes Xfrd"
print arr[:10,[0,1]]

print "5 PID of the transfer(s) with the fastest rate"

''' sort by Mbs (col=3) descending order  & dump 1st 10 rows '''

col = 3
arr = arr[np.argsort(arr[:,col])[::-1]]
print "  PID      Mbs"
print arr[:10,[0,3]]

