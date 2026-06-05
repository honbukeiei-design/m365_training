import streamlit as st
from modules.ui import load_css, top_bar, page_title, training_bar, complete_task, reset, tabs, ribbon_start, ribbon_end
SERVICE="SharePoint"
TASKS=[{"id":"site","label":"サイトを選択してください。"},{"id":"doc","label":"ドキュメントライブラリにファイルを追加してください。"},{"id":"permission","label":"権限を設定してください。"},{"id":"news","label":"ニュースを投稿してください。"}]
TABS=["サイト","ドキュメント","権限","ニュース"]
st.set_page_config(page_title="SharePoint 体験",layout="wide"); load_css(); top_bar("SharePoint"); page_title("SharePoint","チームサイト、文書管理、権限、ニュース投稿を体験します。"); training_bar(SERVICE,TASKS)
for k,v in {"SharePoint_site":"未選択","SharePoint_docs":["運用ルール.docx"],"SharePoint_perm":"閲覧のみ","SharePoint_news":""}.items(): st.session_state.setdefault(k,v)
active=tabs(SERVICE,TABS); ribbon_start()
if active=="サイト":
    site=st.selectbox("サイト",["経営企画","情報システム","総務"])
    if st.button("サイトを開く",use_container_width=True): st.session_state.SharePoint_site=site; complete_task(SERVICE,"site")
elif active=="ドキュメント":
    doc=st.text_input("追加ファイル","会議資料.docx")
    if st.button("ライブラリに追加",use_container_width=True): st.session_state.SharePoint_docs.append(doc); complete_task(SERVICE,"doc")
elif active=="権限":
    perm=st.radio("権限",["閲覧のみ","編集可","所有者"],horizontal=True)
    if st.button("権限を適用",use_container_width=True): st.session_state.SharePoint_perm=perm; complete_task(SERVICE,"permission")
elif active=="ニュース":
    news=st.text_input("ニュースタイトル","M365移行研修を開始します")
    if st.button("投稿",use_container_width=True): st.session_state.SharePoint_news=news; complete_task(SERVICE,"news")
ribbon_end()
docs="".join(f"<div class='file-card'>{d}</div>" for d in st.session_state.SharePoint_docs)
st.markdown(f"<div class='office-shell'><div class='office-titlebar'>SharePoint - {st.session_state.SharePoint_site}</div><div class='office-canvas'><div class='site-card'>権限：{st.session_state.SharePoint_perm}</div>{docs}<div class='site-card'>ニュース：{st.session_state.SharePoint_news or '未投稿'}</div></div></div>",unsafe_allow_html=True)
if st.button("SharePointの体験をリセット"): reset(SERVICE)
