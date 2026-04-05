import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv
load_dotenv()


# Langsmith Tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot with history" 

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to queries"),
        ("user","Question:{question}")
    ]
)

def gererate_response(question, llm, temperature, max_tokens):
    output_parser = StrOutputParser()


    # chain is something that tells you interaction is going to happen
    chain = prompt| llm | output_parser
    
    answer = chain.invoke({'question':question})
    return answer

# Title of the app
st.title("Q&A Chatbot with History")
st.sidebar.title("Settings")
 
 # Drop down to select various models
llm = st.sidebar.selectbox("Select a model", ["phi3:mini"])

# Adjust reponse parameter
temperature =st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value= 0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value =300, value = 150)


# Main interface for user input

st.write("Ask any question")
user_input = st.text_input("You:")

# Currently using my local llm model phi3 mini
llm = ChatOllama(model="phi3:mini")

if user_input:
    response = gererate_response(user_input,llm,temperature,max_tokens)
    st.write(response)

else:
    st.write("Ask something first")
