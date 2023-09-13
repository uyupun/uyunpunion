# 開発サーバの環境構築

- 以下の用途で使用します
    - Ansibleのテスト
    - より本番環境に近い環境での動作確認
        - ※ Debian 11(bullseye)が動作します

- 以下のソフトウェアが必要です
    - Homebrew
    - VirtualBox
    - Vagrant

```bash
$ cd develop
$ vagrant up
$ vagrant ssh
$ vagrant status
$ vagrant halt
$ vagrant reload
$ vagrant destroy
$ ssh-keygen -R 192.168.56.10   # 検証サーバを作り直した場合に実行が必要
```
