# Ansibleによる設定の流し込み

- 以下の用途で使用します
    - 開発/本番サーバに設定を流し込む

- 以下のソフトウェアが必要です
    - Python又はPyenv(Pythonのバージョンは3.9系)
    - Pipenv

- 以下のファイルが必要です
    - `playbook/roles/user/files/id_ed25519`
    - `playbook/ANSIBLE_VAULT_PASSWORD`

```bash
$ cd playbook
$ chmod 600 roles/user/files/id_ed25519                             # 秘密鍵のパーミッションを変更しないとSSH接続できないため
$ ssh-add roles/user/files/id_ed25519                               # パスフレーズの入力を省略させるための設定(オプション)
$ touch ANSIBLE_VAULT_PASSWORD                                      # Ansible Vaultのパスワードを設定する
$ pipenv sync --dev
$ pipenv shell
$ ansible-vault encrypt roles/user/vars/main.yml
$ ansible-vault decrypt roles/user/vars/main.yml
$ ansible all -i inventories/devel -m ping                          # 疎通確認
$ ansible-playbook -i inventories/devel site.yml --list-tasks       # タスク一覧
$ ansible-playbook -i inventories/devel site.yml --syntax-check     # 構文エラーのチェック
$ ansible-lint site.yml                                             # リンターの実行
$ ansible-playbook -i inventories/devel site.yml --check --diff     # ドライラン
$ ansible-playbook -i inventories/devel site.yml                    # 実行
$ ansible-playbook -i inventories/devel site.yml --tags ssh         # タグを指定して実行
$ ansible-playbook -i inventories/prod site.yml                     # 本番環境の場合
```
