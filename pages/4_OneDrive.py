import streamlit as st
from modules.state import init_state, set_progress
from modules.tutorial import show_steps
from modules.ui import load_css, task_card

st.set_page_config(page_title="OneDrive Training", page_icon="☁", layout="wide")
load_css(); init_state()

st.title("☁ OneDrive：個人ファイルと共有リンク")
st.caption("個人作業ファイルの保存、共有リンク、アクセス権を確認します。")

files = [
    {"icon": "📄", "name": "M365移行説明.docx", "owner": "自分", "status": "非共有"},
    {"icon": "📊", "name": "部署別進捗.xlsx", "owner": "自分", "status": "指定ユーザー"},
    {"icon": "📎", "name": "研修アンケート.pdf", "owner": "自分", "status": "組織内リンク"},
]

left, right = st.columns([2, 1])
with left:
    st.markdown("### ファイル一覧")
    st.markdown("<div class='m365-card'>", unsafe_allow_html=True)
    for f in files:
        st.markdown(
            f"""
            <div class="file-row">
              <div class="file-icon">{f['icon']}</div>
              <div><strong>{f['name']}</strong><br><span class="m365-muted">所有者: {f['owner']}</span></div>
              <div><span class="badge badge-gray">{f['status']}</span></div>
              <div>⋯</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)
with right:
    st.markdown("### 共有設定")
    selected = st.selectbox("対象ファイル", [f["name"] for f in files])
    permission = st.radio("リンク権限", ["指定したユーザー", "組織内のユーザー", "リンクを知っている全員（非推奨）"])
    allow_edit = st.toggle("編集を許可", value=False)
    expire = st.date_input("リンク有効期限")
    if st.button("共有リンクを作成", type="primary"):
        set_progress("OneDrive", 80)
        st.success(f"{selected} の共有リンクを「{permission}」で作成しました。")
    task_card("課題1", "共有範囲は原則として指定ユーザーにする", permission == "指定したユーザー")
    task_card("課題2", "編集許可の有無を確認する", True)

show_steps("OneDrive", [
    "① OneDriveは個人の作業ファイル置き場です。完成前の資料や自分中心の資料に向いています。",
    "② 共有時は『誰が見られるか』『編集できるか』『期限があるか』を確認します。",
    "③ チームで継続管理する資料はSharePointへ移すことを検討します。",
])
