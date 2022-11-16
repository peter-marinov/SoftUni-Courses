def stock_availability(stock, *args):
    if args[0] == 'delivery':
        stock.extend(args[1:])
    elif args[0] == 'sell':
        if len(args) > 1:
            if str(args[1]).isdigit():
                for _ in range(args[1]):
                    stock.pop(0)
            else:
                for item in args[1:]:
                    while item in stock:
                        stock.remove(item)
        else:
            stock.pop(0)
    return stock

print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
