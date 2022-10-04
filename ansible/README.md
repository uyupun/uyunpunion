# Ansibleによる設定の流し込み

- 以下の用途で使用します
    - 本番環境で使用するラズパイに設定を流し込む
    - その前段階として検証サーバに設定を流し込む

- 以下のソフトウェアが必要です
    - Python又はPyenv(Pythonのバージョンは3.9系)
    - Pipenv

- 以下のファイルが必要です
    - `ansible/roles/user/files/id_ed25519`

```bash
$ cd ansible
$ chmod 600 roles/user/files/id_ed25519                     # 秘密鍵のパーミッションを変更しないとSSH接続できないため
$ touch VAULT_PASSWORD                                      # Ansible Vaultのパスワードを設定する
$ pipenv install
$ pipenv shell
$ ansible all -i hosts/test -m ping                         # 疎通確認
$ ansible-playbook -i hosts/test infra.yml --list-tasks     # タスク一覧
$ ansible-playbook -i hosts/test infra.yml --syntax-check   # 構文エラーのチェック
$ ansible-lint infra.yml                                    # リンターの実行
$ ansible-playbook -i hosts/test infra.yml --check --diff   # ドライラン
$ ansible-playbook -i hosts/test infra.yml                  # 実行
$ ssh -i roles/user/files/id_ed25519 takashi@192.168.56.10  # SSH接続
```
