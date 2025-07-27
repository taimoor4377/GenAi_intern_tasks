# Streamlit LLM Interface

A user-friendly web interface for interacting with locally installed Large Language Models (LLMs) via Ollama.

## Overview

This application provides a clean, intuitive chat interface that connects to your local Ollama installation, allowing you to interact with LLMs through a web browser instead of command-line tools. Features include conversation history, reset functionality, and robust error handling.

## Features

- **Interactive Chat Interface**: Clean text input and response display
- **Conversation History**: Persistent chat history during your session
- **Reset Functionality**: Clear conversation and start fresh
- **Error Handling**: Graceful handling of connection issues and timeouts
- **Responsive Design**: Works on desktop and mobile devices
- **Real-time Status**: Loading indicators and connection status

## Prerequisites

- Python 3.8 or higher
- [Ollama](https://ollama.ai/) installed and running locally
- At least one LLM model installed in Ollama

### Installing Ollama

1. Visit [ollama.ai](https://ollama.ai/) and download for your platform
2. Install and start the Ollama service
3. Pull a model (e.g., `ollama pull llama2`)

## Installation

1. Clone or download this project
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure Ollama is running:
   ```bash
   ollama serve
   ```

2. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```

3. Open your browser to `http://localhost:8501`

4. Start chatting with your local LLM!

## Configuration

The application can be configured by modifying `config.py`:

- **OLLAMA_ENDPOINT**: Ollama API endpoint (default: http://localhost:11434)
- **DEFAULT_MODEL**: Default LLM model to use
- **TIMEOUT_SECONDS**: Request timeout duration
- **MAX_HISTORY_LENGTH**: Maximum conversation history length

## Project Structure

```
streamlit-llm-interface/
├── app.py                 # Main Streamlit application
├── config.py             # Configuration settings
├── ollama_client.py      # Ollama API client
├── session_manager.py    # Session state management
├── ui_components.py      # Reusable UI components
├── models.py            # Data models and structures
├── requirements.txt     # Python dependencies
├── tests/              # Test files
│   ├── test_ollama_client.py
│   ├── test_session_manager.py
│   └── test_ui_components.py
└── README.md           # This file
```

## API Reference

### Ollama Client (`ollama_client.py`)

#### `OllamaClient`

Main class for interacting with the Ollama API.

**Methods:**

- `send_query(prompt: str, model: str = None) -> str`
  - Send a query to the LLM and return the response
  - Raises: `ConnectionError`, `TimeoutError`, `ModelNotFoundError`

- `check_connection() -> bool`
  - Check if Ollama service is available
  - Returns: `True` if connected, `False` otherwise

- `list_models() -> List[str]`
  - Get list of available models
  - Returns: List of model names

- `is_model_available(model: str) -> bool`
  - Check if a specific model is available
  - Returns: `True` if model exists, `False` otherwise

### Session Manager (`session_manager.py`)

#### Functions

- `initialize_session()`
  - Initialize Streamlit session state variables

- `add_message(role: str, content: str)`
  - Add a message to conversation history
  - Parameters: `role` ("user" or "assistant"), `content` (message text)

- `clear_conversation()`
  - Clear all conversation history

- `get_conversation_history() -> List[Message]`
  - Get the complete conversation history

### UI Components (`ui_components.py`)

#### Functions

- `render_chat_input() -> str`
  - Render text input component
  - Returns: User input text or empty string

- `render_conversation_history()`
  - Display conversation history with proper formatting

- `render_reset_button() -> bool`
  - Render reset button
  - Returns: `True` if button was clicked

- `render_status_indicator(status: str)`
  - Display connection/loading status
  - Parameters: `status` ("connected", "loading", "error")

- `render_error_message(error: str)`
  - Display error message to user
  - Parameters: `error` (error message text)

## Data Models

### Message

```python
@dataclass
class Message:
    role: str          # "user" or "assistant"
    content: str       # Message content
    timestamp: datetime # When message was created
    id: str           # Unique identifier
```

### ConversationState

```python
@dataclass
class ConversationState:
    messages: List[Message]  # All conversation messages
    current_model: str       # Currently selected model
    is_loading: bool        # Whether request is in progress
    last_error: Optional[str] # Last error message
```

### OllamaResponse

```python
@dataclass
class OllamaResponse:
    content: str           # Response content
    model: str            # Model that generated response
    done: bool           # Whether response is complete
    error: Optional[str] # Error message if any
```

## Error Handling

The application handles several types of errors gracefully:

### Connection Errors
- **Cause**: Ollama service not running
- **Display**: "Unable to connect to Ollama. Please ensure Ollama is running."
- **Action**: Retry button available

### Model Errors
- **Cause**: Requested model not available
- **Display**: List of available models with installation instructions
- **Action**: Model selection dropdown

### Timeout Errors
- **Cause**: LLM response takes too long
- **Display**: "Request timed out. Please try again."
- **Action**: Retry with same or different query

### Input Validation Errors
- **Cause**: Empty or invalid input
- **Display**: Inline validation messages
- **Action**: Input field highlights and guidance

## Testing

Run the test suite:

```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_ollama_client.py

# Run with coverage
python -m pytest --cov=. tests/
```

### Test Structure

- **Unit Tests**: Test individual components in isolation
- **Integration Tests**: Test component interactions
- **Mock Tests**: Test with simulated Ollama responses

## Troubleshooting

### Common Issues

**"Connection refused" error**
- Ensure Ollama is installed and running (`ollama serve`)
- Check that Ollama is listening on the correct port (11434)

**"Model not found" error**
- Install a model: `ollama pull llama2`
- Check available models: `ollama list`

**Slow responses**
- Large models may take time to respond
- Consider using smaller models for faster responses
- Check system resources (RAM, CPU)

**Interface not loading**
- Ensure all dependencies are installed
- Check Python version compatibility
- Verify Streamlit installation: `streamlit --version`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues and questions:
1. Check the troubleshooting section above
2. Review the [Ollama documentation](https://ollama.ai/docs)
3. Check [Streamlit documentation](https://docs.streamlit.io)
4. Open an issue in the project repository