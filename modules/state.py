import streamlit as st

DEFAULT_PROGRESS = {
    "Word": 0,
    "Excel": 0,
    "Teams": 0,
    "OneDrive": 0,
    "SharePoint": 0,
    "Copilot": 0,
}


def init_state() -> None:
    st.session_state.setdefault("license", "Microsoft 365 Business Standard")
    st.session_state.setdefault("role", "一般職員")
    st.session_state.setdefault("progress", DEFAULT_PROGRESS.copy())
    st.session_state.setdefault("chat_messages", [
        {"name": "佐藤", "text": "移行後のファイル共有ルールを確認したいです。", "mine": False},
        {"name": "田中", "text": "会議資料はチームのチャネルに置きました。", "mine": False},
    ])


def set_progress(area: str, value: int) -> None:
    init_state()
    st.session_state.progress[area] = max(st.session_state.progress.get(area, 0), value)


def get_progress(area: str) -> int:
    init_state()
    return st.session_state.progress.get(area, 0)
