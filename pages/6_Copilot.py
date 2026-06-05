import streamlit as st
from modules.common import init_page, training_banner, complete_step, safe
init_page("Copilot 体験")
steps=["目的が伝わる依頼文を入力してください。","生成結果を確認してください。","次の操作提案を選んでください。"]
idx,done=training_banner('Copilot',steps)
st.session_state.setdefault('cp_prompt','Teams投稿用に、M365移行後の保存ルールを短く説明してください。')
st.session_state.setdefault('cp_result','')
st.session_state.setdefault('cp_next','未選択')
st.markdown("<div class='m365-shell'><div class='m365-titlebar'><span>Copilot</span><span>業務支援</span></div></div>", unsafe_allow_html=True)
prompt=st.text_area('依頼文',value=st.session_state.cp_prompt,height=120)
if st.button('生成',type='primary'):
    st.session_state.cp_prompt=prompt
    st.session_state.cp_result='M365移行後は、個人作業はOneDrive、部署共有はSharePoint、会議やチャットでの共有はTeamsを使い分けましょう。ファイルはクラウドに保存すると、共同編集や版管理がしやすくなります。'
    complete_step('Copilot',0); complete_step('Copilot',1); st.rerun()
if st.session_state.cp_result:
    st.markdown(f"<div class='word-page compact'><strong>Copilotの回答</strong><br><br>{safe(st.session_state.cp_result)}</div>",unsafe_allow_html=True)
    next_action=st.selectbox('次の操作',['Teams投稿に整える','箇条書きにする','管理者向け説明にする'])
    if st.button('次の操作を選択'):
        st.session_state.cp_next=next_action; complete_step('Copilot',2); st.rerun()
if st.button('トップへ戻る'): st.switch_page('app.py')
