import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatMessagePromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

import os

from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")


# Langsmith Tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot with history" 


#  Initialize chat history in session state if it doesn't exist
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Prompt Template
system_prompt = (
    "You are a helpful, professional, and concise assistant. "
    "Use the provided chat history to maintain context and continuity in the conversation. "
    "Answer the user's questions accurately using your internal knowledge. "
    "If you don't know the answer to a question, simply state that you don't know."
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",system_prompt),
        MessagesPlaceholder("chat_history"),
        ("user","Question:{question}")
    ]
)

def gererate_response(question, temperature, max_tokens):

    output_parser = StrOutputParser()

    # chain is something that tells you interaction is going to happen
    chain = prompt| llm | output_parser
    
    answer = chain.invoke({'question':question,'chat_history':st.session_state.chat_history})

    st.session_state.chat_history.extend([
        HumanMessage(content=question),
        AIMessage(content=answer)
    ])

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
