import math

shape = input()

if shape == 'square':
    square_a = float(input())
    square_size = square_a * square_a
    print(f'{square_size:.3f}')
    # print(f'{a:.2f}')
elif shape == 'rectangle':
    rectangle_a = float(input())
    rectangle_b = float(input())
    area = rectangle_a * rectangle_b
    # print(f'{rectangle_size:.3f}')
elif shape == 'circle':
    circle_r = float(input())
    area = math.pi * (circle_r ** 2)
    # print(f'{circle_size:.3f}')
else: # triangle
    triangle_a = float(input())
    triangle_h = float(input())
    area = triangle_a * triangle_h / 2
    # print(f'{triangle_size:.3f}')

print(area)
