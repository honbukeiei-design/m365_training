# M365 Training Lab

買い切り型OfficeからMicrosoft 365へ移行する職員向けの、Streamlit製トレーニングアプリです。
Word / Excel / Teams / OneDrive / SharePoint / Copilot を、実際の操作に近い疑似UIで練習できます。

> このプロジェクトは研修用シミュレーターです。Microsoft公式製品ではなく、Microsoftによる承認・提携を示すものではありません。

## 特徴

- Microsoft 365風の疑似UI
- ライセンス別の機能制限表示
- Word / Excel / Teams / OneDrive / SharePoint / Copilot のページ分割
- 進捗トラッキング
- Copilot風の研修用AI支援
- `OPENAI_API_KEY` 未設定時はモック応答で動作
- GitHub公開しやすいREADME / LICENSE / .gitignore付き

## 画面構成

```text
m365-training-app/
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── modules/
│   ├── copilot.py
│   ├── license.py
│   ├── state.py
│   ├── tutorial.py
│   └── ui.py
├── pages/
│   ├── 1_Word.py
│   ├── 2_Excel.py
│   ├── 3_Teams.py
│   ├── 4_OneDrive.py
│   ├── 5_SharePoint.py
│   └── 6_Copilot.py
├── assets/
│   └── style.css
└── data/
    └── scenarios.json
```

## セットアップ

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Copilot風AI応答を有効化する場合

`.env.example` を参考に環境変数を設定してください。

```bash
export OPENAI_API_KEY="your-api-key"
export OPENAI_MODEL="gpt-4o-mini"
streamlit run app.py
```

APIキーを設定しない場合でも、モック応答でアプリは動作します。

## 研修での使い方

1. サイドバーで想定ライセンスと受講者ロールを選択します。
2. 各ページで操作を疑似体験します。
3. 操作ガイドに沿って課題を完了します。
4. 進捗バーで学習状況を確認します。

## 実運用に向けた拡張案

- 受講者ログイン
- SQLite / PostgreSQL による進捗保存
- 部署別シナリオ
- 管理者向けダッシュボード
- SCORM / LMS連携
- Microsoft Graph API連携
- アクセシビリティチェック

## GitHub公開手順

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_NAME/m365-training-app.git
git push -u origin main
```

## 注意事項

- UIは研修用の疑似再現であり、Microsoft 365の実画面と完全一致するものではありません。
- ライセンス差分は研修用に単純化しています。実際の契約・機能差分は組織の契約内容を確認してください。
- AI応答は下書き支援です。機密情報・個人情報の取り扱いには十分注意してください。

## License

MIT
