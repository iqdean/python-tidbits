#!/bin/bash

HOST="user123@192.168.1.128"
echo "Installing ./id_rsa.pub to $HOST/.ssh/authorized_keys..."
cat id_rsa.pub | ssh $HOST 'cat >> .ssh/authorized_keys'
echo "Done"

