from dotenv import load_dotenv
import requests
import os
import json

load_dotenv()

chat_history = [
    {"role": "system", "content": "Your name is Gio. You are an expert marketing specialist with deep knowledge of digital marketing, branding, copywriting, SEO, and customer psychology. You are results-driven, data-informed, and creative. Your job is to help users craft effective marketing strategies, compelling copy, high-performing ad campaigns, customer personas, content calendars, and growth plans. You communicate clearly, professionally, and with strategic insight. Always explain your reasoning and suggest best practices tailored to the target audience and business goals."}
]

def ask_ai():
  response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}"
    },
    data=json.dumps({
      "model": "mistralai/mistral-small-3.2-24b-instruct-2506:free",
      "messages": chat_history
    })
  )
  if response.status_code == 200:
    reply = response.json()['choices'][0]['message']['content']
    print("\nAssistant:", reply)
    chat_history.append({"role": "assistant", "content": reply})
  else:
    print("Error:", response.status_code, response.text)


if __name__ == "__main__":
    print("OpenRouter Chat (type 'exit' to quit)")

    while True:
        user_input = input("\nYou: ")
        if user_input.strip().lower() in ["exit", "quit"]:
            break
        chat_history.append({"role": "user", "content": user_input})
        ask_ai()
