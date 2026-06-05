import re
import streamlit as st
from modules.common import init_page, training_banner, complete_step

init_page("Excel 体験")
steps = [
    "セルの値を編集してください。",
    "数式バーに =SUM(B2:B4) を入力して合計を計算してください。",
    "ホームで罫線または塗りつぶしを選び、表に反映してください。",
    "挿入でグラフの種類を選び、グラフを表示してください。",
]
idx, done = training_banner("Excel", steps)

st.session_state.setdefault("excel_tab", "ホーム")
st.session_state.setdefault("excel_values", {"B2":120,"B3":180,"B4":260,"C2":80,"C3":120,"C4":150})
st.session_state.setdefault("excel_formula", "=SUM(B2:B4)")
st.session_state.setdefault("excel_result", "")
st.session_state.setdefault("excel_border", False)
st.session_state.setdefault("excel_fill", False)
st.session_state.setdefault("excel_chart", "なし")
st.session_state.setdefault("excel_protect", "未保護")

st.markdown("<div class='excel-shell'><div class='excel-titlebar'><span>Excel</span><span>研修集計.xlsx</span></div></div>", unsafe_allow_html=True)
tabs = ["ファイル", "ホーム", "挿入", "ページ レイアウト", "数式", "データ", "校閲", "表示"]
cols = st.columns(len(tabs))
for col, t in zip(cols, tabs):
    with col:
        if st.button(t, key=f"excel_tab_{t}", type="primary" if st.session_state.excel_tab == t else "secondary", use_container_width=True):
            st.session_state.excel_tab = t
            st.rerun()

def calc_formula(formula: str):
    formula = formula.strip().upper()
    m = re.fullmatch(r"=(SUM|AVERAGE|MAX|MIN)\((B2|B3|B4|C2|C3|C4):(B2|B3|B4|C2|C3|C4)\)", formula)
    if not m:
        return "対応例：=SUM(B2:B4)"
    func, start, end = m.groups()
    col = start[0]
    srow, erow = int(start[1]), int(end[1])
    vals = [st.session_state.excel_values.get(f"{col}{r}",0) for r in range(min(srow,erow), max(srow,erow)+1)]
    if func == "SUM": return sum(vals)
    if func == "AVERAGE": return round(sum(vals)/len(vals), 1)
    if func == "MAX": return max(vals)
    if func == "MIN": return min(vals)

if st.session_state.excel_tab == "ホーム":
    c1, c2, c3 = st.columns(3)
    with c1: border = st.checkbox("罫線", value=st.session_state.excel_border)
    with c2: fill = st.checkbox("塗りつぶし", value=st.session_state.excel_fill)
    with c3:
        if st.button("表に反映", type="primary"):
            st.session_state.excel_border = border
            st.session_state.excel_fill = fill
            complete_step("Excel", 2)
            st.rerun()
elif st.session_state.excel_tab == "挿入":
    chart = st.selectbox("グラフ", ["なし", "縦棒グラフ", "折れ線グラフ", "円グラフ"])
    if st.button("グラフを挿入", type="primary"):
        st.session_state.excel_chart = chart
        complete_step("Excel", 3)
        st.rerun()
elif st.session_state.excel_tab == "数式":
    formula = st.text_input("数式バー", value=st.session_state.excel_formula)
    if st.button("計算", type="primary"):
        st.session_state.excel_formula = formula
        st.session_state.excel_result = calc_formula(formula)
        complete_step("Excel", 1)
        st.rerun()
elif st.session_state.excel_tab == "校閲":
    if st.button("シートを保護"):
        st.session_state.excel_protect = "保護中"
        st.rerun()
else:
    st.caption("このタブでは表示・データ確認の体験を行います。")

st.markdown("<div class='workspace'>", unsafe_allow_html=True)
c1, c2, c3 = st.columns([1,1,2])
with c1:
    st.session_state.excel_values["B2"] = st.number_input("B2", value=int(st.session_state.excel_values["B2"]), step=10)
with c2:
    st.session_state.excel_values["B3"] = st.number_input("B3", value=int(st.session_state.excel_values["B3"]), step=10)
with c3:
    if st.button("セル編集を反映", type="primary"):
        complete_step("Excel", 0)
        st.rerun()

border_css = "border:2px solid #107c41;" if st.session_state.excel_border else ""
fill_css = "background:#eaf6ef;" if st.session_state.excel_fill else ""
B2=st.session_state.excel_values['B2']; B3=st.session_state.excel_values['B3']; B4=st.session_state.excel_values['B4']
C2=st.session_state.excel_values['C2']; C3=st.session_state.excel_values['C3']; C4=st.session_state.excel_values['C4']
result = st.session_state.excel_result
st.markdown(f"""
<div class='formula-bar'><strong>fx</strong><span>{st.session_state.excel_formula}</span><strong>結果：</strong><span>{result}</span></div>
<table class='excel-grid' style='{border_css}'>
<tr><th></th><th>A</th><th>B</th><th>C</th><th>D</th></tr>
<tr><th>1</th><td style='{fill_css}'>月</td><td style='{fill_css}'>研修受講</td><td style='{fill_css}'>完了</td><td style='{fill_css}'>合計</td></tr>
<tr><th>2</th><td>4月</td><td class='selected'>{B2}</td><td>{C2}</td><td rowspan='3'>{result}</td></tr>
<tr><th>3</th><td>5月</td><td>{B3}</td><td>{C3}</td></tr>
<tr><th>4</th><td>6月</td><td>{B4}</td><td>{C4}</td></tr>
</table>
""", unsafe_allow_html=True)
if st.session_state.excel_chart != "なし":
    st.bar_chart({"研修受講":[B2,B3,B4]}, height=260)
st.markdown("</div>", unsafe_allow_html=True)
st.markdown(f"<div class='statusbar'><span>準備完了</span><span>{st.session_state.excel_protect}</span></div>", unsafe_allow_html=True)
if st.button("トップへ戻る"):
    st.switch_page("app.py")
