import streamlit as st
from modules.ui import load_css, top_bar, page_title, training_bar, complete_task, reset, tabs, ribbon_start, ribbon_end
SERVICE="OneDrive"
TASKS=[{"id":"upload","label":"ファイルをアップロードしてください。"},{"id":"share","label":"共有リンクを作成してください。"},{"id":"sync","label":"同期状態を確認してください。"},{"id":"restore","label":"バージョン履歴から復元してください。"}]
TABS=["ホーム","自分のファイル","共有","同期","履歴"]
st.set_page_config(page_title="OneDrive 体験",layout="wide"); load_css(); top_bar("OneDrive"); page_title("OneDrive","個人ファイルの保存、共有、同期、復元を体験します。"); training_bar(SERVICE,TASKS)
for k,v in {"OneDrive_files":["保存ルール.docx","研修集計.xlsx"],"OneDrive_share":"未作成","OneDrive_sync":"未同期","OneDrive_restore":""}.items(): st.session_state.setdefault(k,v)
active=tabs(SERVICE,TABS); ribbon_start()
if active=="ホーム":
    name=st.text_input("ファイル名","説明資料.pptx")
    if st.button("アップロード",use_container_width=True): st.session_state.OneDrive_files.append(name); complete_task(SERVICE,"upload")
elif active=="共有":
    scope=st.radio("リンク範囲",["指定したユーザー","組織内のユーザー","リンクを知っている全員"],horizontal=True)
    if st.button("共有リンクを作成",use_container_width=True): st.session_state.OneDrive_share=scope; complete_task(SERVICE,"share")
elif active=="同期":
    if st.button("同期を開始",use_container_width=True): st.session_state.OneDrive_sync="最新"; complete_task(SERVICE,"sync")
elif active=="履歴":
    ver=st.selectbox("復元するバージョン",["1時間前","昨日 17:30","先週 月曜"])
    if st.button("復元",use_container_width=True): st.session_state.OneDrive_restore=ver; complete_task(SERVICE,"restore")
ribbon_end()
items="".join(f"<div class='file-card'><strong>{f}</strong><div class='small'>共有：{st.session_state.OneDrive_share} ／ 同期：{st.session_state.OneDrive_sync}</div></div>" for f in st.session_state.OneDrive_files)
st.markdown(f"<div class='office-shell'><div class='office-titlebar'>OneDrive</div><div class='office-canvas'>{items}<div class='small'>復元：{st.session_state.OneDrive_restore or '未実行'}</div></div></div>",unsafe_allow_html=True)
if st.button("OneDriveの体験をリセット"): reset(SERVICE)
