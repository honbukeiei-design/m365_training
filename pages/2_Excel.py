import streamlit as st
import pandas as pd
from modules.state import init_state, set_progress
from modules.tutorial import show_steps
from modules.ui import load_css, ribbon, task_card

st.set_page_config(page_title="Excel Training", page_icon="📊", layout="wide")
load_css(); init_state()

st.title("📊 Excel：表計算と共同編集")
st.caption("セル、数式、簡単な集計、共同編集コメントを体験します。")
ribbon("ホーム", ["ホーム", "挿入", "数式", "データ", "校閲", "表示", "自動化"])

data = pd.DataFrame({
    "部門": ["総務", "医事", "看護", "薬剤"],
    "4月": [120, 180, 240, 90],
    "5月": [135, 172, 260, 95],
    "6月": [128, 190, 252, 105],
})
data["合計"] = data[["4月", "5月", "6月"]].sum(axis=1)

a, b = st.columns([2, 1])
with a:
    st.markdown("### ワークシート")
    html = "<table class='excel-grid'><tr><th></th><th>A</th><th>B</th><th>C</th><th>D</th><th>E</th></tr>"
    headers = ["部門", "4月", "5月", "6月", "合計"]
    html += "<tr><th>1</th>" + "".join(f"<th>{h}</th>" for h in headers) + "</tr>"
    for idx, row in data.iterrows():
        html += f"<tr><th>{idx+2}</th>"
        for col in headers:
            cls = " class='cell-active'" if col == "合計" and idx == 0 else ""
            html += f"<td{cls}>{row[col]}</td>"
        html += "</tr>"
    html += "</table>"
    st.markdown(html, unsafe_allow_html=True)
    st.caption("選択セル E2: =SUM(B2:D2)")
with b:
    st.markdown("### 演習")
    total = int(data["合計"].sum())
    answer = st.number_input("全体合計はいくらですか？", min_value=0, step=1)
    if st.button("チェック", type="primary"):
        if answer == total:
            set_progress("Excel", 70)
            st.success("正解です。各部門の3か月合計をさらに集計できています。")
        else:
            st.error(f"惜しいです。ヒント：合計列の合計は {total} です。")
    comment = st.text_input("共同編集コメント", "6月の数値を確認してください")
    task_card("課題1", "合計列の意味を確認する", True)
    task_card("課題2", "コメント欄に確認依頼を書く", bool(comment))

show_steps("Excel", [
    "① 表の行・列・セル参照を確認します。",
    "② 合計列は SUM 関数で月別数値を集計しています。",
    "③ 共同編集ではコメントで確認依頼を残し、Teams通知と組み合わせます。",
])
