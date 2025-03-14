from functions import analyze_stocks
from helpers import get_stock_list

tickers = get_stock_list()
stock_data = analyze_stocks(tickers)

print(stock_data)
input("Press Enter to exit...")