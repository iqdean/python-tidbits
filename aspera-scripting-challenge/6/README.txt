
Write a script that periodically executes.  This script will check disk space utilization of a
defined volume/directory that is passed to it.  It will write to a configured file a log entry
that indicates the expected date the storage will fill up based on the growth pattern of the
storage.

To run manually:
----------------
iqdean@hpdm4:~/u1404/Aspera/aspera-scripting-challenge/6$ ./diskmon.sh
iqdean@hpdm4:~/u1404/Aspera/aspera-scripting-challenge/6$ cat diskmon.log 
Time: 20160715000327 Volume: /media/iqdean/Lexar  Used: 47% 

iqdean@hpdm4:~/u1404/Aspera/aspera-scripting-challenge/6$ ./diskmon.sh
iqdean@hpdm4:~/u1404/Aspera/aspera-scripting-challenge/6$ cat diskmon.log 
Time: 20160715000327 Volume: /media/iqdean/Lexar  Used: 47% 
Time: 20160715000346 Volume: /media/iqdean/Lexar  Used: 47% 

iqdean@hpdm4:~/u1404/Aspera/aspera-scripting-challenge/6$ ./diskmon.sh
iqdean@hpdm4:~/u1404/Aspera/aspera-scripting-challenge/6$ cat diskmon.log 
Time: 20160715000327 Volume: /media/iqdean/Lexar  Used: 47% 
Time: 20160715000346 Volume: /media/iqdean/Lexar  Used: 47% 
Time: 20160715000354 Volume: /media/iqdean/Lexar  Used: 47% 

To run periodically, 
--------------------
add diskmon.sh to your crobtab as shown in example below:

$ crontab -e

# to run every minute
* * * * * ~/diskmon.sh

To confirm its running periodically
-----------------------------------

wait a few minutes & verify there's a log entry
at the rate you specd in your crontab

Ex:

iqdean@hpdm4:~$ cat diskmon.log
Time: 20160715000327 Volume: /media/iqdean/Lexar  Used: 47% 
Time: 20160715000346 Volume: /media/iqdean/Lexar  Used: 47% 
Time: 20160715000354 Volume: /media/iqdean/Lexar  Used: 47% 
Time: 20160715002101 Volume: /media/iqdean/Lexar  Used: 47%   < 
Time: 20160715002201 Volume: /media/iqdean/Lexar  Used: 47%   <

TODO:
------

Add code to determine:

	expected date the storage will fill up based on the growth pattern

based on crontab periodic run rate, & diskmon.log file contents (timestamp, and %Used)


