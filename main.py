import os
import streamlit as st
import llm_helper

"""
Simple Chat Bot using Streamlit and OpenAI's LLM.
This application allows users to interact with a chatbot powered by OpenAI's Language Model.
Users can input messages and receive responses from the chatbot.
"""

st.title("Simple Chat Bot")
# initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

#Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(name=message["role"]):
        st.markdown(message["content"])

#React to user input
prompt = st.chat_input("hi")
if prompt:
    # Display user message
    with st.chat_message(name="user"):
        st.markdown(prompt)
    # add user message to chat history
    st.session_state.messages.append({"role":"user", "content":prompt})
    # Get response from the llm
    response = llm_helper.ask(prompt)
    # Display chatbot response
    with st.chat_message(name="assistant"):
        st.markdown(response)
    # add user message to chat history
    st.session_state.messages.append({"role":"assistant", "content":response})