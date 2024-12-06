import streamlit as st
import pandas as pd

home_page = st.Page("Home.py")

claude_agents_page = st.Page(
    "pages/ClaudeAgents.py", 
    title="Claude", 
    url_path="claude-agents"
    )

open_ai_agents_page = st.Page(
    "pages/OpenAiAgents.py", 
    title="Open AI", 
    url_path="open-ai-agents"
    )

page = st.navigation(
    {
        "Home": [home_page],
        "Agents": [claude_agents_page, open_ai_agents_page]
    },
    position="hidden"
)

container = st.container
with st.sidebar:
    st.text("AI Agents")
    st.page_link(page=claude_agents_page, label="Claude")
    st.page_link(page=open_ai_agents_page, label="Open AI")

page.run()
