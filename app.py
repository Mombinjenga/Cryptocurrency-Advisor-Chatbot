import streamlit as st
from datetime import datetime
from backend.chatbot import get_response  # Your existing backend function

# Page config — modern look
st.set_page_config(
    page_title="Crypto Advisor Chatbot",
    page_icon="₿",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS for extra polish (dark mode, rounded bubbles, better spacing)
st.markdown("""
<style>
    .stChatMessage {margin-bottom: 20px;}
    .user-msg {background-color: #2b2b2b; border-radius: 15px; padding: 10px;}
    .bot-msg {background-color: #004d40; border-radius: 15px; padding: 10px;}
    .title {text-align: center; font-size: 2.5em; margin-bottom: 0.5em;}
    .subtitle {text-align: center; color: #888; margin-bottom: 2em;}
</style>
""", unsafe_allow_html=True)

# Title & welcome
st.markdown('<div class="title">₿ Crypto Advisor Chatbot</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your AI-powered Bitcoin trend analyst & predictor</div>', unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Welcome message from bot
    welcome = "Hello! 👋 I'm your Cryptocurrency Advisor.\nAsk me anything about Bitcoin trends, price predictions, volatility, or market insights."
    st.session_state.messages.append({"role": "assistant", "content": welcome})

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar="👤" if message["role"] == "user" else "🤖"):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask about Bitcoin..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # Get bot response
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Analyzing market data..."):
            response = get_response(prompt)  # Calls your backend!
        st.markdown(response)

    # Add bot response to history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Run with: streamlit run app.py