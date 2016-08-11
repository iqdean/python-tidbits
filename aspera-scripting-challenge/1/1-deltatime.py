#!/usr/bin/python

'''
Title:		Aspera Scripting Challenge 1

Description:
Write a script that makes a REST call to http://time.jsontest.com and uses the result to
compare against the localhosts time/date setting.  Script result should note the systems
discrepancy between the times in seconds.

Author:		ike dean iad1046@gmail.com 	
'''

import json
import os

f = os.popen('curl -s time.jsontest.com')
rest = f.read()
print "\nREST API CALL to time.jsontest.com returned: \n", rest

jsondata = json.loads(rest)
remote_time = jsondata['milliseconds_since_epoch']
remote_time = remote_time/1000
print "Remote EPOCH: ", remote_time

h = os.popen('date +%s')
local_time = int(h.read())
print "Local  EPOCH: ", local_time

delta_time = remote_time - local_time
print "DELTA TIME  : ", delta_time, "\n"




