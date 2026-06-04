import streamlit as st

REAL_URLS = {
    "Word": "https://www.microsoft365.com/launch/word",
    "Excel": "https://www.microsoft365.com/launch/excel",
    "Teams": "https://teams.microsoft.com/",
    "OneDrive": "https://onedrive.live.com/",
    "SharePoint": "https://www.microsoft365.com/launch/sharepoint",
    "Copilot": "https://copilot.microsoft.com/",
}

def complete_card(app_name: str, description: str = "体験完了です。次は実際のサービスで同じ操作を試してみましょう。"):
    url = REAL_URLS.get(app_name, "https://www.microsoft365.com/")
    st.markdown(f"""
    <div class="complete-card">
      <div>
        <div class="complete-kicker">実際に使用してみよう</div>
        <h3>{app_name} の公式画面を開く</h3>
        <p>{description}</p>
      </div>
      <a class="open-real" href="{url}" target="_blank" rel="noopener">実際のURLを開く</a>
    </div>
    """, unsafe_allow_html=True)

def page_header(icon: str, title: str, lead: str):
    st.markdown(f"""
    <div class="page-heading">
      <div class="app-icon">{icon}</div>
      <div>
        <h1>{title}</h1>
        <p>{lead}</p>
      </div>
    </div>
    """, unsafe_allow_html=True)
