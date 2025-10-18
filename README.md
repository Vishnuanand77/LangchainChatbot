---
title: LangChain Chatbot
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: 1.50.0
app_file: app.py
pinned: false
license: mit
short_description: A simple chatbot built with LangChain and Streamlit using OpenAI's GPT models
---

# LangChain Chatbot

A simple and interactive chatbot built with LangChain and Streamlit that uses OpenAI's GPT models for intelligent conversations.

## Features

- 🤖 Interactive chat interface powered by OpenAI's GPT-3.5-turbo
- 🚀 Built with Streamlit for easy deployment
- 🔧 Environment variable configuration
- 💬 Real-time conversation capabilities

## How to Use

1. Enter your question or message in the input field
2. Click "Ask the question" button
3. Get an intelligent response from the AI model

## Setup for Local Development

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
5. Run the app:
   ```bash
   streamlit run app.py
   ```

## Requirements

- Python 3.8+
- OpenAI API key
- See `requirements.txt` for package dependencies

## License

MIT License
