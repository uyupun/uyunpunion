## デプロイ

```bash
$ cd deploy
$ chmod +x get_server_ssh_key.sh    # デプロイ対象のサーバから公開鍵を取得。取得後、GitHub上のリポジトリのSettings > Deploy keysに登録する
$ chmod +x init.sh
$ chmod +x update.sh
$ git checkout master
$ git pull origin master
$ git tag x.x.x
$ git push origin x.x.x             # その後、GitHub上のリポジトリのReleasesからリリースを作成する
$ ./init.sh
$ ./update.sh
```
