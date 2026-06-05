import streamlit as st
from modules.ui import load_css, page_header, note
from modules.urls import M365_URLS

st.set_page_config(page_title="M365 Training", page_icon="🧭", layout="wide")
load_css()
page_header("M365 Training Hub", "Word、Excel、Teamsなどを、疑似UIで操作してから実サービスへ進む研修アプリです。")
note("左のページメニューからアプリを選択してください。各ページ上部に“次に体験する操作”が表示され、完了すると実サービスURLが自動表示されます。")

cards = [
    ("Word", "リボン、文書編集、コメント、共有、クラウド保存を体験します。"),
    ("Excel", "セル編集、書式、合計、グラフ、保護、表示倍率を体験します。"),
    ("Teams", "チャット、返信、ファイル共有、会議開始を体験します。"),
    ("OneDrive", "アップロード、共有リンク、同期状態、復元を体験します。"),
    ("SharePoint", "サイト選択、ドキュメント管理、権限、ニュース投稿を体験します。"),
    ("Copilot", "依頼文、要約、文章作成、次の操作提案を体験します。"),
]

html = "<div class='card-grid'>"
for name, desc in cards:
    html += f"""
    <div class='training-card'>
      <h3>{name}</h3>
      <p>{desc}</p>
      <a class='training-link' href='{M365_URLS.get(name, M365_URLS['Microsoft 365'])}' target='_blank'>実サービスを開く ↗</a>
    </div>
    """
html += "</div>"
st.markdown(html, unsafe_allow_html=True)

st.markdown("---")
st.subheader("公開後の使い方")
st.write("GitHubに配置した後、Streamlit Community Cloudで `app.py` を指定してデプロイしてください。受講者にはStreamlitの公開URLを案内します。")
