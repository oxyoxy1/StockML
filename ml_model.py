import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def train_stock_model(data):
    """Trains a machine learning model to predict stock prices."""
    if data.isna().sum().sum() > 0:
    	print("NaN values present, cleaning data...")
    	data = data.dropna()
    if len(data) < 20:
    	print("Not enough data to train model.")
    	return None

    # Prepare features and labels
    data["Future_Close"] = data["Close"].shift(-1)  # Predict next day's close
    data.dropna(inplace=True)  # Ensure no NaN values in training data

    X = data[["Open", "High", "Low", "Volume"]]
    y = data["Future_Close"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Train the model
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train, y_train)

    # Print model performance on test set
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Model trained. Mean Squared Error: {mse:.2f}")

    return model

def predict_stock_price(model, latest_data):
    """Predicts the next day's closing price using the trained model."""
    if model and not latest_data.empty:
        X_latest = latest_data[["Open", "High", "Low", "Volume"]].iloc[-1:].values
        return model.predict(X_latest)[0]
    return None
