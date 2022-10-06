#!/bin/sh

set -e

ssh -i ../ansible/roles/user/files/id_ed25519 takashi@192.168.56.10 << EOF
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
