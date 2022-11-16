def products_check(stock_dict: list, search_products: list):
    for item in search_products:
        if item in stock_dict:
            print(f"We have {stock_dict.get(item)} of {item} left")
        else:
            print(f"Sorry, we don't have {item}")

data = input().split(' ')
search_products = input().split(' ')

stock_dict = {data[i]: int(data[i + 1]) for i in range(0, len(data), 2)}
products_check(stock_dict, search_products)

