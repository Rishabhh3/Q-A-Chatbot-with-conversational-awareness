import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import os

from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")


# Langsmith Tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot with history" 


# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to queries"),
        ("user","Question:{question}")
    ]
)

def gererate_response(question, temperature, max_tokens):
    output_parser = StrOutputParser()

    # chain is something that tells you interaction is going to happen
    chain = prompt| llm | output_parser
    
    answer = chain.invoke({'question':question})
    return answer

# Title of the app
st.title("Q&A Chatbot with History")
st.sidebar.title("Settings")
 
# Adjust reponse parameter
temperature =st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value= 0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value =300, value = 150)


 # Drop down to select various models
selected_model = st.sidebar.selectbox(
    "Select a model",
    ["llama-3.1-8b-instant"]
)
# specify which model to use
llm=ChatGroq(groq_api_key=groq_api_key,
             model_name=selected_model,
             temperature=temperature,
             max_tokens=max_tokens) 


# Main interface for user input

st.write("Ask any question")
user_input = st.text_input("You:")


if user_input:
    response = gererate_response(user_input,temperature,max_tokens)
    st.write(response)

else:
    st.write("Ask something first")
