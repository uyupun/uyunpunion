# リバースプロキシの環境構築

- 以下の用途で使用します
    - リバースプロキシ
    - TLS終端

- 以下のソフトウェアが必要です
    - Docker
    - Docker Compose

- 以下のファイルが必要です
    - `proxy/certs/selfsigned.key`

```bash
$ cd proxy
$ cp config/api.toml.example config/api.toml                                                                    # urlにAPIのIPとポートの指定が必須
$ openssl req -x509 -nodes -days 99999 -newkey ed25519 -keyout certs/selfsigned.key -out certs/selfsigned.crt   # 自己署名証明書を作成する場合
$ htpasswd -n takashi                                                                                           # ユーザを作成する場合
$ docker compose up -d
$ docker compose ps
$ docker compose down
$ open https://localhost/dashboard/                                                                             # ダッシュボード
$ curl -k -L "https://localhost/ping"                                                                           # 疎通確認
$ curl -k -L "https://<private ip address>/ping"                                                                # 疎通確認
$ curl -i -k -L "http://localhost/ping"                                                                         # 疎通確認(HTTPSにリダイレクトされる)
```
