stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOGLE": 140
}
total_amount = 0
print("Stock Portfolio Tracker")
number_of_stocks = int(input("How many stocks do you want to enter? "))
for i in range(number_of_stocks):
    stock_name = input("Enter Stock Name : ").upper()
    quantity = int(input("Enter Quantity : "))
    if stock_name in stock_prices:
        amount = stock_prices[stock_name] * quantity
        print("Value of", stock_name, "=", amount)
        total_amount += amount
    else:
        print("Stock Not Found")
print("\nTotal Investment Value =", total_amount)
file = open("portfolio_result.txt", "w")
file.write("Total Investment Value = " + str(total_amount))
file.close()
print("Result Saved Successfully")



