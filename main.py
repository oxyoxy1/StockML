import matplotlib.pyplot as plt
from helpers import get_stock_list
from functions import analyze_stocks
from ml_model import train_stock_model, predict_stock_price
import pandas as pd
from tabulate import tabulate

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

def display_predictions(predictions):
    """Displays stock predictions in a table."""
    if predictions:  # Check if predictions list is not empty
        # Convert predictions to a DataFrame
        df = pd.DataFrame(predictions)
        print("\nStock Predictions Table:")
        print(tabulate(df, headers='keys', tablefmt='pretty'))
    else:
        print("\nNo predictions were made.")

def run_main_program():
    """Runs the main program (existing functionality)"""
    print("Running main program...")
    try:
        print("Fetching stock list...")
        tickers = get_stock_list()
        print(f"Tickers: {tickers}")

        print("Analyzing stocks...")
        stock_data = analyze_stocks(tickers)
        print(f"Stock data fetched and analyzed.")

        visualize_stocks(stock_data)

        predictions = []  # List to store predictions for the table

        for ticker, data in stock_data.items():
            print(f"Training model for {ticker}...")
            model = train_stock_model(data)
            if model:
                print(f"Model trained for {ticker}. Predicting price...")
                prediction = predict_stock_price(model, data)
                if prediction:
                    print(f"Predicted next close for {ticker}: ${prediction:.2f}")
                    predictions.append({"Ticker": ticker, "Predicted Next Close": f"${prediction:.2f}"})
                else:
                    print(f"No prediction for {ticker}")
        
        # Display predictions in a table format
        display_predictions(predictions)
        
    except Exception as e:
        print(f"An error occurred: {e}")

    input("Press Enter to exit...")  # Keeps window open

if __name__ == "__main__":
    run_main_program()
