Create a script that will SSH into a remote host and install the user's SSH public key.
Assume a target host is Linux.  Solution does not need to cover every edge case, but you
will need to describe pitfalls with your approach, and how you would address those
issues.

send_sshkey.sh
--------------

#!/bin/bash

HOST="user123@192.168.1.128"
echo $HOST
cat id_rsa.pub | ssh $HOST 'cat >> .ssh/authorized_keys'

Assumes:
-------
1. Remote machine is of Linux/Unix variety

2. User has a valid user account on the remote machine and can ssh to the machine
   using his/her login credentials (username:password)

3. User's home dir (ex: ~/home/user123) has .ssh dir
   if not, create this dir before running this script

4. User's home dir has a ~/.ssh/authorized_keys file to which the ssh key
   transfered by this script will be added.
   if not, change last line in the send_sshkey.sh before running it
   from: 'cat >> .ssh/authorized_keys' 
   to  : 'cat > .ssh/authorized_keys'

To run:
-------

1. copy the ssh key you want to install on the remote machine (id_rsa.pub) 
   to the same dir you are running the send_sshkey.sh

2. modify the HOST="user123@192.168.1.128" to reflect the
   actual userid on the remote machine & the actual ip of the remote machine
   your working with

3. Run the send_sshkey.sh to install ./id_rsa.pub to remote host

Ex:
iqdean@hpdm4:~/u1404/Aspera/aspera-scripting-challenge/5$ ./send_sshkey.sh 
Installing ./id_rsa.pub to user123@192.168.1.128/.ssh/authorized_keys...
Done

To confirm:
-----------

4. several options:

4.1
   ssh to the remote machine and $ cat ~/.ssh/authorized_keys
   to confirm contents of users id_rsa.pub got installed
4.2
   user should be able to ssh to remote using the password he/she
   created for his/her sshkey pair instead of the password assigned
   to user on the remote





