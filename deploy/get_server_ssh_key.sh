#!/bin/sh

set -e

# バリデーション
if [ $# -eq 0 ]; then
    printf "\e[31m%s\e[m\n" "接続先が指定されていません。"
    exit 1
fi
if [ $# -gt 1 ]; then
    printf "\e[31m%s\e[m\n" "引数の数が不正です。"
    exit 1
fi

HOST=$1

rm -f id_rsa.pub
scp -i ../ansible/roles/user/files/id_ed25519 takashi@$HOST:~/.ssh/id_rsa.pub ./

open https://github.com/uyupun/uyunpunion/settings/keys