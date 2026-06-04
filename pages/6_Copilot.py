from pathlib import Path
import streamlit as st
from modules.training import page_header, complete_card
from modules.copilot import ask_copilot

st.set_page_config(page_title="Copilot Training", page_icon="🤖", layout="wide")
st.markdown(f"<style>{Path('assets/style.css').read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)
page_header("🤖", "Copilot：依頼と生成", "要約、メール案、表作成などを依頼する体験をします。APIキー未設定時はデモ応答します。")

if "copilot_done" not in st.session_state:
    st.session_state.copilot_done = False
prompt = st.text_area("Copilotに依頼する内容", "M365移行後のファイル保存ルールを職員向けに短く要約してください。", height=120)
if st.button("生成する", type="primary"):
    st.markdown("<div class='m365-card'>", unsafe_allow_html=True)
    st.markdown(ask_copilot(prompt))
    st.markdown("</div>", unsafe_allow_html=True)
    st.session_state.copilot_done = True

if st.session_state.copilot_done:
    complete_card("Copilot")
