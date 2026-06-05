import html
import pandas as pd
import streamlit as st
from modules.ui import load_css, titlebar, app_header, close_shell, service_launcher, training_strip, ribbon_tabs, mark_task_done, reset_service

SERVICE = "Excel"
TASKS = [
    {"id": "cell_edit", "label": "セルを選び、値を変更して表に反映してください。"},
    {"id": "format", "label": "ホームで書式を選び、選択セルに反映してください。"},
    {"id": "calc", "label": "数式で集計方法を選び、合計などを計算してください。"},
    {"id": "chart", "label": "挿入でグラフ種類を選び、グラフを表示してください。"},
    {"id": "view", "label": "表示倍率を選び、表の表示に反映してください。"},
    {"id": "protect", "label": "校閲で保護設定を選び、シート状態に反映してください。"},
]
TABS = ["ホーム", "挿入", "ページ レイアウト", "数式", "データ", "校閲", "表示"]

def init():
    st.session_state.setdefault("Excel_rows", [
        {"項目": "コピー用紙", "数量": 12, "単価": 500},
        {"項目": "封筒", "数量": 8, "単価": 250},
        {"項目": "ファイル", "数量": 6, "単価": 700},
    ])
    st.session_state.setdefault("Excel_selected", "B2")
    st.session_state.setdefault("Excel_cell_format", "標準")
    st.session_state.setdefault("Excel_calc", "未計算")
    st.session_state.setdefault("Excel_chart", "未挿入")
    st.session_state.setdefault("Excel_zoom", "100%")
    st.session_state.setdefault("Excel_protect", "未保護")

st.set_page_config(page_title="Excel 体験", page_icon="📊", layout="wide")
load_css(); titlebar(); service_launcher(SERVICE); training_strip(SERVICE, TASKS); init()
app_header("Excel", "セル操作、書式、集計、グラフ、保護を順番に体験します。")
active = ribbon_tabs(SERVICE, TABS)
st.markdown("<div class='ribbon'>", unsafe_allow_html=True)

if active == "ホーム":
    st.markdown("#### 書式")
    cell = st.selectbox("対象セル", ["A2", "B2", "C2", "D2", "A3", "B3", "C3", "D3"], index=1)
    fmt = st.radio("書式", ["太字", "下線", "塗りつぶし", "罫線"], horizontal=True)
    if st.button("選択セルに書式を適用", use_container_width=True):
        st.session_state.Excel_selected = cell
        st.session_state.Excel_cell_format = fmt
        mark_task_done(SERVICE, "format")
elif active == "挿入":
    st.markdown("#### グラフ")
    chart = st.radio("グラフ種類", ["縦棒グラフ", "折れ線グラフ"], horizontal=True)
    if st.button("グラフを挿入", use_container_width=True):
        st.session_state.Excel_chart = chart
        mark_task_done(SERVICE, "chart")
elif active == "ページ レイアウト":
    st.markdown("#### 印刷向き")
    st.radio("印刷向き", ["縦", "横"], horizontal=True)
    st.caption("ここでは画面右下の状態表示のみを更新します。")
elif active == "数式":
    st.markdown("#### 集計")
    calc = st.selectbox("集計方法", ["合計", "平均", "最大値"])
    if st.button("集計を計算", use_container_width=True):
        values = [r["数量"] * r["単価"] for r in st.session_state.Excel_rows]
        if calc == "合計":
            result = sum(values)
        elif calc == "平均":
            result = round(sum(values) / len(values), 1)
        else:
            result = max(values)
        st.session_state.Excel_calc = f"{calc}: {result:,} 円"
        mark_task_done(SERVICE, "calc")
elif active == "データ":
    st.markdown("#### 並べ替え")
    if st.button("金額の大きい順に並べ替え", use_container_width=True):
        st.session_state.Excel_rows = sorted(st.session_state.Excel_rows, key=lambda x: x["数量"] * x["単価"], reverse=True)
elif active == "校閲":
    st.markdown("#### シート保護")
    protect = st.radio("保護設定", ["未保護", "編集を制限", "読み取り専用"], horizontal=True)
    if st.button("保護設定を適用", use_container_width=True):
        st.session_state.Excel_protect = protect
        mark_task_done(SERVICE, "protect")
elif active == "表示":
    st.markdown("#### 表示倍率")
    zoom = st.radio("ズーム", ["75%", "100%", "125%"], horizontal=True)
    if st.button("表示倍率を適用", use_container_width=True):
        st.session_state.Excel_zoom = zoom
        mark_task_done(SERVICE, "view")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("#### セル編集")
edited = st.data_editor(pd.DataFrame(st.session_state.Excel_rows), num_rows="dynamic", use_container_width=True, key="Excel_editor")
if st.button("セル編集を表に反映", use_container_width=True):
    records = edited.fillna(0).to_dict("records")
    for r in records:
        r["数量"] = int(r.get("数量", 0)); r["単価"] = int(r.get("単価", 0))
    st.session_state.Excel_rows = records
    mark_task_done(SERVICE, "cell_edit")

zoom_scale = {"75%":"0.85", "100%":"1", "125%":"1.12"}[st.session_state.Excel_zoom]
rows = st.session_state.Excel_rows
fmt = st.session_state.Excel_cell_format
selected = st.session_state.Excel_selected
cell_class = {"太字":" excel-bold", "下線":" excel-under", "塗りつぶし":" excel-fill", "罫線":" excel-cell-selected"}.get(fmt, "")

def cell(value, address):
    cls = "excel-cell-selected" if address == selected else ""
    if address == selected:
        cls += cell_class
    return f"<td class='{cls}'>{html.escape(str(value))}</td>"

body = ""
for i, r in enumerate(rows, start=2):
    amount = int(r["数量"]) * int(r["単価"])
    body += "<tr>" + cell(r["項目"], f"A{i}") + cell(r["数量"], f"B{i}") + cell(r["単価"], f"C{i}") + cell(f"{amount:,}", f"D{i}") + "</tr>"
chart_html = ""
if st.session_state.Excel_chart != "未挿入":
    max_amount = max([int(r["数量"]) * int(r["単価"]) for r in rows] + [1])
    bars = "".join(f"<div title='{html.escape(str(r['項目']))}' class='chart-bar' style='height:{max(10, int((int(r['数量'])*int(r['単価']))/max_amount*150))}px'></div>" for r in rows)
    chart_html = f"<h4>{html.escape(st.session_state.Excel_chart)}</h4><div class='chart-bars'>{bars}</div>"

st.markdown(
    f"""
    <div class='page-stage'>
      <div style='transform:scale({zoom_scale});transform-origin:top left'>
        <div class='excel-grid'>
          <table class='excel-table'>
            <tr><th>項目</th><th>数量</th><th>単価</th><th>金額</th></tr>
            {body}
            <tr><td colspan='3'><strong>集計セル</strong></td><td><strong>{html.escape(st.session_state.Excel_calc)}</strong></td></tr>
          </table>
        </div>
        {chart_html}
      </div>
    </div>
    <div class='footer-status'><span>選択セル {html.escape(selected)} / 書式 {html.escape(fmt)}</span><span>表示 {html.escape(st.session_state.Excel_zoom)} ・ 保護 {html.escape(st.session_state.Excel_protect)}</span></div>
    """,
    unsafe_allow_html=True,
)

if st.button("Excelの体験をリセット"):
    reset_service(SERVICE)
close_shell()
