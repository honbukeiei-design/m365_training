import streamlit as st
from modules.copilot import ask_copilot
from modules.license import has_feature
from modules.state import init_state, set_progress
from modules.tutorial import show_steps
from modules.ui import load_css, task_card

st.set_page_config(page_title="Copilot Training", page_icon="🤖", layout="wide")
load_css(); init_state()

st.title("🤖 Copilot：指示の書き方と業務支援")
st.caption("研修用AI支援として、要約・文面作成・会議準備を体験します。APIキー未設定時はモック応答です。")

if not has_feature(st.session_state.license, "copilot_ready"):
    st.warning("現在のライセンス設定ではCopilot導入前提が制限されています。ここでは研修用デモとして体験します。")

left, right = st.columns([1.6, 1])
with left:
    st.markdown("<div class='copilot-panel'>", unsafe_allow_html=True)
    mode = st.selectbox("目的", ["文章を要約", "メール文を作成", "会議の論点を整理", "Teams投稿を整える"])
    context = st.text_area(
        "材料・背景",
        "M365移行研修の案内を職員に送ります。OneDriveとTeamsの基本操作を学ぶ内容です。参加を促す文面にしてください。",
        height=150,
    )
    prompt = f"目的: {mode}\n背景: {context}\n出力条件: 箇条書きまたは短い文章で、職員向けにわかりやすく。"
    if st.button("生成", type="primary"):
        with st.spinner("生成中..."):
            result = ask_copilot(prompt)
        st.session_state["last_copilot_result"] = result
        set_progress("Copilot", 70)
    st.markdown("</div>", unsafe_allow_html=True)

    if "last_copilot_result" in st.session_state:
        st.markdown("### 生成結果")
        st.markdown(f"<div class='copilot-answer'>{st.session_state['last_copilot_result']}</div>", unsafe_allow_html=True)
with right:
    st.markdown("### よい指示の型")
    st.markdown("""
    <div class="m365-card">
      <strong>1. 目的</strong><br><span class="m365-muted">何を作りたいか</span><br><br>
      <strong>2. 背景</strong><br><span class="m365-muted">誰向け・何のためか</span><br><br>
      <strong>3. 条件</strong><br><span class="m365-muted">文字数、形式、トーン</span><br><br>
      <strong>4. 確認</strong><br><span class="m365-muted">機密情報を入れすぎない</span>
    </div>
    """, unsafe_allow_html=True)
    task_card("課題1", "目的・背景・条件を含めて指示を書く", bool(context))
    task_card("課題2", "生成結果をそのまま送らず、人が確認する", "last_copilot_result" in st.session_state)

show_steps("Copilot", [
    "① 目的、背景、条件を分けて入力すると、期待する出力に近づきます。",
    "② 個人情報・機密情報・未公開情報は入力しすぎないようにします。",
    "③ 生成結果は下書きとして扱い、必ず人が確認してから送信します。",
])
