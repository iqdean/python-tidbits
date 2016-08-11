#!/usr/bin/python

import subprocess

def os_system_dd():
   print "executing the time dd command"

   cmd_list = ['time','dd','if=/dev/urandom', 'of=test1.img', 'bs=512' ,'count=100']
   '''           0      1          2              3              4          5     '''

   print cmd_list
   sqn = 3
   bs = 256
   count = 512
   cmd_list[3] = 'of=test' + str(sqn) + '.img'
   cmd_list[4] = 'bs=' + str(bs)
   cmd_list[5] = 'count=' + str(count)
   print cmd_list

   ##a = subprocess.Popen(cmd_list)  < dd stdout/stderr spews to console
   ##a = subprocess.Popen(cmd_list, stdout=subprocess.PIPE) <console spew still there
   ##a = subprocess.Popen(cmd_list, stderr=subprocess.PIPE) <all console spew in a now
   a = subprocess.Popen(cmd_list, stderr=subprocess.PIPE)
   a.communicate()

if __name__ == '__main__':
   os_system_dd()
