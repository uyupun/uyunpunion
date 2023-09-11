# Gitフックの設定

```bash
$ cd hooks
$ pipenv sync --dev
$ pipenv run pre-commit install
$ pipenv run pch        # pre-commit-hooksを実行
$ pipenv run yamllint   # yamllintを実行
```
