#!/usr/bin/python

'''
Write a script that can copy a file, without using cp .  The script will take two command
line parameters: source file and destination file. Describe the performance implications of
the approach that you took and compare it to other methods of copying a file.
'''

''' create a 10MB file to play with using dd:
$ dd if=/dev/urandom of=test10.img bs=1M count=10        10MB
$ dd if=/dev/urandom of=test1024.img bs=1M count=1024   1.1GB
'''

import sys
import os

if len(sys.argv) < 3:
    ''' print 'Number of arguments:', len(sys.argv), 'arguments.' '''
    print 'Usage: $ ./program.py source_file destination_file '
else:
    print 'copying :'
    print '  source: ', str(sys.argv[1])
    print '  destin: ', str(sys.argv[2])
    cmd = 'rsync ' + str(sys.argv[1]) + ' ' + str(sys.argv[2])
    print cmd
    f = os.popen(cmd)
    cmd_stdout = f.read()
    print 'copy complete'






