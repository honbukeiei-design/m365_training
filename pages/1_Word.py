from __future__ import annotations
import html
import streamlit as st
from modules.ui import load_css, top_bar, page_title, training_bar, complete_task, reset, tabs, ribbon_start, ribbon_end

SERVICE = "Word"
TASKS = [
    {"id":"format","label":"ホームで書式を選択し、文書に反映してください。"},
    {"id":"insert_table","label":"挿入で表の行列を選び、文書に挿入してください。"},
    {"id":"layout","label":"レイアウトで余白を選び、ページに反映してください。"},
    {"id":"design","label":"デザインで背景または罫線を選び、ページに反映してください。"},
    {"id":"review","label":"校閲でコメントを入力し、文書に表示してください。"},
    {"id":"view","label":"表示でズーム倍率を選び、表示に反映してください。"},
    {"id":"merge","label":"差し込み文書で宛先を選び、差し込み表示してください。"},
]
TABS = ["ホーム","挿入","レイアウト","デザイン","校閲","表示","差し込み文書"]

st.set_page_config(page_title="Word 体験", layout="wide")
load_css(); top_bar("Word")
page_title("Word", "白紙ページに文書を作成し、リボン操作で書式・表・コメントを反映します。")
training_bar(SERVICE, TASKS)

defaults = {
    "Word_text": "M365移行後のファイル保存ルール\n\n旧Officeでは個人PCや共有フォルダーに保存していました。\nMicrosoft 365移行後は、OneDriveとSharePointを使い分け、Teamsから関係者へ共有します。",
    "Word_format": "標準", "Word_table_rows": 0, "Word_table_cols": 0, "Word_margin": "標準", "Word_design": "白紙",
    "Word_comment": "", "Word_zoom": "100%", "Word_recipient": "", "Word_saved": False
}
for k, v in defaults.items(): st.session_state.setdefault(k, v)

active = tabs(SERVICE, TABS)
ribbon_start()
if active == "ホーム":
    c1, c2 = st.columns([2,1])
    with c1:
        choice = st.radio("書式", ["標準", "太字", "下線", "見出し", "箇条書き"], horizontal=True)
    with c2:
        if st.button("書式を適用", use_container_width=True):
            st.session_state.Word_format = choice
            st.session_state.Word_saved = False
            complete_task(SERVICE, "format")
elif active == "挿入":
    c1, c2, c3 = st.columns([1,1,1])
    rows = c1.selectbox("行", [2,3,4,5])
    cols = c2.selectbox("列", [2,3,4])
    if c3.button("表を挿入", use_container_width=True):
        st.session_state.Word_table_rows = rows
        st.session_state.Word_table_cols = cols
        st.session_state.Word_saved = False
        complete_task(SERVICE, "insert_table")
elif active == "レイアウト":
    choice = st.radio("余白", ["標準", "狭い", "広い"], horizontal=True)
    if st.button("余白を適用", use_container_width=True):
        st.session_state.Word_margin = choice
        st.session_state.Word_saved = False
        complete_task(SERVICE, "layout")
elif active == "デザイン":
    choice = st.radio("ページデザイン", ["白紙", "淡い背景", "グリッド", "青い罫線"], horizontal=True)
    if st.button("デザインを適用", use_container_width=True):
        st.session_state.Word_design = choice
        st.session_state.Word_saved = False
        complete_task(SERVICE, "design")
elif active == "校閲":
    comment = st.text_input("コメント", "保存先は用途に応じてOneDriveとSharePointを使い分けましょう。")
    if st.button("コメントを追加", use_container_width=True):
        st.session_state.Word_comment = comment
        st.session_state.Word_saved = False
        complete_task(SERVICE, "review")
elif active == "表示":
    zoom = st.radio("ズーム", ["80%", "100%", "120%"], horizontal=True)
    if st.button("ズームを適用", use_container_width=True):
        st.session_state.Word_zoom = zoom
        complete_task(SERVICE, "view")
elif active == "差し込み文書":
    rec = st.selectbox("宛先", ["総務部", "経営企画課", "情報システム担当", "全職員"])
    if st.button("差し込み結果を表示", use_container_width=True):
        st.session_state.Word_recipient = rec
        st.session_state.Word_saved = False
        complete_task(SERVICE, "merge")
ribbon_end()

c1, c2, c3 = st.columns([1,1,4])
if c1.button("保存", use_container_width=True):
    st.session_state.Word_saved = True
if c2.button("リセット", use_container_width=True):
    reset(SERVICE)
c3.caption("保存状態：" + ("保存済み" if st.session_state.Word_saved else "未保存の変更"))

# Input styled as a page; rendered document below uses the same page surface to avoid raw HTML/code display.
text = st.text_area("白紙ページ", key="Word_text", height=170, label_visibility="collapsed")
raw = html.escape(text)
if st.session_state.Word_format == "箇条書き":
    raw = "\n".join([("• " + html.escape(line)) if line.strip() else "" for line in text.splitlines()])
fmt = {"太字":"bold", "下線":"underline", "見出し":"heading"}.get(st.session_state.Word_format, "")
margin = {"狭い":"narrow", "広い":"wide"}.get(st.session_state.Word_margin, "")
design = {"淡い背景":"blue", "グリッド":"grid", "青い罫線":"border-blue"}.get(st.session_state.Word_design, "")
zoom = {"80%":"0.8", "100%":"1", "120%":"1.2"}[st.session_state.Word_zoom]
table_html = ""
if st.session_state.Word_table_rows and st.session_state.Word_table_cols:
    r, c = st.session_state.Word_table_rows, st.session_state.Word_table_cols
    table_html = "<table class='insert-table'>" + "".join("<tr>" + "".join(f"<td>項目 {i+1}-{j+1}</td>" for j in range(c)) + "</tr>" for i in range(r)) + "</table>"
comment = f"<div class='comment'>コメント：{html.escape(st.session_state.Word_comment)}</div>" if st.session_state.Word_comment else ""
merge = f"<p><span class='badge'>{html.escape(st.session_state.Word_recipient)} 各位</span></p>" if st.session_state.Word_recipient else ""
st.markdown(f"""
<div class='office-shell'>
  <div class='office-titlebar'><span>Word</span><span class='file'>保存ルール.docx</span></div>
  <div class='office-ribbon-strip'>ファイル　ホーム　挿入　レイアウト　デザイン　校閲　表示　差し込み文書</div>
  <div class='office-canvas'>
    <div style='transform:scale({zoom});transform-origin:top center;margin-bottom:70px;'>
      <div class='word-paper {fmt} {margin} {design}'>{merge}<div>{raw}</div>{table_html}{comment}</div>
    </div>
  </div>
  <div class='statusbar'><span>ページ 1/1</span><span>表示 {html.escape(st.session_state.Word_zoom)} ・ {html.escape(st.session_state.Word_margin)}余白 ・ {html.escape(st.session_state.Word_format)}</span></div>
</div>
""", unsafe_allow_html=True)
