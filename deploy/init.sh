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

ssh-add ../playbook/roles/user/files/id_ed25519

# GitHubからリポジトリをクローン
ssh -i ../playbook/roles/user/files/id_ed25519 takashi@$HOST << EOF
    ssh-keyscan -t rsa github.com >> .ssh/known_hosts
    git clone git@github.com:uyupun/uyunpunion.git
EOF

# .envの作成
cd ../api
UYUNPUNION_TOKEN=`pipenv run python generate_uyunpunion_token.py`
cd ../deploy
cp ../api/.env.example .env.tmp
sed -i -e "s/PIPENV_VENV_IN_PROJECT=true/PIPENV_VENV_IN_PROJECT=false/" ./.env.tmp
sed -i -e "s/ENV=dev/ENV=prod/" ./.env.tmp
sed -i -e "s/UYUNPUNION_TOKEN=/UYUNPUNION_TOKEN=$UYUNPUNION_TOKEN/" ./.env.tmp
scp -i ../playbook/roles/user/files/id_ed25519 ./.env.tmp takashi@$HOST:~/uyunpunion/api/.env
rm -rf .env.tmp .env.tmp-e

# api.tomlの作成
cp ../proxy/config/api.toml.example api.toml.tmp
sed -i -e "s#http://192.168.0.10:8080#http://$HOST:8080#" ./api.toml.tmp
scp -i ../ansible/roles/user/files/id_ed25519 ./api.toml.tmp takashi@$HOST:~/uyunpunion/proxy/config/api.toml
rm -rf api.toml.tmp api.toml.tmp-e

# APIとリバプロの起動
ssh -i ../playbook/roles/user/files/id_ed25519 takashi@$HOST << EOF
    cd uyunpunion/api
    pipenv sync --system
    cd ../ops
    make start
    sleep 5
    echo ""
    echo Gunicorn processes
    echo "****************************************************************************************************"
    make ps
    echo "****************************************************************************************************"
    echo ""

    cd ../proxy
    make nw
    make start
    echo ""
    echo Docker processes
    echo "****************************************************************************************************"
    make ps
    echo "****************************************************************************************************"
    echo ""
EOF
