from langchain import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os 
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
##Langsmith trackingpwd
os.environ["LANGCHAIN_HANDLER"] = "langchain_core"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN__API_KEY")

## prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that helps answer questions about the worls. please resond to the user in a friendly and concisre manner."),
        ("user", "Question: {question}" )
    ]
)

## streamlit framework
st.title("ChatBot with LangChain and Streamlit and OpenAI")
input_text = st.text_input("Search the topic you want to know about")

##OpenAI LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text: 
    st.write(chain.invoke({"question": input_text}))
