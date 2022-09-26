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
├ ansible               Ansibleの設定
├ images
├ proxy                 リバースプロキシ(Traefik)の設定
├ src
│ ├ manipulators        ウユンプニオン・コアの制御スクリプト
│ ├ middlewares         カスタムミドルウェア
│ ├ routes              APIの各エンドポイント
│ ├ schemas             レスポンスのスキーマ
│ ├ app.py              アプリケーションのエントリーポイント
│ ├ gunicorn.conf.py    本番環境で使用するGunicornの設定
│ ├ Makefile            本番環境で使用するコマンド群の定義
│ └ settings.py         環境変数、グローバル変数
├ test                  検証サーバ(Vagrant)の設定
└ README.md
```

## APIの環境構築(開発環境)

- 以下の用途で使用する場合にこの手順が必要です
    - APIを開発する場合
    - APIの動作を検証する場合
    - API仕様(Swagger/Redoc)を閲覧したい場合

- 以下のソフトウェアが必要です
    - Python又はPyenv(Pythonのバージョンは3.9系)
    - Pipenv
    - Visual Studio Code
        - 開発しない場合(APIを動作させるのみの場合)は必要ありません
        - 本リポジトリには[VSCode上でFlake8(リンター)とBlack(フォーマッター)を動作させるための設定](./.vscode/settings.json)が含まれています

```bash
$ cd src
$ cp .env.example .env                   # UYUNPUNION_TOKENの設定が必須
$ pipenv install --dev
$ pipenv shell
$ pipenv run dev                         # サーバの起動
$ pipenv run dev --port 8081             # ポート指定する場合
$ pipenv run dev --host 0.0.0.0          # ホスト指定する場合(0.0.0.0の場合、プライベートIPでのアクセスが可能となる)
$ open localhost:8080                    # API
$ open localhost:8080/docs               # Swagger
$ open localhost:8080/redoc              # Redoc
$ python manipulators/blower.py start    # マニピュレータ単体で実行させる場合
```

## APIの環境構築(本番環境)

- 以下の用途で使用する場合にこの手順が必要です
    - 本番環境にAPIをデプロイする場合
    - ※ 主にMakefile経由で操作します

```bash
$ cd src
$ cp .env.example .env  # UYUNPUNION_TOKEN、ENV=prodの設定が必須
$ pipenv install
$ make up               # サーバの起動
$ make reload           # サーバの再起動(graceful)
$ make down             # サーバの停止
$ make ps               # サーバのプロセスの確認
```

## リバースプロキシの環境構築

- 以下の用途で使用します
    - リバースプロキシ
    - TLS終端
    - ※ 主に本番環境で使用するものです

- 以下のソフトウェアが必要です
    - Docker
    - Docker Compose

```bash
$ cd proxy
$ docker compose up -d
$ docker compose ps
$ docker compose down
$ open localhost:8080                                                   # ダッシュボード
$ curl -H "Host: uyunpunion.uyupun.tech" -L "localhost:80/ping"         # 疎通確認
$ curl -H "Host: uyunpunion.uyupun.tech" -L "<private ip address>/ping" # 疎通確認
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
$ cd test
$ vagrant up
$ vagrant ssh
$ vagrant status
$ vagrant halt
$ vagrant reload
$ vagrant destroy
```

<img src="images/omedetou.jpg" width="500px">

*おめでとう ────*
