from pathlib import Path
import streamlit as st
from modules.training import page_header, complete_card

st.set_page_config(page_title="Teams Training", page_icon="💬", layout="wide")
st.markdown(f"<style>{Path('assets/style.css').read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)
page_header("💬", "Teams：チャットと会議", "メッセージ送信、会議開始、ファイル共有を体験します。")

if "teams_messages" not in st.session_state:
    st.session_state.teams_messages = ["佐藤：会議資料を共有してください", "田中：SharePointに保存しました"]
if "teams_done" not in st.session_state:
    st.session_state.teams_done = False

st.markdown("<div class='m365-card'>", unsafe_allow_html=True)
st.subheader("チーム：M365移行プロジェクト")
for msg in st.session_state.teams_messages:
    st.chat_message("user").write(msg)
msg = st.chat_input("メッセージを入力")
if msg:
    st.session_state.teams_messages.append(f"あなた：{msg}")
    st.session_state.teams_done = True
    st.rerun()
col1, col2, col3 = st.columns(3)
if col1.button("📅 会議を開始", use_container_width=True):
    st.success("会議ウィンドウを開始しました。マイク・カメラ・参加者パネルを確認できます。")
    st.session_state.teams_done = True
if col2.button("📎 ファイルを共有", use_container_width=True):
    st.info("SharePoint上の『移行説明資料.pptx』をチャネルに共有しました。")
    st.session_state.teams_done = True
if col3.button("✅ チャネルに投稿", use_container_width=True):
    st.session_state.teams_messages.append("あなた：本日の研修ログを投稿しました")
    st.session_state.teams_done = True
    st.rerun()
st.markdown("</div>", unsafe_allow_html=True)

if st.session_state.teams_done:
    complete_card("Teams")
