import pandas as pd

def calculate_moving_average(data, window=10):
    """Calculates the moving average of a stock."""
    # Calculate the moving average and add as a new column
    data[f"MA_{window}"] = data["Close"].rolling(window=window).mean()

    # Drop NaN values (rows where MA cannot be calculated)
    return data.dropna()

def analyze_stocks(tickers):
    """Fetch and analyze multiple stocks."""
    from helpers import fetch_stock_data
    results = {}

    for ticker in tickers:
        data = fetch_stock_data(ticker)
        if not data.empty:
            data = calculate_moving_average(data)
            results[ticker] = data
    return results
