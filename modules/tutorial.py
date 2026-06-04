import streamlit as st
from modules.state import set_progress


def show_steps(area: str, steps: list[str]) -> None:
    key = f"{area}_step"
    st.session_state.setdefault(key, 0)
    step = st.session_state[key]

    st.markdown("### 操作ガイド")
    st.progress((step + 1) / len(steps))
    st.info(steps[step])

    col1, col2, col3 = st.columns([1, 1, 4])
    with col1:
        if st.button("戻る", key=f"{area}_prev", disabled=step == 0):
            st.session_state[key] -= 1
            st.rerun()
    with col2:
        label = "完了" if step == len(steps) - 1 else "次へ"
        if st.button(label, key=f"{area}_next"):
            if step < len(steps) - 1:
                st.session_state[key] += 1
            else:
                set_progress(area, 100)
                st.success(f"{area} の演習を完了しました。")
            st.rerun()
