# APIの環境構築

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
$ pipenv run pre-commit install         # pre-commitの設定
$ pipenv shell
$ python generate_uyunpunion_token.py   # UYUNPUNION_TOKENの生成
$ cp .env.example .env                  # UYUNPUNION_TOKENの設定が必須、起動アドレスや起動ポートの設定も可能
$ pipenv run dev                        # サーバの起動
$ open localhost:8080                   # API
$ open localhost:8080/docs              # Swagger
$ open localhost:8080/redoc             # Redoc
$ python drivers/blower.py start        # ドライバ単体で実行させる場合
$ pipenv run flake8 .                   # リンター(Flake8)の実行
$ pipenv run black .                    # フォーマッタ(Black)の実行(自動修正)
$ pipenv run isort .                    # インポートのソート(isort)の実行(自動修正)
$ pipenv run pyright .                  # 型チェッカー(Pyright)の実行
```

# APIの本番ビルド

- 以下の用途で使用する場合にこの手順が必要です
    - APIの本番ビルドを開発環境で検証する場合
    - ※ 実際の統合開発環境/本番環境ではsystemdからGunicornを操作します

```bash
$ cd api
$ pipenv sync --dev
$ pipenv shell
$ python generate_uyunpunion_token.py   # UYUNPUNION_TOKENの生成
$ cp .env.example .env                  # UYUNPUNION_TOKEN、ENV=prodの設定が必須
$ make start                            # デーモン(Gunicorn)の起動
$ make restart                          # デーモン(Gunicorn)の再起動
$ make stop                             # デーモン(Gunicorn)の停止
$ make ps                               # デーモン(Gunicorn)のプロセスの確認(8080番ポート)
$ make ps port=8081                     # デーモン(Gunicorn)のプロセスの確認(ポート番号を指定)
```
