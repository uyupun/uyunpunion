# 汎用五感伝達機構 ウユンプニオン 零号機

<img src="images/saiteida_orette.jpg" width="500px">

*──── 最低だ...俺って...*

## 概要

<img src="images/key_visual.png" width="500px">

- **汎用五感伝達機構 ウユンプニオン 零号機**(通称: **UYU 零号機**)
- **人体刺激計画**の完遂のため、五感に多彩な刺激を与えるインタフェースを提供します
- e.g. 冷却、加熱、送風、etc ...

<img src="images/uyunpunion_zero_1.jpg" width="500px">
<img src="images/uyunpunion_zero_2.jpg" width="500px">
<img src="images/uyunpunion_zero_3.jpg" width="500px">

## アーキテクチャ

### 全体像

<img src="images/architecture_uyunpunion.png" width="800px">

### ウユンプニオン・コア

- Raspberry Piから各マニピュレータを駆動させる際の回路図を以下に示します

<img src="images/architecture_uyunpunion_core.drawio.png" width="500px">

- 各マニピュレータを制御するGPIOピンはマニピュレータごとに固定とし(ウェルノウンピン)、新たなマニピュレータを接続する際は以下に示すピン番号以外を用いてください

|ピン番号|用途|
|:--|:--|
|19|ペルチェ素子の強さ(PWM)|
|20|ペルチェ素子の発熱(冷却とは排他)|
|21|ペルチェ素子の冷却(発熱とは排他)|
|23|加湿器の噴霧 ※1|
|25|ブロワーの駆動|

- ※1 加湿器のスイッチングは本来モーメンタリスイッチのため、0.5秒を目安に信号をオフにしてください
  - なお、加湿器はスイッチをオンにするごとに 電源オフ → 常時噴霧 → 3秒間隔で噴霧 → 電源オフ を繰り返します

## ディレクトリ構造

```
├ .vscode               Visual Studio Codeの設定
├ ansible
│ ├ hosts               Ansibleの接続先の設定
│ ├ roles               Ansibleの各タスク
│ ├ ansible.cfg         Ansible自体の挙動の設定
│ ├ infra.yml           Ansibleで設定を流すためのエントリーポイント
├ deploy                デプロイスクリプト関連
├ images
├ proxy
│ ├ api.toml            リバースプロキシ(Traefik)の動的設定
│ ├ docker-compose.yml  リバースプロキシ(Traefik)のDocker周りの設定
│ ├ traefik.toml        リバースプロキシ(Traefik)の静的設定
├ src
│ ├ drivers             ウユンプニオン・ドライバの制御スクリプト
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

## バージョニング

- バージョニングはセマンティックバージョニングを参考にしつつも、完全には準拠していません
- 大まかな基準としては以下の通りです
  - 互換性を損なう変更はメジャーバージョンを上げる
  - 後方互換性のある機能追加はマイナーバージョンを上げる
  - 後方互換性のあるバグ修正はパッチバージョンを上げる

## その他ドキュメント

- [APIの環境構築](./src/README.md)
- [リバースプロキシの環境構築](./proxy/README.md)
- [検証サーバの環境構築](./test/README.md)
- [Ansibleによる設定の流し込み](./ansible/README.md)
- [デプロイ](./deploy/README.md)

---

<img src="images/omedetou.jpg" width="500px">

*おめでとう ────*
