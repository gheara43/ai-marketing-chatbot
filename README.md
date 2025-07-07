# 🧠 OpenRouter AI Marketing Chatbot

This is a Python-based terminal chatbot that connects to OpenRouter.ai to simulate a professional digital marketing assistant named Gio. Gio specializes in branding, SEO, content strategy, and customer psychology, providing strategic and creative marketing advice.

## 🚀 Features

- Uses OpenRouter API to access advanced AI language models  
- Emulates a marketing expert for strategy, copywriting, SEO, and growth insights  
- Maintains conversation context with `chat_history`  
- Runs directly in your terminal  
- Built with Python and easily customizable  

## 🛠️ Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/openrouter-marketing-chatbot.git  
    cd openrouter-marketing-chatbot
    ```
2. Install dependencies:
    ```bash
    pip install requests python-dotenv
    ```
3. Modify the .env file and add your API key:
    ```env
    OPENROUTER_API_KEY=your_openrouter_api_key
    ```
You can get a free API key at https://openrouter.ai/

## 💬 Usage

Run the chatbot with:

    python main.py

Start chatting with Gio, your personal marketing strategist.
Type "exit" or "quit" to end the session.

## ✨ Example Conversation
 
    You: Help me improve my email campaign open rates.  
    Assistant: To boost open rates, start with compelling subject lines using urgency or curiosity. Personalization also helps...
  
## 📌  Notes

- The default model is `mistralai/mistral-small-3.2-24b-instruct-2506:free` via OpenRouter  
- You can change the model in `main.py` 
- Modify or expand the system prompt in `chat_history` for custom behavior  
