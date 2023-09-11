# Gitフックの設定

```bash
$ cd hooks
$ pipenv sync --dev
$ pipenv run pre-commit install     # pre-commitのインストール
$ pipenv run pch                    # pre-commit-hooksを実行
$ pipenv run yamllint               # yamllintを実行
```
