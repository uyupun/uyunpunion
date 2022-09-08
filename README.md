# 汎用五感伝達機構 ウユンプニオン 零号機

<img src="images/saiteida_orette.jpg" width="500px">

*──── 最低だ...俺って...*

## 概要

<img src="images/key_visual.png" width="500px">

- 汎用五感伝達機構 ウユンプニオン 零号機(通称: UYU 零号機)
- 五感に多彩な刺激を与えるためのインタフェースを提供します
- 冷却、加熱、送風、etc ...

## アーキテクチャ

### 全体像

<img src="images/architecture_uyunpunion.png" width="800px">

### ウユンプニオン・コア

<img src="images/architecture_uyunpunion_core.png" width="500px">

### ディレクトリ構造

```
├ ansible       Ansibleの設定
├ images
├ README.md
├ server        Webサーバ、ASGI、API等
├ manipulator   ウユンプニオン・コアを制御するためのコード
└ vagrant       検証用途で使用するVagrantの設定
```

## 環境構築

```bash
$ cd server
$ pipenv install
$ pipenv shell
$ uvicorn app:app --reload --port 8080
```

<img src="images/omedetou.jpg" width="500px">

*おめでとう ────*
