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
├ src
│ ├ manipulators        ウユンプニオン・コアの制御スクリプト
│ ├ middlewares         カスタムミドルウェア
│ ├ routes              APIの各エンドポイント
│ ├ schemas             レスポンスのスキーマ
│ ├ app.py              アプリケーションのエントリーポイント
│ ├ gunicorn.conf.py    Gunicornの設定
│ └ settings.py         環境変数、グローバル変数
├ vagrant               検証サーバの設定
└ README.md
```

## APIの環境構築(開発環境)

- 以下の用途で使用する場合にこの手順が必要です
    - APIを開発する場合
    - APIの動作を検証する場合

- 以下のソフトウェアが必要です
    - Python又はPyenv
    - Pipenv
    - Visual Studio Code
        - 開発しない場合(APIを動作させるのみの場合)は必要ありません
        - 本リポジトリには[VSCode上でFlake8(リンター)とBlack(フォーマッター)を動作させるための設定](./.vscode/settings.json)が含まれています

```bash
$ cd src
$ cp .env.example .env          # UYUNPUNION_TOKENの設定が必須
$ pipenv install --dev
$ pipenv shell
$ pipenv run dev                # サーバの起動
$ pipenv run dev --port 8081    # ポート指定する場合
$ open localhost:8080           # API
$ open localhost:8080/docs      # OpenAPI
$ open localhost:8080/redoc     # Redoc
```

## APIの環境構築(本番環境)

```bash
$ cd src
$ cp .env.example .env          # UYUNPUNION_TOKENの設定が必須
$ pipenv install
$ pipenv run prod               # サーバの起動
$ pipenv run prod --bind :8081  # ポート指定する場合
```

## 検証サーバの環境構築

- 以下の用途で使用します
    - Ansibleのテスト
    - より本番環境に近い環境での動作確認

- 以下のソフトウェアが必要です
    - Homebrew
    - VirtualBox
    - Vagrant

```bash
$ cd vagrant
$ vagrant up
$ vagrant ssh
$ vagrant status
$ vagrant halt
$ vagrant reload
$ vagrant destroy
```

<img src="images/omedetou.jpg" width="500px">

*おめでとう ────*
