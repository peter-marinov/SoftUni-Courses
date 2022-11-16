def shopping_cart(*food_cart):
    def limit(meal):
        if meal == 'Soup':
            if len(food_dict[meal]) < soup_limit:
                return True
        elif meal == 'Pizza':
            if len(food_dict[meal]) < pizza_limit:
                return True
        elif meal == 'Dessert':
            if len(food_dict[meal]) < dessert_limit:
                return True
        return False

    def food_sort(food_dict):
        result_str = ''
        products_exists = False
        for some_product in food_dict.values():
            # print(f'----{some_product}')
            if len(some_product) > 0:
                products_exists = True
                break
        if products_exists:
            sorted_dict = dict(sorted(food_dict.items(), key=lambda x: (-len(x[1]), x[0])))
            for key, values in sorted_dict.items():
                result_str += f'{key}:\n'
                sorted_values = sorted(values)
                for value in sorted_values:
                    result_str += f' - {value}\n'
        else:
            result_str += "No products in the cart!"
        return result_str

    soup_limit = 3
    pizza_limit = 4
    dessert_limit = 2

    food_dict = {'Soup': [], 'Pizza': [], 'Dessert': []}
    for food in food_cart:
        if food == 'Stop':
            result = food_sort(food_dict)
            return result

        meal, product = food
        # if meal not in food_dict:
        #     food_dict[meal] = []
        if product not in food_dict[meal] and limit(meal):
            food_dict[meal].append(product)
    result = food_sort(food_dict)
    return result


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))