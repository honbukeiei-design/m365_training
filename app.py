import streamlit as st
from modules.common import init_page, SERVICE_URLS

init_page("Microsoft 365 体験トレーニング")

st.markdown("""
<div class='app-hero'>
  <h1>Microsoft 365 体験トレーニング</h1>
  <div>上部で体験するサービスを選び、疑似画面で操作した後、下部から実サービスを開いて同じ操作を試します。</div>
</div>
""", unsafe_allow_html=True)

st.subheader("体験するサービスを選択")
services = [
    ("Word", "文書作成、リボン操作、保存、共有"),
    ("Excel", "セル編集、数式、合計、表、グラフ"),
    ("Teams", "チャット、@メンション、ファイル共有、会議"),
    ("OneDrive", "保存、共有リンク、同期、復元"),
    ("SharePoint", "サイト、ドキュメント、権限、ニュース"),
    ("Copilot", "依頼文、要約、文章作成、次の操作提案"),
]
cols = st.columns(3)
for idx, (name, desc) in enumerate(services):
    with cols[idx % 3]:
        st.markdown(f"<div class='service-card'><h3>{name}</h3><p>{desc}</p></div>", unsafe_allow_html=True)
        if st.button("体験する", key=f"go_{name}", use_container_width=True):
            page_map = {
                "Word": "pages/1_Word.py",
                "Excel": "pages/2_Excel.py",
                "Teams": "pages/3_Teams.py",
                "OneDrive": "pages/4_OneDrive.py",
                "SharePoint": "pages/5_SharePoint.py",
                "Copilot": "pages/6_Copilot.py",
            }
            st.switch_page(page_map[name])

st.divider()
st.subheader("実サービス")
link_cols = st.columns(6)
for c, (name, _) in zip(link_cols, services):
    with c:
        st.link_button("開く", SERVICE_URLS[name], use_container_width=True)
        st.caption(name)
