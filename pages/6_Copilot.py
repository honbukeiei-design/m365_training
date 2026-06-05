import streamlit as st
from modules.ui import load_css, page_header, note
from modules.urls import M365_URLS
from modules.copilot import ask_copilot
st.set_page_config(page_title="Copilot Training", page_icon="🤖", layout="wide")
load_css(); page_header("Copilot：依頼文と業務支援", "画面上部の体験順に沿って、依頼文作成、要約、文章案作成、次の操作確認を体験します。")
steps=["依頼文を入力してください。","生成結果を確認してください。","結果を研修用メモに追加してください。","実体験URLからCopilotを開いてください。"]
if 'copilot_step' not in st.session_state: st.session_state.copilot_step=0
if 'copilot_notes' not in st.session_state: st.session_state.copilot_notes=[]
st.markdown(f"<div class='clean-note'><b>体験 {min(st.session_state.copilot_step+1,4)}/4：</b>{steps[min(st.session_state.copilot_step,3)]}</div>", unsafe_allow_html=True)
prompt=st.text_area("Copilotに依頼する内容", value="M365移行後のファイル保存ルールを、職員向けに3点で要約してください。", height=120)
col1,col2=st.columns([1,3])
with col1:
    run=st.button("生成する", use_container_width=True)
with col2:
    st.write("例：会議メモを要約、共有メールを作成、Excel表の分析観点を出す、など")
if run:
    st.session_state.copilot_result=ask_copilot(prompt)
    st.session_state.copilot_step=max(st.session_state.copilot_step,1)
if 'copilot_result' in st.session_state:
    st.subheader("Copilot提案")
    st.markdown(f"<div class='training-card'><pre style='white-space:pre-wrap;font-family:inherit'>{st.session_state.copilot_result}</pre></div>", unsafe_allow_html=True)
    if st.button("研修用メモに追加", use_container_width=True):
        st.session_state.copilot_notes.append(st.session_state.copilot_result)
        st.session_state.copilot_step=3
if st.session_state.copilot_notes:
    st.subheader("研修用メモ")
    for i,n in enumerate(st.session_state.copilot_notes,1): st.write(f"{i}. {n[:160]}...")
    note(f"体験完了です。次は実際のCopilotで同じ依頼文を試してください。<br><a href='{M365_URLS['Copilot']}' target='_blank'>実体験をしてください：Copilotを開く ↗</a><br>{M365_URLS['Copilot']}")
