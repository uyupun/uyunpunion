#!/bin/sh

set -e

rm -f id_rsa.pub
scp -i ../ansible/roles/user/files/id_ed25519 takashi@192.168.56.10:~/.ssh/id_rsa.pub ./
