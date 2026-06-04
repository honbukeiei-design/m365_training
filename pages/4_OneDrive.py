from pathlib import Path
import streamlit as st
from modules.training import page_header, complete_card

st.set_page_config(page_title="OneDrive Training", page_icon="☁️", layout="wide")
st.markdown(f"<style>{Path('assets/style.css').read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)
page_header("☁️", "OneDrive：保存と共有", "ファイルの保存、共有リンク、同期状態を体験します。")

if "onedrive_files" not in st.session_state:
    st.session_state.onedrive_files = {"研修メモ.docx":"非共有", "売上集計.xlsx":"非共有"}
if "onedrive_done" not in st.session_state:
    st.session_state.onedrive_done = False

st.markdown("<div class='m365-card'>", unsafe_allow_html=True)
new_file = st.text_input("新しいファイル名", "M365操作メモ.docx")
if st.button("＋ OneDriveに保存"):
    st.session_state.onedrive_files[new_file] = "保存済み"
    st.session_state.onedrive_done = True

for name, state in list(st.session_state.onedrive_files.items()):
    c1, c2, c3, c4 = st.columns([4,2,2,2])
    c1.write(f"📄 **{name}**")
    c2.write(state)
    if c3.button("共有", key=f"share_{name}"):
        st.session_state.onedrive_files[name] = "指定ユーザーと共有"
        st.session_state.onedrive_done = True
        st.rerun()
    if c4.button("同期済みにする", key=f"sync_{name}"):
        st.session_state.onedrive_files[name] = "同期済み"
        st.session_state.onedrive_done = True
        st.rerun()
st.markdown("</div>", unsafe_allow_html=True)

if st.session_state.onedrive_done:
    complete_card("OneDrive")
