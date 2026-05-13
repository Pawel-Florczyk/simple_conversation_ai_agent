# Simple Conversation Agent

A lightweight and responsive AI agent built with Python, leveraging the **Google Gemini 2.5 Flash** model. This project serves as a foundational template for learning LLM interactions and conversation history management.

## Features
- **Gemini Integration:** Powered by the `langchain-google-genai` library.
- **Persistent Memory:** Automatically saves conversation history, allowing the agent to remember context across different sessions.
- **Security First:** Robust API key management using environment variables via `.env`.
- **Interactive CLI:** Real-time chat interface directly in your terminal.

## Requirements
- Python 3.10+
- A Google Cloud / [Google AI Studio](https://aistudio.google.com/) account and an API Key.

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YourUsername/simple_conversation_agent.git](https://github.com/YourUsername/simple_conversation_agent.git)

2. **Install dependencies:**
   ```bash
   pip install langchain-google-genai langchain-core python-dotenv
   ```
3. **Configure API Key:**
   - Create a `.env` file in the root directory.
   - Add your Gemini API key:
     ```text
     [GOOGLE_API_KEY]=your_api_key_here
     ```

## Usage
To start a conversation with the agent, simply run the main script:
```bash
python main.py
