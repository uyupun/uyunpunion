# 本番サーバ(Raspberry Pi)の環境構築

- 以下のファイルが必要です
    - `prod/id_ed25519`
    - `prod/id_ed25519.pub`

1. [Raspberry Pi 4 Model B 8GB RAM](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/?variant=raspberry-pi-4-model-b-8gb) を購入
1. microSDカードをPCに接続
1. [Raspberry Pi Imager](https://www.raspberrypi.com/software/) をインストールして起動
1. OSは「Raspberry Pi OS Lite (64-bit)」を選択
    - 構築時最新の 2023/05/03 のリリースを使用
1. ストレージは接続したmicroSDカードを選択
1. 設定から以下の項目を設定
    - ホスト名: `uyunpunion-XX.local` (`XX` はLAN内で重複しないID)
    - SSH: 公開鍵認証
    - ユーザ
        - ユーザ名: `pi`
        - パスワード: `raspberry`
        - 鍵: `prod/id_ed25519.pub` を参照
    - Wi-Fi
        - SSID: 任意
        - パスワード: 任意
        - Wi-Fiを使用する国: `JP`
    - ロケール
        - タイムゾーン: `Asia/Tokyo`
        - キーボードレイアウト: `us`
1. 「書き込む」ボタンを押して書き込みを実行
1. microSDカードをPCから取り外し、Raspberry Piに挿入して起動

```bash
$ ssh-keygen -t ed25519 -f ./id_ed25519 # 秘密鍵と公開鍵の生成
$ brew install arp-scan
$ make scan                             # LAN内のデバイスをスキャンしてRaspberry Piを探す
Interface: en0, type: EN10MB, MAC: XX:XX:XX:XX:XX:XX, IPv4: 192.168.XX.XX
Starting arp-scan 1.10.0 with 256 hosts (https://github.com/royhills/arp-scan)
...
192.168.XX.XX    d8:3a:dd:48:96:3f       Raspberry Pi Trading Ltd
...
$ make pssh                             # SSH接続(piユーザ)
$ make ssh                              # SSH接続(takashiユーザ) ※ Ansibleで設定を流し込んだ後に利用可能
$ make remkey                           # 本番サーバ(Raspberry Pi)を作り直した場合に実行が必要
$ make wlstatus                         # Wi-Fiの接続状況を確認 ※ このコマンドは本番サーバ内で実行可能
$ make wlls                             # 接続可能なWi-Fiの一覧を確認 ※ このコマンドは本番サーバ内で実行可能
$ make wlchange ssid="XXXX" psk="XXXX"  # Wi-Fiの接続先を変更 ※ このコマンドは本番サーバ内で実行可能
```

- `pssh` / `ssh` / `remkey` はホストを示す `host` の指定が可能です。デフォルトでは `uyunpunion-01.local` が指定されています
