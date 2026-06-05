import streamlit as st
from modules.ui import load_css, service_launcher

st.set_page_config(page_title="Microsoft 365 体験トレーニング", page_icon="🧩", layout="wide")
load_css()

st.title("Microsoft 365 体験トレーニング")
st.caption("疑似UIで操作を体験し、各サービスの実画面へ進めます。")

service_launcher()

st.divider()
st.subheader("体験するサービスを選択")
cols = st.columns(3)
with cols[0]:
    with st.container(border=True):
        st.markdown("### 📄 Word")
        st.caption("文書作成、書式、表、コメント、共有を体験")
        st.page_link("pages/1_Word.py", label="Wordを体験", icon="📄", use_container_width=True)
    with st.container(border=True):
        st.markdown("### 📊 Excel")
        st.caption("セル編集、数式、合計、グラフ、保護を体験")
        st.page_link("pages/2_Excel.py", label="Excelを体験", icon="📊", use_container_width=True)
with cols[1]:
    with st.container(border=True):
        st.markdown("### 💬 Teams")
        st.caption("チャット、ファイル共有、会議開始を体験")
        st.page_link("pages/3_Teams.py", label="Teamsを体験", icon="💬", use_container_width=True)
    with st.container(border=True):
        st.markdown("### ☁️ OneDrive")
        st.caption("アップロード、共有、同期、復元を体験")
        st.page_link("pages/4_OneDrive.py", label="OneDriveを体験", icon="☁️", use_container_width=True)
with cols[2]:
    with st.container(border=True):
        st.markdown("### 📁 SharePoint")
        st.caption("サイト、権限、ニュース、文書管理を体験")
        st.page_link("pages/5_SharePoint.py", label="SharePointを体験", icon="📁", use_container_width=True)
    with st.container(border=True):
        st.markdown("### 🤖 Copilot")
        st.caption("要約、文章作成、次の操作提案を体験")
        st.page_link("pages/6_Copilot.py", label="Copilotを体験", icon="🤖", use_container_width=True)
