# リバースプロキシの環境構築

- 以下の用途で使用します
    - リバースプロキシ
    - TLS終端

- 以下のソフトウェアが必要です
    - Docker
    - Docker Compose

- 以下のファイルが必要です
    - `proxy/certs/selfsigned.key`
    - `proxy/certs/selfsigned.crt`

```bash
$ cd proxy
$ cp config/api.toml.example config/api.toml                                                                    # URLにAPIのIPとポートの指定が必須
$ openssl req -x509 -nodes -days 99999 -newkey ed25519 -keyout certs/selfsigned.key -out certs/selfsigned.crt   # 秘密鍵と自己署名証明書を発行する
$ openssl x509 -in certs/selfsigned.crt -text -noout                                                            # 証明書の内容を確認する
$ openssl pkey -in certs/selfsigned.key -text -noout                                                            # 秘密鍵の内容を確認する
$ htpasswd -n takashi                                                                                           # Basic認証のユーザを生成する(生成後、config/dashboard.tomlへの記載が必須)
$ make start                                                                                                    # リバースプロキシ(Traefik)の起動
$ make restart                                                                                                  # リバースプロキシ(Traefik)の再起動
$ make stop                                                                                                     # リバースプロキシ(Traefik)の停止
$ make ps                                                                                                       # リバースプロキシ(Traefik)の状態確認
$ make log                                                                                                      # リバースプロキシ(Traefik)のログ確認
$ make shell                                                                                                    # リバースプロキシ(Traefik)のシェルに入る
$ open https://localhost/dashboard/                                                                             # ダッシュボードを開く
$ curl -k -L "https://localhost/ping"                                                                           # 疎通確認
$ curl -k -L "https://<private ip address>/ping"                                                                # 疎通確認
$ curl -i -k -L "http://localhost/ping"                                                                         # 疎通確認(HTTPSにリダイレクトされる)
```
