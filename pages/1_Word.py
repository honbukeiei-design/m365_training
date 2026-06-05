import streamlit as st
from modules.common import init_page, training_banner, complete_step, safe

init_page("Word 体験")
steps = [
    "ホームで文字書式を選び、文書に反映してください。",
    "挿入で表のサイズを選び、白紙ページに表を入れてください。",
    "校閲でコメントを追加してください。",
    "共有で共有範囲を選び、共有状態を反映してください。",
    "保存先を選び、クラウド保存してください。",
]
step_idx, done = training_banner("Word", steps)

st.session_state.setdefault("word_tab", "ホーム")
st.session_state.setdefault("word_text", "M365移行後のファイル保存ルール\n旧Officeでは個人PCや共有フォルダーに保存していました。\nMicrosoft 365移行後は、OneDriveとSharePointを使い分け、Teamsから関係者へ共有します。")
st.session_state.setdefault("word_bold", False)
st.session_state.setdefault("word_underline", False)
st.session_state.setdefault("word_bullets", False)
st.session_state.setdefault("word_style", "標準")
st.session_state.setdefault("word_table", None)
st.session_state.setdefault("word_comment", "")
st.session_state.setdefault("word_shared", "未共有")
st.session_state.setdefault("word_saved", "未保存")
st.session_state.setdefault("word_margin", "標準余白")
st.session_state.setdefault("word_zoom", "100%")
st.session_state.setdefault("word_bg", "白")

st.markdown("""
<div class='m365-shell'>
  <div class='m365-titlebar'><span>Word</span><span class='file'>保存ルール.docx</span></div>
</div>
""", unsafe_allow_html=True)

tabs = ["ファイル", "ホーム", "挿入", "レイアウト", "デザイン", "校閲", "表示", "差し込み文書"]
cols = st.columns(len(tabs))
for col, t in zip(cols, tabs):
    with col:
        if st.button(t, key=f"word_tab_{t}", type="primary" if st.session_state.word_tab == t else "secondary", use_container_width=True):
            st.session_state.word_tab = t
            st.rerun()

st.markdown("<div class='m365-ribbon'>", unsafe_allow_html=True)
tab = st.session_state.word_tab
if tab == "ホーム":
    c1, c2, c3, c4 = st.columns([1,1,1,2])
    with c1:
        bold = st.checkbox("太字", value=st.session_state.word_bold)
    with c2:
        underline = st.checkbox("下線", value=st.session_state.word_underline)
    with c3:
        bullets = st.checkbox("箇条書き", value=st.session_state.word_bullets)
    with c4:
        style = st.selectbox("スタイル", ["標準", "見出し", "報告書", "メモ"], index=["標準","見出し","報告書","メモ"].index(st.session_state.word_style))
    if st.button("文書に適用", type="primary"):
        st.session_state.word_bold = bold
        st.session_state.word_underline = underline
        st.session_state.word_bullets = bullets
        st.session_state.word_style = style
        complete_step("Word", 0)
        st.rerun()
elif tab == "挿入":
    c1, c2, c3 = st.columns([1,1,2])
    with c1:
        rows = st.number_input("行", min_value=2, max_value=6, value=3)
    with c2:
        cols_n = st.number_input("列", min_value=2, max_value=5, value=3)
    with c3:
        st.caption("表サイズを選び、挿入すると文書下部に反映されます。")
    if st.button("表を挿入", type="primary"):
        st.session_state.word_table = (int(rows), int(cols_n))
        complete_step("Word", 1)
        st.rerun()
elif tab == "レイアウト":
    c1, c2 = st.columns(2)
    with c1:
        margin = st.radio("余白", ["標準余白", "狭い余白", "広い余白"], horizontal=True)
    with c2:
        orientation = st.radio("印刷の向き", ["縦", "横"], horizontal=True)
    if st.button("レイアウトを反映", type="primary"):
        st.session_state.word_margin = margin
        st.session_state.word_orientation = orientation
        st.rerun()
elif tab == "デザイン":
    c1, c2 = st.columns(2)
    with c1:
        bg = st.radio("ページ背景", ["白", "薄い青", "薄い黄"], horizontal=True)
    with c2:
        border = st.checkbox("ページ罫線を表示", value=st.session_state.get("word_border", False))
    if st.button("デザインを反映", type="primary"):
        st.session_state.word_bg = bg
        st.session_state.word_border = border
        st.rerun()
elif tab == "校閲":
    comment = st.text_input("コメント", value=st.session_state.word_comment or "保存先のルールを全員で統一しましょう。")
    if st.button("コメントを追加", type="primary"):
        st.session_state.word_comment = comment
        complete_step("Word", 2)
        st.rerun()
elif tab == "表示":
    zoom = st.radio("ズーム", ["80%", "100%", "120%"], horizontal=True, index=["80%","100%","120%"].index(st.session_state.word_zoom))
    if st.button("表示倍率を変更", type="primary"):
        st.session_state.word_zoom = zoom
        st.rerun()
elif tab == "差し込み文書":
    field = st.selectbox("差し込みフィールド", ["{氏名}", "{部署}", "{日付}"])
    if st.button("本文に差し込みフィールドを挿入", type="primary"):
        st.session_state.word_text += f"\n{field} 様"
        st.rerun()
else:
    c1, c2 = st.columns(2)
    with c1:
        place = st.selectbox("保存先", ["OneDrive - 個人", "SharePoint - 部署サイト", "Teams - チーム"])
        if st.button("クラウドに保存", type="primary"):
            st.session_state.word_saved = f"保存済み：{place}"
            complete_step("Word", 4)
            st.rerun()
    with c2:
        share_to = st.selectbox("共有範囲", ["指定したユーザー", "組織内のリンク", "自分のみ"])
        if st.button("共有を反映", type="primary"):
            st.session_state.word_shared = share_to
            complete_step("Word", 3)
            st.rerun()
st.markdown("</div>", unsafe_allow_html=True)

# document editing surface
bg = {"白":"#ffffff", "薄い青":"#f5f9ff", "薄い黄":"#fffdf0"}[st.session_state.word_bg]
border_style = "2px solid #185abd" if st.session_state.get("word_border", False) else "1px solid #d9dee8"
page_class = "word-page compact" if st.session_state.word_margin == "狭い余白" else "word-page"
text_class = "word-preview"
if st.session_state.word_bold: text_class += " bold"
if st.session_state.word_underline: text_class += " underline"
if st.session_state.word_bullets: text_class += " bullets"
if st.session_state.word_style == "報告書": text_class += " report"
if st.session_state.word_style == "メモ": text_class += " memo"
zoom = st.session_state.word_zoom

st.markdown("<div class='workspace'>", unsafe_allow_html=True)
st.session_state.word_text = st.text_area("白紙ページに直接入力", value=st.session_state.word_text, height=170, label_visibility="collapsed")
lines = [safe(x) for x in st.session_state.word_text.splitlines()]
if st.session_state.word_bullets:
    body = "".join(f"<div>{line}</div>" for line in lines if line.strip())
else:
    title = lines[0] if lines else ""
    rest = "<br>".join(lines[1:]) if len(lines) > 1 else ""
    if st.session_state.word_style in ["報告書", "メモ", "見出し"]:
        body = f"<h2>{title}</h2><div>{rest}</div>"
    else:
        body = "<br>".join(lines)

table_html = ""
if st.session_state.word_table:
    r, c = st.session_state.word_table
    rows_html = []
    for i in range(r):
        cells = "".join(f"<td>{'見出し' if i==0 else '項目'} {j+1}</td>" for j in range(c))
        rows_html.append(f"<tr>{cells}</tr>")
    table_html = "<table class='word-table'>" + "".join(rows_html) + "</table>"
comment_html = f"<div class='word-comment'>コメント：{safe(st.session_state.word_comment)}</div>" if st.session_state.word_comment else ""
st.markdown(f"""
<div class='{page_class}' style='background:{bg};border:{border_style};transform:scale({int(zoom.strip('%'))/100});transform-origin:top center;'>
  <div class='{text_class}'>{body}</div>
  {table_html}
  {comment_html}
</div>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
st.markdown(f"<div class='statusbar'><span>ページ 1/1</span><span>{st.session_state.word_saved} ・ 共有状態：{st.session_state.word_shared} ・ 表示 {st.session_state.word_zoom}</span></div>", unsafe_allow_html=True)

if st.button("トップへ戻る"):
    st.switch_page("app.py")
