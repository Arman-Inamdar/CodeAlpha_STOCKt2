
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 3300,
    "MSFT": 310
}


portfolio = {}

print("Enter your stock investments. Type 'done' to finish.")

while True:
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found in price list. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        if quantity <= 0:
            raise ValueError
    except ValueError:
        print("Invalid quantity. Enter a positive integer.")
        continue
    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Calculation of total investment
total_investment = 0
print("\nYour Investment Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    print(f"{stock} - Quantity: {qty}, Price: ${stock_prices[stock]}, Value: ${value}")
    total_investment += value

print(f"\nTotal Investment Value: ${total_investment}")

# Optional: Save to a file
save = input("\nDo you want to save the result to a file? (yes/no): ").lower()
if save == "yes":
    filename = input("Enter filename (with .txt or .csv): ")
    with open(filename, "w") as f:
        f.write("Stock,Quantity,Price,Value\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            f.write(f"{stock},{qty},{price},{value}\n")
        f.write(f"\nTotal Investment Value,,,{total_investment}")
    print(f"Data saved to {filename}")
