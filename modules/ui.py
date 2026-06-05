from pathlib import Path
import streamlit as st


def load_css() -> None:
    css_path = Path(__file__).resolve().parents[1] / "assets" / "style.css"
    st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)


def page_header(title: str, subtitle: str) -> None:
    st.markdown(
        f"""
        <div class='app-hero'>
            <div>
                <div class='eyebrow'>Microsoft 365 体験トレーニング</div>
                <h1>{title}</h1>
                <p>{subtitle}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def note(text: str) -> None:
    st.markdown(f"<div class='clean-note'>{text}</div>", unsafe_allow_html=True)
