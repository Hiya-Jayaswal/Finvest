import google.generativeai as genai

API_KEY = "AIzaSyCZg8rEBIZYKchotxqWEkgo5-fcGqVIrv4"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(model_name="gemini-1.0-pro")

chat = model.start_chat(history=[])

instruction = "Identify yourself as Arya, a financial AI. Respond to user queries with a financial lens, even if non-financial also give me advice based on it and provide me the current data of stock prices of the companies. Educate and empower users with financial knowledge, providing full but short and crisp information."

print("Arya: Hi, I'm Arya, your virtual financial advisor. How can I assist you today?")

while True:
    question = input("You: ")

    if question.strip().lower() == 'quit':
        print("Arya: Goodbye!")
        break
    elif "who are you" in question.lower():
        print("Arya: I am Arya, a financial advisor.")
    else:
        response = chat.send_message(instruction + ' ' + question)
        print(f"Arya: {response.text}")
        