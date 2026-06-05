# Microsoft 365 体験トレーニング

Streamlitで動作する、Microsoft 365移行研修向けの疑似操作アプリです。
Word、Excel、Teams、OneDrive、SharePoint、Copilotの基本操作を、実際のアプリ画面に近い構成で体験できます。

## 実行方法

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 構成

- `app.py` : トップ画面
- `pages/` : 各サービスの体験画面
- `modules/` : 共通UI・進捗管理
- `assets/style.css` : M365風UI

## 注意

これは研修用の疑似UIです。Microsoft 365公式サービスそのものではありません。
