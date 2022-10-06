#!/bin/sh

set -e

# masterブランチの最新状態に移動する
git checkout master
git pull origin master

read -p "タグ打ちするバージョンを入力してください(例: v1.0.0): " NEXT_VERSION

# バリデーション
if [[ ! $VERSION  =~ v[0-9]{1}.[0-9]{1}.[0-9]{1} ]]; then
    printf "\e[31m%s\e[m\n" "タグの形式に誤りがあります。タグ打ちに失敗しました。"
    exit 1
fi

# .envと.env.exampleのバージョンの書き換え
CURRENT_VERSION=`cat ../src/.env | grep VERSION`
sed -i -e "s/$CURRENT_VERSION/VERSION=$NEXT_VERSION/" ../src/.env
sed -i -e "s/$CURRENT_VERSION/VERSION=$NEXT_VERSION/" ../src/.env.example
git add .env.example
git commit -m "Add version ($CURRENT_VERSION to $NEXT_VERSION)"
git push origin master

# タグ打ち
git tag $NEXT_VERSION
git push origin $NEXT_VERSION

echo ""
echo バージョン $NEXT_VERSION でタグ打ちしました。
echo GitHub上でReleaseを作成してください。
open https://github.com/uyupun/uyunpunion/releases
