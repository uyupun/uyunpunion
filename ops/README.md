# 統合開発環境/本番環境の運用

- 以下の用途で使用します
    - 統合開発環境/本番環境の運用
    - ※ 本番サーバ固有の運用コマンドは [prod/README.md](../prod/README.md) に記載
    - ※ リバースプロキシ(Traefik)は開発環境/統合開発環境/本番環境で同様のコマンドを使用するため、 [proxy/README.md](../proxy/README.md) に記載

```bash
$ cd prod
$ make start        # デーモン(systemd)の起動(通常はデプロイスクリプトから実行されます)
$ make reload       # デーモン(systemd)の設定の再読み込み(通常はデプロイスクリプトから実行されます)
$ make restart      # デーモン(systemd)の再起動(通常はデプロイスクリプトから実行されます)
$ make stop         # デーモン(systemd)の停止
$ make status       # デーモン(systemd)の状態確認
$ make ps           # デーモン(systemd)のプロセスの確認(8080番ポート)
$ make ps port=8081 # デーモン(systemd)のプロセスの確認(ポート番号を指定)
$ make log          # デーモン(systemd)のログの確認
```
