import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def get_stock_data(symbol):
    """Fetch stock data for the last 30 days."""
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    data = yf.download(symbol, start=start_date, end=end_date)
    return data

def plot_stock(data, symbol):
    """Plot closing price of the stock."""
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data['Close'], linewidth=2)
    plt.title(f"{symbol.upper()} Stock Prices (Last 30 Days)")
    plt.xlabel("Date")
    plt.ylabel("Closing Price (USD)")
    plt.grid(True)
    plt.show()

def main():
    print("📈 Welcome to the Stock Price Tracker!")
    symbol = input("Enter a stock symbol (e.g., AAPL, TSLA, MSFT): ").upper()

    try:
        data = get_stock_data(symbol)
        if data.empty:
            print("❌ No data found. Check the symbol and try again.")
        else:
            print(f"✅ Successfully fetched data for {symbol}.")
            plot_stock(data, symbol)
    except Exception as e:
        print("⚠️ Error fetching stock data:", e)

if __name__ == "__main__":
    main()
