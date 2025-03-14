from helpers import fetch_stock_data

data = fetch_stock_data("AAPL")
print(data.head())

input("Press Enter to exit...")