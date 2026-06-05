import html
import streamlit as st
from modules.ui import load_css, titlebar, app_header, close_shell, service_launcher, training_strip, ribbon_tabs, mark_task_done, reset_service
SERVICE="Teams"
TASKS=[{"id":"chat","label":"チャットで宛先とメッセージを選び、送信してください。"},{"id":"share","label":"ファイルを選び、チャットに共有してください。"},{"id":"meeting","label":"会議の種類を選び、会議開始を反映してください。"}]
TABS=["チャット","チーム","予定表","ファイル","アプリ"]
st.set_page_config(page_title="Teams 体験",page_icon="💬",layout="wide")
load_css(); titlebar(); service_launcher(SERVICE); training_strip(SERVICE,TASKS)
st.session_state.setdefault("Teams_messages", ["佐藤: 会議資料を確認してください。", "田中: OneDriveに保存しました。"])
st.session_state.setdefault("Teams_shared", "未共有")
st.session_state.setdefault("Teams_meeting", "未開始")
app_header("Teams","チャット、ファイル共有、会議開始を選択肢付きで体験します。")
active=ribbon_tabs(SERVICE,TABS)
st.markdown("<div class='ribbon'>",unsafe_allow_html=True)
if active=="チャット":
    to=st.selectbox("送信先",["佐藤さん","田中さん","M365移行チーム"])
    msg=st.text_input("メッセージ",value="資料を共有しました。確認をお願いします。")
    if st.button("送信",use_container_width=True):
        st.session_state.Teams_messages.append(f"あなた → {to}: {msg}"); mark_task_done(SERVICE,"chat")
elif active=="ファイル":
    f=st.selectbox("共有するファイル",["移行手順書.docx","研修日程.xlsx","FAQ.pdf"])
    if st.button("チャットに共有",use_container_width=True):
        st.session_state.Teams_shared=f; st.session_state.Teams_messages.append(f"あなた: {f} を共有しました。論") if False else st.session_state.Teams_messages.append(f"あなた: {f} を共有しました。"); mark_task_done(SERVICE,"share")
elif active=="予定表":
    meeting=st.radio("会議の種類",["今すぐ会議","予定された会議","画面共有のみ"],horizontal=True)
    if st.button("会議を開始",use_container_width=True):
        st.session_state.Teams_meeting=meeting; mark_task_done(SERVICE,"meeting")
else:
    st.caption("このタブはTeamsの画面構成を確認するための表示です。")
st.markdown("</div>",unsafe_allow_html=True)
st.markdown("<div class='teams-shell'><div class='teams-left'><strong>チーム</strong><br>一般<br>M365移行<br>研修連絡</div><div class='teams-main'>",unsafe_allow_html=True)
for i,m in enumerate(st.session_state.Teams_messages):
    cls="chat-me" if m.startswith("あなた") else "chat-other"
    st.markdown(f"<div class='chat-bubble {cls}'>{html.escape(m)}</div>",unsafe_allow_html=True)
st.markdown(f"<div class='share-panel'>共有ファイル：{html.escape(st.session_state.Teams_shared)}<br>会議状態：{html.escape(st.session_state.Teams_meeting)}</div>",unsafe_allow_html=True)
st.markdown("</div></div>",unsafe_allow_html=True)
if st.button("Teamsの体験をリセット"):
    reset_service(SERVICE)
close_shell()
