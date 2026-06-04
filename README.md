# M365 Training UI Simulator

Microsoft 365 移行研修向けの Streamlit アプリです。Word / Excel / Teams / OneDrive / SharePoint / Copilot の操作を、実画面に近い疑似UIで体験できます。

## 今回の版の特徴

- Word のリボンタブが展開され、各機能が文書画面に反映されます。
  - ホーム / 挿入 / レイアウト / デザイン / 校閲 / 表示 / 差し込み文書
  - 太字 / 下線 / 箇条書き / スタイル / コメント / 共有
- Word は入力欄と表示欄を分けず、白紙ページ上で直接編集します。
- Excel はセルを直接編集でき、セル書式、合計、行挿入、グラフ、保護、表示倍率を体験できます。
- 操作完了後に、実際の Microsoft 365 サービスURLを表示します。
- 画面全体を Microsoft 365 風のタイトルバー、リボン、作業領域、ステータスバーで構成しています。

## 実行方法

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Streamlit Community Cloud で公開する場合

1. GitHub にこのフォルダの中身をアップロードします。
2. Streamlit Community Cloud にログインします。
3. New app を選択します。
4. Repository に `honbukeiei-design/m365_training` を指定します。
5. Branch は `main`、Main file path は `app.py` を指定します。
6. Deploy を押します。

公開URLは、Streamlit側で設定したアプリ名に応じて次の形式になります。

```text
https://設定したアプリ名.streamlit.app/
```

## APIキーについて

Copilot画面は `OPENAI_API_KEY` が未設定でもデモ応答で動作します。実AI連携を行う場合のみ、Streamlit Cloud の Secrets またはローカル環境変数に `OPENAI_API_KEY` を設定してください。

## 注意

このアプリは研修用の疑似UIです。Microsoft 365 の公式UIを完全に複製するものではありません。商標・サービス名称は説明目的で使用しています。
