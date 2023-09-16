# ディレクトリ構造

```
├ api
│ ├ drivers                       ウユンプニオン・ドライバの制御スクリプト
│ ├ middlewares                   カスタムミドルウェア
│ ├ routes                        APIの各エンドポイント
│ ├ schemas                       レスポンスのスキーマ
│ ├ .flake8                       リンター(Flake8)の設定
│ ├ .isort.cfg                    ソートツール(isort)の設定
│ ├ app.py                        アプリケーションのエントリーポイント
│ ├ generate_uyunpunion_token.py  UYUNPUNION_TOKENの生成スクリプト
│ ├ gunicorn.conf.py              本番環境で使用するGunicornの設定
│ ├ Makefile                      本番環境で使用するコマンド群の定義
│ └ settings.py                   環境変数、グローバル変数
├ deploy                          デプロイスクリプト関連
│ ├ get_server_ssh_key.sh         デプロイ対象のサーバから公開鍵を取得するスクリプト
│ ├ init.sh                       初回デプロイ時に使用するスクリプト
│ ├ tag.sh                        タグ打ちに使用するスクリプト
│ └ update.sh                     2回目以降のデプロイ時に使用するスクリプト
├ devel                           開発サーバ(Vagrant)の設定
├ docs                            ドキュメント
├ hooks
│ ├ .pre-commit-config.yaml       pre-commitの設定
│ ├ .yamllint                     yamllintの設定
│ └ pre_commit_ansible_lint.sh    pre-commitからAnsible-lintを実行するためのスクリプト
├ images
├ ops
│ └ Makefile                      本番環境で使用する運用コマンド群の定義
├ playbook
│ ├ inventories                   Ansibleの接続先の設定
│ ├ roles                         Ansibleの各タスク
│ ├ ansible.cfg                   Ansible自体の挙動の設定
│ └ site.yml                      Ansibleで設定を流すためのエントリーポイント
├ prod
│ └ Makefile                      本番サーバ固有の運用コマンド群の定義
├ proxy
│ ├ certs                         TLS終端に使用する証明書と秘密鍵
│ ├ config
│ │ ├ api.toml                    API関連の動的設定
│ │ ├ dashboard.toml              ダッシュボード関連の動的設定
│ │ └ http.toml                   HTTPからHTTPSへのリダイレクトの動的設定
│ ├ compose.yml                   Docker周りの設定
│ ├ Makefile                      リバースプロキシ(Traefik)の運用コマンド群の定義
│ └ traefik.toml                  リバースプロキシ(Traefik)全体の静的設定
├ .cspell.json                    スペルチェックツール(CSpell)の設定
└ README.md
```
