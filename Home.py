import streamlit as st

st.title("Home Page")

if st.button("Use Claude"):
    st.switch_page("pages/ClaudeAgents.py")