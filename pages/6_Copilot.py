import html
import streamlit as st
from modules.ui import load_css, titlebar, app_header, close_shell, service_launcher, training_strip, ribbon_tabs, mark_task_done, reset_service
SERVICE="Copilot"
TASKS=[{"id":"summarize","label":"依頼内容を選び、Copilot風の回答を生成してください。"},{"id":"rewrite","label":"文章作成のトーンを選び、文案を生成してください。"},{"id":"next_action","label":"次の操作提案を選び、業務アクションを表示してください。"}]
TABS=["チャット","要約","文章作成","次の操作","履歴"]
st.set_page_config(page_title="Copilot 体験",page_icon="🤖",layout="wide")
load_css(); titlebar(); service_launcher(SERVICE); training_strip(SERVICE,TASKS)
st.session_state.setdefault("Copilot_output","まだ実行されていません。")
app_header("Copilot","依頼、要約、文章作成、次の操作提案を選択肢付きで体験します。")
active=ribbon_tabs(SERVICE,TABS)
st.markdown("<div class='ribbon'>",unsafe_allow_html=True)
if active in ["チャット","要約"]:
    request=st.selectbox("依頼内容",["会議メモを3点に要約","移行案内メールの要点整理","FAQを箇条書き化"])
    if st.button("回答を生成",use_container_width=True):
        st.session_state.Copilot_output=f"{request}\n\n1. 目的を短く整理しました。\n2. 関係者が次に取る行動を明確にしました。\n3. 共有前に確認すべき注意点を追加しました。"
        mark_task_done(SERVICE,"summarize")
elif active=="文章作成":
    tone=st.radio("トーン",["丁寧","簡潔","職員向けにやさしく"],horizontal=True)
    if st.button("文案を作成",use_container_width=True):
        st.session_state.Copilot_output=f"【{tone}】Microsoft 365への移行に伴い、ファイル保存と共有方法が変わります。研修画面で基本操作を確認し、実サービスで一度試してください。"
        mark_task_done(SERVICE,"rewrite")
elif active=="次の操作":
    action=st.selectbox("提案してほしい操作",["Wordで案内文を作る","Excelで集計する","Teamsで共有する"])
    if st.button("次の操作を提案",use_container_width=True):
        st.session_state.Copilot_output=f"次の操作：{action}\n\nおすすめ手順：\n1. 目的を1文で入力\n2. 必要な条件を追加\n3. 生成結果を確認して修正\n4. TeamsまたはOneDriveで共有"
        mark_task_done(SERVICE,"next_action")
else:
    st.caption("生成された結果は下部のカードに残ります。")
st.markdown("</div>",unsafe_allow_html=True)
st.markdown(f"<div class='copilot-card'><h3>Copilotの提案</h3><pre style='white-space:pre-wrap;font-family:inherit'>{html.escape(st.session_state.Copilot_output)}</pre></div>",unsafe_allow_html=True)
if st.button("Copilotの体験をリセット"):
    reset_service(SERVICE)
close_shell()
