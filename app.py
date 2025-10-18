from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
import streamlit as st

# Load environment variables from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


# Function to load OpenAI model and get a response
def get_response(prompt):
    llm = ChatOpenAI(
        model="gpt-3.5-turbo", 
        temperature=0.6,
        api_key=openai_api_key
    )
    response = llm.invoke(prompt)
    return response.content

# Streamlit app
st.set_page_config(page_title="Langchain Chatbot", page_icon=":robot:")
st.header("Langchain Chatbot")

# Get user input
input = st.text_input("Input: ", key="input")
response = get_response(input)


submit_button = st.button("Ask the question")

if submit_button:
    st.header("Answer:")
    st.write(response)
