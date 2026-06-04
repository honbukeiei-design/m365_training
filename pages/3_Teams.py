import streamlit as st
from modules.state import init_state, set_progress
from modules.tutorial import show_steps
from modules.ui import load_css, task_card

st.set_page_config(page_title="Teams Training", page_icon="💬", layout="wide")
load_css(); init_state()

st.title("💬 Teams：チャット・チャネル・会議")
st.caption("会話、チャネル投稿、ファイル共有、会議開始までを疑似体験します。")

st.markdown("""
<div class="teams-layout">
  <div class="teams-nav">
    <strong>チーム</strong>
    <div class="teams-channel active">移行プロジェクト</div>
    <div class="teams-channel">総務連絡</div>
    <div class="teams-channel">FAQ</div>
    <hr>
    <strong>チャネル</strong>
    <div class="teams-channel active">一般</div>
    <div class="teams-channel">研修資料</div>
    <div class="teams-channel">質問箱</div>
  </div>
  <div class="teams-chat">
    <strong># 一般</strong><br><span class="m365-muted">M365移行に関する連絡と質問</span>
  </div>
</div>
""", unsafe_allow_html=True)

left, right = st.columns([2, 1])
with left:
    st.markdown("### スレッド")
    for m in st.session_state.chat_messages:
        cls = "chat-bubble chat-right" if m["mine"] else "chat-bubble chat-left"
        st.markdown(f"<div class='{cls}'><strong>{m['name']}</strong><br>{m['text']}</div>", unsafe_allow_html=True)
    msg = st.text_input("メッセージを入力", placeholder="例：資料をSharePointに保存しました")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("送信", type="primary", disabled=not msg):
            st.session_state.chat_messages.append({"name": "あなた", "text": msg, "mine": True})
            set_progress("Teams", 50)
            st.rerun()
    with c2:
        st.button("📎 ファイル添付")
    with c3:
        if st.button("📅 会議を開始"):
            set_progress("Teams", 75)
            st.success("会議開始の操作を体験しました。")
with right:
    st.markdown("### 会議パネル")
    st.toggle("カメラ", value=False)
    st.toggle("マイク", value=True)
    st.selectbox("会議の目的", ["進捗確認", "研修説明", "質疑応答"])
    task_card("課題1", "チャネルにメッセージを投稿する", len(st.session_state.chat_messages) > 2)
    task_card("課題2", "会議開始ボタンを押す", st.session_state.progress.get("Teams", 0) >= 75)

show_steps("Teams", [
    "① 個別チャットとチャネル投稿の違いを確認します。チーム全体に残す内容はチャネルへ投稿します。",
    "② ファイルはTeamsに直接置くのではなく、裏側ではSharePointに保存されます。",
    "③ 会議前にマイク・カメラ・目的を確認してから開始します。",
])
