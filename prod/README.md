# 本番サーバ(Raspberry Pi)の環境構築

1. [Raspberry Pi 4 Model B 8GB RAM](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/?variant=raspberry-pi-4-model-b-8gb) を購入
1. microSDカードをPCに接続
1. [Raspberry Pi Imager](https://www.raspberrypi.com/software/) をインストールして起動
1. OSは「Raspberry Pi OS Lite (64-bit)」を選択
1. ストレージは接続したmicroSDカードを選択
1. 設定から以下の項目を設定
    - ホスト名: `uyunpunion.local`
    - SSH: パスワード認証
    - ユーザ
        - ユーザ名: `pi`
        - パスワード: `raspberry`
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
$ ssh pi@192.168.XX.XX
$ ssh pi@raspberry.local
```
