
Title:		Aspera Scripting Challenge 4

Description:
Devise a method for creating temporary file data for use in testing file transfer.  The result
of the script should be a directory that may have one or more nested directories (quantity
randomly determined).  Inside these directories are a random number of files in each
directory.  The files should be large (greater than 1MB) and mimic a collection of data.

Please note rationale in the collection chosen, and how the files were generated.  What
optimizations or considerations need to be made.

Script Name:	4-gentestdata.py
------------

Prerequisites:
--------------

This script requires the unix tree util, please install if not already installed on your system

$ sudo apt-get install tree

NOTES:
------

Builds a directory tree of random depth and width   < You can set adjust the size of the dir tree
                                                      by changing these 2 params in the code:

							depth = random.randint(0,3)
							width = random.randint(1,4)


& populates ea dir with a random number of files     \ TODO: currently my script will write a
  that are of random size (1MBmin < size < XMB)      / small fixed size 'test1.img' file in ea dir
--------------------------------------------------              \__ 51200 Jul 15 20:31 test1.img


CAUTION:
---------

The number of directories & files that get created are a exponential function of the
'depth' variable. In a real world scenario, where there would be a random number of 
1MB files in all those directories, this script could consume a whole lot of disk space
very quickly.

# compute the number of dirs we will endup with in our dir tree
x = 0
for n in range(depth+1):
    x = x + (width*math.pow(width,n))
print "Total # of Dirs in the tree will be : ", x 

To avoid extremely large directory tree's, the random range of both depth & width params
is limited to the ranges set in the following 2 lines:

depth = random.randint(0,3)
width = random.randint(1,4)


To Run:
-------

Example 1:
----------

iqdean@hpdm4:/media/8C365D65365D5176/u1404/Aspera/aspera-scripting-challenge/4$ rm -rf test
iqdean@hpdm4:/media/8C365D65365D5176/u1404/Aspera/aspera-scripting-challenge/4$ ./4-gentestdata.py

Building a directory tree of random depth and width
& populating ea dir with a random number of files 
  that are of random size (1MBmin < size < 3MB)
-------------------------------------------------- 

base dir ./test  depth 1  width 4
Total # of Dirs in the tree will be :  20.0
Created 20 dirs
Created 20 files
Waiting on file creation threads to finish ... 
All threads completed
*** dir tree  ***
./test
├── D0_L1
│   ├── D0_L0
│   │   └── test1.img
│   ├── D1_L0
│   │   └── test1.img
│   ├── D2_L0
│   │   └── test1.img
│   ├── D3_L0
│   │   └── test1.img
│   └── test1.img
├── D1_L1
│   ├── D0_L0
│   │   └── test1.img
│   ├── D1_L0
│   │   └── test1.img
│   ├── D2_L0
│   │   └── test1.img
│   ├── D3_L0
│   │   └── test1.img
│   └── test1.img
├── D2_L1
│   ├── D0_L0
│   │   └── test1.img
│   ├── D1_L0
│   │   └── test1.img
│   ├── D2_L0
│   │   └── test1.img
│   ├── D3_L0
│   │   └── test1.img
│   └── test1.img
└── D3_L1
    ├── D0_L0
    │   └── test1.img
    ├── D1_L0
    │   └── test1.img
    ├── D2_L0
    │   └── test1.img
    ├── D3_L0
    │   └── test1.img
    └── test1.img

20 directories, 20 files

Example 2:
----------

iqdean@hpdm4:/media/8C365D65365D5176/u1404/Aspera/aspera-scripting-challenge/4$ rm -rf test
iqdean@hpdm4:/media/8C365D65365D5176/u1404/Aspera/aspera-scripting-challenge/4$ ./4-gentestdata.py

Building a directory tree of random depth and width
& populating ea dir with a random number of files 
  that are of random size (1MBmin < size < 3MB) 
--------------------------------------------------

base dir ./test  depth 3  width 1
Total # of Dirs in the tree will be :  4.0
Created 4 dirs
Created 4 files
Waiting on file creation threads to finish ... 
All threads completed
*** dir tree  ***
./test
└── D0_L3
    ├── D0_L2
    │   ├── D0_L1
    │   │   ├── D0_L0
    │   │   │   └── test1.img
    │   │   └── test1.img
    │   └── test1.img
    └── test1.img

4 directories, 4 files


