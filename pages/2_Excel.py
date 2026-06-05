from __future__ import annotations
import re
import pandas as pd
import streamlit as st
from modules.ui import load_css, top_bar, page_title, training_bar, complete_task, reset, tabs, ribbon_start, ribbon_end

SERVICE="Excel"
TASKS=[
 {"id":"edit","label":"セルを選択して数値を入力してください。"},
 {"id":"formula","label":"数式バーに =SUM(B2:B4) を入力し、合計を計算してください。"},
 {"id":"format","label":"ホームで表示形式を選び、セルに反映してください。"},
 {"id":"chart","label":"挿入でグラフ種類を選び、グラフを表示してください。"},
 {"id":"protect","label":"校閲でシート保護を設定してください。"},
]
TABS=["ホーム","挿入","数式","データ","校閲","表示"]

st.set_page_config(page_title="Excel 体験", layout="wide")
load_css(); top_bar("Excel")
page_title("Excel", "セル編集、数式、グラフ、保護を表計算画面で体験します。")
training_bar(SERVICE,TASKS)

if "Excel_df" not in st.session_state:
    st.session_state.Excel_df = pd.DataFrame({"A":["項目","研修A","研修B","研修C","合計"],"B":["参加者",120,95,80,0],"C":["満足度",4.2,4.5,4.1,""],"D":["備考","初回","応用","確認",""]})
st.session_state.setdefault("Excel_selected", "B2")
st.session_state.setdefault("Excel_formula", "")
st.session_state.setdefault("Excel_format", "標準")
st.session_state.setdefault("Excel_chart", "")
st.session_state.setdefault("Excel_protected", False)

active=tabs(SERVICE,TABS)
ribbon_start()
if active=="ホーム":
    fmt=st.radio("表示形式",["標準","桁区切り","太字","塗りつぶし"],horizontal=True)
    if st.button("表示形式を適用",use_container_width=True):
        st.session_state.Excel_format=fmt; complete_task(SERVICE,"format")
elif active=="挿入":
    chart=st.radio("グラフ",["縦棒グラフ","折れ線グラフ"],horizontal=True)
    if st.button("グラフを挿入",use_container_width=True):
        st.session_state.Excel_chart=chart; complete_task(SERVICE,"chart")
elif active=="数式":
    st.info("例：=SUM(B2:B4)、=AVERAGE(B2:B4)、=MAX(B2:B4)")
elif active=="データ":
    if st.button("参加者数で降順に並べ替え",use_container_width=True):
        df=st.session_state.Excel_df.copy()
        body=df.iloc[1:4].copy(); body["B"]=pd.to_numeric(body["B"])
        body=body.sort_values("B",ascending=False)
        st.session_state.Excel_df=pd.concat([df.iloc[[0]],body,df.iloc[[4]]],ignore_index=True)
elif active=="校閲":
    if st.button("シートを保護",use_container_width=True):
        st.session_state.Excel_protected=True; complete_task(SERVICE,"protect")
    if st.button("保護を解除",use_container_width=True):
        st.session_state.Excel_protected=False
elif active=="表示":
    st.radio("表示",["標準","改ページプレビュー"],horizontal=True)
ribbon_end()

c1,c2,c3,c4=st.columns([1,1,2,2])
cell=c1.selectbox("セル",["B2","B3","B4","B5","C2","C3","C4"],index=["B2","B3","B4","B5","C2","C3","C4"].index(st.session_state.Excel_selected))
st.session_state.Excel_selected=cell
value=c2.text_input("値","")
if c3.button("セルに入力",use_container_width=True):
    if st.session_state.Excel_protected:
        st.warning("シート保護中のため編集できません。")
    else:
        col=cell[0]; row=int(cell[1:])-1
        try: value=float(value) if "." in value else int(value)
        except Exception: pass
        st.session_state.Excel_df.loc[row,col]=value
        complete_task(SERVICE,"edit")
if c4.button("リセット",use_container_width=True): reset(SERVICE)

formula=st.text_input("数式バー",value=st.session_state.Excel_formula,placeholder="=SUM(B2:B4)")
if st.button("数式を計算",use_container_width=True):
    st.session_state.Excel_formula=formula
    m=re.match(r"=(SUM|AVERAGE|MAX|MIN)\((B[0-9]+):B([0-9]+)\)",formula.strip().upper())
    if not m:
        st.error("この体験では =SUM(B2:B4) 形式を入力してください。")
    else:
        fn,start,end=m.group(1),int(m.group(2)[1:])-1,int(m.group(3))-1
        vals=pd.to_numeric(st.session_state.Excel_df.loc[start:end,"B"],errors="coerce").dropna().tolist()
        result={"SUM":sum(vals),"AVERAGE":sum(vals)/len(vals),"MAX":max(vals),"MIN":min(vals)}[fn]
        st.session_state.Excel_df.loc[4,"B"]=round(result,2)
        complete_task(SERVICE,"formula")

df=st.session_state.Excel_df
html="<table><tr><th></th>"+"".join(f"<th>{c}</th>" for c in df.columns)+"</tr>"
for i,row in df.iterrows():
    html+=f"<tr><th>{i+1}</th>"
    for c in df.columns:
        selected="selected" if f"{c}{i+1}"==st.session_state.Excel_selected else ""
        val=row[c]
        if c=="B" and isinstance(val,(int,float)) and st.session_state.Excel_format=="桁区切り": val=f"{val:,}"
        html+=f"<td class='{selected}'>{val}</td>"
    html+="</tr>"
html+="</table>"
st.markdown(f"""
<div class='office-shell'>
 <div class='office-titlebar'><span>Excel</span><span class='file'>研修集計.xlsx</span></div>
 <div class='office-ribbon-strip'>ファイル　ホーム　挿入　数式　データ　校閲　表示</div>
 <div class='office-canvas'>
  <div class='formula-bar'><span class='fx'>fx</span><span>{st.session_state.Excel_formula or '数式を入力してください'}</span></div>
  <div class='excel-grid'>{html}</div>
  <div class='small'>状態：{'シート保護中' if st.session_state.Excel_protected else '編集可能'} ／ 書式：{st.session_state.Excel_format}</div>
 </div>
 <div class='statusbar'><span>シート1</span><span>合計セル B5</span></div>
</div>
""",unsafe_allow_html=True)
if st.session_state.Excel_chart:
    vals=[float(x) for x in pd.to_numeric(df.loc[1:3,"B"],errors="coerce")]
    maxv=max(vals) if vals else 1
    bars="".join(f"<div class='bar' style='height:{120*v/maxv}px'></div>" for v in vals)
    st.markdown(f"<div class='chart-box'>{bars}<span>{st.session_state.Excel_chart}</span></div>",unsafe_allow_html=True)
