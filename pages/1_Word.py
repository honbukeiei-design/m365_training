from __future__ import annotations
import html
import streamlit as st
from modules.ui import load_css, titlebar, app_header, close_shell, service_launcher, training_strip, ribbon_tabs, status_badge, mark_task_done, reset_service

SERVICE = "Word"
TASKS = [
    {"id": "home_format", "label": "ホームで文字書式を選び、文書に反映してください。"},
    {"id": "insert_table", "label": "挿入で表のサイズを選び、白紙ページに表を挿入してください。"},
    {"id": "layout_margin", "label": "レイアウトで余白を選び、ページの見た目に反映してください。"},
    {"id": "design_theme", "label": "デザインで背景または罫線を選び、ページに反映してください。"},
    {"id": "review_comment", "label": "校閲でコメントを追加し、文書内に表示してください。"},
    {"id": "view_zoom", "label": "表示でズーム倍率を選び、ページ表示に反映してください。"},
    {"id": "mail_merge", "label": "差し込み文書で宛先を選び、差し込み結果を表示してください。"},
    {"id": "share", "label": "共有で共有範囲を選び、共有状態を反映してください。"},
]
TABS = ["ホーム", "挿入", "レイアウト", "デザイン", "校閲", "表示", "差し込み文書"]

st.set_page_config(page_title="Word 体験", page_icon="📄", layout="wide")
load_css(); titlebar(); service_launcher(SERVICE); training_strip(SERVICE, TASKS)

for k, v in {
    "Word_body": "M365移行後のファイル保存ルール\n\n旧Officeでは個人PCや共有フォルダーに保存していました。\nMicrosoft 365移行後は、OneDriveとSharePointを使い分け、Teamsから関係者へ共有します。",
    "Word_format": "標準",
    "Word_bullets": False,
    "Word_table": None,
    "Word_margin": "標準",
    "Word_theme": "白紙",
    "Word_comment": "",
    "Word_zoom": "100%",
    "Word_recipient": "",
    "Word_share": "未共有",
    "Word_saved": False,
}.items():
    st.session_state.setdefault(k, v)

app_header("Word", "リボンを切り替え、選択肢を選び、白紙ページに反映します。")
active = ribbon_tabs(SERVICE, TABS)
st.markdown("<div class='ribbon'>", unsafe_allow_html=True)

if active == "ホーム":
    st.markdown("#### 文字書式")
    c1, c2, c3, c4 = st.columns([1,1,1,1])
    with c1:
        if st.button("太字", use_container_width=True):
            st.session_state.Word_format = "太字"; st.session_state.Word_saved = False; mark_task_done(SERVICE, "home_format")
    with c2:
        if st.button("下線", use_container_width=True):
            st.session_state.Word_format = "下線"; st.session_state.Word_saved = False; mark_task_done(SERVICE, "home_format")
    with c3:
        if st.button("見出しスタイル", use_container_width=True):
            st.session_state.Word_format = "見出し"; st.session_state.Word_saved = False; mark_task_done(SERVICE, "home_format")
    with c4:
        if st.button("箇条書き", use_container_width=True):
            st.session_state.Word_bullets = not st.session_state.Word_bullets; st.session_state.Word_saved = False; mark_task_done(SERVICE, "home_format")
    st.caption("ボタンを押すと、文書全体に書式が反映されます。")
elif active == "挿入":
    st.markdown("#### 挿入")
    size = st.selectbox("表のサイズ", ["2列×2行", "3列×3行", "4列×3行"], key="Word_table_choice")
    if st.button("表を挿入", use_container_width=True):
        st.session_state.Word_table = size; st.session_state.Word_saved = False; mark_task_done(SERVICE, "insert_table")
    if st.button("リンクを挿入", use_container_width=True):
        st.session_state.Word_body += "\n\n参考リンク：https://www.microsoft.com/ja-jp/microsoft-365"
        st.session_state.Word_saved = False
elif active == "レイアウト":
    st.markdown("#### ページ設定")
    margin = st.radio("余白", ["標準", "狭い", "広い"], horizontal=True, key="Word_margin_choice")
    if st.button("余白を適用", use_container_width=True):
        st.session_state.Word_margin = margin; st.session_state.Word_saved = False; mark_task_done(SERVICE, "layout_margin")
elif active == "デザイン":
    st.markdown("#### ページの背景と罫線")
    theme = st.radio("デザイン", ["白紙", "薄い青の背景", "グリッド背景", "青いページ罫線"], horizontal=True, key="Word_theme_choice")
    if st.button("デザインを適用", use_container_width=True):
        st.session_state.Word_theme = theme; st.session_state.Word_saved = False; mark_task_done(SERVICE, "design_theme")
elif active == "校閲":
    st.markdown("#### コメント")
    comment = st.text_input("コメント内容", value="保存場所はOneDriveかSharePointに統一しましょう。", key="Word_comment_input")
    if st.button("コメントを追加", use_container_width=True):
        st.session_state.Word_comment = comment; st.session_state.Word_saved = False; mark_task_done(SERVICE, "review_comment")
elif active == "表示":
    st.markdown("#### 表示倍率")
    zoom = st.radio("ズーム", ["75%", "100%", "125%"], horizontal=True, key="Word_zoom_choice")
    if st.button("ズームを適用", use_container_width=True):
        st.session_state.Word_zoom = zoom; mark_task_done(SERVICE, "view_zoom")
elif active == "差し込み文書":
    st.markdown("#### 宛先の選択")
    recipient = st.selectbox("宛先リスト", ["総務部", "経営企画課", "情報システム担当", "全職員"], key="Word_recipient_choice")
    if st.button("差し込み結果を表示", use_container_width=True):
        st.session_state.Word_recipient = recipient; st.session_state.Word_saved = False; mark_task_done(SERVICE, "mail_merge")

st.markdown("</div>", unsafe_allow_html=True)

s1, s2, s3, s4 = st.columns([1,1,1,3])
with s1:
    if st.button("💾 保存", use_container_width=True):
        st.session_state.Word_saved = True
with s2:
    share_choice = st.selectbox("共有範囲", ["未共有", "自分のみ", "指定したユーザー", "組織内リンク"], label_visibility="collapsed")
with s3:
    if st.button("共有", use_container_width=True):
        st.session_state.Word_share = share_choice; st.session_state.Word_saved = False; mark_task_done(SERVICE, "share")
with s4:
    status_badge(st.session_state.Word_saved)

body = st.text_area("白紙ページ内の本文", key="Word_body", height=140, label_visibility="collapsed")
text = html.escape(body)
if st.session_state.Word_bullets:
    lines = [f"• {html.escape(line)}" if line.strip() else "" for line in body.splitlines()]
    text = "\n".join(lines)
fmt_class = {"太字":"bold", "下線":"underline", "見出し":"title"}.get(st.session_state.Word_format, "")
margin_class = {"狭い":"wide", "広い":"narrow"}.get(st.session_state.Word_margin, "")
theme_class = {"薄い青の背景":"blue", "グリッド背景":"grid", "青いページ罫線":"bordered"}.get(st.session_state.Word_theme, "")
zoom_scale = {"75%":"0.75", "100%":"1", "125%":"1.15"}[st.session_state.Word_zoom]

inserted_table = ""
if st.session_state.Word_table:
    cols, rows = {"2列×2行":(2,2), "3列×3行":(3,3), "4列×3行":(4,3)}[st.session_state.Word_table]
    inserted_table = "<table class='inserted-table'>" + "".join("<tr>" + "".join(f"<td>セル {r+1}-{c+1}</td>" for c in range(cols)) + "</tr>" for r in range(rows)) + "</table>"
comment_html = f"<div class='comment-box'>コメント：{html.escape(st.session_state.Word_comment)}</div>" if st.session_state.Word_comment else ""
merge_html = f"<p><strong>差し込み表示：</strong>{html.escape(st.session_state.Word_recipient)} 各位</p>" if st.session_state.Word_recipient else ""
share_html = f"<p><span class='badge'>共有状態：{html.escape(st.session_state.Word_share)}</span></p>"

st.markdown(
    f"""
    <div class='page-stage'>
      <div style='transform:scale({zoom_scale});transform-origin:top center;margin-bottom:{'90px' if st.session_state.Word_zoom == '125%' else '0'}'>
        <div class='word-page {margin_class} {theme_class}'>
          <div class='word-document {fmt_class}'>{text}</div>
          {inserted_table}
          {merge_html}
          {comment_html}
          {share_html}
        </div>
      </div>
    </div>
    <div class='footer-status'><span>ページ 1/1</span><span>表示 {html.escape(st.session_state.Word_zoom)} ・ {html.escape(st.session_state.Word_margin)}余白 ・ {html.escape(st.session_state.Word_format)}</span></div>
    """,
    unsafe_allow_html=True,
)

if st.button("Wordの体験をリセット"):
    reset_service(SERVICE)
close_shell()
