from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st
import os

# Set OpenAI API credentials from Streamlit secrets
os.environ["OPENAI_API_TYPE"] = st.secrets["OPENAI_TYPE"]
os.environ["OPENAI_API_BASE"] = st.secrets["OPENAI_BASE"]
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_KEY"]
os.environ["OPENAI_API_VERSION"] = st.secrets["OPENAI_VERSION"]

# Initialize ChatOpenAI object for interacting with OpenAI's language model
llm = ChatOpenAI(   model_name = st.secrets["OPENAI_MODEL_NAME"],
                    temperature = 0.1,
                    model_kwargs = {"engine":st.secrets["OPENAI_ENGINE"]} )

def generate(template,input_variables,variables_dict,llm_selected):
    """
    Generate a response using a prompt template and variables.

    Args:
    - template (str): The template for generating the prompt.
    - input_variables (list): List of variables to be replaced in the template.
    - variables_dict (dict): Dictionary containing variable values.
    - llm_selected: Selected language model for generating the response.

    Returns:
    - str: The generated response.
    """
    # Create a PromptTemplate object
    prompt_template = PromptTemplate(input_variables=input_variables,template=template)
    # Create an LLMChain object
    chain = LLMChain(llm=llm_selected,prompt=prompt_template)
    response = chain.run(variables_dict)
    return response

def ask(question):
    """
    Generate a response to a user question.

    Args:
    - question (str): The user's question.

    Returns:
    - str: The generated response to the question.
    """
    template = """Answer the question.
                question:{QUESTION}
                response:"""
    input_variables = ["QUESTION"]
    variables_dict = {"QUESTION": question}
    response = generate(template,input_variables,variables_dict,llm)
    return response


