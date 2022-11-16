def price_calculator(product: str, quantity: int):
    total_price = 0
    if product == "coffee":
        total_price = quantity * 1.5
    elif product == "coke":
        total_price = quantity * 1.4
    elif product == "water":
        total_price = quantity * 1
    elif product == "snacks":
        total_price = quantity * 2
    return f'{total_price:.2f}'

wanted_product = input()
product_quantity = int(input())

sum = price_calculator(wanted_product, product_quantity)
print(sum)


# def price_calculator(product: str, quantity: int):
#     price = 0
#     if product == "coffee":
#         price = 1.5
#     elif product == "coke":
#         price = 1.4
#     elif product == "water":
#         price = 1
#     elif product == "snacks":
#         price = 2
#     return f'{price * quantity:.2f}'
#
# wanted_product = input()
# product_quantity = int(input())
#
# sum = price_calculator(wanted_product, product_quantity)
# print(sum)