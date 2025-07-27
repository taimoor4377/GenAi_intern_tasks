def format_conversation_history(history):
    return "\n".join([f"User: {entry['user']}\nLLM: {entry['llm']}" for entry in history])

def reset_conversation_state(session_state):
    session_state.history = []
    session_state.user_input = ""