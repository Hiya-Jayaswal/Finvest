import pandas as pd
import yfinance as yf
from tabulate import tabulate
pd.set_option('display.max_columns', None)

stock_symbols = ['^BSESN', '^NSEI', "^NSEBANK"]


stock_data = []
for symbol in stock_symbols:
    try:
        
        stock = yf.Ticker(symbol)
        
        # DATA FOR THE MOST RECENT DAY
        historical_data = stock.history(period="3d")
        
        # CHECK IF DATA EXIST
        if historical_data.empty:
            print(f"No data found for {symbol}. Skipping.")
            continue
        
        # GET LATEST PRICE
        price = historical_data['Close'].iloc[-1]
        
        # CLOSING
        if len(historical_data) > 1:
            prev_close = historical_data['Close'].iloc[-2]
        else:
            prev_close = price  
        
        # Extract the latest OHLC (Open, High, Low, Close) for the most recent day
        latest_ohlc = historical_data[['Open', 'High', 'Low', 'Close']].iloc[-1]
        
        # Add to the list of stock data
        stock_data.append({
            'Stock Symbol': symbol,
            'Current Price': price,
            'Previous Close': prev_close,
            'Open': latest_ohlc['Open'],
            'High': latest_ohlc['High'],
            'Low': latest_ohlc['Low'],
            'Close': latest_ohlc['Close']
        })
        
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")

# Convert to a DataFrame for better readability
df = pd.DataFrame(stock_data)

# Ensure that data exists before sorting
if not df.empty:
    

    
    print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))
else:
    print("No valid data fetched.")
