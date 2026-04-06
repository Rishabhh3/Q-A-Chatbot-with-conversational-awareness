#  Q&A Chatbot with History (Streamlit + LangChain + Groq)

A simple yet powerful Q&A chatbot built using **Streamlit**, **LangChain (LCEL)**, and **Groq API**.  
This app allows users to ask questions and get responses from a high-performance LLM in real time.
The user if want can choose any model of choice by adding them in list in model selection.

---

## Features

-  Interactive UI using Streamlit  
-  Fast inference using Groq LLMs  
-  Clean LCEL-based pipeline (`prompt | llm | parser`)  
-  Adjustable parameters (temperature, max tokens)  
-  Modular and extensible design  

---

##  Tech Stack

- **Frontend/UI**: Streamlit  
- **LLM Orchestration**: LangChain (LCEL)  
- **Model Provider**: Groq API  
- **Environment Management**: dotenv  

---

## How it works
The application uses LangChain Expression Language (LCEL) to create a pipeline:

`User Input → Prompt Template → LLM (Groq) → Output Parser → Response`


---
##  Project Structure

```text
.
├── app.py              # Main Streamlit app
├── .env                # API keys 
├── requirements.txt    # Dependencies
└── README.md
```

---

##  Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Rishabhh3/Q-A-Chatbot-with-conversational-awareness
```

## 2. Install dependencies
```bash
pip install -r requirements.txt
```

## 3. Set up environment variables
Create a .env file in the root directory:
```bash
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langsmith_key
```

## 4. Run the app
```bash
streamlit run app.py
```

