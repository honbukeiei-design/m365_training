import streamlit as st
from modules.ui import load_css, top_bar, page_title, training_bar, complete_task, reset, tabs, ribbon_start, ribbon_end
SERVICE="Copilot"
TASKS=[{"id":"prompt","label":"依頼文を入力し、提案を生成してください。"},{"id":"summary","label":"要約を生成してください。"},{"id":"next","label":"次の操作提案を確認してください。"}]
TABS=["チャット","要約","作成","次の操作"]
st.set_page_config(page_title="Copilot 体験",layout="wide"); load_css(); top_bar("Copilot"); page_title("Copilot","依頼文、要約、文章作成、次の操作提案を体験します。あくまで研修用の模擬応答です。"); training_bar(SERVICE,TASKS)
st.session_state.setdefault("Copilot_result","")
active=tabs(SERVICE,TABS); ribbon_start()
if active=="チャット":
    prompt=st.text_area("依頼文","M365移行後のファイル保存ルールを短く説明してください。")
    if st.button("生成",use_container_width=True): st.session_state.Copilot_result="OneDriveは個人作業、SharePointはチーム共有、Teamsは会話と会議の入口として使い分けます。"; complete_task(SERVICE,"prompt")
elif active=="要約":
    if st.button("要約を生成",use_container_width=True): st.session_state.Copilot_result="要約：保存場所を統一し、共有はリンクで管理し、Teamsから関係者へ案内します。"; complete_task(SERVICE,"summary")
elif active=="作成":
    if st.button("案内文を作成",use_container_width=True): st.session_state.Copilot_result="案内文：本日よりM365の保存・共有ルールに基づき、ファイルはOneDriveまたはSharePointに保存してください。"
elif active=="次の操作":
    if st.button("次の操作を提案",use_container_width=True): st.session_state.Copilot_result="次の操作：1. 文書をOneDriveに保存 2. 共有範囲を指定 3. Teamsで関係者に通知"; complete_task(SERVICE,"next")
ribbon_end()
st.markdown(f"<div class='office-shell'><div class='office-titlebar'>Copilot</div><div class='office-canvas'><div class='file-card'>{st.session_state.Copilot_result or 'ここに結果が表示されます。'}</div></div></div>",unsafe_allow_html=True)
if st.button("Copilotの体験をリセット"): reset(SERVICE)
