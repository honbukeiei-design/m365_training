import html
import streamlit as st
from modules.ui import load_css, titlebar, app_header, close_shell, service_launcher, training_strip, ribbon_tabs, mark_task_done, reset_service
SERVICE="OneDrive"
TASKS=[{"id":"upload","label":"アップロードするファイル種類を選び、一覧に追加してください。"},{"id":"share","label":"共有方法を選び、共有リンク状態を反映してください。"},{"id":"sync","label":"同期対象を選び、同期状態を更新してください。"},{"id":"restore","label":"復元する版を選び、復元状態を表示してください。"}]
TABS=["ホーム","アップロード","共有","同期","履歴","ごみ箱"]
st.set_page_config(page_title="OneDrive 体験",page_icon="☁️",layout="wide")
load_css(); titlebar(); service_launcher(SERVICE); training_strip(SERVICE,TASKS)
st.session_state.setdefault("OneDrive_files", ["移行手順書.docx","研修日程.xlsx"])
st.session_state.setdefault("OneDrive_share", "未共有")
st.session_state.setdefault("OneDrive_sync", "未同期")
st.session_state.setdefault("OneDrive_restore", "未実行")
app_header("OneDrive","アップロード、共有、同期、復元を選択肢付きで体験します。")
active=ribbon_tabs(SERVICE,TABS)
st.markdown("<div class='ribbon'>",unsafe_allow_html=True)
if active=="アップロード":
    f=st.selectbox("アップロードするファイル",["会議資料.docx","予算表.xlsx","説明動画.mp4"])
    if st.button("アップロード",use_container_width=True):
        if f not in st.session_state.OneDrive_files: st.session_state.OneDrive_files.append(f)
        mark_task_done(SERVICE,"upload")
elif active=="共有":
    f=st.selectbox("共有対象",st.session_state.OneDrive_files)
    method=st.radio("共有方法",["指定したユーザー","組織内リンク","閲覧のみリンク"],horizontal=True)
    if st.button("共有リンクを作成",use_container_width=True):
        st.session_state.OneDrive_share=f"{f}：{method}"; mark_task_done(SERVICE,"share")
elif active=="同期":
    target=st.radio("同期対象",["デスクトップ","ドキュメント","写真"],horizontal=True)
    if st.button("同期を開始",use_container_width=True):
        st.session_state.OneDrive_sync=f"{target} を同期中"; mark_task_done(SERVICE,"sync")
elif active=="履歴":
    version=st.selectbox("復元する版",["1時間前","昨日 17:30","先週金曜日"])
    if st.button("この版を復元",use_container_width=True):
        st.session_state.OneDrive_restore=f"{version} の版を復元"; mark_task_done(SERVICE,"restore")
else:
    st.caption("ファイル一覧から状態を確認できます。")
st.markdown("</div>",unsafe_allow_html=True)
rows="".join(f"<div class='file-row'><span>📄 {html.escape(f)}</span><span class='badge'>クラウド</span><span>最終更新 今日</span></div>" for f in st.session_state.OneDrive_files)
st.markdown(f"<div class='file-list'>{rows}</div><div class='share-panel'>共有：{html.escape(st.session_state.OneDrive_share)}<br>同期：{html.escape(st.session_state.OneDrive_sync)}<br>復元：{html.escape(st.session_state.OneDrive_restore)}</div>",unsafe_allow_html=True)
if st.button("OneDriveの体験をリセット"):
    reset_service(SERVICE)
close_shell()
