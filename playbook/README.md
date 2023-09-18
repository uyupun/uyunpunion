# Ansibleによる設定の流し込み

- 以下の用途で使用します
    - 開発/本番サーバに設定を流し込む

- 以下のソフトウェアが必要です
    - Python又はPyenv(Pythonのバージョンは3.9系)
    - Pipenv

- 以下のファイルが必要です
    - `playbook/roles/user/files/id_ed25519`
    - `playbook/roles/user/files/id_ed25519.pub`
    - `playbook/ANSIBLE_VAULT_PASSWORD`

```bash
$ cd playbook
$ ssh-keygen -t ed25519 -f roles/user/files/id_ed25519  # 秘密鍵と公開鍵の生成
$ touch ANSIBLE_VAULT_PASSWORD                          # 作成後、パスワードを記載する
$ make chmod                                            # 秘密鍵のパーミッションを適切なものに変更
$ make addkey                                           # コマンドの実行毎にパスフレーズの入力を催促することを回避するための設定(オプション)
$ make encrypt                                          # Ansible Vaultによるroles/user/vars/main.ymlの暗号化
$ make decrypt                                          # Ansible Vaultによるroles/user/vars/main.ymlの復号
$ make ping                                             # 疎通確認
$ make ls                                               # タスク一覧
$ make check                                            # 構文エラーのチェック
$ make dryrun env=devel tags=all                        # ドライラン
$ make run                                              # 実行
```

- `ping` / `ls` / `check` / `dryrun` / `run` はインベントリを示す `env` の指定が可能です。デフォルトでは開発サーバである `devel` が指定されています。本番サーバの場合は `prod` を指定してください
- `dryrun` / `run` はタスクのタグを示す `tags` の指定が可能です。デフォルトでは全てのタスクが実行される `all` が指定されています
