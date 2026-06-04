from pathlib import Path
import streamlit as st

st.set_page_config(page_title="M365 Training UI", page_icon="🧩", layout="wide")
css = Path("assets/style.css").read_text(encoding="utf-8")
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

st.sidebar.title("M365 Training")
st.sidebar.caption("疑似UIで操作を練習し、最後に実サービスへ移動します。")
license_type = st.sidebar.selectbox("ライセンス想定", ["Microsoft 365 F3", "Business Standard", "Microsoft 365 E3"], index=2)
st.session_state["license_type"] = license_type
st.sidebar.divider()
st.sidebar.markdown("**操作対象**")
st.sidebar.page_link("app.py", label="ホーム", icon="🏠")
st.sidebar.page_link("pages/1_Word.py", label="Word", icon="📄")
st.sidebar.page_link("pages/2_Excel.py", label="Excel", icon="📊")
st.sidebar.page_link("pages/3_Teams.py", label="Teams", icon="💬")
st.sidebar.page_link("pages/4_OneDrive.py", label="OneDrive", icon="☁️")
st.sidebar.page_link("pages/5_SharePoint.py", label="SharePoint", icon="📁")
st.sidebar.page_link("pages/6_Copilot.py", label="Copilot", icon="🤖")

st.markdown("""
<div class="page-heading">
  <div class="app-icon">🧩</div>
  <div>
    <h1>Microsoft 365 研修シミュレーター</h1>
    <p>Word / Excel / Teams / OneDrive / SharePoint / Copilot を、実際の画面に近い疑似UIで体験します。</p>
  </div>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("""<div class="m365-card"><h3>1. 操作する</h3><p class="small-note">リボン、ツールバー、保存、共有などを押して画面変化を確認します。</p></div>""", unsafe_allow_html=True)
with c2:
    st.markdown("""<div class="m365-card"><h3>2. 結果を見る</h3><p class="small-note">文書、表、チャット、共有状態などがUI上に反映されます。</p></div>""", unsafe_allow_html=True)
with c3:
    st.markdown("""<div class="m365-card"><h3>3. 実際に使う</h3><p class="small-note">体験完了後、公式URLを開いて本番環境で同じ操作を試します。</p></div>""", unsafe_allow_html=True)

st.info("左メニューから Word または Excel を開くと、リボン操作が展開・反映される研修画面を確認できます。")
