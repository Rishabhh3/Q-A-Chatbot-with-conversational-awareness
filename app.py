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
    # Currently using my local llm model phi3 mini
    llm = ChatOllama(model="phi3:mini")
    output_parser = StrOutputParser()


    # chain is something that tells you interaction is going to happen
    chain = prompt| llm | output_parser
    
    answer = chain.invoke({'question':question})
    return answer

