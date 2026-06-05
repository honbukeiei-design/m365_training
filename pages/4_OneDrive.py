import streamlit as st
from modules.common import init_page, training_banner, complete_step, safe
init_page("OneDrive 体験")
steps=["ファイルをアップロードしてください。","共有リンクの権限を選んで作成してください。","同期状態を確認してください。","版の履歴から復元してください。"]
idx,done=training_banner("OneDrive",steps)
st.session_state.setdefault('od_files',['保存ルール.docx','研修集計.xlsx'])
st.session_state.setdefault('od_share','未作成')
st.session_state.setdefault('od_sync','同期済み')
st.markdown("<div class='m365-shell'><div class='m365-titlebar'><span>OneDrive</span><span>自分のファイル</span></div></div>", unsafe_allow_html=True)
c1,c2,c3,c4=st.columns(4)
with c1:
    name=st.text_input('ファイル名','移行チェックリスト.docx')
    if st.button('アップロード',type='primary'):
        st.session_state.od_files.append(name); complete_step('OneDrive',0); st.rerun()
with c2:
    perm=st.selectbox('リンク権限',['指定したユーザー','組織内のユーザー','表示のみ'])
    if st.button('リンク作成'):
        st.session_state.od_share=perm; complete_step('OneDrive',1); st.rerun()
with c3:
    if st.button('同期を確認'):
        st.session_state.od_sync='最新の状態'; complete_step('OneDrive',2); st.rerun()
with c4:
    if st.button('前の版を復元'):
        complete_step('OneDrive',3); st.success('保存ルール.docx を前の版に復元しました。')
st.markdown('<div class="workspace">',unsafe_allow_html=True)
for f in st.session_state.od_files:
    st.markdown(f"<div class='service-card'><h3>{safe(f)}</h3><p>共有：{safe(st.session_state.od_share)} / 同期：{safe(st.session_state.od_sync)}</p></div>",unsafe_allow_html=True)
st.markdown('</div>',unsafe_allow_html=True)
if st.button('トップへ戻る'): st.switch_page('app.py')
