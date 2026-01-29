
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "AMZN": 3300,
    "MSFT": 320
}

total_investment = 0
portfolio_details = []

print("Available Stocks:", ", ".join(stock_prices.keys()))

while True:
    stock_name = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        portfolio_details.append(f"{stock_name} - {quantity} shares = ${investment}")
        print(f"Added {stock_name} investment: ${investment}")
    else:
        print("Stock not found in price list!")

print("\n----- Portfolio Summary -----")
for item in portfolio_details:
    print(item)

print(f"\nTotal Investment Value: ${total_investment}")


save_choice = input("\nDo you want to save the result to a file? (yes/no): ").lower()

if save_choice == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("------------------------\n")
        for item in portfolio_details:
            file.write(item + "\n")
        file.write(f"\nTotal Investment Value: ${total_investment}")

    print("Portfolio saved to portfolio.txt")
else:
    print("Program finished without saving.")
