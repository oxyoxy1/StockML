import yfinance as yf

def get_existing_tickers():
    """Reads the current tickers from helpers.py and returns them as a list."""
    helpers_path = 'helpers.py'
    
    try:
        with open(helpers_path, 'r') as file:
            content = file.read()
        
        # Extract the tickers from the return statement manually
        start_index = content.find('return [') + len('return [')
        end_index = content.find(']', start_index)
        tickers_str = content[start_index:end_index]
        
        # Clean up and split the tickers
        tickers_list = [ticker.strip().strip('"') for ticker in tickers_str.split(',')]
        return tickers_list
        
    except FileNotFoundError:
        print(f"Error: {helpers_path} not found.")
        return []

def validate_tickers(ticker_list):
    """Validates if tickers correspond to real stocks."""
    valid_tickers = []
    invalid_tickers = []
    
    for ticker in ticker_list:
        try:
            stock = yf.Ticker(ticker)
            stock.history(period="1d")  # Check if data exists for the ticker
            valid_tickers.append(ticker)
        except Exception:
            invalid_tickers.append(ticker)
    
    return valid_tickers, invalid_tickers

def update_helpers(new_tickers):
    """Updates helpers.py with the new tickers list."""
    helpers_path = 'helpers.py'
    
    try:
        with open(helpers_path, 'r') as file:
            lines = file.readlines()

        # Update the return statement to include the new list of tickers
        for i, line in enumerate(lines):
            if "return [" in line:
                updated_tickers_str = ', '.join(f'"{ticker}"' for ticker in sorted(set(new_tickers)))
                lines[i] = f"    return [{updated_tickers_str}]\n"
        
        # Write the updated tickers back into helpers.py
        with open(helpers_path, 'w') as file:
            file.writelines(lines)
    
    except FileNotFoundError:
        print(f"Error: {helpers_path} not found.")

def main():
    # Display current tickers
    existing_tickers = get_existing_tickers()
    print("Current tickers in the system:")
    if existing_tickers:
        print(", ".join(existing_tickers))
    else:
        print("No existing tickers found.")
    print()

    # User input for new tickers
    tickers_input = input("Please enter stock tickers (separated by a comma and space): ")
    tickers = [ticker.strip().upper() for ticker in tickers_input.split(",")]

    # Combine old and new tickers, removing duplicates
    combined_tickers = list(set(existing_tickers + tickers))

    # Validate tickers
    valid_tickers, invalid_tickers = validate_tickers(combined_tickers)

    if valid_tickers:
        print(f"Valid tickers: {', '.join(valid_tickers)}")
        update_helpers(valid_tickers)
        print("The helpers.py file has been updated with the new tickers!")
    else:
        print("No valid tickers were entered.")
    
    if invalid_tickers:
        print(f"Invalid tickers: {', '.join(invalid_tickers)}")

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
