#!/bin/sh

ssh -i ../ansible/roles/user/files/id_ed25519 takashi@192.168.56.10 << EOF
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
    docker compose down
    docker compose up -d
    echo ""
    echo Docker processes
    echo "****************************************************************************************************"
    docker compose ps
    echo "****************************************************************************************************"
    echo ""
EOF
