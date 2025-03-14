# Ticker Program

A Python-based program that analyzes stock tickers, visualizes stock data, and predicts stock prices using machine learning. This project includes a GUI menu built with Tkinter, allowing users to:
- Edit stock tickers.
- Run stock analysis and visualize data.
- Purge tickers from the helper file.

## Features
- **Ticker Editing**: Add or modify stock tickers using a simple UI.
- **Stock Analysis**: Fetches stock data and performs analysis (e.g., moving averages).
- **Stock Prediction**: Trains a machine learning model and predicts future stock prices.
- **Purging Tickers**: Option to remove all tickers from the helper file.

## Requirements
- Python 3.x
- Libraries:
  - `yfinance`
  - `pandas`
  - `matplotlib`
  - `sklearn`
  - `tkinter`
  - `tabulate`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/oxyoxy1/StockML.git

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the program:
   ```bash
   python menu.py