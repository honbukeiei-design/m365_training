from __future__ import annotations
import html
from pathlib import Path
import streamlit as st
from modules.services import SERVICES


def load_css() -> None:
    css_path = Path(__file__).resolve().parents[1] / "assets" / "style.css"
    st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)


def titlebar(label: str = "Microsoft 365 体験トレーニング") -> None:
    st.markdown(
        f"""
        <div class='m365-titlebar'>
            <div class='brand'>{html.escape(label)}</div>
            <div class='right'>疑似UIで体験 → 実サービスへ</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def app_header(name: str, subtitle: str) -> None:
    svc = SERVICES.get(name, {"icon": "◻️"})
    st.markdown(
        f"""
        <div class='app-shell'>
          <div class='app-header'>
            <div class='app-icon'>{svc['icon']}</div>
            <div>
              <h1>{html.escape(name)}</h1>
              <div class='app-subtitle'>{html.escape(subtitle)}</div>
            </div>
          </div>
        """,
        unsafe_allow_html=True,
    )


def close_shell() -> None:
    st.markdown("</div>", unsafe_allow_html=True)


def service_launcher(current: str | None = None) -> None:
    """Render service launch buttons with native Streamlit widgets.

    Earlier builds used a single large HTML string. On Streamlit Cloud that could be
    displayed as literal HTML if escaping/markdown parsing changed. Native widgets
    prevent that failure mode and keep links clickable.
    """
    st.markdown("##### 実サービスを開く")
    cols = st.columns(6)
    for col, (name, svc) in zip(cols, SERVICES.items()):
        with col:
            with st.container(border=True):
                label = f"{svc['icon']} {name}"
                if current == name:
                    st.markdown(f"**{label}**  ")
                    st.caption("表示中")
                else:
                    st.markdown(f"**{label}**")
                    st.caption(svc.get("description", ""))
                st.link_button("実サービスを開く", svc["url"], use_container_width=True)


def training_strip(service: str, tasks: list[dict]) -> None:
    key = f"{service}_task_index"
    done_key = f"{service}_done"
    if key not in st.session_state:
        st.session_state[key] = 0
    if done_key not in st.session_state:
        st.session_state[done_key] = []
    idx = min(st.session_state[key], len(tasks) - 1)
    complete_count = len(set(st.session_state[done_key]))
    if complete_count >= len(tasks):
        svc = SERVICES[service]
        st.success("体験完了です。実サービスでも同じ操作を確認してみましょう。")
        st.link_button(f"実体験をしてください：{service} を開く", svc["url"], use_container_width=True)
        return
    task = tasks[idx]
    st.markdown(
        f"""
        <div class='training-strip'>
          <div><strong>体験：</strong>{html.escape(task['label'])}</div>
          <div class='training-progress'>{complete_count}/{len(tasks)} 完了</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def mark_task_done(service: str, task_id: str) -> None:
    done_key = f"{service}_done"
    index_key = f"{service}_task_index"
    if done_key not in st.session_state:
        st.session_state[done_key] = []
    if task_id not in st.session_state[done_key]:
        st.session_state[done_key].append(task_id)
    st.session_state[index_key] = len(set(st.session_state[done_key]))
    st.rerun()


def reset_service(service: str) -> None:
    for k in list(st.session_state.keys()):
        if k.startswith(f"{service}_"):
            del st.session_state[k]
    st.rerun()


def ribbon_tabs(service: str, tabs: list[str], default: str = "ホーム") -> str:
    key = f"{service}_active_tab"
    if key not in st.session_state:
        st.session_state[key] = default
    cols = st.columns(len(tabs))
    for col, tab in zip(cols, tabs):
        btn_label = f"● {tab}" if st.session_state[key] == tab else tab
        if col.button(btn_label, key=f"{service}_tab_{tab}", use_container_width=True):
            st.session_state[key] = tab
            st.rerun()
    active = st.session_state[key]
    tab_html = "".join(
        f"<span class='ribbon-tab {'active' if t == active else ''}'>{html.escape(t)}</span>" for t in tabs
    )
    st.markdown(f"<div class='ribbon-tabs'>{tab_html}</div>", unsafe_allow_html=True)
    return active


def status_badge(saved: bool) -> None:
    cls = "mini-status saved" if saved else "mini-status"
    text = "保存済み" if saved else "未保存の変更"
    st.markdown(f"<span class='{cls}'>{text}</span>", unsafe_allow_html=True)
