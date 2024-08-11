from datetime import datetime
import yfinance as yf
import matplotlib.pyplot as plt

def get_apple_stock_data():
    now = datetime.now()
    start_of_month = now.replace(day=1)
    apple_stock = yf.download('AAPL', start=start_of_month, end=now)
    apple_stock.index = apple_stock.index.strftime('%Y-%m-%d')
    stock_data = apple_stock.to_dict('index')
    return stock_data

def dividend():
    now = datetime.now()
    start_of_month = now.replace(day=1)
    
    print("Fetching stock data...")
    
    BATS = yf.download('BATS.L', start=start_of_month, end=now)
    LGEN = yf.download('LGEN.L', start=start_of_month, end=now)
    NG = yf.download('NG.L', start=start_of_month, end=now)
    PHNX = yf.download('PHNX.L', start=start_of_month, end=now)
    ULVR = yf.download('ULVR.L', start=start_of_month, end=now)
    
    print("Data fetched successfully. Now plotting...")
    
    plt.figure(figsize=(10, 6))
    plt.plot(BATS['Close'], label='BATS')
    plt.plot(LGEN['Close'], label='LGEN')
    plt.plot(NG['Close'], label='NG')
    plt.plot(PHNX['Close'], label='PHNX')
    plt.plot(ULVR['Close'], label='ULVR')
    
    plt.title('Stock Prices from Start of Month to Now')
    plt.xlabel('Date')
    plt.ylabel('Close Price (GBP)')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    plt.show()
    print("Plot displayed successfully.")

# Calling the dividend function to test it
dividend()
