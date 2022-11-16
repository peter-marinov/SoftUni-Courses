def shopping_list(budget, **kwargs):
    result = ''
    product_type = 0
    if budget < 100:
        return "You do not have enough budget."

    for key, values in kwargs.items():
        if product_type == 5:
            return result

        money_needed = values[0] * values[1]
        if money_needed <= budget:
            budget -= money_needed
            result += f'You bought {key} for {money_needed:.2f} leva.\n'
            product_type += 1

    return result


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))