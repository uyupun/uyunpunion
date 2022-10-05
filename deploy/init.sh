#!/bin/sh

ssh -i ../ansible/roles/user/files/id_ed25519 takashi@192.168.56.10 << EOF
    git clone git@github.com:uyupun/uyunpunion.git
    cd uyunpunion/src
    cp .env.example .env
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
