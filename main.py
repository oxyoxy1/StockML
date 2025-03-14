import matplotlib.pyplot as plt
from helpers import get_stock_list
from functions import analyze_stocks
from ml_model import train_stock_model, predict_stock_price

def visualize_stocks(stock_data):
    """Plots stock prices with moving averages."""
    print("Visualizing stock data...")
    plt.figure(figsize=(10, 5))
    for ticker, data in stock_data.items():
        plt.plot(data.index, data["Close"], label=f"{ticker} Close Price")
        if f"MA_10" in data:
            plt.plot(data.index, data["MA_10"], linestyle="dashed", label=f"{ticker} MA_10")

    plt.legend()
    plt.title("Stock Prices & Moving Averages")
    plt.show()

def main():
    try:
        print("Fetching stock list...")
        tickers = get_stock_list()
        print(f"Tickers: {tickers}")

        print("Analyzing stocks...")
        stock_data = analyze_stocks(tickers)
        print(f"Stock data: {stock_data}")

        visualize_stocks(stock_data)

        for ticker, data in stock_data.items():
            print(f"Training model for {ticker}...")
            model = train_stock_model(data)
            if model:
                print(f"Model trained for {ticker}. Predicting price...")
                prediction = predict_stock_price(model, data)
                if prediction:
                    print(f"Predicted next close for {ticker}: ${prediction:.2f}")
                else:
                    print(f"No prediction for {ticker}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

    input("Press Enter to exit...")  # Keeps window open

if __name__ == "__main__":
    main()

