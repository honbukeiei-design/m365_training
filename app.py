from __future__ import annotations

import re
from datetime import datetime
from typing import Any

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Microsoft 365 体験トレーニング",
    layout="wide",
    initial_sidebar_state="collapsed",
)

SERVICES = ["Word", "Excel", "Teams", "OneDrive", "SharePoint", "Copilot"]
SERVICE_URLS = {
    "Word": "https://word.cloud.microsoft/",
    "Excel": "https://excel.cloud.microsoft/",
    "Teams": "https://teams.microsoft.com/",
    "OneDrive": "https://onedrive.live.com/",
    "SharePoint": "https://www.microsoft.com/ja-jp/microsoft-365/sharepoint/collaboration",
    "Copilot": "https://copilot.microsoft.com/",
}

CSS = """
<style>
[data-testid="stSidebar"], [data-testid="collapsedControl"], #MainMenu, footer, header {display:none !important; visibility:hidden !important;}
.block-container {padding: 16px 22px 26px !important; max-width: 1540px !important;}
html, body, [class*="css"] {font-family: "Segoe UI", "Yu Gothic", sans-serif; color:#0f1b2d;}
.stButton > button {border-radius: 6px; border: 1px solid #c7d3e5; background:#fff; min-height:38px; color:#14213d;}
.stButton > button:hover {border-color:#2564cf; color:#0f4fbf; background:#f7fbff;}
.stButton > button[kind="primary"] {background:#2564cf; color:#fff; border-color:#2564cf;}
.stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"], .stNumberInput input {border-color:#c8d5e8 !important;}
.app-title {font-size: 30px; font-weight: 800; margin: 2px 0 14px;}
.section-title {font-size: 17px; font-weight: 700; margin: 20px 0 8px;}
.office-shell {border:1px solid #cfd9e8; border-radius:12px; overflow:hidden; background:#eaf0f8; box-shadow:0 8px 24px rgba(13, 35, 67, .08); margin-top:14px;}
.office-titlebar {height:54px; display:flex; align-items:center; gap:18px; padding:0 22px; background:#185abd; color:#fff; font-size:21px; font-weight:800;}
.office-titlebar.green {background:#107c41;}
.office-titlebar.purple {background:#6264a7;}
.office-titlebar.teal {background:#03787c;}
.office-titlebar.blue {background:#0f6cbd;}
.office-tabs {background:#fff; border-bottom:1px solid #d6dfed; padding: 6px 12px;}
.ribbon-area {background:#fbfcff; border-bottom:1px solid #d6dfed; padding: 14px 18px 8px; min-height: 90px;}
.training-line {margin: 14px 20px; padding: 12px 16px; border:1px solid #a8c7ff; border-radius:10px; background:#eef6ff; display:flex; align-items:center; justify-content:space-between;}
.training-line b {color:#064db5;}
.workbench {padding: 20px 26px 24px; background:#e7eef8; min-height: 560px;}
.doc-page {background:#fff; border:1px solid #cfd8e6; box-shadow:0 6px 24px rgba(15,27,45,.13); width:min(920px, 88%); min-height:560px; margin: 6px auto 14px; padding:64px 78px; line-height:1.85; font-size:18px;}
.doc-status {height:34px; display:flex; gap:24px; align-items:center; padding:0 18px; background:#f7f9fc; border-top:1px solid #d6dfed; color:#526071; font-size:13px;}
.badge {display:inline-block; padding:5px 10px; border:1px solid #bcd3ff; border-radius:999px; background:#eef5ff; color:#0f4fbf; font-weight:700; font-size:13px;}
.badge-green {background:#e8f7ee; color:#107c10; border-color:#b7e3c5;}
.badge-warn {background:#fff5df; color:#8a5a00; border-color:#ffd485;}
.card {background:#fff; border:1px solid #d6dfed; border-radius:12px; padding:18px; box-shadow:0 4px 16px rgba(15,27,45,.05);}
.file-list {border:1px solid #d6dfed; border-radius:10px; overflow:hidden; background:#fff;}
.file-row {display:grid; grid-template-columns: 40px 1.5fr 110px 130px 110px; gap:10px; align-items:center; padding:10px 12px; border-bottom:1px solid #e6ecf5;}
.file-row:last-child {border-bottom:none;}
.file-row.header {background:#f5f7fb; color:#526071; font-weight:700;}
.file-row.selected {background:#edf5ff; box-shadow: inset 3px 0 0 #2564cf;}
.service-card {background:#fff; border:1px solid #d6dfed; border-radius:10px; padding:14px; min-height:86px;}
.left-nav {background:#fff; border:1px solid #d6dfed; border-radius:10px; padding:12px;}
.nav-item {padding:9px 10px; border-radius:6px; margin:4px 0;}
.nav-item.active {background:#eaf2ff; color:#0f4fbf; font-weight:700;}
.detail-pane {background:#fff; border:1px solid #d6dfed; border-radius:10px; padding:16px; min-height:320px;}
.activity {border-left:4px solid #2564cf; background:#f0f5ff; padding:10px 14px; margin-top:12px;}
.teams-message {padding:10px 12px; border-radius:10px; background:#f5f7fb; margin:8px 0;}
.teams-message.me {background:#ecebff; border-left:4px solid #6264a7;}
.excel-grid table {border-collapse:collapse; width:100%; background:#fff;}
.excel-grid th {background:#f3f6fb; border:1px solid #ccd6e5; padding:7px; text-align:center; font-weight:700;}
.excel-grid td {border:1px solid #ccd6e5; padding:8px 10px; min-width:84px; height:34px;}
.excel-grid td.active {outline:2px solid #107c41; outline-offset:-2px; background:#f0fff5;}
.formula-bar {display:flex; align-items:center; gap:10px; border:1px solid #ccd6e5; background:#fff; padding:8px 12px; border-radius:8px; margin-bottom:12px;}
.formula-bar span {font-weight:800; color:#107c41;}
.copilot-answer {background:#f6f9ff; border:1px solid #cfe0ff; border-radius:12px; padding:16px; min-height:190px;}
.footer-links {margin-top:26px; padding:16px 0 0; border-top:1px solid #d6dfed;}
.small-muted {color:#667085; font-size:13px;}
@media (max-width: 980px){.doc-page{width:auto;padding:42px 30px}.file-row{grid-template-columns:32px 1fr 90px}.file-row div:nth-child(4),.file-row div:nth-child(5){display:none}}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


def init_state() -> None:
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
    st.session_state.setdefault("word_body", "旧Officeでは個人PCや共有フォルダーに保存していました。\nMicrosoft 365移行後は、OneDriveとSharePointを使い分け、Teamsから関係者へ共有します。")
    st.session_state.setdefault("word_fields", [])

    st.session_state.setdefault("excel_formula", "=SUM(B2:B4)")
    st.session_state.setdefault("excel_result", "")
    st.session_state.setdefault("excel_selected", "B5")
    st.session_state.setdefault("excel_table", {"B2": 120, "B3": 180, "B4": 220, "C2": 15, "C3": 22, "C4": 30})

    st.session_state.setdefault("teams_messages", [("佐藤", "会議資料を確認してください。"), ("田中", "共有フォルダーに最新版を置きました。")])
    st.session_state.setdefault("teams_text", "@佐藤 研修資料を確認しました。")
    st.session_state.setdefault("teams_file", False)
    st.session_state.setdefault("teams_reaction", False)
    st.session_state.setdefault("teams_meeting", False)

    st.session_state.setdefault("onedrive_files", [
        {"name": "研修資料.docx", "owner": "自分", "sync": "同期済み", "shared": "未共有", "version": 3},
        {"name": "売上一覧.xlsx", "owner": "自分", "sync": "同期済み", "shared": "リンク共有", "version": 5},
        {"name": "共有フォルダー", "owner": "チーム", "sync": "オンラインのみ", "shared": "組織内", "version": 1},
    ])
    st.session_state.setdefault("onedrive_selected", "研修資料.docx")
    st.session_state.setdefault("onedrive_activity", "ファイルを選択し、アップロード・共有・同期・復元を体験します。")

    st.session_state.setdefault("sp_site", "経営企画サイト")
    st.session_state.setdefault("sp_files", [
        {"name": "研修資料.docx", "modified": "今日 09:20", "user": "佐藤", "status": "承認済み"},
        {"name": "売上一覧.xlsx", "modified": "昨日 16:40", "user": "田中", "status": "レビュー中"},
        {"name": "議事録.docx", "modified": "月曜 11:05", "user": "自分", "status": "下書き"},
    ])
    st.session_state.setdefault("sp_activity", "サイトを選択し、ドキュメントライブラリを操作します。")
    st.session_state.setdefault("sp_permission", "閲覧者: 組織内 / 編集者: 経営企画チーム")
    st.session_state.setdefault("sp_news", ["M365研修のお知らせ", "ファイル管理ルール更新"])

    st.session_state.setdefault("copilot_prompt", "研修資料.docxの内容を3行で要約してください。")
    st.session_state.setdefault("copilot_answer", "ここにCopilotの提案が表示されます。")


def mark_done(service: str, key: str) -> None:
    done_key = f"done_{service}"
    done = set(st.session_state.get(done_key, []))
    done.add(key)
    st.session_state[done_key] = sorted(done)


def training_line(service: str, tasks: list[tuple[str, str]]) -> None:
    done = set(st.session_state.get(f"done_{service}", []))
    current = next((label for key, label in tasks if key not in done), "体験完了。下部の実サービスで同じ操作を試してください。")
    st.markdown(
        f"<div class='training-line'><div><b>体験：</b>{current}</div><b>{len(done)}/{len(tasks)} 完了</b></div>",
        unsafe_allow_html=True,
    )


def service_selector() -> None:
    st.markdown("<div class='app-title'>体験するサービスを選択</div>", unsafe_allow_html=True)
    cols = st.columns(len(SERVICES))
    for i, svc in enumerate(SERVICES):
        with cols[i]:
            if st.button(svc, key=f"svc_{svc}", use_container_width=True, type="primary" if st.session_state.service == svc else "secondary"):
                st.session_state.service = svc
                st.rerun()


def service_links() -> None:
    st.markdown("<div class='footer-links'><div class='section-title'>実サービス</div></div>", unsafe_allow_html=True)
    cols = st.columns(6)
    for i, svc in enumerate(SERVICES):
        with cols[i]:
            st.caption(svc)
            st.link_button("開く", SERVICE_URLS[svc], use_container_width=True)


def titlebar(name: str, subtitle: str = "", color_class: str = "") -> None:
    label = name if not subtitle else f"{name}　{subtitle}"
    st.markdown(f"<div class='office-shell'><div class='office-titlebar {color_class}'>{label}</div></div>", unsafe_allow_html=True)


def tab_buttons(prefix: str, tabs: list[str], current_key: str) -> None:
    st.markdown("<div class='office-tabs'></div>", unsafe_allow_html=True)
    cols = st.columns(len(tabs))
    for i, tab in enumerate(tabs):
        with cols[i]:
            if st.button(tab, key=f"{prefix}_{tab}", use_container_width=True, type="primary" if st.session_state[current_key] == tab else "secondary"):
                st.session_state[current_key] = tab
                st.rerun()


def render_word_page() -> None:
    body_lines = [line for line in st.session_state.word_body.splitlines() if line.strip()]
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
    bg = {"白": "#ffffff", "薄い青": "#f7fbff", "薄いグレー": "#fbfbfc"}.get(st.session_state.word_bg, "#ffffff")
    border = "2px solid #6b8fd6" if st.session_state.word_border else "1px solid #cfd8e6"
    padding = {"狭い": "48px 62px", "標準": "64px 78px", "広い": "86px 104px"}.get(st.session_state.word_margin, "64px 78px")
    title_tag = "h2" if st.session_state.word_style == "見出し" else "h3"
    if st.session_state.word_bullets:
        body_html = "<ul>" + "".join(f"<li style='{style}'>{line}</li>" for line in body_lines) + "</ul>"
    else:
        body_html = "".join(f"<p style='{style}'>{line}</p>" for line in body_lines)
    table_html = ""
    if st.session_state.word_table:
        rows, cols = st.session_state.word_table
        table_rows = "".join("<tr>" + "".join(f"<td>項目{r+1}-{c+1}</td>" for c in range(cols)) + "</tr>" for r in range(rows))
        table_html = f"<table style='border-collapse:collapse;width:80%;margin-top:18px;'>{table_rows}</table>".replace("<td>", "<td style='border:1px solid #8aa3c7;padding:8px;'>")
    comment_html = f"<div class='activity'>コメント: {st.session_state.word_comment}</div>" if st.session_state.word_comment else ""
    fields_html = " ".join(f"<span class='badge'>{field}</span>" for field in st.session_state.word_fields)
    field_block = f"<p>{fields_html}</p>" if fields_html else ""
    st.markdown(
        f"<div class='doc-page' style='background:{bg}; border:{border}; padding:{padding}; zoom:{st.session_state.word_zoom/100};'><{title_tag}>M365移行後のファイル保存ルール</{title_tag}>{body_html}{table_html}{field_block}{comment_html}</div>",
        unsafe_allow_html=True,
    )


def word_page() -> None:
    tasks = [("home", "ホームで文字書式を変更"), ("edit", "白紙ページの本文を編集"), ("insert", "表を挿入"), ("layout", "余白を変更"), ("design", "背景・罫線を変更"), ("review", "コメントを追加"), ("view", "ズームを変更"), ("mail", "差し込みフィールドを追加"), ("file", "保存・共有状態を確認")]
    titlebar("Word", "保存ルール.docx")
    tab_buttons("word_tab", ["ファイル", "ホーム", "挿入", "レイアウト", "デザイン", "校閲", "表示", "差し込み文書"], "word_tab")

    with st.container(border=True):
        tab = st.session_state.word_tab
        if tab == "ホーム":
            c1, c2, c3, c4 = st.columns([1, 1, 1, 2])
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
            rows, cols = [int(x.strip()) for x in table_size.split("x")]
            st.session_state.word_table = (rows, cols)
            st.caption("表サイズを選ぶと、文書内に自動で反映されます。")
            mark_done("Word", "insert")
        elif tab == "レイアウト":
            st.session_state.word_margin = st.radio("余白", ["狭い", "標準", "広い"], horizontal=True, index=["狭い", "標準", "広い"].index(st.session_state.word_margin))
            mark_done("Word", "layout")
        elif tab == "デザイン":
            st.session_state.word_bg = st.radio("ページ背景", ["白", "薄い青", "薄いグレー"], horizontal=True, index=["白", "薄い青", "薄いグレー"].index(st.session_state.word_bg))
            st.session_state.word_border = st.toggle("ページ罫線", value=st.session_state.word_border)
            mark_done("Word", "design")
        elif tab == "校閲":
            st.session_state.word_comment = st.text_input("コメント", value=st.session_state.word_comment or "保存先をOneDriveに統一しましょう")
            mark_done("Word", "review")
        elif tab == "表示":
            st.session_state.word_zoom = st.slider("ズーム", 75, 150, st.session_state.word_zoom, 25)
            mark_done("Word", "view")
        elif tab == "差し込み文書":
            selected_field = st.selectbox("差し込みフィールド", ["氏名", "所属", "メールアドレス"])
            if selected_field not in st.session_state.word_fields:
                st.session_state.word_fields.append(selected_field)
            mark_done("Word", "mail")
        elif tab == "ファイル":
            c1, c2 = st.columns(2)
            with c1:
                st.session_state.word_save = st.selectbox("保存先", ["未保存", "OneDrive - 個人", "SharePoint - 経営企画サイト"], index=["未保存", "OneDrive - 個人", "SharePoint - 経営企画サイト"].index(st.session_state.word_save))
            with c2:
                st.session_state.word_share = st.selectbox("共有範囲", ["未共有", "指定したユーザー", "組織内リンク"], index=["未共有", "指定したユーザー", "組織内リンク"].index(st.session_state.word_share))
            mark_done("Word", "file")

    training_line("Word", tasks)
    st.markdown("<div class='workbench'>", unsafe_allow_html=True)
    c_edit, c_view = st.columns([0.34, 0.66])
    with c_edit:
        st.markdown("<div class='card'><b>白紙ページに直接入力する想定</b><br><span class='small-muted'>本文を編集すると、右の文書に即時反映します。</span></div>", unsafe_allow_html=True)
        st.session_state.word_body = st.text_area("本文", value=st.session_state.word_body, height=250, label_visibility="collapsed")
        if st.session_state.word_body.strip():
            mark_done("Word", "edit")
    with c_view:
        render_word_page()
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='doc-status'><span>ページ 1/1</span><span>表示 {st.session_state.word_zoom}%</span><span>保存: {st.session_state.word_save}</span><span>共有: {st.session_state.word_share}</span></div>", unsafe_allow_html=True)


def parse_excel_formula(formula: str) -> Any:
    f = formula.strip().upper().replace(" ", "")
    m = re.fullmatch(r"=(SUM|AVERAGE|MAX|MIN)\((B|C)(\d):(B|C)(\d)\)", f)
    if not m:
        return "対応例: =SUM(B2:B4), =AVERAGE(B2:B4), =MAX(B2:B4), =MIN(B2:B4)"
    func, col1, r1, col2, r2 = m.groups()
    if col1 != col2:
        return "同じ列の範囲を指定してください。"
    rows = range(int(r1), int(r2) + 1)
    values = [st.session_state.excel_table.get(f"{col1}{r}", 0) for r in rows]
    if func == "SUM":
        return sum(values)
    if func == "AVERAGE":
        return round(sum(values) / len(values), 2)
    if func == "MAX":
        return max(values)
    return min(values)


def excel_page() -> None:
    tasks = [("select", "セルを選択"), ("edit", "数値を編集"), ("formula", "数式バーで =SUM(B2:B4) を計算"), ("chart", "グラフを挿入"), ("protect", "シート保護を確認")]
    titlebar("Excel", "売上一覧.xlsx", "green")
    st.markdown("<div class='office-tabs'></div>", unsafe_allow_html=True)
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        st.session_state.excel_selected = st.selectbox("選択セル", ["B2", "B3", "B4", "B5", "C2", "C3", "C4"], index=["B2", "B3", "B4", "B5", "C2", "C3", "C4"].index(st.session_state.excel_selected))
        mark_done("Excel", "select")
    with c2:
        target = st.selectbox("編集対象", ["B2", "B3", "B4", "C2", "C3", "C4"])
    with c3:
        st.session_state.excel_table[target] = st.number_input("値", value=int(st.session_state.excel_table[target]), step=1)
        mark_done("Excel", "edit")
    with c4:
        if st.button("グラフを挿入", use_container_width=True):
            mark_done("Excel", "chart")
            st.session_state.excel_chart = True
    with c5:
        if st.button("シートを保護", use_container_width=True):
            mark_done("Excel", "protect")
            st.session_state.excel_protect = True
    training_line("Excel", tasks)
    st.markdown("<div class='workbench'><div class='card'>", unsafe_allow_html=True)
    f1, f2 = st.columns([0.28, 0.72])
    with f1:
        st.markdown("<div class='formula-bar'><span>fx</span></div>", unsafe_allow_html=True)
    with f2:
        st.session_state.excel_formula = st.text_input("数式", value=st.session_state.excel_formula, label_visibility="collapsed")
    result = parse_excel_formula(st.session_state.excel_formula)
    st.session_state.excel_result = result
    if not isinstance(result, str):
        mark_done("Excel", "formula")
    rows = [
        ["", "A", "B", "C"],
        ["1", "月", "売上", "件数"],
        ["2", "4月", st.session_state.excel_table["B2"], st.session_state.excel_table["C2"]],
        ["3", "5月", st.session_state.excel_table["B3"], st.session_state.excel_table["C3"]],
        ["4", "6月", st.session_state.excel_table["B4"], st.session_state.excel_table["C4"]],
        ["5", "合計", result, ""],
    ]
    table_html = "<div class='excel-grid'><table>"
    for r_index, row in enumerate(rows):
        table_html += "<tr>"
        for c_index, val in enumerate(row):
            tag = "th" if r_index == 0 or c_index == 0 else "td"
            cell_name = "" if r_index == 0 or c_index == 0 else f"{chr(64+c_index)}{r_index}"
            active = " class='active'" if cell_name == st.session_state.excel_selected else ""
            table_html += f"<{tag}{active}>{val}</{tag}>"
        table_html += "</tr>"
    table_html += "</table></div>"
    st.markdown(table_html, unsafe_allow_html=True)
    if st.session_state.get("excel_chart"):
        st.bar_chart(pd.DataFrame({"売上": [st.session_state.excel_table["B2"], st.session_state.excel_table["B3"], st.session_state.excel_table["B4"]]}, index=["4月", "5月", "6月"]))
    if st.session_state.get("excel_protect"):
        st.markdown("<span class='badge-green'>シート保護: 有効</span>", unsafe_allow_html=True)
    st.markdown("</div></div>", unsafe_allow_html=True)


def teams_page() -> None:
    tasks = [("mention", "@メンションを付けて送信"), ("file", "ファイルを共有"), ("reaction", "リアクション"), ("meeting", "会議開始")]
    titlebar("Teams", "研修チャネル", "purple")
    b1, b2, b3 = st.columns([1, 1, 1])
    with b1:
        if st.button("ファイルを共有", use_container_width=True):
            st.session_state.teams_file = True
            mark_done("Teams", "file")
    with b2:
        if st.button("リアクション", use_container_width=True):
            st.session_state.teams_reaction = True
            mark_done("Teams", "reaction")
    with b3:
        if st.button("今すぐ会議", use_container_width=True):
            st.session_state.teams_meeting = True
            mark_done("Teams", "meeting")
    training_line("Teams", tasks)
    st.markdown("<div class='workbench'>", unsafe_allow_html=True)
    left, center, right = st.columns([0.22, 0.52, 0.26])
    with left:
        st.markdown("<div class='left-nav'><b>チーム</b><div class='nav-item active'>経営企画</div><div class='nav-item'>一般</div><div class='nav-item'>研修</div></div>", unsafe_allow_html=True)
    with center:
        st.markdown("<div class='card'><h3>チャネル: 研修</h3>", unsafe_allow_html=True)
        for sender, text in st.session_state.teams_messages:
            cls = "teams-message me" if sender == "自分" else "teams-message"
            st.markdown(f"<div class='{cls}'><b>{sender}</b><br>{text}</div>", unsafe_allow_html=True)
        st.session_state.teams_text = st.text_input("メッセージ", value=st.session_state.teams_text)
        if st.button("送信", use_container_width=True):
            if "@" in st.session_state.teams_text:
                mark_done("Teams", "mention")
            st.session_state.teams_messages.append(("自分", st.session_state.teams_text))
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    with right:
        meeting_status = "会議中" if st.session_state.teams_meeting else "未開始"
        st.markdown(f"<div class='detail-pane'><h3>操作状態</h3><p><span class='badge'>{meeting_status}</span></p>", unsafe_allow_html=True)
        if st.session_state.teams_file:
            st.markdown("<div class='activity'>研修資料.docx を共有しました。</div>", unsafe_allow_html=True)
        if st.session_state.teams_reaction:
            st.markdown("<div class='activity'>田中さんの投稿にリアクションしました。</div>", unsafe_allow_html=True)
        st.markdown("<p class='small-muted'>@メンションを使うと、相手に通知が届きやすくなります。</p></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


def onedrive_page() -> None:
    tasks = [("upload", "ファイルをアップロード"), ("share", "共有リンクを作成"), ("sync", "同期状態を確認"), ("restore", "バージョン履歴から復元")]
    titlebar("OneDrive", "自分のファイル", "blue")
    b1, b2, b3, b4 = st.columns(4)
    with b1:
        if st.button("ファイルをアップロード", use_container_width=True):
            name = f"追加資料_{datetime.now().strftime('%H%M')}.docx"
            st.session_state.onedrive_files.insert(0, {"name": name, "owner": "自分", "sync": "同期中", "shared": "未共有", "version": 1})
            st.session_state.onedrive_selected = name
            st.session_state.onedrive_activity = f"{name} をアップロードしました。"
            mark_done("OneDrive", "upload")
    with b2:
        if st.button("共有リンクを作成", use_container_width=True):
            for f in st.session_state.onedrive_files:
                if f["name"] == st.session_state.onedrive_selected:
                    f["shared"] = "リンク共有"
            st.session_state.onedrive_activity = "共有リンクを作成しました。"
            mark_done("OneDrive", "share")
    with b3:
        if st.button("同期状態を確認", use_container_width=True):
            for f in st.session_state.onedrive_files:
                if f["name"] == st.session_state.onedrive_selected:
                    f["sync"] = "同期済み"
            st.session_state.onedrive_activity = "同期状態を確認し、最新になりました。"
            mark_done("OneDrive", "sync")
    with b4:
        if st.button("バージョンを復元", use_container_width=True):
            for f in st.session_state.onedrive_files:
                if f["name"] == st.session_state.onedrive_selected:
                    f["version"] += 1
            st.session_state.onedrive_activity = "過去バージョンから復元しました。"
            mark_done("OneDrive", "restore")
    training_line("OneDrive", tasks)
    st.markdown("<div class='workbench'>", unsafe_allow_html=True)
    left, main, detail = st.columns([0.18, 0.56, 0.26])
    with left:
        st.markdown("<div class='left-nav'><div class='nav-item active'>自分のファイル</div><div class='nav-item'>最近使った項目</div><div class='nav-item'>共有</div><div class='nav-item'>ごみ箱</div></div>", unsafe_allow_html=True)
    with main:
        st.markdown("<div class='file-list'><div class='file-row header'><div></div><div>名前</div><div>所有者</div><div>同期</div><div>共有</div></div>", unsafe_allow_html=True)
        for f in st.session_state.onedrive_files:
            selected = " selected" if f["name"] == st.session_state.onedrive_selected else ""
            cols = st.columns([0.05, 0.43, 0.16, 0.18, 0.18])
            with cols[0]:
                if st.button("□", key=f"od_{f['name']}"):
                    st.session_state.onedrive_selected = f["name"]
                    st.rerun()
            with cols[1]:
                st.write(f["name"])
            with cols[2]:
                st.write(f["owner"])
            with cols[3]:
                st.write(f["sync"])
            with cols[4]:
                st.write(f["shared"])
        st.markdown("</div>", unsafe_allow_html=True)
    selected = next(f for f in st.session_state.onedrive_files if f["name"] == st.session_state.onedrive_selected)
    with detail:
        st.markdown(f"<div class='detail-pane'><h3>詳細</h3><p><b>{selected['name']}</b></p><p>同期: <span class='badge'>{selected['sync']}</span></p><p>共有: {selected['shared']}</p><p>バージョン: {selected['version']}</p><div class='activity'>{st.session_state.onedrive_activity}</div></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


def sharepoint_page() -> None:
    tasks = [("site", "サイトを選択"), ("add", "ドキュメントを追加"), ("open", "ドキュメントを開く"), ("permission", "権限を確認"), ("news", "ニュースを投稿")]
    titlebar("SharePoint", "経営企画サイト", "teal")
    b1, b2, b3, b4 = st.columns(4)
    with b1:
        st.session_state.sp_site = st.selectbox("サイト", ["経営企画サイト", "総務サイト", "研修サイト"], index=["経営企画サイト", "総務サイト", "研修サイト"].index(st.session_state.sp_site))
        mark_done("SharePoint", "site")
    with b2:
        if st.button("ドキュメントを追加", use_container_width=True):
            new_name = f"追加ファイル_{datetime.now().strftime('%H%M')}.docx"
            st.session_state.sp_files.insert(0, {"name": new_name, "modified": "今", "user": "自分", "status": "下書き"})
            st.session_state.sp_activity = f"{new_name} をドキュメントライブラリに追加しました。"
            mark_done("SharePoint", "add")
    with b3:
        if st.button("権限を確認", use_container_width=True):
            st.session_state.sp_permission = "所有者: 管理者 / 編集者: 経営企画チーム / 閲覧者: 組織内"
            st.session_state.sp_activity = "サイトとライブラリの権限を確認しました。"
            mark_done("SharePoint", "permission")
    with b4:
        if st.button("ニュースを投稿", use_container_width=True):
            st.session_state.sp_news.insert(0, "研修資料を更新しました")
            st.session_state.sp_activity = "ニュースを投稿しました。"
            mark_done("SharePoint", "news")
    training_line("SharePoint", tasks)
    st.markdown("<div class='workbench'>", unsafe_allow_html=True)
    left, main, right = st.columns([0.18, 0.56, 0.26])
    with left:
        st.markdown(f"<div class='left-nav'><b>{st.session_state.sp_site}</b><div class='nav-item active'>ホーム</div><div class='nav-item'>ドキュメント</div><div class='nav-item'>ニュース</div><div class='nav-item'>サイトの内容</div></div>", unsafe_allow_html=True)
    with main:
        st.markdown("<div class='file-list'><div class='file-row header'><div></div><div>名前</div><div>更新日時</div><div>更新者</div><div>状態</div></div>", unsafe_allow_html=True)
        for f in st.session_state.sp_files:
            cols = st.columns([0.05, 0.43, 0.16, 0.18, 0.18])
            with cols[0]:
                if st.button("□", key=f"sp_{f['name']}"):
                    st.session_state.sp_activity = f"{f['name']} を開きました。"
                    mark_done("SharePoint", "open")
                    st.rerun()
            with cols[1]:
                st.write(f["name"])
            with cols[2]:
                st.write(f["modified"])
            with cols[3]:
                st.write(f["user"])
            with cols[4]:
                st.write(f["status"])
        st.markdown("</div>", unsafe_allow_html=True)
    with right:
        news_html = "".join(f"<li>{n}</li>" for n in st.session_state.sp_news[:4])
        st.markdown(f"<div class='detail-pane'><h3>サイト情報</h3><p><b>権限</b></p><p>{st.session_state.sp_permission}</p><p><b>最近のニュース</b></p><ul>{news_html}</ul><div class='activity'>{st.session_state.sp_activity}</div></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


def copilot_answer(prompt: str) -> str:
    text = prompt.strip()
    if not text:
        return "プロンプトを入力すると、ここに回答が表示されます。"
    if "要約" in text:
        return "要約案:\n1. 旧Officeでは個人PCや共有フォルダーへの保存が中心でした。\n2. M365ではOneDriveとSharePointを使い分けます。\n3. Teamsから関係者へ共有し、共同編集につなげます。"
    if "文章" in text or "作成" in text:
        return "文章案:\nMicrosoft 365移行後は、個人作業はOneDrive、組織共有はSharePointを利用します。関係者への連絡や共同編集はTeamsから行い、最新版のファイルを安全に共有してください。"
    if "次" in text or "操作" in text:
        return "次の操作提案:\n- 保存先をOneDriveまたはSharePointに決める\n- 共有範囲を指定したユーザーに限定する\n- Teamsで@メンションを付けて確認依頼を送る"
    return f"入力内容をもとにした提案:\n{text}\n\nこの内容を、研修用にわかりやすく整理できます。必要に応じて、要約・文章作成・次の操作提案を指定してください。"


def copilot_page() -> None:
    tasks = [("prompt", "プロンプトを入力"), ("summary", "要約を作成"), ("draft", "文章を整える"), ("next", "次の操作を提案")]
    titlebar("Copilot", "基本操作", "blue")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("要約プロンプト", use_container_width=True):
            st.session_state.copilot_prompt = "研修資料.docxの内容を3行で要約してください。"
            mark_done("Copilot", "summary")
    with c2:
        if st.button("文章作成プロンプト", use_container_width=True):
            st.session_state.copilot_prompt = "M365移行後のファイル保存ルールを職員向けに説明する文章を作成してください。"
            mark_done("Copilot", "draft")
    with c3:
        if st.button("次の操作プロンプト", use_container_width=True):
            st.session_state.copilot_prompt = "この後に行うべき次の操作を提案してください。"
            mark_done("Copilot", "next")
    training_line("Copilot", tasks)
    st.markdown("<div class='workbench'>", unsafe_allow_html=True)
    left, main = st.columns([0.25, 0.75])
    with left:
        st.markdown("<div class='detail-pane'><h3>参照データ</h3><p>研修資料.docx</p><p>売上一覧.xlsx</p><p>共有フォルダー</p><p class='small-muted'>実際のCopilotでは、権限のあるファイルや会議情報などを参照して回答します。</p></div>", unsafe_allow_html=True)
    with main:
        st.markdown("<div class='card'><h3>プロンプト入力</h3></div>", unsafe_allow_html=True)
        st.session_state.copilot_prompt = st.text_area("Copilotに依頼する内容", value=st.session_state.copilot_prompt, height=130)
        if st.session_state.copilot_prompt.strip():
            mark_done("Copilot", "prompt")
        if st.button("生成", type="primary", use_container_width=True):
            st.session_state.copilot_answer = copilot_answer(st.session_state.copilot_prompt)
        st.markdown(f"<div class='copilot-answer'><b>Copilotの回答</b><br><br>{st.session_state.copilot_answer.replace(chr(10), '<br>')}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


def main() -> None:
    init_state()
    service_selector()
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
    else:
        copilot_page()
    service_links()


if __name__ == "__main__":
    main()
