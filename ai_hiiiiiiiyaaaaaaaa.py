import google.generativeai as genai

API_KEY = "AIzaSyCZg8rEBIZYKchotxqWEkgo5-fcGqVIrv4"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(model_name="gemini-1.0-pro")

chat = model.start_chat(history=[])

def remove_asterisks(text):
    return text.replace('*', '')

def info(question):
    instruction = "Identify yourself as Arya, a financial AI. Respond to user queries with a financial lens."

    if question.strip().lower() == 'quit':
        print("Arya: Goodbye!")
        return
        
    elif "who are you" in question.lower():
        print("Arya: I am Arya, a financial advisor.")
    else:
        response = chat.send_message(instruction + ' ' + question)
        cleaned_response = remove_asterisks(response.text)
        print(f"Arya: {cleaned_response}")
        
    return f"Arya: {cleaned_response}"


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        info(user_input)
