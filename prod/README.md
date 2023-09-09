# 統合開発環境/本番環境の運用

- 以下の用途で使用します
    - 統合開発環境/本番環境の運用

```bash
$ cd prod
# Gunicornの起動(通常はデプロイスクリプトから実行されます)
$ make start
# デーモンの設定の再読み込み(通常はデプロイスクリプトから実行されます)
$ make reload
# Gunicornの再起動(通常はデプロイスクリプトから実行されます)
$ make restart
# Gunicornの停止
$ make stop
# Gunicornの状態確認
$ make status
# Gunicornのプロセスの確認
$ make ps
# Gunicornのログの確認
$ make log
```
