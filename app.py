from langchain_openai import ChatOpenAI
import os
import streamlit as st

# Load environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

# Function to load OpenAI model and get a response
def get_response(prompt):
    if not openai_api_key:
        return "❌ OpenAI API key not found. Please set the OPENAI_API_KEY environment variable."
    
    try:
        llm = ChatOpenAI(
            model="gpt-3.5-turbo", 
            temperature=0.6,
            api_key=openai_api_key
        )
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Streamlit app
st.set_page_config(
    page_title="LangChain Chatbot", 
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 LangChain Chatbot")
st.markdown("Ask me anything! I'm powered by OpenAI's GPT-3.5-turbo model.")

# Sidebar for additional info
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    This chatbot is built with:
    - **LangChain** for AI orchestration
    - **Streamlit** for the web interface
    - **OpenAI GPT-3.5-turbo** for responses
    """)
    
    if not openai_api_key:
        st.error("⚠️ OpenAI API key not configured")
    else:
        st.success("✅ OpenAI API key configured")

# Main chat interface
col1, col2 = st.columns([3, 1])

with col1:
    user_input = st.text_input(
        "💬 Ask me anything:", 
        placeholder="Type your question here...",
        key="user_input"
    )

with col2:
    submit_button = st.button("🚀 Ask", type="primary", use_container_width=True)

if submit_button and user_input:
    with st.spinner("🤔 Thinking..."):
        response = get_response(user_input)
    
    st.markdown("---")
    st.markdown("### 💡 Response:")
    st.write(response)
    
    # Add some styling
    st.markdown("---")
    st.markdown("*Powered by LangChain & OpenAI*")
elif submit_button and not user_input:
    st.warning("⚠️ Please enter a question first!")
