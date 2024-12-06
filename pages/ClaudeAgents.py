import streamlit as st
from anthropic import Anthropic
from dotenv import dotenv_values

config = dotenv_values("./.env")

client = Anthropic(
    api_key=config.get("ANTHROPIC_API_KEY")
)

message = client.messages.create(
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Hello, Claude"
        }
    ],
    model="claude-3-opus-20240229"
)

st.title(message)