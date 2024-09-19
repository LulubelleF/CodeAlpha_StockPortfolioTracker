import yfinance as yf

# Step 1: Create a dictionary to store stock portfolio
portfolio = {}

# Step 2: Function to add stocks to the portfolio
def add_stock(stock_symbol, quantity):
    # Validate the stock symbol before adding it
    if validate_stock_symbol(stock_symbol):
        if stock_symbol in portfolio:
            portfolio[stock_symbol] += quantity
        else:
            portfolio[stock_symbol] = quantity
        print(f"Added {quantity} shares of {stock_symbol} to the portfolio.")
    else:
        print(f"Error: {stock_symbol} is not a valid stock symbol or data could not be fetched.")

# Step 3: Function to remove stocks from the portfolio
def remove_stock(stock_symbol, quantity):
    if stock_symbol in portfolio:
        if portfolio[stock_symbol] > quantity:
            portfolio[stock_symbol] -= quantity
            print(f"Removed {quantity} shares of {stock_symbol} from the portfolio.")
        elif portfolio[stock_symbol] == quantity:
            del portfolio[stock_symbol]
            print(f"Removed {stock_symbol} entirely from the portfolio.")
        else:
            print(f"Error: You only own {portfolio[stock_symbol]} shares of {stock_symbol}.")
    else:
        print(f"Error: {stock_symbol} is not in your portfolio.")

# Step 4: Function to fetch real-time stock data using yfinance
def fetch_stock_data(stock_symbol):
    stock = yf.Ticker(stock_symbol)
    stock_info = stock.history(period="1d")
    
    # Check if valid data is returned
    if stock_info.empty:
        print(f"Error: Unable to fetch data for {stock_symbol}. Please check the stock symbol.")
        return None
    else:
        current_price = current_price = stock_info['Close'].iloc[0]
        return current_price

# Step 5: Function to validate if the stock symbol exists
def validate_stock_symbol(stock_symbol):
    stock = yf.Ticker(stock_symbol)
    stock_info = stock.history(period="1d")
    
    # If data is empty, the symbol is invalid or delisted
    if stock_info.empty:
        return False
    return True

# Step 6: Function to view the portfolio and its value
def view_portfolio():
    total_value = 0
    print("\nYour Portfolio:")
    print("-----------------------------")
    for stock_symbol, quantity in portfolio.items():
        current_price = fetch_stock_data(stock_symbol)
        if current_price:
            stock_value = current_price * quantity
            total_value += stock_value
            print(f"{stock_symbol}: {quantity} shares @ ${current_price:.2f} each = ${stock_value:.2f}")
    print(f"-----------------------------\nTotal Portfolio Value: ${total_value:.2f}")

# Step 7: Menu to interact with the tracker
def menu():
    while True:
        print("\n--- Stock Portfolio Tracker ---")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            stock_symbol = input("Enter the stock symbol (e.g., AAPL): ").upper()
            quantity = int(input("Enter the number of shares: "))
            add_stock(stock_symbol, quantity)

        elif choice == "2":
            stock_symbol = input("Enter the stock symbol to remove (e.g., AAPL): ").upper()
            quantity = int(input("Enter the number of shares to remove: "))
            remove_stock(stock_symbol, quantity)

        elif choice == "3":
            view_portfolio()

        elif choice == "4":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")

# Step 8: Run the tracker
if __name__ == "__main__":
    menu()