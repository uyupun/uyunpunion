#!/bin/sh

git checkout master
git pull origin master

read -p "version: " VERSION

git tag $VERSION
git push origin $VERSION

echo ""
echo バージョン $VERSION でタグ打ちしました
echo ""
echo GitHub上でReleaseを作成してください
echo "-> https://github.com/uyupun/uyunpunion/releases"
