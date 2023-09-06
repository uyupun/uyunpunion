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
sed -i -e "s/UYUNPUNION_TOKEN=/UYUNPUNION_TOKEN=$UYUNPUNION_TOKEN/" ./.env.tmp
sed -i -e "s/ENV=dev/ENV=prod/" ./.env.tmp
scp -i ../playbook/roles/user/files/id_ed25519 ./.env.tmp takashi@$HOST:~/uyunpunion/api/.env
rm -rf .env.tmp .env.tmp-e

# api.tomlの作成
cp ../proxy/api.toml.example api.toml.tmp
sed -i -e "s#http://192.168.0.10:8081#http://$HOST:8081#" ./api.toml.tmp
scp -i ../playbook/roles/user/files/id_ed25519 ./api.toml.tmp takashi@$HOST:~/uyunpunion/proxy/api.toml
rm -rf api.toml.tmp api.toml.tmp-e

# APIとリバプロの起動
read -sp "takashiユーザのパスワードを入力してください: " PASSWORD
ssh -i ../playbook/roles/user/files/id_ed25519 takashi@$HOST << EOF
    cd uyunpunion/api
    pipenv sync --system
    echo $PASSWORD | sudo -S systemctl enable --now gunicorn.service
    sleep 5
    echo ""
    echo Gunicorn processes
    echo "****************************************************************************************************"
    make ps
    echo "****************************************************************************************************"
    echo ""

    cd ../proxy
    docker network create --driver bridge --subnet 172.20.0.0/16 uyunpunion-network
    docker compose up -d
    echo ""
    echo Docker processes
    echo "****************************************************************************************************"
    docker compose ps
    echo "****************************************************************************************************"
    echo ""
EOF
