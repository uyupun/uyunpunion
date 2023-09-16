# 本番サーバ(Raspberry Pi)の環境構築

- 以下のファイルが必要です
    - `prod/id_ed25519`

1. [Raspberry Pi 4 Model B 8GB RAM](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/?variant=raspberry-pi-4-model-b-8gb) を購入
1. microSDカードをPCに接続
1. [Raspberry Pi Imager](https://www.raspberrypi.com/software/) をインストールして起動
1. OSは「Raspberry Pi OS Lite (64-bit)」を選択
    - 構築時最新の 2023/05/03 のリリースを使用
1. ストレージは接続したmicroSDカードを選択
1. 設定から以下の項目を設定
    - ホスト名: `uyunpunion.local`
    - SSH: 公開鍵認証
    - ユーザ
        - ユーザ名: `pi`
        - 鍵: `prod/id_ed25519.pub` を参照
    - Wi-Fi
        - SSID: 任意
        - パスワード: 任意
        - Wi-Fiを使用する国: `JP`
    - ロケール
        - タイムゾーン: `Asia/Tokyo`
        - キーボードレイアウト: `us`
1. 「書き込む」ボタンを押して書き込みを実行

```bash
$ brew install arp-scan
$ arp-scan -l --interface en0
Interface: en0, type: EN10MB, MAC: XX:XX:XX:XX:XX:XX, IPv4: 192.168.XX.XX
Starting arp-scan 1.10.0 with 256 hosts (https://github.com/royhills/arp-scan)
...
192.168.XX.XX    d8:3a:dd:48:96:3f       Raspberry Pi Trading Ltd
...
$ cd prod
$ ssh -i id_ed25519 pi@192.168.XX.XX                                        # SSH接続(piユーザ)
$ ssh -i id_ed25519 pi@uyunpunion.local                                     # SSH接続(piユーザ)
$ ssh -i ../playbook/roles/user/files/id_ed25519 takashi@uyunpunion.local   # SSH接続(takashiユーザ)
$ ssh-keygen -R 192.168.XX.XX                                               # 本番サーバを作り直した場合に実行が必要
$ ssh-keygen -R uyunpunion.local                                            # 本番サーバを作り直した場合に実行が必要
$ make wlan-status                                                          # Wi-Fiの接続状況を確認
$ make wlan-ls                                                              # 接続可能なWi-Fiの一覧を確認
$ make wlan-change ssid="XXXX" psk="XXXX"                                   # Wi-Fiの接続先を変更
```
