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

if [[ $HOST == *.local ]]; then
    HOST=$(dig +short "$HOST" @224.0.0.251 -p 5353)
fi

# 公開鍵の取得
rm -f id_rsa.pub
scp -i ../playbook/roles/user/files/id_ed25519 takashi@$HOST:~/.ssh/id_rsa.pub ./

echo ""
echo GitHub上でDeploy keyを登録してください。
echo "-> https://github.com/uyupun/uyunpunion/settings/keys"
open https://github.com/uyupun/uyunpunion/settings/keys
