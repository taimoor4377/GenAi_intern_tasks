import streamlit as st
from ollama_client import OllamaClient
from utils import reset_conversation_state, format_conversation_history

# Initialize the Ollama client
client = OllamaClient()

# Session state to hold conversation history
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

# Title of the app
st.title("Ollama LLM Chatbot")

# Text input for user query
user_input = st.text_input("You:", "")

# Button to send the query
if st.button("Send"):
    if user_input:
        # Send the query to the LLM and get the response
        response = client.send_query(user_input)
        
        # Update conversation history
        st.session_state.conversation_history.append({"user": user_input, "response": response})

# Display conversation history
if st.session_state.conversation_history:
    st.subheader("Conversation History")
    conversation_display = format_conversation_history(st.session_state.conversation_history)
    st.write(conversation_display)

# Reset button to clear conversation history
if st.button("Reset"):
    reset_conversation()