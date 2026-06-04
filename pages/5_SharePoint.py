import streamlit as st
from modules.state import init_state, set_progress
from modules.tutorial import show_steps
from modules.ui import load_css, task_card

st.set_page_config(page_title="SharePoint Training", page_icon="📁", layout="wide")
load_css(); init_state()

st.title("📁 SharePoint：チームサイトとドキュメント管理")
st.caption("部門・プロジェクト単位のファイル管理、権限、ドキュメントライブラリを練習します。")

site = st.selectbox("サイト", ["総務部ポータル", "M365移行プロジェクト", "研修資料サイト"])
ribbon_tabs = ["ホーム", "ドキュメント", "ページ", "サイトコンテンツ", "権限"]
st.markdown("<div class='ribbon'>" + "".join(f"<span class='ribbon-tab {'active' if t=='ドキュメント' else ''}'>{t}</span>" for t in ribbon_tabs) + "</div>", unsafe_allow_html=True)

left, right = st.columns([2, 1])
with left:
    st.markdown(f"### {site} / ドキュメント")
    docs = [
        ("📄", "移行手順書.docx", "更新: 今日", "閲覧・編集"),
        ("📊", "受講者進捗.xlsx", "更新: 昨日", "閲覧のみ"),
        ("📁", "FAQ", "更新: 3日前", "閲覧・編集"),
        ("📄", "情報セキュリティ注意事項.docx", "更新: 5日前", "閲覧のみ"),
    ]
    st.markdown("<div class='m365-card'>", unsafe_allow_html=True)
    for icon, name, update, perm in docs:
        badge = "badge-green" if perm == "閲覧・編集" else "badge-amber"
        st.markdown(
            f"<div class='file-row'><div class='file-icon'>{icon}</div><div><strong>{name}</strong><br><span class='m365-muted'>{update}</span></div><div><span class='badge {badge}'>{perm}</span></div><div>⋯</div></div>",
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)
with right:
    st.markdown("### 権限確認")
    group = st.selectbox("対象グループ", ["サイト所有者", "サイトメンバー", "サイト閲覧者"])
    action = st.radio("確認する操作", ["閲覧", "編集", "共有リンク作成", "権限変更"])
    allowed = not (group == "サイト閲覧者" and action in ["編集", "共有リンク作成", "権限変更"]) and not (group == "サイトメンバー" and action == "権限変更")
    if st.button("権限を判定", type="primary"):
        set_progress("SharePoint", 70)
        if allowed:
            st.success("この操作は許可される想定です。")
        else:
            st.warning("この操作は制限される想定です。権限設計を確認してください。")
    task_card("課題1", "閲覧者とメンバーの違いを確認する", group in ["サイトメンバー", "サイト閲覧者"])
    task_card("課題2", "権限変更は所有者のみと理解する", action == "権限変更")

show_steps("SharePoint", [
    "① SharePointはチーム・部門で共有する正式な資料置き場です。",
    "② ドキュメントライブラリでは、ファイル更新日や権限を確認します。",
    "③ 権限変更は影響範囲が大きいため、所有者・管理者の役割として扱います。",
])
