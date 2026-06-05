# Microsoft 365 体験トレーニング

Microsoft 365 の主要サービスを、実操作画面に近いUI上で体験するStreamlitアプリです。

## 対象サービス

- Word
- Excel
- Teams
- OneDrive
- SharePoint
- Copilot

## 実行方法

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 設計方針

- M365風の画面上で操作を体験できる構成
- 操作後に別の「適用」ボタンを押さず、自動でUIに反映
- 各サービスの体験完了後は、下部の実サービスリンクから本番環境へ移行

## 注意

このアプリは研修用の疑似UIです。Microsoft 365そのものではありません。
