#!/bin/sh

HOST="192.168.56.10"

rm -f id_rsa.pub
scp -i ../ansible/roles/user/files/id_ed25519 takashi@$HOST:~/.ssh/id_rsa.pub ./
