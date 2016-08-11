#!/usr/bin/python

'''
Title:		Aspera Scripting Challenge 4

Description:
Devise a method for creating temporary file data for use in testing file transfer.  The result
of the script should be a directory that may have one or more nested directories (quantity
randomly determined).  Inside these directories are a random number of files in each
directory.  The files should be large (greater than 1MB) and mimic a collection of data.

Please note rationale in the collection chosen, and how the files were generated.  What
optimizations or considerations need to be made.

Author:		ike dean iad1046@gmail.com 	

Credits:
To avoid 'reinventing the wheel', I'm reusing the following code in this script:

Python directory tree generator, using recursion
https://gist.github.com/samuelsh/b837f8ab8b33c344f01128568dd12019
rdir.py - build_dir_tree(base, depth, width) 
	
'''

import sys
import os
import random
import subprocess
#from multiprocessing import Process, Queue
from threading import Thread

def build_dir_tree(base, depth, width):
    '''print("Call #%d" % depth)'''
    if depth >= 0:
        curr_depth = depth
        depth -= 1

        for i in xrange(width):
            # first creating all folder at current depth
            os.makedirs('%s/D%d_L%d' % (base, i, curr_depth))

        dirs = os.walk(base).next()[1]

        for dir in dirs:
            newbase = os.path.join(base,dir)
            build_dir_tree(newbase, depth, width)
    else:
        return

'''
if not sys.argv[1:]:
    print('Usage: ./scriptname.py base depth width ')
    print('   Ex: ./scriptname.py ./test 1 2       ')
    sys.exit(1)

print('path: %s, depth: %d, width: %d' % (sys.argv[1], int(sys.argv[2]), int(sys.argv[3])))
build_dir_tree(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

 
1. Create a random number of nested directories

base = './test'
depth = random.randint(1,4)    < number of subdir in ea dir
width = random.randint(1,4)    < number of dirs

build_dir_tree(base, depth, width)

Warning:
Be careful what you feed this script, it can quickly eatup your
disk space, esp when ea dir could be poplulated with a random
number of files that are at least 1MB in size

depth   width    Total Dir
  1       1        2
  1       2        6
  1       3       12
  1       4       20

  2       1        3
  2       2       14
  2       3       39
  2       4       84

  3       1        4
  3       2       30
  3       3      120
  3       4      340
  3       5      780

  4       1        5
  4       2       62
  4       3      363
  4       4     1364
  4       5     3905
 
'''

base = './test'
depth = random.randint(1,3)
width = random.randint(1,4)

print('1. Building a directory tree of random depth & width ...')
print('base %s  depth %d  width %d' % (base, depth, width))

''' 
build_dir_tree(base, depth, width)
we need a way to wait for build_dir_tree() to finish
before proceeding... if depth & width r large, it
takes a while for build_dir_tree to be complete
'''
#p = Process(target=build_dir_tree, args=(base, depth, width))
p = Thread(target=build_dir_tree, args=(base, depth, width))
p.start()
p.join()   # wait for build_dir_tree to finish


''' 
to see what we ended up with
$ tree test
'''

p = subprocess.Popen(["tree", "./test"], stdout=subprocess.PIPE)
output, err = p.communicate()
print "*** dir tree  ***\n", output


'''
now we can walk the dir tree to populate ea dir w a random number
of files of random size
dd if=/dev/urandom of=test1.img bs=1M count=10 
'''






