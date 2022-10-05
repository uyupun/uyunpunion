## デプロイ

```bash
$ cd deploy
$ make chmod                # 各シェルスクリプトを使用できるようにパーミッションを変更する
$ ./get_server_ssh_key.sh   # デプロイ対象のサーバから公開鍵を取得。取得後、GitHub上のリポジトリのSettings > Deploy keysに登録する
$ ./tag.sh                  # タグ打ちに使用。タグ打ち後、GitHub上のリポジトリのReleasesからリリースを作成する
$ ./init.sh                 # 初回デプロイ時に使用
$ ./update.sh               # 2回目以降のデプロイ時に使用
```
