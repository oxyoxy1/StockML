import yfinance as yf

def get_stock_list():
    """Returns a list of popular stock tickers."""
    return ["AAPL", "AMZN", "BON", "DOCU", "GOOGL", "META", "MSTR", "NVDA", "QBTS", "RBRK", "RGTI", "TSLA"]

def fetch_stock_data(ticker, period="12mo"):
    """Fetches historical stock data for a given ticker."""
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    
    if data.empty:
        print(f"Warning: No data found for {ticker}")
    return data