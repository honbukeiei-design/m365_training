import streamlit as st
from modules.common import init_page, training_banner, complete_step, safe
init_page("SharePoint 体験")
steps=["サイトを選択してください。","ドキュメントライブラリにファイルを追加してください。","権限を選んで反映してください。","ニュース投稿を作成してください。"]
idx,done=training_banner('SharePoint',steps)
st.session_state.setdefault('sp_site','総務サイト')
st.session_state.setdefault('sp_docs',['規程集.docx','移行計画.xlsx'])
st.session_state.setdefault('sp_perm','閲覧')
st.session_state.setdefault('sp_news','')
st.markdown("<div class='m365-shell'><div class='m365-titlebar'><span>SharePoint</span><span>チームサイト</span></div></div>", unsafe_allow_html=True)
c1,c2,c3,c4=st.columns(4)
with c1:
    site=st.selectbox('サイト',['総務サイト','経営企画サイト','情報システムサイト'])
    if st.button('サイトを開く'):
        st.session_state.sp_site=site; complete_step('SharePoint',0); st.rerun()
with c2:
    doc=st.text_input('追加ファイル','議事録.docx')
    if st.button('追加'):
        st.session_state.sp_docs.append(doc); complete_step('SharePoint',1); st.rerun()
with c3:
    perm=st.selectbox('権限',['閲覧','編集','所有者'])
    if st.button('権限を反映'):
        st.session_state.sp_perm=perm; complete_step('SharePoint',2); st.rerun()
with c4:
    news=st.text_input('ニュースタイトル','M365研修を開始します')
    if st.button('投稿'):
        st.session_state.sp_news=news; complete_step('SharePoint',3); st.rerun()
st.markdown('<div class="workspace">',unsafe_allow_html=True)
st.subheader(st.session_state.sp_site)
st.caption(f"権限：{st.session_state.sp_perm}")
for d in st.session_state.sp_docs:
    st.markdown(f"<div class='message'>{safe(d)}</div>",unsafe_allow_html=True)
if st.session_state.sp_news: st.info('ニュース：'+st.session_state.sp_news)
st.markdown('</div>',unsafe_allow_html=True)
if st.button('トップへ戻る'): st.switch_page('app.py')
