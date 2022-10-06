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
    git clone git@github.com:uyupun/uyunpunion.git

    cd uyunpunion/src
    cp .env.example .env
    read -p "UYUNPUNION_TOKENを入力してください" UYUNPUNION_TOKEN
    EMPTY_UYUNPUNION_TOKEN=`cat ../src/.env | grep EMPTY_UYUNPUNION_TOKEN`
    sed -i -e "s/$EMPTY_UYUNPUNION_TOKEN/UYUNPUNION_TOKEN=$UYUNPUNION_TOKEN/" ../src/.env
    ENV=`cat ../src/.env | grep ENV`
    sed -i -e "s/$ENV/ENV=prod/" ../src/.env
    pipenv install
    make up
    sleep 5
    echo ""
    echo Gunicorn processes
    echo "****************************************************************************************************"
    make ps
    echo "****************************************************************************************************"
    echo ""

    cd ../proxy
    docker compose up -d
    echo ""
    echo Docker processes
    echo "****************************************************************************************************"
    docker compose ps
    echo "****************************************************************************************************"
    echo ""
EOF
