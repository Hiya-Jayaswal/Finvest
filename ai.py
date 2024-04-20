import google.generativeai as genai
import requests
from bs4 import BeautifulSoup
import os 

load_dotenv()

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(model_name="gemini-1.0-pro")

chat = model.start_chat(history=[])


def ai(question):
    instruction = (
        "respond to the questions in short but crisp and with full information"
    )

    if question.strip().lower() == "quit":
        print("Chanakya: Goodbye!")

        # Check if the question contains stock-related keywords
    stock_keywords = [
        "hello",
        "stock",
        "market",
        "company",
        "investment",
        "portfolio",
        "finance",
        "NASDAQ",
        "NYSE",
        "S&P",
        "Dow Jones",
        "index",
        "help",
        "saving",
        "advice",
    ]
    response = {}
    response["text"] = ""
    if any(keyword in question.lower() for keyword in stock_keywords):
        response = chat.send_message(instruction + " " + question)
        print(f"Bot: {response.text}")
        instruction = ""
    else:
        response["text"] = (
            "Chanakya: Please ask a question related to the stock market."
        )
    return response.text


def price(ticker):
    ticker = ticker.upper()
    url = f"https://www.google.com/finance/quote/{ticker}:NSE"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    price = soup.find(class_="YMlKec fxKbKc").text
    return price


def name(ticker):
    ticker = ticker.upper()
    url = f"https://www.google.com/finance/quote/{ticker}:NSE"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    name = soup.find(class_="zzDege").text
    return name



