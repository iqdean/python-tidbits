#!/usr/bin/python

'''

Some notes for future ref:

$ wget -q time.jsontest.com -O test.json   <- writes to file

$ curl -s time.jsontest.com   <- spews to console only
                                 redirect to file if u want a file
{
   "time": "11:28:01 PM",
   "milliseconds_since_epoch": 1468366081349,
   "date": "07-12-2016"
}

'''

import json
import os

f = os.popen('curl -s time.jsontest.com')
rest = f.read()
print "REST API CALL to time.jsontest.com returned:"
print rest
'''
{
   "time": "11:35:21 PM",
   "milliseconds_since_epoch": 1468366521141,
   "date": "07-12-2016"
}
'''

jsondata = json.loads(rest)
'''
print jsondata
{u'date': u'07-12-2016', u'milliseconds_since_epoch': 1468365136933, u'time': u'11:12:16 PM'}
'''
remote_time = jsondata['milliseconds_since_epoch']
remote_time = remote_time/1000
print "Remote EPOCH:"
print remote_time
'''
1468366521141
'''

h = os.popen('date +%s')
local_time = int(h.read())
print "Local EPOCH:"
print local_time

print "DELTA TIME (in seconds) between local and remote systems:"
delta_time = remote_time - local_time
print delta_time



