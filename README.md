# 汎用五感伝達機構 ウユンプニオン 零号機

<img src="images/saiteida_orette.jpg" width="500px">

*──── 最低だ...俺って...*

## 概要

<img src="images/key_visual.png" width="500px">

- **汎用五感伝達機構 ウユンプニオン 零号機**(通称: **UYU 零号機**)
- **人体刺激計画**の完遂のため、五感に多彩な刺激を与えるインタフェースを提供します
- 冷却、加熱、送風、etc ...

## アーキテクチャ

### 全体像

<img src="images/architecture_uyunpunion.png" width="800px">

### ウユンプニオン・コア

<img src="images/architecture_uyunpunion_core.png" width="500px">

### ディレクトリ構造

```
├ .vscode               Visual Studio Codeの設定
├ ansible               Ansibleの設定(TLS終端、リバプロ、WSGI、ASGI等)
├ images
├ qemu                  開発環境でRaspberry Pi OSを立ち上げるための設定
├ src
│ ├ manipulators        ウユンプニオン・コアの制御スクリプト
│ ├ middlewares         カスタムミドルウェア
│ ├ routes              APIの各エンドポイント
│ ├ schemas             レスポンスのスキーマ
│ ├ app.py              アプリケーションのエントリーポイント
│ ├ gunicorn.conf.py    Gunicornの設定
│ └ settings.py         環境変数、グローバル変数
└ README.md
```

## APIの環境構築(開発環境)

```bash
$ cd src
$ cp .env.example .env          # UYUNPUNION_TOKENの設定が必須
$ pipenv install --dev
$ pipenv run dev                # サーバの起動
$ pipenv run dev --port 8081    # ポートを指定する場合
$ open localhost:8080           # API
$ open localhost:8080/docs      # OpenAPI
$ open localhost:8080/redoc     # Redoc
```

## APIの環境構築(本番環境)

```bash
$ cd src
$ cp .env.example .env  # UYUNPUNION_TOKENの設定が必須
$ pipenv install
$ pipenv run prod               # サーバの起動
$ pipenv run prod --bind :8081  # ポートを指定する場合
```

## Raspberry Piの検証環境の構築

- Raspberry Pi OS Buster armhf

```bash
$ brew install qemu
$ qemu-system-aarch64 --version
$ cd qemu
$ chmod +x ./download.sh
$ chmod +x ./run.sh
$ ./setup.sh
$ ./run.sh
```

<img src="images/omedetou.jpg" width="500px">

*おめでとう ────*
