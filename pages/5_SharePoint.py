import html
import streamlit as st
from modules.ui import load_css, titlebar, app_header, close_shell, service_launcher, training_strip, ribbon_tabs, mark_task_done, reset_service
SERVICE="SharePoint"
TASKS=[{"id":"site","label":"サイトを選び、表示対象のドキュメント ライブラリを切り替えてください。"},{"id":"permission","label":"権限レベルを選び、サイト権限に反映してください。"},{"id":"news","label":"ニュース投稿の種類を選び、サイトに追加してください。"}]
TABS=["ホーム","ドキュメント","ページ","ニュース","権限","サイトの設定"]
st.set_page_config(page_title="SharePoint 体験",page_icon="📁",layout="wide")
load_css(); titlebar(); service_launcher(SERVICE); training_strip(SERVICE,TASKS)
st.session_state.setdefault("SharePoint_site","経営企画サイト")
st.session_state.setdefault("SharePoint_permission","閲覧")
st.session_state.setdefault("SharePoint_news",[])
app_header("SharePoint","サイト、ドキュメント、ニュース、権限管理を選択肢付きで体験します。")
active=ribbon_tabs(SERVICE,TABS)
st.markdown("<div class='ribbon'>",unsafe_allow_html=True)
if active=="ホーム":
    site=st.selectbox("サイト",["経営企画サイト","情報システムサイト","M365移行プロジェクト"])
    if st.button("サイトを表示",use_container_width=True):
        st.session_state.SharePoint_site=site; mark_task_done(SERVICE,"site")
elif active=="権限":
    level=st.radio("権限",["閲覧","投稿","編集","所有者"],horizontal=True)
    if st.button("権限を適用",use_container_width=True):
        st.session_state.SharePoint_permission=level; mark_task_done(SERVICE,"permission")
elif active=="ニュース":
    news=st.selectbox("ニュース種別",["移行のお知らせ","研修開催案内","FAQ更新"])
    if st.button("ニュースを投稿",use_container_width=True):
        if news not in st.session_state.SharePoint_news: st.session_state.SharePoint_news.append(news)
        mark_task_done(SERVICE,"news")
else:
    st.caption("選択したサイトの内容を下に表示します。")
st.markdown("</div>",unsafe_allow_html=True)
st.markdown(f"<div class='site-card'><h3>{html.escape(st.session_state.SharePoint_site)}</h3><span class='badge'>権限：{html.escape(st.session_state.SharePoint_permission)}</span></div>",unsafe_allow_html=True)
st.markdown("#### ドキュメント ライブラリ")
rows="".join(f"<div class='file-row'><span>📄 {html.escape(f)}</span><span class='badge'>SharePoint</span><span>共有済み</span></div>" for f in ["議事録.docx","移行計画.xlsx","権限一覧.xlsx"])
st.markdown(f"<div class='file-list'>{rows}</div>",unsafe_allow_html=True)
if st.session_state.SharePoint_news:
    st.markdown("#### ニュース")
    for n in st.session_state.SharePoint_news:
        st.markdown(f"<div class='share-panel'>📰 {html.escape(n)}</div>",unsafe_allow_html=True)
if st.button("SharePointの体験をリセット"):
    reset_service(SERVICE)
close_shell()
