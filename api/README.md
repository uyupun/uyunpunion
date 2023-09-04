# APIの環境構築(開発環境)

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
$ cd api
$ pipenv sync --dev
$ pipenv shell
$ python generate_uyunpunion_token.py   # UYUNPUNION_TOKENの生成
$ cp .env.example .env                  # UYUNPUNION_TOKENの設定が必須
$ pipenv run dev                        # サーバの起動
$ pipenv run dev --port 8081            # ポート指定する場合
$ pipenv run dev --host 0.0.0.0         # ホスト指定する場合(0.0.0.0の場合、プライベートIPでのアクセスが可能となる)
$ open localhost:8080                   # API
$ open localhost:8080/docs              # Swagger
$ open localhost:8080/redoc             # Redoc
$ python drivers/blower.py start        # ドライバ単体で実行させる場合
```

# APIの環境構築(統合開発環境/本番環境)

- 以下の用途で使用する場合にこの手順が必要です
    - 統合開発環境にAPIをデプロイする場合
    - 本番環境にAPIをデプロイする場合
    - ※ 主にMakefile経由で操作します

```bash
$ cd api
$ pipenv sync --dev
$ pipenv shell
$ python generate_uyunpunion_token.py   # UYUNPUNION_TOKENの生成
$ cp .env.example .env                  # UYUNPUNION_TOKEN、ENV=prodの設定が必須
$ make up                               # サーバの起動
$ make reload                           # サーバの再起動(graceful)
$ make down                             # サーバの停止
$ make ps                               # サーバのプロセスの確認
```
