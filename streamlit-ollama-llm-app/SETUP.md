# Setup Guide

This guide will walk you through setting up the Streamlit LLM Interface from scratch.

## Prerequisites Check

Before starting, verify you have the required software:

### 1. Python Installation

Check your Python version:
```bash
python --version
# or
python3 --version
```

You need Python 3.8 or higher. If you don't have Python installed:
- **macOS**: Use Homebrew: `brew install python`
- **Windows**: Download from [python.org](https://python.org)
- **Linux**: Use your package manager: `sudo apt install python3`

### 2. Ollama Installation

#### Install Ollama

**macOS/Linux:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

**Windows:**
Download the installer from [ollama.ai](https://ollama.ai)

#### Verify Ollama Installation

```bash
ollama --version
```

#### Start Ollama Service

```bash
ollama serve
```

Keep this terminal open - Ollama needs to run in the background.

#### Install an LLM Model

In a new terminal:
```bash
# Install a lightweight model (recommended for testing)
ollama pull llama2:7b

# Or install a larger, more capable model
ollama pull llama2:13b

# List available models
ollama list
```

## Project Setup

### 1. Create Project Directory

```bash
mkdir streamlit-llm-interface
cd streamlit-llm-interface
```

### 2. Set Up Python Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Create Requirements File

Create `requirements.txt`:
```txt
streamlit>=1.28.0
requests>=2.31.0
python-dateutil>=2.8.2
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Verify Streamlit Installation

```bash
streamlit --version
```

## Quick Test Setup

Before implementing the full application, let's create a minimal test to verify everything works:

### 1. Create Test File

Create `test_setup.py`:
```python
import streamlit as st
import requests

st.title("Setup Test")

# Test Ollama connection
try:
    response = requests.get("http://localhost:11434/api/tags", timeout=5)
    if response.status_code == 200:
        st.success("✅ Ollama connection successful!")
        models = response.json().get('models', [])
        if models:
            st.write("Available models:")
            for model in models:
                st.write(f"- {model['name']}")
        else:
            st.warning("No models installed. Run: ollama pull llama2")
    else:
        st.error("❌ Ollama responded with error")
except requests.exceptions.ConnectionError:
    st.error("❌ Cannot connect to Ollama. Is it running?")
except Exception as e:
    st.error(f"❌ Error: {e}")

# Test basic Streamlit functionality
user_input = st.text_input("Test input:")
if user_input:
    st.write(f"You entered: {user_input}")
```

### 2. Run Test

```bash
streamlit run test_setup.py
```

This should open your browser to `http://localhost:8501` and show:
- ✅ Ollama connection successful
- List of installed models
- A working text input

## Troubleshooting Setup Issues

### Python Issues

**"python: command not found"**
- Install Python or use `python3` instead of `python`

**"pip: command not found"**
- Use `python -m pip` instead of `pip`

### Ollama Issues

**"Connection refused" to localhost:11434**
- Start Ollama: `ollama serve`
- Check if port 11434 is available: `lsof -i :11434`

**"No models available"**
- Install a model: `ollama pull llama2`
- Verify installation: `ollama list`

**Ollama service won't start**
- Check system resources (RAM/disk space)
- Try restarting: `pkill ollama && ollama serve`

### Streamlit Issues

**"ModuleNotFoundError: No module named 'streamlit'"**
- Activate virtual environment
- Reinstall: `pip install streamlit`

**Port 8501 already in use**
- Use different port: `streamlit run app.py --server.port 8502`
- Or kill existing process: `pkill -f streamlit`

### Virtual Environment Issues

**Virtual environment not activating**
- Check path: `which python` (should show venv path when activated)
- Recreate environment: `rm -rf venv && python -m venv venv`

## Next Steps

Once setup is complete:

1. **Delete test file**: `rm test_setup.py`
2. **Start development**: Begin with Task 1 from the implementation plan
3. **Create project structure**: Set up the directories and files as outlined in the tasks

## Development Environment Tips

### Recommended VS Code Extensions
- Python
- Streamlit
- Python Docstring Generator

### Useful Commands
```bash
# Run with auto-reload
streamlit run app.py

# Run on different port
streamlit run app.py --server.port 8502

# Run with debug mode
streamlit run app.py --logger.level debug

# Check Ollama models
ollama list

# Test Ollama API directly
curl http://localhost:11434/api/tags
```

### Environment Variables (Optional)
Create `.env` file for configuration:
```bash
OLLAMA_ENDPOINT=http://localhost:11434
DEFAULT_MODEL=llama2
TIMEOUT_SECONDS=30
```

## Ready to Code!

Your development environment is now ready. You can start implementing the tasks from the implementation plan, beginning with Task 1: "Set up project structure and dependencies".