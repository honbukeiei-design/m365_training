# Microsoft 365 体験トレーニング

Microsoft 365 の主要サービスを、M365風の疑似UI上で体験するための Streamlit アプリです。

## 体験できる内容

- Word: リボン操作、本文編集、表挿入、保存・共有
- Excel: B5セル選択、数式バーへの `=SUM(B2:B4)` 入力、計算、グラフ、シート保護
- Outlook: 新規メール作成、宛先・件名・本文入力、本文中の @メンション、添付、送信
- Teams: Shift+Enterによる改行、Enterによる送信、@メンション、ファイル共有、リアクション、会議開始
- OneDrive: ファイル選択、アップロード、共有リンク、同期確認、復元
- SharePoint: サイト選択、ドキュメント追加、権限確認、ニュース投稿
- Copilot: プロンプト入力、要約、文章整理、操作提案

## 実行方法

```bash
pip install -r requirements.txt
streamlit run app.py
```

## v9 修正内容

- Outlookの予定表作成シナリオを削除しました。
- Outlookの添付操作に、ドラッグ＆ドロップ風アニメーションを追加しました。
- Teamsに「Shift+Enterで改行」「Enterで送信」の体験シナリオを追加しました。
- Teamsの入力欄を実操作に近い複数行入力に変更し、Enterキーで送信できるようにしました。
- 既存のM365風デザインは維持しています。
