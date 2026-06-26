# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 150
}

# Variable to store total investment value
total_investment = 0

print("===== Stock Portfolio Tracker =====")

# Number of stocks user wants to add
num_stocks = int(input("Enter the number of stocks you want to add: "))

# List to store portfolio details
portfolio_details = []

# Taking stock details from user
for i in range(num_stocks):
    print(f"\nStock {i + 1}")

    stock_name = input("Enter Stock Symbol (AAPL, TSLA, GOOGL, MSFT, AMZN): ").upper()

    # Check if stock exists in price dictionary
    if stock_name not in stock_prices:
        print("Invalid Stock Symbol! Please choose from the available stocks.")
        continue

    quantity = int(input("Enter Quantity: "))

    # Calculate investment for current stock
    investment = stock_prices[stock_name] * quantity

    # Add to total investment
    total_investment += investment

    # Store stock details
    portfolio_details.append([
        stock_name,
        quantity,
        stock_prices[stock_name],
        investment
    ])

# Display Portfolio Summary
print("\n===== Portfolio Summary =====")

for stock in portfolio_details:
    print(
        f"Stock: {stock[0]} | "
        f"Quantity: {stock[1]} | "
        f"Price: ${stock[2]} | "
        f"Investment: ${stock[3]}"
    )

print(f"\nTotal Investment Value: ${total_investment}")

# Save portfolio summary to a text file
with open("portfolio_summary.txt", "w") as file:
    file.write("===== Stock Portfolio Summary =====\n\n")

    for stock in portfolio_details:
        file.write(
            f"Stock: {stock[0]} | "
            f"Quantity: {stock[1]} | "
            f"Price: ${stock[2]} | "
            f"Investment: ${stock[3]}\n"
        )

    file.write(f"\nTotal Investment Value: ${total_investment}")

print("\nPortfolio summary has been saved to 'portfolio_summary.txt'")