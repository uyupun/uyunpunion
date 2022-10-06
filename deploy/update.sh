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

ssh -i ../ansible/roles/user/files/id_ed25519 takashi@$HOST << EOF
    cd uyunpunion
    git pull origin master
    cd src
    pipenv install
    make reload
    sleep 5
    echo ""
    echo Gunicorn processes
    echo "****************************************************************************************************"
    make ps
    echo "****************************************************************************************************"
    echo ""
    cd ../proxy
    docker compose restart
    echo ""
    echo Docker processes
    echo "****************************************************************************************************"
    docker compose ps
    echo "****************************************************************************************************"
    echo ""
EOF
