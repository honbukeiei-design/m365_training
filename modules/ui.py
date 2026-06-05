from __future__ import annotations
from pathlib import Path
import html
import streamlit as st
from modules.services import SERVICES


def load_css() -> None:
    css = Path(__file__).resolve().parents[1].joinpath("assets", "style.css").read_text(encoding="utf-8")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def top_bar(app: str = "Microsoft 365 体験トレーニング") -> None:
    st.markdown(
        f"""
        <div class="m365-topbar">
          <div class="waffle">▦</div>
          <div class="m365-title">{html.escape(app)}</div>
          <div class="m365-search">検索</div>
          <div class="m365-user">ユーザー</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def page_title(name: str, subtitle: str = "") -> None:
    st.markdown(
        f"""
        <div class="page-title">
          <h1>{html.escape(name)}</h1>
          <p>{html.escape(subtitle)}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def training_bar(service: str, tasks: list[dict]) -> None:
    done_key = f"{service}_done"
    idx_key = f"{service}_idx"
    st.session_state.setdefault(done_key, [])
    st.session_state.setdefault(idx_key, 0)
    done = list(dict.fromkeys(st.session_state[done_key]))
    if len(done) >= len(tasks):
        st.markdown(
            f"""
            <div class="training-done">
              <strong>体験完了</strong><span>実サービスでも同じ操作を確認してください。</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.link_button(f"{service} を開く", SERVICES[service]["url"], use_container_width=True)
        return
    idx = min(len(done), len(tasks) - 1)
    st.session_state[idx_key] = idx
    st.markdown(
        f"""
        <div class="training-bar">
          <div><span class="label">体験</span> {html.escape(tasks[idx]['label'])}</div>
          <div class="count">{len(done)}/{len(tasks)} 完了</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def complete_task(service: str, task_id: str) -> None:
    key = f"{service}_done"
    st.session_state.setdefault(key, [])
    if task_id not in st.session_state[key]:
        st.session_state[key].append(task_id)
    st.rerun()


def reset(service: str) -> None:
    for key in list(st.session_state.keys()):
        if key.startswith(f"{service}_"):
            del st.session_state[key]
    st.rerun()


def tabs(service: str, tab_names: list[str]) -> str:
    key = f"{service}_tab"
    st.session_state.setdefault(key, tab_names[0])
    cols = st.columns(len(tab_names))
    for col, name in zip(cols, tab_names):
        selected = st.session_state[key] == name
        if col.button(name, key=f"{service}_tabbtn_{name}", type="primary" if selected else "secondary", use_container_width=True):
            st.session_state[key] = name
            st.rerun()
    return st.session_state[key]


def ribbon_start() -> None:
    st.markdown('<div class="ribbon-panel">', unsafe_allow_html=True)


def ribbon_end() -> None:
    st.markdown('</div>', unsafe_allow_html=True)


def service_selector_cards() -> None:
    services = list(SERVICES.keys())
    cols = st.columns(3)
    for i, name in enumerate(services):
        with cols[i % 3]:
            with st.container(border=True):
                st.markdown(f"### {name}")
                st.caption(SERVICES[name]["desc"])
                page = {
                    "Word": "pages/1_Word.py",
                    "Excel": "pages/2_Excel.py",
                    "Teams": "pages/3_Teams.py",
                    "OneDrive": "pages/4_OneDrive.py",
                    "SharePoint": "pages/5_SharePoint.py",
                    "Copilot": "pages/6_Copilot.py",
                }[name]
                st.page_link(page, label="体験する", use_container_width=True)


def service_links_bottom() -> None:
    st.markdown("---")
    st.subheader("実サービス")
    cols = st.columns(6)
    for col, (name, svc) in zip(cols, SERVICES.items()):
        with col:
            st.markdown(f"**{name}**")
            st.caption(svc["desc"])
            st.link_button("開く", svc["url"], use_container_width=True)
