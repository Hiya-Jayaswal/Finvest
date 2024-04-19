import google.generativeai as genai
import requests
from bs4 import BeautifulSoup

API_KEY = "AIzaSyCZg8rEBIZYKchotxqWEkgo5-fcGqVIrv4"

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


def price(ticker, exchange="NSE"):
    ticker = ticker.upper()
    exchange = exchange.upper()
    url = f"https://www.google.com/finance/quote/{ticker}:{exchange}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    class1 = "YMlKec fxKbKc"
    price = (soup.find(class_=class1)).text.replace("₹", "")
    name = soup.find(class_="zzDege").text
    print(price)


def name(ticker, exchange="NSE"):
    ticker = ticker.upper()
    exchange = exchange.upper()
    url = f"https://www.google.com/finance/quote/{ticker}:{exchange}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    name = soup.find(class_="zzDege").text
    print(name)
