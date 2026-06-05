import streamlit as st
from modules.common import init_page, training_banner, complete_step, safe

init_page("Teams 体験")
steps = [
    "@メンションを付けて、相手に通知が届く形で送信してください。",
    "ファイル共有を選び、チャットに添付表示してください。",
    "メッセージにリアクションを付けてください。",
    "会議を開始してください。",
]
idx, done = training_banner("Teams", steps)
st.session_state.setdefault("teams_messages", ["佐藤：会議資料を確認お願いします。", "田中：SharePointに資料を置きました。"])
st.session_state.setdefault("teams_file", "未共有")
st.session_state.setdefault("teams_reaction", "")
st.session_state.setdefault("teams_meeting", "未開始")

st.markdown("<div class='teams-shell'><div class='teams-titlebar'><span>Teams</span><span>総務・経営企画 チャネル</span></div></div>", unsafe_allow_html=True)
cols = st.columns(4)
with cols[0]:
    mention = st.selectbox("宛先", ["@佐藤", "@田中", "@チーム"])
with cols[1]:
    text = st.text_input("メッセージ", value="資料を確認してください。")
with cols[2]:
    if st.button("送信", type="primary"):
        st.session_state.teams_messages.append(f"あなた：{mention} {text}")
        complete_step("Teams", 0)
        st.rerun()
with cols[3]:
    if st.button("会議開始"):
        st.session_state.teams_meeting = "会議中"
        complete_step("Teams", 3)
        st.rerun()

c1, c2 = st.columns(2)
with c1:
    file_name = st.selectbox("共有するファイル", ["保存ルール.docx", "研修集計.xlsx", "移行手順.pdf"])
    if st.button("ファイルを共有"):
        st.session_state.teams_file = file_name
        st.session_state.teams_messages.append(f"あなた：{file_name} を共有しました。")
        complete_step("Teams", 1)
        st.rerun()
with c2:
    reaction = st.radio("リアクション", ["いいね", "確認しました", "質問あり"], horizontal=True)
    if st.button("リアクションを付ける"):
        st.session_state.teams_reaction = reaction
        complete_step("Teams", 2)
        st.rerun()

st.markdown("<div class='teams-layout'><div class='teams-rail'><strong>チャット</strong><br><br>総務・経営企画<br>情報共有<br>研修チーム</div><div class='teams-chat'>", unsafe_allow_html=True)
for m in st.session_state.teams_messages:
    cls = "message me" if m.startswith("あなた") else "message"
    msg = safe(m).replace("@佐藤", "<span class='mention'>@佐藤</span>").replace("@田中", "<span class='mention'>@田中</span>").replace("@チーム", "<span class='mention'>@チーム</span>")
    st.markdown(f"<div class='{cls}'>{msg}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='statusbar'><span>共有ファイル：{safe(st.session_state.teams_file)}</span><span>リアクション：{safe(st.session_state.teams_reaction)} ・ 会議：{safe(st.session_state.teams_meeting)}</span></div>", unsafe_allow_html=True)
st.markdown("</div></div>", unsafe_allow_html=True)
if st.button("トップへ戻る"):
    st.switch_page("app.py")
