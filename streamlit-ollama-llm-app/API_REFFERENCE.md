# API Reference

Complete reference for all modules, classes, and functions in the Streamlit LLM Interface.

## Table of Contents

- [Configuration (`config.py`)](#configuration)
- [Data Models (`models.py`)](#data-models)
- [Ollama Client (`ollama_client.py`)](#ollama-client)
- [Session Manager (`session_manager.py`)](#session-manager)
- [UI Components (`ui_components.py`)](#ui-components)
- [Main Application (`app.py`)](#main-application)

## Configuration

### `config.py`

Application configuration constants and settings.

#### Constants

```python
# API Configuration
OLLAMA_ENDPOINT: str = "http://localhost:11434"
DEFAULT_MODEL: str = "llama2"
TIMEOUT_SECONDS: int = 30
MAX_RETRIES: int = 3

# UI Configuration
MAX_HISTORY_LENGTH: int = 100
PAGE_TITLE: str = "LLM Chat Interface"
PAGE_ICON: str = "🤖"

# Styling
USER_MESSAGE_COLOR: str = "#E3F2FD"
ASSISTANT_MESSAGE_COLOR: str = "#F5F5F5"
ERROR_COLOR: str = "#FFEBEE"
SUCCESS_COLOR: str = "#E8F5E8"
```

#### Functions

```python
def get_config() -> Dict[str, Any]:
    """Get all configuration values as dictionary."""
    
def validate_config() -> bool:
    """Validate configuration values."""
    
def update_config(key: str, value: Any) -> None:
    """Update a configuration value."""
```

## Data Models

### `models.py`

Data structures used throughout the application.

#### `Message`

Represents a single message in the conversation.

```python
@dataclass
class Message:
    role: str          # "user" or "assistant"
    content: str       # Message content
    timestamp: datetime # When message was created
    id: str           # Unique identifier (UUID)
    
    def __post_init__(self):
        """Generate ID if not provided."""
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Message':
        """Create Message from dictionary."""
        
    def is_user_message(self) -> bool:
        """Check if message is from user."""
        
    def is_assistant_message(self) -> bool:
        """Check if message is from assistant."""
```

#### `ConversationState`

Represents the current state of the conversation.

```python
@dataclass
class ConversationState:
    messages: List[Message] = field(default_factory=list)
    current_model: str = DEFAULT_MODEL
    is_loading: bool = False
    last_error: Optional[str] = None
    connection_status: str = "unknown"  # "connected", "disconnected", "error"
    
    def add_message(self, message: Message) -> None:
        """Add message to conversation."""
        
    def clear_messages(self) -> None:
        """Clear all messages."""
        
    def get_message_count(self) -> int:
        """Get total number of messages."""
        
    def get_last_message(self) -> Optional[Message]:
        """Get the most recent message."""
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
```

#### `OllamaResponse`

Represents a response from the Ollama API.

```python
@dataclass
class OllamaResponse:
    content: str
    model: str
    done: bool
    error: Optional[str] = None
    response_time: Optional[float] = None
    
    def is_successful(self) -> bool:
        """Check if response was successful."""
        
    def has_error(self) -> bool:
        """Check if response contains an error."""
        
    @classmethod
    def from_api_response(cls, response_data: Dict[str, Any]) -> 'OllamaResponse':
        """Create from Ollama API response."""
```

## Ollama Client

### `ollama_client.py`

Client for communicating with the Ollama API.

#### `OllamaClient`

Main class for Ollama API interactions.

```python
class OllamaClient:
    def __init__(self, 
                 endpoint: str = OLLAMA_ENDPOINT,
                 timeout: int = TIMEOUT_SECONDS,
                 max_retries: int = MAX_RETRIES):
        """Initialize Ollama client."""
```

##### Methods

```python
def send_query(self, 
               prompt: str, 
               model: str = None,
               stream: bool = False) -> OllamaResponse:
    """
    Send a query to the LLM.
    
    Args:
        prompt: The user's query
        model: Model to use (defaults to configured model)
        stream: Whether to stream the response
        
    Returns:
        OllamaResponse object
        
    Raises:
        ConnectionError: If cannot connect to Ollama
        TimeoutError: If request times out
        ModelNotFoundError: If model is not available
        OllamaAPIError: For other API errors
    """

def check_connection(self) -> bool:
    """
    Check if Ollama service is available.
    
    Returns:
        True if connected, False otherwise
    """

def list_models(self) -> List[str]:
    """
    Get list of available models.
    
    Returns:
        List of model names
        
    Raises:
        ConnectionError: If cannot connect to Ollama
    """

def is_model_available(self, model: str) -> bool:
    """
    Check if a specific model is available.
    
    Args:
        model: Model name to check
        
    Returns:
        True if model exists, False otherwise
    """

def get_model_info(self, model: str) -> Dict[str, Any]:
    """
    Get detailed information about a model.
    
    Args:
        model: Model name
        
    Returns:
        Dictionary with model information
        
    Raises:
        ModelNotFoundError: If model doesn't exist
    """

def health_check(self) -> Dict[str, Any]:
    """
    Perform comprehensive health check.
    
    Returns:
        Dictionary with health status information
    """
```

#### Custom Exceptions

```python
class OllamaAPIError(Exception):
    """Base exception for Ollama API errors."""

class ConnectionError(OllamaAPIError):
    """Raised when cannot connect to Ollama service."""

class TimeoutError(OllamaAPIError):
    """Raised when request times out."""

class ModelNotFoundError(OllamaAPIError):
    """Raised when requested model is not available."""
```

## Session Manager

### `session_manager.py`

Manages Streamlit session state and conversation history.

#### Functions

```python
def initialize_session() -> None:
    """
    Initialize Streamlit session state variables.
    
    Sets up:
    - conversation_state: ConversationState object
    - ollama_client: OllamaClient instance
    - ui_state: UI-specific state variables
    """

def get_conversation_state() -> ConversationState:
    """
    Get current conversation state.
    
    Returns:
        ConversationState object from session
    """

def update_conversation_state(state: ConversationState) -> None:
    """
    Update conversation state in session.
    
    Args:
        state: New ConversationState object
    """

def add_message(role: str, content: str) -> None:
    """
    Add a message to conversation history.
    
    Args:
        role: "user" or "assistant"
        content: Message content
    """

def clear_conversation() -> None:
    """Clear all conversation history."""

def get_conversation_history() -> List[Message]:
    """
    Get complete conversation history.
    
    Returns:
        List of Message objects in chronological order
    """

def set_loading_state(is_loading: bool) -> None:
    """
    Set loading state.
    
    Args:
        is_loading: Whether app is currently loading
    """

def is_loading() -> bool:
    """
    Check if app is in loading state.
    
    Returns:
        True if loading, False otherwise
    """

def set_error(error_message: str) -> None:
    """
    Set error message.
    
    Args:
        error_message: Error message to display
    """

def get_error() -> Optional[str]:
    """
    Get current error message.
    
    Returns:
        Error message or None if no error
    """

def clear_error() -> None:
    """Clear current error message."""

def get_ollama_client() -> OllamaClient:
    """
    Get Ollama client instance.
    
    Returns:
        OllamaClient from session state
    """
```

## UI Components

### `ui_components.py`

Reusable Streamlit UI components.

#### Input Components

```python
def render_chat_input() -> Optional[str]:
    """
    Render chat input component.
    
    Returns:
        User input text or None if no input
    """

def render_model_selector() -> str:
    """
    Render model selection dropdown.
    
    Returns:
        Selected model name
    """
```

#### Display Components

```python
def render_conversation_history() -> None:
    """
    Render conversation history with proper formatting.
    
    Displays all messages with:
    - User messages on the right
    - Assistant messages on the left
    - Timestamps
    - Proper styling
    """

def render_message(message: Message) -> None:
    """
    Render a single message.
    
    Args:
        message: Message object to render
    """

def render_status_indicator(status: str) -> None:
    """
    Render connection/loading status indicator.
    
    Args:
        status: "connected", "loading", "error", "disconnected"
    """

def render_error_message(error: str) -> None:
    """
    Render error message with appropriate styling.
    
    Args:
        error: Error message to display
    """
```

#### Action Components

```python
def render_reset_button() -> bool:
    """
    Render conversation reset button.
    
    Returns:
        True if button was clicked, False otherwise
    """

def render_retry_button() -> bool:
    """
    Render retry button for failed requests.
    
    Returns:
        True if button was clicked, False otherwise
    """

def render_connection_test_button() -> bool:
    """
    Render button to test Ollama connection.
    
    Returns:
        True if button was clicked, False otherwise
    """
```

#### Layout Components

```python
def render_header() -> None:
    """Render application header with title and status."""

def render_sidebar() -> None:
    """
    Render sidebar with:
    - Model selection
    - Connection status
    - Settings
    """

def render_footer() -> None:
    """Render application footer with info and links."""
```

#### Utility Functions

```python
def format_timestamp(timestamp: datetime) -> str:
    """
    Format timestamp for display.
    
    Args:
        timestamp: Datetime object
        
    Returns:
        Formatted timestamp string
    """

def apply_message_styling(role: str) -> str:
    """
    Get CSS styling for message based on role.
    
    Args:
        role: "user" or "assistant"
        
    Returns:
        CSS style string
    """

def show_loading_spinner(message: str = "Processing...") -> None:
    """
    Show loading spinner with message.
    
    Args:
        message: Loading message to display
    """
```

## Main Application

### `app.py`

Main Streamlit application entry point.

#### Functions

```python
def main() -> None:
    """
    Main application function.
    
    Orchestrates:
    - Session initialization
    - UI rendering
    - User interaction handling
    - API communication
    """

def setup_page_config() -> None:
    """Configure Streamlit page settings."""

def handle_user_input(user_input: str) -> None:
    """
    Process user input and generate response.
    
    Args:
        user_input: User's query text
    """

def handle_reset() -> None:
    """Handle conversation reset action."""

def handle_model_change(new_model: str) -> None:
    """
    Handle model selection change.
    
    Args:
        new_model: Newly selected model name
    """

def update_ui() -> None:
    """Update UI components based on current state."""

def run_health_check() -> None:
    """Run system health check and update status."""

if __name__ == "__main__":
    main()
```

## Error Handling

### Exception Hierarchy

```
Exception
├── OllamaAPIError
│   ├── ConnectionError
│   ├── TimeoutError
│   └── ModelNotFoundError
└── ValidationError
    ├── InvalidInputError
    └── ConfigurationError
```

### Error Response Format

All API functions return errors in a consistent format:

```python
{
    "success": False,
    "error": {
        "type": "ConnectionError",
        "message": "Cannot connect to Ollama service",
        "details": "Connection refused on localhost:11434",
        "timestamp": "2024-01-01T12:00:00Z"
    }
}
```

## Usage Examples

### Basic Usage

```python
from ollama_client import OllamaClient
from session_manager import initialize_session, add_message

# Initialize
initialize_session()
client = OllamaClient()

# Send query
response = client.send_query("Hello, how are you?")
add_message("user", "Hello, how are you?")
add_message("assistant", response.content)
```

### Error Handling

```python
try:
    response = client.send_query("What is AI?")
except ConnectionError:
    st.error("Cannot connect to Ollama. Please start the service.")
except TimeoutError:
    st.error("Request timed out. Please try again.")
except ModelNotFoundError:
    st.error("Model not found. Please install a model first.")
```

### Custom Configuration

```python
from config import update_config

# Update timeout
update_config("TIMEOUT_SECONDS", 60)

# Update default model
update_config("DEFAULT_MODEL", "llama2:13b")
```