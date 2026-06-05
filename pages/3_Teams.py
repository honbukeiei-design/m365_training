import html
import streamlit as st
from modules.ui import load_css, top_bar, page_title, training_bar, complete_task, reset, tabs, ribbon_start, ribbon_end

SERVICE="Teams"
TASKS=[
 {"id":"mention","label":"チャットで @メンション を付けて送信してください。"},
 {"id":"file","label":"ファイルを添付し、チャットに共有してください。"},
 {"id":"reaction","label":"メッセージにリアクションを付けてください。"},
 {"id":"meeting","label":"会議タイトルを入力し、会議を開始してください。"},
]
TABS=["チャット","チーム","会議","ファイル","アクティビティ"]
st.set_page_config(page_title="Teams 体験", layout="wide")
load_css(); top_bar("Teams")
page_title("Teams", "@メンション、返信、ファイル共有、会議開始の基本操作を体験します。")
training_bar(SERVICE,TASKS)
for k,v in {"Teams_messages":[("佐藤","会議資料を確認してください。",False)],"Teams_file":"","Teams_meeting":"","Teams_reaction":""}.items(): st.session_state.setdefault(k,v)
active=tabs(SERVICE,TABS); ribbon_start()
if active=="チャット":
    mention=st.selectbox("メンション先",["@佐藤","@田中","@情報システム担当"])
    body=st.text_input("本文","確認しました。OneDriveに保存して共有します。")
    if st.button("メンション付きで送信",use_container_width=True):
        st.session_state.Teams_messages.append(("あなた",f"{mention} {body}",False)); complete_task(SERVICE,"mention")
    if st.button("リアクションを付ける",use_container_width=True):
        st.session_state.Teams_reaction="いいね"; complete_task(SERVICE,"reaction")
elif active=="ファイル":
    fname=st.selectbox("共有するファイル",["M365移行手順.docx","研修参加者.xlsx","保存ルール.pdf"])
    if st.button("チャットに共有",use_container_width=True):
        st.session_state.Teams_file=fname; st.session_state.Teams_messages.append(("あなた",f"ファイルを共有しました：{fname}",True)); complete_task(SERVICE,"file")
elif active=="会議":
    title=st.text_input("会議タイトル","M365移行説明会")
    if st.button("今すぐ会議を開始",use_container_width=True):
        st.session_state.Teams_meeting=title; complete_task(SERVICE,"meeting")
elif active=="チーム": st.info("チームではチャネル単位で会話とファイルを管理します。")
elif active=="アクティビティ": st.info("メンションや返信の通知をここで確認します。")
ribbon_end()

msgs=""
for sender,msg,isfile in st.session_state.Teams_messages:
    cls="msg me" if sender=="あなた" else "msg"
    msg=html.escape(msg).replace("@佐藤","<span class='mention'>@佐藤</span>").replace("@田中","<span class='mention'>@田中</span>").replace("@情報システム担当","<span class='mention'>@情報システム担当</span>")
    msgs+=f"<div class='{cls}'><strong>{sender}</strong><br>{msg}</div>"
if st.session_state.Teams_reaction:
    msgs += f"<div class='small'>リアクション：{html.escape(st.session_state.Teams_reaction)}</div>"
meeting = f"<div class='file-card'>進行中の会議：{html.escape(st.session_state.Teams_meeting)}</div>" if st.session_state.Teams_meeting else ""
st.markdown(f"""
<div class='teams-shell'>
 <div class='teams-sidebar'><strong>Microsoft Teams</strong><p class='muted'>チャット</p><p>移行プロジェクト</p><p>情報共有</p></div>
 <div class='teams-main'><div class='teams-head'>移行プロジェクト</div><div class='chat-list'>{msgs}{meeting}</div></div>
</div>
""",unsafe_allow_html=True)
if st.button("Teamsの体験をリセット"): reset(SERVICE)
