# m365_training

Microsoft 365移行研修用のStreamlitアプリです。

## 特徴

- Word / Excel / Teams / OneDrive / SharePoint / Copilot の疑似UIを収録
- 各ページ上部に「次に体験する操作」を表示
- 操作完了後、実サービスURLを自動表示
- WordとExcelはリボンタブを展開し、ボタン操作がUIに反映される設計
- GitHubとStreamlit Community Cloudで公開しやすい構成

## 実行方法

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Streamlit Community Cloudで公開する場合

1. GitHubにこのプロジェクトをアップロード
2. Streamlit Community CloudでNew appを選択
3. Repository: `honbukeiei-design/m365_training`
4. Branch: `main`
5. Main file path: `app.py`
6. Deploy

## 実体験URL

- Word: https://word.cloud.microsoft/ja-jp/
- Excel: https://excel.cloud.microsoft/ja-jp/
- Teams: https://www.microsoft.com/ja-jp/microsoft-teams/log-in
- OneDrive: https://onedrive.live.com/
- SharePoint: https://www.microsoft.com/ja-jp/microsoft-365/sharepoint/collaboration
- Copilot: https://copilot.microsoft.com/
- Microsoft 365: https://www.office.com/

## 注意

このアプリは研修用の疑似UIです。Microsoft公式アプリではありません。
Microsoft、Microsoft 365、Word、Excel、Teams、OneDrive、SharePoint、CopilotはMicrosoft Corporationの商標または登録商標です。
