#!/bin/sh

set -e

# バージョンの取得
CURRENT_VERSION=`cat ../api/.env.example | grep VERSION | sed -e "s/VERSION=//g"`
NEXT_VERSION=$1

# masterブランチの最新状態に移動する
git checkout master
git pull origin master

# バリデーション
if [[ ! $NEXT_VERSION  =~ v[0-9]{1}.[0-9]{1}.[0-9]{1} ]]; then
    printf "\e[31m%s\e[m\n" "タグの形式に誤りがあります。v0.1.0のような形式で指定してください。"
    exit 1
fi
if [[ $CURRENT_VERSION > $NEXT_VERSION ]]; then
    printf "\e[31m%s\e[m\n" "現在のバージョンよりも低いバージョンは指定できません。"
    exit 1
fi

# .envと.env.exampleのバージョンの書き換え
sed -i -e "s/VERSION=$CURRENT_VERSION/VERSION=$NEXT_VERSION/" ../api/.env
sed -i -e "s/VERSION=$CURRENT_VERSION/VERSION=$NEXT_VERSION/" ../api/.env.example
git add ../api/.env.example
git commit -m "Add version ($CURRENT_VERSION to $NEXT_VERSION)"
git push origin master

# タグ打ち
git tag $NEXT_VERSION
git push origin $NEXT_VERSION

echo ""
echo バージョン $NEXT_VERSION でタグ打ちしました。
echo GitHub上でReleaseを作成してください。
echo "-> https://github.com/uyupun/uyunpunion/releases"
open https://github.com/uyupun/uyunpunion/releases
