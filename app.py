import streamlit as st
from modules.ui import load_css, titlebar, service_launcher

st.set_page_config(page_title="Microsoft 365 体験トレーニング", page_icon="🧩", layout="wide")
load_css()
titlebar()

st.markdown("""
<div class='app-shell'>
  <div class='app-header'>
    <div class='app-icon'>🧩</div>
    <div>
      <h1>Microsoft 365 体験トレーニング</h1>
      <div class='app-subtitle'>各サービスを疑似UIで操作し、完了後に実サービスへ進みます。</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

service_launcher()

st.markdown("### 体験するサービスを選択")
cols = st.columns(3)
with cols[0]:
    st.page_link("pages/1_Word.py", label="Wordを体験", icon="📄", use_container_width=True)
    st.page_link("pages/2_Excel.py", label="Excelを体験", icon="📊", use_container_width=True)
with cols[1]:
    st.page_link("pages/3_Teams.py", label="Teamsを体験", icon="💬", use_container_width=True)
    st.page_link("pages/4_OneDrive.py", label="OneDriveを体験", icon="☁️", use_container_width=True)
with cols[2]:
    st.page_link("pages/5_SharePoint.py", label="SharePointを体験", icon="📁", use_container_width=True)
    st.page_link("pages/6_Copilot.py", label="Copilotを体験", icon="🤖", use_container_width=True)
