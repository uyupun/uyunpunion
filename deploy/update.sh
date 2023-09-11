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

# APIとリバプロの起動
read -sp "takashiユーザのパスワードを入力してください: " PASSWORD
ssh -i ../playbook/roles/user/files/id_ed25519 takashi@$HOST << EOF
    cd uyunpunion
    git pull origin master

    cd api
    pipenv sync --system
    cd ../ops
    make reload password=$PASSWORD
    make restart password=$PASSWORD
    sleep 5
    echo ""
    echo Gunicorn processes
    echo "****************************************************************************************************"
    make ps
    echo "****************************************************************************************************"
    echo ""

    cd ../proxy
    docker compose down
    docker compose up -d
    echo ""
    echo Docker processes
    echo "****************************************************************************************************"
    docker compose ps
    echo "****************************************************************************************************"
    echo ""
EOF
