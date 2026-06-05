from __future__ import annotations
import html
import pathlib
import streamlit as st

ROOT = pathlib.Path(__file__).resolve().parents[1]

SERVICE_URLS = {
    "Word": "https://word.cloud.microsoft/",
    "Excel": "https://excel.cloud.microsoft/",
    "Teams": "https://teams.microsoft.com/",
    "OneDrive": "https://onedrive.live.com/",
    "SharePoint": "https://www.microsoft.com/ja-jp/microsoft-365/sharepoint/collaboration/",
    "Copilot": "https://copilot.microsoft.com/",
}


def load_css():
    css = (ROOT / "assets" / "style.css").read_text(encoding="utf-8")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def init_page(title: str):
    st.set_page_config(page_title=title, layout="wide", initial_sidebar_state="collapsed")
    load_css()


def training_banner(service: str, steps: list[str]):
    key = f"{service}_step"
    st.session_state.setdefault(key, 0)
    index = min(st.session_state[key], len(steps))
    if index >= len(steps):
        st.markdown(
            f"""
            <div class='done-card'>
              <strong>体験完了</strong><br>
              疑似画面で基本操作を確認できました。次は実サービスで同じ操作を試してください。
              <div class='link-row'><a class='simple-link' href='{SERVICE_URLS[service]}' target='_blank'>実サービスを開く</a></div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return len(steps), True
    st.markdown(
        f"""
        <div class='training-banner'>
          <div><strong>体験</strong>：{html.escape(steps[index])}</div>
          <div><strong>{index}/{len(steps)} 完了</strong></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    return index, False


def complete_step(service: str, current_index: int):
    key = f"{service}_step"
    if st.session_state.get(key, 0) <= current_index:
        st.session_state[key] = current_index + 1


def top_menu(active: str, tabs: list[str], key_prefix: str):
    cols = st.columns(len(tabs))
    for c, tab in zip(cols, tabs):
        with c:
            if st.button(tab, type="primary" if tab == active else "secondary", key=f"{key_prefix}_{tab}"):
                st.session_state[f"{key_prefix}_active"] = tab
                st.rerun()


def safe(s: str) -> str:
    return html.escape(s or "")
