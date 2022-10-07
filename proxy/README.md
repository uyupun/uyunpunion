# リバースプロキシの環境構築

- 以下の用途で使用します
    - リバースプロキシ
    - TLS終端
    - ※ 主に本番環境で使用するものです

- 以下のソフトウェアが必要です
    - Docker
    - Docker Compose

```bash
$ cd proxy
$ cp api.toml.example api.toml                                          # urlにAPIのIPとポートの指定が必須
$ docker compose up -d
$ docker compose ps
$ docker compose down
$ open localhost:8080                                                   # ダッシュボード
$ curl -H "Host: uyunpunion.uyupun.tech" -L "localhost/ping"            # 疎通確認
$ curl -H "Host: uyunpunion.uyupun.tech" -L "<private ip address>/ping" # 疎通確認
```
