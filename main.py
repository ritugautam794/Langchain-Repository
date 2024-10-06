import os
from constants import openai_key
from langchain import OpenAI
import streamlit as st 
#streamlit framework


os.environ["OPENAI_API_KEY"] = openai_key
st.title('langchain demo with openai api')
input_text = st.text_input("search the topic you want")

# open ai llms models

llm = OpenAI(temperature=0.0)

if input_text:
    st.write(llm(input_text))