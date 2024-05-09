import streamlit as st 
from regex_chatbot import RegexChatbot
rc = RegexChatbot()
st.title("Regex Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Pls enter your question ... "):
    with st.chat_message("User"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

if prompt: 
    print(prompt)
    response = rc.answer_qs(prompt)
else:
    response = "..."

with st.chat_message("assistant"):
    st.markdown(response)
st.session_state.messages.append({"role": "assistant", "content": response})
