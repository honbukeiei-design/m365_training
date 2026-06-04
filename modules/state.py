import streamlit as st

AREAS = ["Word", "Excel", "Teams", "OneDrive", "SharePoint", "Copilot"]

DEFAULT_FILES = [
    {"name": "移行説明会_案内.docx", "kind": "Word", "owner": "自分", "shared": "自分のみ", "favorite": False},
    {"name": "部署別ライセンス一覧.xlsx", "kind": "Excel", "owner": "総務", "shared": "指定ユーザー", "favorite": True},
    {"name": "研修資料.pdf", "kind": "PDF", "owner": "情報政策", "shared": "組織内", "favorite": False},
]

DEFAULT_MESSAGES = [
    {"name": "佐藤", "text": "M365研修資料をSharePointに置きました。確認お願いします。", "mine": False},
    {"name": "田中", "text": "承知しました。Teams会議でも確認しましょう。", "mine": False},
]


def init_state() -> None:
    st.session_state.setdefault("license", "Microsoft 365 Business Standard")
    st.session_state.setdefault("role", "一般職員")
    st.session_state.setdefault("progress", {area: 0 for area in AREAS})
    st.session_state.setdefault("word_saved", False)
    st.session_state.setdefault("word_comments", [])
    st.session_state.setdefault("word_shared_to", "")
    st.session_state.setdefault("excel_filter", "すべて")
    st.session_state.setdefault("excel_comment", "")
    st.session_state.setdefault("excel_chart", False)
    st.session_state.setdefault("teams_messages", DEFAULT_MESSAGES.copy())
    st.session_state.setdefault("teams_meeting", False)
    st.session_state.setdefault("teams_channel", "一般")
    st.session_state.setdefault("onedrive_files", DEFAULT_FILES.copy())
    st.session_state.setdefault("onedrive_selected", DEFAULT_FILES[0]["name"])
    st.session_state.setdefault("onedrive_link", "")
    st.session_state.setdefault("sp_site", "総務部ポータル")
    st.session_state.setdefault("sp_news", [])
    st.session_state.setdefault("sp_library_view", "一覧")
    st.session_state.setdefault("copilot_history", [])


def set_progress(area: str, value: int) -> None:
    init_state()
    st.session_state.progress[area] = max(st.session_state.progress.get(area, 0), min(100, value))


def reset_area(area: str) -> None:
    init_state()
    st.session_state.progress[area] = 0
