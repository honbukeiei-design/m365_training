import streamlit as st
from modules.ui import load_css, top_bar, page_title, service_selector_cards, service_links_bottom

st.set_page_config(page_title="Microsoft 365 体験トレーニング", layout="wide")
load_css()
top_bar()
page_title("Microsoft 365 体験トレーニング", "上部から体験するサービスを選択し、操作完了後に実サービスへ進みます。")

st.subheader("体験するサービスを選択")
service_selector_cards()

service_links_bottom()
