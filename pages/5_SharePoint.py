from pathlib import Path
import streamlit as st
from modules.training import page_header, complete_card

st.set_page_config(page_title="SharePoint Training", page_icon="📁", layout="wide")
st.markdown(f"<style>{Path('assets/style.css').read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)
page_header("📁", "SharePoint：チーム文書管理", "サイト、ドキュメントライブラリ、権限、ニュース投稿を体験します。")

if "sp_done" not in st.session_state:
    st.session_state.sp_done = False
site = st.selectbox("サイト", ["M365移行チーム", "総務部", "情報システム"])
st.markdown("<div class='m365-card'>", unsafe_allow_html=True)
st.subheader(f"{site} / ドキュメント")
cols = st.columns(4)
if cols[0].button("📁 ライブラリ作成", use_container_width=True):
    st.success("『研修資料』ライブラリを作成しました。")
    st.session_state.sp_done = True
if cols[1].button("🔐 権限設定", use_container_width=True):
    st.info("メンバー：編集可、閲覧者：閲覧のみ に設定しました。")
    st.session_state.sp_done = True
if cols[2].button("📰 ニュース投稿", use_container_width=True):
    st.success("『M365移行のお知らせ』を投稿しました。")
    st.session_state.sp_done = True
if cols[3].button("🔗 Teams連携", use_container_width=True):
    st.info("Teamsチャネルのファイルタブと連携しました。")
    st.session_state.sp_done = True
st.table({"ファイル":["移行手順書.docx","FAQ.xlsx","研修動画リンク.url"],"状態":["公開中","編集中","公開中"],"権限":["組織内閲覧","メンバー編集","組織内閲覧"]})
st.markdown("</div>", unsafe_allow_html=True)

if st.session_state.sp_done:
    complete_card("SharePoint")
