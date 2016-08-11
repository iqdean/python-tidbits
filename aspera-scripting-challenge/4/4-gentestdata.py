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
Inspired by 'Python directory tree generator, using recursion'
https://gist.github.com/samuelsh/b837f8ab8b33c344f01128568dd12019
rdir.py - build_dir_tree(base, depth, width) 
	
'''

import sys
import os
import random
import subprocess
from threading import Thread
import math

# globals

dir_tree = []
thread_list = []

'''
TODO: update populate_dir() to wr random number of files of random size
      each time its called
'''

def create_file(path):
    cmd_list = ['time','dd','if=/dev/urandom', 'of=test1.img', 'bs=512' ,'count=100']
    cmd_list[3] = 'of=' + path + '/' + 'test1.img'
    #print "Creating file in : ", path
    a = subprocess.Popen(cmd_list, stderr=subprocess.PIPE)
    a.communicate()

def populate_dir(path):
    create_file(path)

def create_dir_tree(base, depth, width):
    if depth >= 0:
        curr_depth = depth
        depth -= 1
        for i in xrange(width):
            # first create the dir
            os.makedirs('%s/D%d_L%d' % (base, i, curr_depth))
            # then launch a thread to populate ea dir with random number of files
            rp = '%s/D%d_L%d' % (base, i, curr_depth)
            fp = os.path.abspath(rp)
            dir_tree.append(fp)
            t = Thread(target=populate_dir, args=(fp,))
            thread_list.append(t)
            t.start()
 
        dirs = os.walk(base).next()[1]

        for dir in dirs:
            newbase = os.path.join(base,dir)
            create_dir_tree(newbase, depth, width)
    else:
        return

base = './test'
depth = random.randint(0,3)
width = random.randint(1,4)

#depth = 2
#width = 3

print('\nBuilding a directory tree of random depth and width')
print('& populating ea dir with a random number of files ')
print('  that are of random size (1MBmin < size < 3MB) ')
print('--------------------------------------------------\n')

print('base dir %s  depth %d  width %d' % (base, depth, width))

# compute the number of dirs we will endup with in our dir tree
x = 0
for n in range(depth+1):
    x = x + (width*math.pow(width,n))
print "Total # of Dirs in the tree will be : ", x 
    
p = Thread(target=create_dir_tree, args=(base, depth, width))
p.start()
p.join()   # wait for recursive build_dir_tree() to finish

print 'Created %d dirs'%(len(dir_tree))
print 'Created %d files'%(len(thread_list))

print 'Waiting on file creation threads to finish ... '

for t in thread_list:
    t.join()

print "All threads completed"

# print dir_tree

''' 
to see what we ended up with using $ tree
'''

p = subprocess.Popen(["tree", "./test"], stdout=subprocess.PIPE)
output, err = p.communicate()
print "*** dir tree  ***\n", output

