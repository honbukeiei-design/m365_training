import html
from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Microsoft 365 体験トレーニング", layout="wide", initial_sidebar_state="collapsed")

SERVICES = ["Word", "Excel", "Teams", "OneDrive", "SharePoint", "Copilot"]
SERVICE_URLS = {
    "Word": "https://word.cloud.microsoft/",
    "Excel": "https://excel.cloud.microsoft/",
    "Teams": "https://teams.microsoft.com/",
    "OneDrive": "https://onedrive.live.com/",
    "SharePoint": "https://www.microsoft.com/microsoft-365/sharepoint/collaboration",
    "Copilot": "https://copilot.microsoft.com/",
}

CSS = """
<style>
[data-testid="stSidebar"] {display:none;}
[data-testid="collapsedControl"] {display:none;}
.block-container {padding: 0.6rem 1.0rem 1.2rem; max-width: 1520px;}
#MainMenu, footer, header {visibility:hidden;}
html, body, [class*="css"] {font-family: "Segoe UI", "Yu Gothic", sans-serif;}
.stButton > button {border-radius: 6px; border: 1px solid #c7d3e5; background: #fff; color:#17233c; min-height: 38px;}
.stButton > button:hover {border-color:#2564cf; color:#0f4fbf; background:#f7fbff;}
.stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {border-color:#c7d3e5;}
.app-shell {background:#f3f6fb; border:1px solid #d7e0ee; border-radius:12px; overflow:hidden; box-shadow:0 8px 26px rgba(0,0,0,.06);}
.app-top {height:52px; background:#0f6cbd; color:#fff; display:flex; align-items:center; gap:18px; padding:0 22px; font-weight:700; font-size:22px;}
.app-top.green {background:#03787c;}
.app-top.purple {background:#6264a7;}
.app-top.gray {background:#2564cf;}
.ribbon-tabs {background:#ffffff; border-bottom:1px solid #d4dcea; padding: 8px 16px; display:flex; gap:18px; font-size:15px;}
.ribbon {background:#fbfcff; border-bottom:1px solid #d4dcea; padding:12px 18px; display:flex; gap:10px; flex-wrap:wrap; align-items:center;}
.ribbon-note {border-left:1px solid #d4dcea; margin-left:8px; padding-left:14px; color:#5b6679; font-size:13px;}
.training-bar {margin:14px 22px; background:#eff6ff; border:1px solid #a8c7ff; border-radius:10px; padding:12px 18px; display:flex; justify-content:space-between; align-items:center;}
.training-main {background:#e9eff8; padding:20px 28px 24px; min-height:560px;}
.office-card {background:#fff; border:1px solid #d9e1ee; border-radius:12px; padding:20px; box-shadow:0 10px 24px rgba(0,0,0,.05);}
.doc-page {background:#fff; width:78%; min-height:590px; margin:10px auto; padding:78px 90px; box-shadow:0 3px 18px rgba(0,0,0,.10); border:1px solid #d0d7e2; line-height:1.9; font-size:18px;}
.doc-page.compact {width:86%; min-height:420px; padding:44px 54px;}
.status-bar {background:#f8fafc; border-top:1px solid #d4dcea; padding:7px 18px; display:flex; gap:24px; color:#536074; font-size:13px;}
.badge {display:inline-block; padding:5px 10px; border-radius:999px; background:#eaf2ff; color:#0f4fbf; border:1px solid #b8d1ff; font-weight:700; font-size:13px;}
.badge.ok {background:#e8f7ee; color:#107c10; border-color:#b7e3c5;}
.badge.warn {background:#fff5df; color:#8a5a00; border-color:#ffd485;}
.service-grid {display:grid; grid-template-columns:repeat(6, minmax(120px, 1fr)); gap:12px; margin:14px 0 24px;}
.service-card {background:#fff; border:1px solid #d9e1ee; border-radius:10px; padding:14px; min-height:84px;}
.service-card strong {font-size:18px;}
.service-card small {color:#667085;}
.file-grid {display:grid; grid-template-columns: repeat(4, minmax(140px, 1fr)); gap:12px; margin:12px 0 18px;}
.file-tile {background:#fff; border:1px solid #d9e1ee; border-radius:8px; padding:12px; min-height:88px;}
.file-tile.selected {border-color:#2564cf; box-shadow: inset 0 0 0 1px #2564cf;}
.file-name {font-weight:700; margin-bottom:8px;}
.meta {color:#667085; font-size:13px;}
.activity {border-left:4px solid #2564cf; background:#f0f5ff; padding:10px 14px; margin-top:10px;}
.teams-layout {display:grid; grid-template-columns:240px 1fr 300px; gap:14px;}
.panel {background:#fff; border:1px solid #d9e1ee; border-radius:10px; padding:14px;}
.chat-message {padding:10px 12px; border-radius:10px; background:#f5f7fb; margin:8px 0;}
.chat-message.me {background:#e8f1ff; border-left:4px solid #6264a7;}
.sharepoint-layout {display:grid; grid-template-columns:240px 1fr 300px; gap:14px;}
.left-nav {background:#fff; border:1px solid #d9e1ee; border-radius:10px; padding:12px;}
.nav-item {padding:9px 10px; border-radius:6px; margin:4px 0;}
.nav-item.active {background:#eaf2ff; color:#0f4fbf; font-weight:700;}
.library-row {display:grid; grid-template-columns: 36px 1fr 150px 150px 110px; gap:10px; align-items:center; padding:10px; border-bottom:1px solid #e5ebf5;}
.library-row.header {font-weight:700; color:#536074; background:#f8fafc; border-radius:8px 8px 0 0;}
.onedrive-layout {display:grid; grid-template-columns:230px 1fr 320px; gap:14px;}
.progress {height:8px; border-radius:999px; background:#e5ebf5; overflow:hidden; margin-top:7px;}
.progress > div {height:100%; background:#2564cf;}
.copilot-layout {display:grid; grid-template-columns:280px 1fr; gap:16px;}
.copilot-answer {background:#f6f9ff; border:1px solid #cfe0ff; border-radius:12px; padding:16px; min-height:170px;}
.prompt-chip {display:inline-block; border:1px solid #c7d3e5; border-radius:999px; padding:7px 10px; margin:4px; background:#fff; font-size:13px;}
.excel-grid table {border-collapse:collapse; width:100%; background:#fff;}
.excel-grid th {background:#f3f6fb; border:1px solid #ccd6e5; padding:8px; text-align:center;}
.excel-grid td {border:1px solid #ccd6e5; padding:9px; min-width:90px;}
.excel-grid td.active {outline:2px solid #107c41; outline-offset:-2px; background:#f1fff6;}
.formula {display:flex; align-items:center; gap:8px; background:#fff; border:1px solid #d4dcea; padding:8px; border-radius:6px; margin-bottom:12px;}
.formula span {font-weight:700; color:#107c41;}
.footer-links {margin-top:28px; padding:18px; border-top:1px solid #d9e1ee; background:#fafcff;}
.footer-links h3 {margin-top:0;}
@media (max-width: 1000px){.service-grid,.file-grid{grid-template-columns:repeat(2,1fr)} .teams-layout,.sharepoint-layout,.onedrive-layout,.copilot-layout{grid-template-columns:1fr} .doc-page{width:auto;padding:40px 30px}}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


def init_state():
    st.session_state.setdefault("service", "Word")
    st.session_state.setdefault("word_tab", "ホーム")
    st.session_state.setdefault("word_bold", False)
    st.session_state.setdefault("word_underline", False)
    st.session_state.setdefault("word_bullets", False)
    st.session_state.setdefault("word_style", "標準")
    st.session_state.setdefault("word_table", None)
    st.session_state.setdefault("word_comment", "")
    st.session_state.setdefault("word_margin", "標準")
    st.session_state.setdefault("word_bg", "白")
    st.session_state.setdefault("word_border", False)
    st.session_state.setdefault("word_zoom", 100)
    st.session_state.setdefault("word_save", "未保存")
    st.session_state.setdefault("word_share", "未共有")
    st.session_state.setdefault("excel_formula", "=SUM(B2:B4)")
    st.session_state.setdefault("excel_result", "")
    st.session_state.setdefault("excel_selected", "B5")
    st.session_state.setdefault("excel_table", {"B2":120, "B3":180, "B4":220, "C2":15, "C3":22, "C4":30})
    st.session_state.setdefault("teams_messages", [
        ("佐藤", "会議資料を確認してください。"),
        ("田中", "共有フォルダーに最新版を置きました。"),
    ])
    st.session_state.setdefault("teams_file", False)
    st.session_state.setdefault("teams_reaction", False)
    st.session_state.setdefault("teams_meeting", False)
    st.session_state.setdefault("onedrive_files", [
        {"name":"研修資料.docx", "owner":"自分", "sync":"同期済み", "shared":"未共有", "version":3},
        {"name":"売上一覧.xlsx", "owner":"自分", "sync":"同期済み", "shared":"リンク共有", "version":5},
        {"name":"共有フォルダー", "owner":"チーム", "sync":"オンラインのみ", "shared":"組織内", "version":1},
    ])
    st.session_state.setdefault("onedrive_selected", "研修資料.docx")
    st.session_state.setdefault("onedrive_activity", "ファイルを選択してください。")
    st.session_state.setdefault("sp_site", "経営企画サイト")
    st.session_state.setdefault("sp_files", [
        {"name":"研修資料.docx", "modified":"今日 09:20", "user":"佐藤", "status":"承認済み"},
        {"name":"売上一覧.xlsx", "modified":"昨日 16:40", "user":"田中", "status":"レビュー中"},
        {"name":"議事録.docx", "modified":"月曜 11:05", "user":"自分", "status":"下書き"},
    ])
    st.session_state.setdefault("sp_activity", "サイトを選択し、ドキュメントライブラリを操作します。")
    st.session_state.setdefault("sp_permission", "閲覧者: 組織内 / 編集者: 経営企画チーム")
    st.session_state.setdefault("copilot_prompt", "")
    st.session_state.setdefault("copilot_answer", "ここにCopilotの提案が表示されます。")
    st.session_state.setdefault("copilot_sources", ["研修資料.docx", "売上一覧.xlsx", "共有フォルダー"])


def mark_done(service, key):
    done_key = f"done_{service}"
    done = set(st.session_state.get(done_key, []))
    done.add(key)
    st.session_state[done_key] = list(done)


def progress_bar(service, tasks):
    done = set(st.session_state.get(f"done_{service}", []))
    current = next((label for key, label in tasks if key not in done), "体験完了。下部の実サービスで同じ操作を試してください。")
    st.markdown(
        f"<div class='training-bar'><div><b>体験：</b>{html.escape(current)}</div><b>{len(done)}/{len(tasks)} 完了</b></div>",
        unsafe_allow_html=True,
    )


def header(title, cls=""):
    st.markdown(f"<div class='app-shell'><div class='app-top {cls}'>{html.escape(title)}</div>", unsafe_allow_html=True)


def close_shell():
    st.markdown("</div>", unsafe_allow_html=True)


def top_selector():
    st.markdown("<h2>体験するサービスを選択</h2>", unsafe_allow_html=True)
    cols = st.columns(len(SERVICES))
    for i, svc in enumerate(SERVICES):
        with cols[i]:
            if st.button(svc, use_container_width=True, type="primary" if st.session_state.service == svc else "secondary"):
                st.session_state.service = svc
                st.rerun()


def service_links():
    st.markdown("<div class='footer-links'><h3>実サービス</h3>", unsafe_allow_html=True)
    cols = st.columns(6)
    for i, svc in enumerate(SERVICES):
        with cols[i]:
            st.link_button("開く", SERVICE_URLS[svc], use_container_width=True)
            st.caption(svc)
    st.markdown("</div>", unsafe_allow_html=True)


def render_word_doc():
    pstyle = []
    if st.session_state.word_bold:
        pstyle.append("font-weight:700")
    if st.session_state.word_underline:
        pstyle.append("text-decoration:underline")
    if st.session_state.word_style == "見出し":
        pstyle.append("font-size:23px")
    if st.session_state.word_style == "強調":
        pstyle.append("color:#0f4fbf")
    style = ";".join(pstyle)
    bg = {"白":"#fff", "薄い青":"#f7fbff", "薄いグレー":"#fbfbfc"}.get(st.session_state.word_bg, "#fff")
    border = "2px solid #6b8fd6" if st.session_state.word_border else "1px solid #d0d7e2"
    margin_padding = {"狭い":"52px 72px", "標準":"78px 90px", "広い":"100px 116px"}.get(st.session_state.word_margin, "78px 90px")
    base_text = [
        "旧Officeでは個人PCや共有フォルダーに保存していました。",
        "Microsoft 365移行後は、OneDriveとSharePointを使い分け、Teamsから関係者へ共有します。",
    ]
    if st.session_state.word_bullets:
        body = "<ul>" + "".join(f"<li style='{style}'>{html.escape(t)}</li>" for t in base_text) + "</ul>"
    else:
        body = "".join(f"<p style='{style}'>{html.escape(t)}</p>" for t in base_text)
    title_tag = "h2" if st.session_state.word_style == "見出し" else "h3"
    table = ""
    if st.session_state.word_table:
        r, c = st.session_state.word_table
        rows = "".join("<tr>" + "".join(f"<td>項目{ri+1}-{ci+1}</td>" for ci in range(c)) + "</tr>" for ri in range(r))
        table = f"<table style='border-collapse:collapse;margin-top:18px;width:80%;'>{rows}</table>".replace("<td>", "<td style='border:1px solid #8aa3c7;padding:8px;'>")
    comment = f"<div class='activity'>コメント: {html.escape(st.session_state.word_comment)}</div>" if st.session_state.word_comment else ""
    field = "<p><span class='badge'>氏名</span> <span class='badge'>所属</span></p>" if "差し込み" in st.session_state.get("done_Word", []) else ""
    st.markdown(
        f"<div class='doc-page' style='background:{bg};border:{border};padding:{margin_padding};zoom:{st.session_state.word_zoom/100};'><{title_tag}>M365移行後のファイル保存ルール</{title_tag}>{body}{table}{field}{comment}</div>",
        unsafe_allow_html=True,
    )


def word_page():
    tasks = [("home", "ホームで文字書式を選ぶ"), ("insert", "挿入で表を入れる"), ("layout", "レイアウトで余白を変える"), ("design", "デザインで背景・罫線を変える"), ("review", "校閲でコメントを追加する"), ("view", "表示でズームを変える"), ("mail", "差し込み文書でフィールドを入れる"), ("file", "ファイルで保存・共有状態を確認する")]
    header("Word　保存ルール.docx")
    tabs = ["ファイル", "ホーム", "挿入", "レイアウト", "デザイン", "校閲", "表示", "差し込み文書"]
    tab_cols = st.columns(len(tabs))
    for i, t in enumerate(tabs):
        with tab_cols[i]:
            if st.button(t, key=f"word_tab_{t}", use_container_width=True):
                st.session_state.word_tab = t
                if t == "ファイル":
                    mark_done("Word", "file")
                st.rerun()
    st.markdown("<div class='ribbon'>", unsafe_allow_html=True)
    tab = st.session_state.word_tab
    if tab == "ホーム":
        c1, c2, c3, c4 = st.columns([1,1,1,2])
        with c1:
            st.session_state.word_bold = st.toggle("太字", value=st.session_state.word_bold)
        with c2:
            st.session_state.word_underline = st.toggle("下線", value=st.session_state.word_underline)
        with c3:
            st.session_state.word_bullets = st.toggle("箇条書き", value=st.session_state.word_bullets)
        with c4:
            st.session_state.word_style = st.selectbox("スタイル", ["標準", "見出し", "強調"], index=["標準", "見出し", "強調"].index(st.session_state.word_style))
        mark_done("Word", "home")
    elif tab == "挿入":
        table_size = st.selectbox("表サイズ", ["2 x 2", "3 x 3", "4 x 3"])
        r, c = [int(x.strip()) for x in table_size.split("x")]
        st.session_state.word_table = (r, c)
        st.caption("選択した表が文書内に自動挿入されます。")
        mark_done("Word", "insert")
    elif tab == "レイアウト":
        st.session_state.word_margin = st.radio("余白", ["狭い", "標準", "広い"], horizontal=True, index=["狭い", "標準", "広い"].index(st.session_state.word_margin))
        mark_done("Word", "layout")
    elif tab == "デザイン":
        st.session_state.word_bg = st.radio("ページ背景", ["白", "薄い青", "薄いグレー"], horizontal=True, index=["白", "薄い青", "薄いグレー"].index(st.session_state.word_bg))
        st.session_state.word_border = st.toggle("ページ罫線", value=st.session_state.word_border)
        mark_done("Word", "design")
    elif tab == "校閲":
        st.session_state.word_comment = st.text_input("コメント", st.session_state.word_comment or "保存先をOneDriveに統一しましょう")
        mark_done("Word", "review")
    elif tab == "表示":
        st.session_state.word_zoom = st.slider("ズーム", 75, 150, st.session_state.word_zoom, 25)
        mark_done("Word", "view")
    elif tab == "差し込み文書":
        st.selectbox("差し込みフィールド", ["氏名", "所属", "メールアドレス"])
        mark_done("Word", "mail")
    elif tab == "ファイル":
        st.session_state.word_save = st.selectbox("保存先", ["未保存", "OneDrive - 個人", "SharePoint - 経営企画サイト"], index=["未保存", "OneDrive - 個人", "SharePoint - 経営企画サイト"].index(st.session_state.word_save))
        st.session_state.word_share = st.radio("共有範囲", ["未共有", "指定したユーザー", "組織内リンク"], horizontal=True, index=["未共有", "指定したユーザー", "組織内リンク"].index(st.session_state.word_share))
    st.markdown("</div>", unsafe_allow_html=True)
    progress_bar("Word", tasks)
    st.markdown("<div class='training-main'>", unsafe_allow_html=True)
    render_word_doc()
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='status-bar'><span>ページ 1/1</span><span>表示 {st.session_state.word_zoom}%</span><span>保存: {html.escape(st.session_state.word_save)}</span><span>共有: {html.escape(st.session_state.word_share)}</span></div>", unsafe_allow_html=True)
    close_shell()


def eval_formula(formula):
    data = st.session_state.excel_table
    vals = [data.get("B2", 0), data.get("B3", 0), data.get("B4", 0)]
    f = formula.strip().upper().replace(" ", "")
    if f == "=SUM(B2:B4)":
        return sum(vals)
    if f == "=AVERAGE(B2:B4)":
        return round(sum(vals)/len(vals), 1)
    if f == "=MAX(B2:B4)":
        return max(vals)
    if f == "=MIN(B2:B4)":
        return min(vals)
    return "対応例: =SUM(B2:B4)"


def excel_page():
    tasks = [("select", "セルを選択する"), ("formula", "数式バーに =SUM(B2:B4) を入力する"), ("style", "セルの書式を変更する"), ("chart", "グラフを表示する")]
    header("Excel　売上一覧.xlsx", "gray")
    st.markdown("<div class='ribbon'>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns([1.4,3,1,1])
    with c1:
        st.session_state.excel_selected = st.selectbox("名前ボックス", ["B2","B3","B4","B5"], index=["B2","B3","B4","B5"].index(st.session_state.excel_selected))
        mark_done("Excel", "select")
    with c2:
        st.session_state.excel_formula = st.text_input("fx", st.session_state.excel_formula)
        st.session_state.excel_result = eval_formula(st.session_state.excel_formula)
        mark_done("Excel", "formula")
    with c3:
        bold = st.toggle("太字", key="excel_bold")
        if bold:
            mark_done("Excel", "style")
    with c4:
        chart = st.toggle("グラフ", key="excel_chart")
        if chart:
            mark_done("Excel", "chart")
    st.markdown("</div>", unsafe_allow_html=True)
    progress_bar("Excel", tasks)
    st.markdown("<div class='training-main'><div class='office-card excel-grid'>", unsafe_allow_html=True)
    rows = [
        ["", "A", "B", "C"],
        ["1", "項目", "金額", "件数"],
        ["2", "Word研修", st.session_state.excel_table["B2"], st.session_state.excel_table["C2"]],
        ["3", "Excel研修", st.session_state.excel_table["B3"], st.session_state.excel_table["C3"]],
        ["4", "Teams研修", st.session_state.excel_table["B4"], st.session_state.excel_table["C4"]],
        ["5", "合計", st.session_state.excel_result, ""],
    ]
    html_table = "<table>"
    for r_i, row in enumerate(rows):
        html_table += "<tr>"
        for c_i, val in enumerate(row):
            tag = "th" if r_i == 0 or c_i == 0 else "td"
            cell_ref = f"{chr(64+c_i)}{r_i}" if c_i > 0 and r_i > 0 else ""
            cls = " class='active'" if cell_ref == st.session_state.excel_selected else ""
            style = " style='font-weight:700'" if st.session_state.get("excel_bold") and cell_ref == st.session_state.excel_selected else ""
            html_table += f"<{tag}{cls}{style}>{html.escape(str(val))}</{tag}>"
        html_table += "</tr>"
    html_table += "</table>"
    st.markdown(html_table, unsafe_allow_html=True)
    if st.session_state.get("excel_chart"):
        st.bar_chart(pd.DataFrame({"金額":[120,180,220]}, index=["Word研修","Excel研修","Teams研修"]))
    st.markdown("</div></div>", unsafe_allow_html=True)
    close_shell()


def teams_page():
    tasks = [("mention", "@メンションを付けて送信する"), ("file", "ファイルを共有する"), ("reaction", "リアクションを付ける"), ("meeting", "会議を開始する")]
    header("Teams　経営企画チーム", "purple")
    st.markdown("<div class='ribbon'>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns([3,1,1,1])
    with c1:
        msg = st.text_input("メッセージ", "@佐藤 研修資料を確認してください。")
    with c2:
        if st.button("送信", use_container_width=True):
            st.session_state.teams_messages.append(("自分", msg))
            if "@" in msg:
                mark_done("Teams", "mention")
    with c3:
        if st.button("ファイル共有", use_container_width=True):
            st.session_state.teams_file = True
            mark_done("Teams", "file")
    with c4:
        if st.button("会議開始", use_container_width=True):
            st.session_state.teams_meeting = True
            mark_done("Teams", "meeting")
    st.markdown("</div>", unsafe_allow_html=True)
    progress_bar("Teams", tasks)
    st.markdown("<div class='training-main'><div class='teams-layout'>", unsafe_allow_html=True)
    st.markdown("<div class='panel'><b>チーム</b><div class='nav-item active'>経営企画</div><div class='nav-item'>一般</div><div class='nav-item'>研修</div></div>", unsafe_allow_html=True)
    with st.container():
        st.markdown("<div class='panel'><h3>チャネル: 研修</h3>", unsafe_allow_html=True)
        for sender, body in st.session_state.teams_messages:
            cls = "chat-message me" if sender == "自分" else "chat-message"
            st.markdown(f"<div class='{cls}'><b>{html.escape(sender)}</b><br>{html.escape(body)}</div>", unsafe_allow_html=True)
        if st.session_state.teams_file:
            st.markdown("<div class='file-tile'><div class='file-name'>研修資料.docx</div><div class='meta'>このチャネルで共有されました</div></div>", unsafe_allow_html=True)
        if st.button("最新メッセージにリアクション", use_container_width=True):
            st.session_state.teams_reaction = True
            mark_done("Teams", "reaction")
        if st.session_state.teams_reaction:
            st.markdown("<span class='badge ok'>リアクション済み</span>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    meeting_status = "会議中" if st.session_state.teams_meeting else "待機中"
    st.markdown(f"<div class='panel'><h3>会議</h3><p><span class='badge'>{meeting_status}</span></p><p class='meta'>@メンション、ファイル、リアクション、会議開始の流れを確認します。</p></div>", unsafe_allow_html=True)
    st.markdown("</div></div>", unsafe_allow_html=True)
    close_shell()


def onedrive_page():
    tasks = [("upload", "ファイルをアップロードする"), ("share", "共有リンクを作成する"), ("sync", "同期状態を確認する"), ("restore", "バージョン履歴から復元する")]
    header("OneDrive　自分のファイル")
    st.markdown("<div class='ribbon'>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        if st.button("ファイルをアップロード", use_container_width=True):
            if not any(f["name"] == "アップロード資料.pdf" for f in st.session_state.onedrive_files):
                st.session_state.onedrive_files.append({"name":"アップロード資料.pdf", "owner":"自分", "sync":"同期中", "shared":"未共有", "version":1})
            st.session_state.onedrive_selected = "アップロード資料.pdf"
            st.session_state.onedrive_activity = "アップロード資料.pdf を追加しました。同期が開始されました。"
            mark_done("OneDrive", "upload")
    with c2:
        if st.button("共有リンクを作成", use_container_width=True):
            for f in st.session_state.onedrive_files:
                if f["name"] == st.session_state.onedrive_selected:
                    f["shared"] = "リンク共有"
            st.session_state.onedrive_activity = f"{st.session_state.onedrive_selected} の共有リンクを作成しました。"
            mark_done("OneDrive", "share")
    with c3:
        if st.button("同期状態を確認", use_container_width=True):
            for f in st.session_state.onedrive_files:
                if f["name"] == st.session_state.onedrive_selected:
                    f["sync"] = "同期済み"
            st.session_state.onedrive_activity = "同期状態を確認しました。最新状態です。"
            mark_done("OneDrive", "sync")
    with c4:
        if st.button("バージョン履歴から復元", use_container_width=True):
            for f in st.session_state.onedrive_files:
                if f["name"] == st.session_state.onedrive_selected:
                    f["version"] += 1
            st.session_state.onedrive_activity = "前のバージョンを復元し、新しい版として保存しました。"
            mark_done("OneDrive", "restore")
    st.markdown("</div>", unsafe_allow_html=True)
    progress_bar("OneDrive", tasks)
    st.markdown("<div class='training-main'><div class='onedrive-layout'>", unsafe_allow_html=True)
    st.markdown("<div class='left-nav'><div class='nav-item active'>自分のファイル</div><div class='nav-item'>最近使った項目</div><div class='nav-item'>共有</div><div class='nav-item'>ごみ箱</div></div>", unsafe_allow_html=True)
    with st.container():
        st.markdown("<div class='panel'><h3>ファイル一覧</h3><div class='file-grid'>", unsafe_allow_html=True)
        cols = st.columns(3)
        for idx, f in enumerate(st.session_state.onedrive_files):
            with cols[idx % 3]:
                selected = f["name"] == st.session_state.onedrive_selected
                if st.button(f["name"], key=f"od_{f['name']}", use_container_width=True, type="primary" if selected else "secondary"):
                    st.session_state.onedrive_selected = f["name"]
                    st.session_state.onedrive_activity = f"{f['name']} を選択しました。"
                    st.rerun()
                st.caption(f"{f['sync']} / {f['shared']} / v{f['version']}")
        st.markdown("</div></div>", unsafe_allow_html=True)
    selected = next((f for f in st.session_state.onedrive_files if f["name"] == st.session_state.onedrive_selected), st.session_state.onedrive_files[0])
    pct = 100 if selected["sync"] == "同期済み" else 55
    st.markdown(f"<div class='panel'><h3>詳細</h3><p><b>{html.escape(selected['name'])}</b></p><p>同期: <span class='badge'>{html.escape(selected['sync'])}</span></p><div class='progress'><div style='width:{pct}%'></div></div><p>共有: {html.escape(selected['shared'])}</p><p>バージョン: {selected['version']}</p><div class='activity'>{html.escape(st.session_state.onedrive_activity)}</div></div>", unsafe_allow_html=True)
    st.markdown("</div></div>", unsafe_allow_html=True)
    close_shell()


def sharepoint_page():
    tasks = [("site", "サイトを選択する"), ("add", "ドキュメントを追加する"), ("permission", "権限を確認する"), ("news", "ニュースを投稿する")]
    header("SharePoint　チームサイト", "green")
    st.markdown("<div class='ribbon'>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns([1.4,1,1,1])
    with c1:
        st.session_state.sp_site = st.selectbox("サイト", ["経営企画サイト", "研修サイト", "総務サイト"], index=["経営企画サイト", "研修サイト", "総務サイト"].index(st.session_state.sp_site))
        mark_done("SharePoint", "site")
    with c2:
        if st.button("ドキュメントを追加", use_container_width=True):
            name = f"追加資料_{len(st.session_state.sp_files)+1}.docx"
            st.session_state.sp_files.insert(0, {"name":name, "modified":"今", "user":"自分", "status":"新規"})
            st.session_state.sp_activity = f"{name} をドキュメントライブラリに追加しました。"
            mark_done("SharePoint", "add")
    with c3:
        if st.button("権限を確認", use_container_width=True):
            st.session_state.sp_permission = "閲覧者: 組織内 / 編集者: 経営企画チーム / 所有者: 管理者"
            st.session_state.sp_activity = "サイトとライブラリの権限を確認しました。"
            mark_done("SharePoint", "permission")
    with c4:
        if st.button("ニュースを投稿", use_container_width=True):
            st.session_state.sp_activity = "ニュース: M365研修のお知らせ を投稿しました。"
            mark_done("SharePoint", "news")
    st.markdown("</div>", unsafe_allow_html=True)
    progress_bar("SharePoint", tasks)
    st.markdown("<div class='training-main'><div class='sharepoint-layout'>", unsafe_allow_html=True)
    st.markdown(f"<div class='left-nav'><h3>{html.escape(st.session_state.sp_site)}</h3><div class='nav-item active'>ホーム</div><div class='nav-item'>ドキュメント</div><div class='nav-item'>ニュース</div><div class='nav-item'>サイトの内容</div></div>", unsafe_allow_html=True)
    with st.container():
        st.markdown("<div class='panel'><h3>ドキュメント ライブラリ</h3><div class='library-row header'><div></div><div>名前</div><div>更新日時</div><div>更新者</div><div>状態</div></div>", unsafe_allow_html=True)
        for f in st.session_state.sp_files:
            st.markdown(f"<div class='library-row'><div>□</div><div><b>{html.escape(f['name'])}</b></div><div>{html.escape(f['modified'])}</div><div>{html.escape(f['user'])}</div><div><span class='badge'>{html.escape(f['status'])}</span></div></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='activity'>{html.escape(st.session_state.sp_activity)}</div></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='panel'><h3>サイト情報</h3><p><b>権限</b></p><p>{html.escape(st.session_state.sp_permission)}</p><p><b>最近のニュース</b></p><p>M365研修のお知らせ</p><p>ファイル管理ルール更新</p></div>", unsafe_allow_html=True)
    st.markdown("</div></div>", unsafe_allow_html=True)
    close_shell()


def copilot_response(prompt):
    p = prompt.strip()
    if not p:
        return "依頼文を入力すると、要約・文章作成・次の操作提案などを表示します。"
    if "要約" in p:
        return "要約案:\n- 研修資料の主題は、ファイル保存先の使い分けです。\n- 個人作業はOneDrive、チーム共有はSharePoint、連絡はTeamsを使います。\n- 共有時は権限範囲を確認します。"
    if "メール" in p or "文章" in p:
        return "文章案:\nMicrosoft 365移行後は、個人作業中のファイルはOneDriveに保存し、チームで共有する正式資料はSharePointに保存してください。関係者への連絡はTeamsで行い、必要に応じてリンク共有を利用してください。"
    if "次" in p or "操作" in p:
        return "次の操作提案:\n1. Wordで資料を作成します。\n2. OneDriveに一時保存します。\n3. 完成後、SharePointのチームサイトへ移動します。\n4. Teamsで関係者に@メンション付きで共有します。"
    return f"Copilot提案:\n「{p}」について、資料・表・共有フォルダーを参照し、要点整理と次の操作案を作成しました。"


def copilot_page():
    tasks = [("prompt", "依頼文を入力する"), ("summary", "要約を作成する"), ("draft", "文章を整える"), ("next", "次の操作を提案する")]
    header("Copilot　作業支援")
    st.markdown("<div class='ribbon'>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("要約用プロンプト", use_container_width=True):
            st.session_state.copilot_prompt = "研修資料.docxを要約してください。"
            st.session_state.copilot_answer = copilot_response(st.session_state.copilot_prompt)
            mark_done("Copilot", "summary")
            mark_done("Copilot", "prompt")
    with c2:
        if st.button("文章作成プロンプト", use_container_width=True):
            st.session_state.copilot_prompt = "M365移行後の保存ルールを説明する文章を作ってください。"
            st.session_state.copilot_answer = copilot_response(st.session_state.copilot_prompt)
            mark_done("Copilot", "draft")
            mark_done("Copilot", "prompt")
    with c3:
        if st.button("次の操作提案", use_container_width=True):
            st.session_state.copilot_prompt = "資料作成後の次の操作を提案してください。"
            st.session_state.copilot_answer = copilot_response(st.session_state.copilot_prompt)
            mark_done("Copilot", "next")
            mark_done("Copilot", "prompt")
    st.markdown("</div>", unsafe_allow_html=True)
    progress_bar("Copilot", tasks)
    st.markdown("<div class='training-main'><div class='copilot-layout'>", unsafe_allow_html=True)
    st.markdown("<div class='panel'><h3>参照できる作業データ</h3><div class='file-tile'>研修資料.docx<br><span class='meta'>Word文書</span></div><div class='file-tile'>売上一覧.xlsx<br><span class='meta'>Excelブック</span></div><div class='file-tile'>共有フォルダー<br><span class='meta'>OneDrive / SharePoint</span></div></div>", unsafe_allow_html=True)
    with st.container():
        st.markdown("<div class='panel'><h3>プロンプト入力</h3>", unsafe_allow_html=True)
        st.session_state.copilot_prompt = st.text_area("Copilotに依頼する内容", st.session_state.copilot_prompt, height=120, placeholder="例: 研修資料.docxを3点で要約してください。")
        if st.button("生成", use_container_width=True, type="primary"):
            st.session_state.copilot_answer = copilot_response(st.session_state.copilot_prompt)
            mark_done("Copilot", "prompt")
        answer = html.escape(st.session_state.copilot_answer).replace("\n", "<br>")
        st.markdown(f"<div class='copilot-answer'><b>Copilotの回答</b><br><br>{answer}</div></div>", unsafe_allow_html=True)
    st.markdown("</div></div>", unsafe_allow_html=True)
    close_shell()


def main():
    init_state()
    top_selector()
    service = st.session_state.service
    if service == "Word":
        word_page()
    elif service == "Excel":
        excel_page()
    elif service == "Teams":
        teams_page()
    elif service == "OneDrive":
        onedrive_page()
    elif service == "SharePoint":
        sharepoint_page()
    elif service == "Copilot":
        copilot_page()
    service_links()


if __name__ == "__main__":
    main()
