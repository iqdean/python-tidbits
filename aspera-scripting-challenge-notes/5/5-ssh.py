import subprocess
import sys

'''
Assumes
1. user123 on can ssh to the remote machine with his/her credentials

2. /home/user123 account has ~./ssh dir in it & user r/w-able by the user

3. user123 has generated his/her rsa key pair on the local machine from
   which he/she is running this script from and from which he/she will
   be accessing the remote machine from

4. the user's public key (id_rsa.pub) is in the same dir as this script

'''

HOST="user123@192.168.1.128"

'''
in case there's already some keys installed use:
COMMAND="cat >> .ssh/authorized_keys"

in case there's no keys installed, use:
COMMAND="cat > .ssh/authorized_keys"

cat id_rsa.pub | ssh user@hostname 'cat >> .ssh/authorized_keys'
'''
COMMAND=" ./id_rsa.pub | ssh " + HOST +" 'cat >> .ssh/authorized_keys'"

print COMMAND

ssh = subprocess.Popen(["cat", "%s" % HOST, COMMAND],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
result = ssh.stdout.readlines()
if result == []:
    error = ssh.stderr.readlines()
    print >>sys.stderr, "ERROR: %s" % error
else:
    print result

