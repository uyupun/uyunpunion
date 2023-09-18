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
$ make up       # 開発サーバ(Vagrant)の起動
$ make vssh     # SSH接続(vagrantユーザ)
$ make halt     # 開発サーバ(Vagrant)の停止
$ make reload   # 開発サーバ(Vagrant)の再起動
$ make destroy  # 開発サーバ(Vagrant)の削除
$ make status   # 開発サーバ(Vagrant)の状態確認
$ make addkey   # コマンドの実行毎にパスフレーズの入力を催促することを回避するための設定(オプション)
$ make ssh      # SSH接続(takashiユーザ) ※ Ansibleで設定を流し込んだ後に利用可能
$ make remkey   # 開発サーバ(Vagrant)を作り直した場合に実行が必要
```
