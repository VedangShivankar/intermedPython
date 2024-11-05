"""
stock_prices = []
with open("stock prices.csv", "r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = str(tokens[1])
        stock_prices.append([day, price])
print(stock_prices)

"""
#section 2

stock_prices = {}
with open("stock prices.csv", "r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices[day] = price
print(stock_prices)


