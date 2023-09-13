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
if ! [[ $1 =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]; then
    printf "\e[31m%s\e[m\n" "接続先はIPアドレスの形式で指定してください。"
    exit 1
fi

HOST=$1

# APIとリバプロの起動
ssh -i ../playbook/roles/user/files/id_ed25519 takashi@$HOST << EOF
    cd uyunpunion
    git pull origin master

    cd api
    pipenv sync --system
    cd ../ops
    make reload
    make restart
    sleep 5
    echo ""
    echo Gunicorn processes
    echo "****************************************************************************************************"
    make ps
    echo "****************************************************************************************************"
    echo ""

    cd ../proxy
    make stop
    sed -i "/url = \"http:\/\/\([0-9]\{1,3\}\.\)\{3\}[0-9]\{1,3\}:8080\"/s//url = \"http:\/\/$HOST:8080\"/" config/api.toml
    make start
    echo ""
    echo Docker processes
    echo "****************************************************************************************************"
    make ps
    echo "****************************************************************************************************"
    echo ""
EOF
