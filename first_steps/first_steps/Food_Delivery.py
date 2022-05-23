chicken_menus = int(input())
fish_menus = int(input())
vege_menus = int(input())

chicken_menus_price = chicken_menus * 10.35
fish_menus_price = fish_menus * 12.40
vege_menus_price = vege_menus * 8.15

menus_price = chicken_menus_price + fish_menus_price + vege_menus_price
desert_price = menus_price * 0.20
delivery_price = 2.50

final_price = menus_price + desert_price + delivery_price
print(final_price)