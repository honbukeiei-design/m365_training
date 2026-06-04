from pathlib import Path
import streamlit as st

APP_ROOT = Path(__file__).resolve().parents[1]


def load_css() -> None:
    css_path = APP_ROOT / "assets" / "style.css"
    st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)


def card(title: str, body: str = "", badge: str | None = None) -> None:
    badge_html = f" <span class='badge badge-blue'>{badge}</span>" if badge else ""
    st.markdown(
        f"""
        <div class="m365-card">
          <div class="m365-section-title">{title}{badge_html}</div>
          <div class="m365-muted">{body}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def ribbon(active: str, tabs: list[str], disabled: list[str] | None = None) -> None:
    disabled = disabled or []
    html = ["<div class='ribbon'>"]
    for tab in tabs:
        cls = "ribbon-tab"
        if tab == active:
            cls += " active"
        if tab in disabled:
            cls += " disabled"
        html.append(f"<span class='{cls}'>{tab}</span>")
    html.append("</div>")
    st.markdown("".join(html), unsafe_allow_html=True)


def task_card(title: str, description: str, done: bool = False) -> None:
    cls = "task-card done" if done else "task-card"
    status = "完了" if done else "未完了"
    badge = "badge-green" if done else "badge-gray"
    st.markdown(
        f"""
        <div class="{cls}">
          <strong>{title}</strong> <span class="badge {badge}">{status}</span><br>
          <span class="m365-muted">{description}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
