import streamlit as st
from modules.license import has_feature
from modules.state import init_state, set_progress
from modules.tutorial import show_steps
from modules.ui import load_css, ribbon, task_card

st.set_page_config(page_title="Word Training", page_icon="📄", layout="wide")
load_css(); init_state()

license_type = st.session_state.get("license")
st.title("📄 Word：文書作成とクラウド保存")
st.caption("リボン、文書編集、OneDrive保存、共有までを一連の流れで練習します。")

disabled_tabs = [] if has_feature(license_type, "desktop") else ["デザイン", "差し込み文書"]
ribbon("ホーム", ["ホーム", "挿入", "レイアウト", "デザイン", "校閲", "表示", "差し込み文書"], disabled_tabs)
st.markdown("""
<div class="m365-card">
  <span class="ribbon-tool">太字</span><span class="ribbon-tool">下線</span><span class="ribbon-tool">箇条書き</span>
  <span class="ribbon-tool">スタイル</span><span class="ribbon-tool">コメント</span><span class="ribbon-tool">共有</span>
</div>
""", unsafe_allow_html=True)

left, right = st.columns([2.2, 1])
with left:
    doc_title = st.text_input("文書タイトル", "M365移行後のファイル保存ルール")
    body = st.text_area(
        "本文編集",
        "旧Officeでは個人PCや共有フォルダーに保存していました。\nMicrosoft 365移行後は、OneDriveとSharePointを使い分け、Teamsから関係者へ共有します。",
        height=160,
    )
    st.markdown(
        f"""
        <div class="doc-surface">
          <div class="doc-title">{doc_title}</div>
          {''.join(f'<div class="doc-paragraph">{line}</div>' for line in body.splitlines() if line.strip())}
        </div>
        """,
        unsafe_allow_html=True,
    )
with right:
    st.markdown("### ファイル状態")
    st.markdown("<span class='badge badge-amber'>未保存の変更</span>", unsafe_allow_html=True)
    location = st.selectbox("保存先", ["OneDrive - 個人", "SharePoint - 部門サイト", "このPC（非推奨）"])
    share = st.radio("共有範囲", ["自分のみ", "指定したユーザー", "組織内のリンク"], index=1)
    if st.button("💾 保存して共有設定を確認", type="primary"):
        set_progress("Word", 60)
        st.success(f"{location} に保存し、共有範囲を「{share}」として設定しました。")
    task_card("課題1", "文書タイトルを変更し、本文を1行追加する", bool(doc_title and len(body) > 50))
    task_card("課題2", "保存先にOneDriveまたはSharePointを選ぶ", location != "このPC（非推奨）")

show_steps("Word", [
    "① 文書タイトルと本文を編集します。旧Officeとの違いは、保存先がクラウド前提になる点です。",
    "② 保存先をOneDriveまたはSharePointから選びます。個人作業はOneDrive、チーム共有はSharePointが基本です。",
    "③ 共有範囲を確認します。リンクを広げすぎると情報漏えいにつながるため、指定ユーザー共有を優先します。",
])
