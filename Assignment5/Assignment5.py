import streamlit as st
from rule_based_chatbot import RuleBasedChatbot
rbc = RuleBasedChatbot()
st.title("Chat Bot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

if prompt:
    response = rbc.answer_qs(prompt)
else:
    response = "..."

with st.chat_message("assistant"):
    st.markdown(response)
st.session_state.messages.append({"role": "assistant", "content": response})
