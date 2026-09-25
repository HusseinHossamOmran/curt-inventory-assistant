import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
import streamlit as st
from app.phase1.assistant import answer_question
from app.database.repository import get_all_parts


st.set_page_config(page_title="CURT Inventory Assistant", layout="wide")

st.title("CURT Inventory Assistant")
st.caption("Phase 1 — Rule-based assistant")

# Sidebar: live inventory table
with st.sidebar:
    st.header("Current Inventory")
    parts = get_all_parts()
    st.dataframe(parts, width='stretch', hide_index=True)

# Chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
question = st.chat_input("Ask about the inventory...")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.write(question)

    answer = answer_question(question)

    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.write(answer)