from pathlib import Path
import streamlit as st
from modules.urls import REAL_URLS

APP_ROOT = Path(__file__).resolve().parents[1]


def load_css() -> None:
    css_path = APP_ROOT / "assets" / "style.css"
    st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)


def top_bar(app: str, title: str) -> None:
    st.markdown(
        f"""
        <div class="topbar">
          <div class="waffle">▦</div>
          <div class="appmark">{app}</div>
          <div class="searchbox">検索、コマンド、またはヘルプ</div>
          <div class="avatar">受</div>
        </div>
        <div class="page-title">{title}</div>
        """,
        unsafe_allow_html=True,
    )


def ribbon(active: str, tabs: list[str], tools: list[str] | None = None, disabled: list[str] | None = None) -> None:
    disabled = disabled or []
    tools = tools or []
    tab_html = "".join(
        f"<span class='rib-tab {'active' if tab == active else ''} {'disabled' if tab in disabled else ''}'>{tab}</span>"
        for tab in tabs
    )
    tool_html = "".join(f"<span class='rib-tool'>{tool}</span>" for tool in tools)
    st.markdown(f"<div class='ribbon'><div>{tab_html}</div><div class='toolrow'>{tool_html}</div></div>", unsafe_allow_html=True)


def card(title: str, body: str = "", badge: str | None = None) -> None:
    badge_html = f"<span class='badge blue'>{badge}</span>" if badge else ""
    st.markdown(f"<div class='card'><div class='card-title'>{title} {badge_html}</div><div class='muted'>{body}</div></div>", unsafe_allow_html=True)


def task(title: str, done: bool, detail: str = "") -> None:
    cls = "done" if done else ""
    status = "完了" if done else "未完了"
    st.markdown(f"<div class='task {cls}'><b>{title}</b><span>{status}</span><p>{detail}</p></div>", unsafe_allow_html=True)


def real_use_box(area: str) -> None:
    url = REAL_URLS.get(area, REAL_URLS["Microsoft 365"])
    st.markdown(
        f"""
        <div class="realbox">
          <div><b>{area} の体験が完了しました。</b><br><span>次は実際のMicrosoft 365で使用してみましょう。</span></div>
          <a href="{url}" target="_blank">実際に使用してみよう ↗</a>
          <code>{url}</code>
        </div>
        """,
        unsafe_allow_html=True,
    )


def progress_panel(area: str) -> None:
    value = st.session_state.progress.get(area, 0)
    st.progress(value / 100, text=f"{area} 進捗: {value}%")
