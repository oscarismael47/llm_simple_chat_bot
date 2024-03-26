import os
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def generate(template,input_variables,variables_dict,llm_selected):
    prompt_template = PromptTemplate(input_variables=input_variables,template=template)
    chain = LLMChain(llm=llm_selected,prompt=prompt_template)
    response = chain.run(variables_dict)
    return response

def ask(question):
    template = """Answer the question.
                question:{QUESTION}
                response:"""
    input_variables = ["QUESTION"]
    variables_dict = {"QUESTION": question}
    response = generate(template,input_variables,variables_dict,llm)
    return response

os.environ["OPENAI_API_TYPE"] = st.secrets["OPENAI_TYPE"]
os.environ["OPENAI_API_BASE"] = st.secrets["OPENAI_BASE"]
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_KEY"]
os.environ["OPENAI_API_VERSION"] = st.secrets["OPENAI_VERSION"]
llm = ChatOpenAI(   model_name = st.secrets["OPENAI_MODEL_NAME"],
                    temperature = 0.1,
                    model_kwargs = {"engine":st.secrets["OPENAI_ENGINE"]} )

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
    with st.chat_message(name="user"):
        st.markdown(prompt)
    # add user message to chat history
    st.session_state.messages.append({"role":"user", "content":prompt})
    response = ask(prompt)

    with st.chat_message(name="assistant"):
        st.markdown(response)

    # add user message to chat history
    st.session_state.messages.append({"role":"assistant", "content":response})