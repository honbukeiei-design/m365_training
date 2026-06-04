import streamlit as st
from modules.license import get_license_profile, LICENSE_FEATURES
from modules.state import init_state
from modules.ui import load_css, card

st.set_page_config(
    page_title="M365 Training Lab",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded",
)
load_css()
init_state()

st.sidebar.title("M365 Training Lab")
st.sidebar.caption("買い切り型OfficeからMicrosoft 365へ移行する職員向け教材")
st.sidebar.selectbox(
    "想定ライセンス",
    list(LICENSE_FEATURES.keys()),
    key="license",
)
st.sidebar.selectbox(
    "受講者ロール",
    ["一般職員", "管理者", "部門リーダー"],
    key="role",
)
st.sidebar.divider()
st.sidebar.write("進捗")
for area, value in st.session_state.progress.items():
    st.sidebar.progress(value / 100, text=f"{area}: {value}%")

license_profile = get_license_profile(st.session_state.license)

st.markdown(
    f"""
    <div class="m365-hero">
      <h1>📘 Microsoft 365 移行トレーニング</h1>
      <p>Word / Excel / Teams / OneDrive / SharePoint / Copilot の操作を、実際の業務画面に近い疑似UIで練習します。</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")
col1, col2, col3 = st.columns(3)
with col1:
    card("現在のライセンス", st.session_state.license, "選択中")
with col2:
    card("受講者ロール", st.session_state.role, "シナリオ分岐")
with col3:
    card("利用目的", "旧Office操作からクラウド共同編集・共有・会議連携へ移行", "研修")

st.markdown("## 学習メニュー")
menu = [
    ("📄 Word", "文書作成、保存、共有、Copilot下書き支援"),
    ("📊 Excel", "表計算、関数、集計、共同編集の基礎"),
    ("💬 Teams", "チャット、チャネル、会議、ファイル連携"),
    ("☁ OneDrive", "個人用ファイル、共有リンク、アクセス権"),
    ("📁 SharePoint", "チームサイト、ドキュメントライブラリ、権限"),
    ("🤖 Copilot", "研修用AI支援、要約、文面作成、指示の書き方"),
]
cols = st.columns(2)
for i, (title, desc) in enumerate(menu):
    with cols[i % 2]:
        card(title, desc)

st.markdown("## ライセンス別の体験差分")
features = {
    "デスクトップアプリ": "desktop",
    "Web版Office": "web_office",
    "OneDrive": "onedrive",
    "SharePoint": "sharepoint",
    "Teams基本機能": "teams_basic",
    "高度なセキュリティ": "advanced_security",
    "Copilot導入前提": "copilot_ready",
}
feature_rows = []
for label, key in features.items():
    feature_rows.append({"機能": label, "利用可否": "✅ 利用可" if license_profile.get(key) else "制限あり"})
st.dataframe(feature_rows, use_container_width=True, hide_index=True)

st.info("左側のページメニューから各アプリの演習画面を開いてください。")
st.markdown("<div class='footer-note'>This project is a training simulator. It is not affiliated with or endorsed by Microsoft.</div>", unsafe_allow_html=True)
