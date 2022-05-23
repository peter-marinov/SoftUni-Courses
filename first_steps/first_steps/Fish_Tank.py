a = int(input())
b = int(input())
c = int(input())
procent = float(input())

obem = a * b * c * 0.001
zaet_obem = obem * procent / 100
water_volum = obem - zaet_obem

print(water_volum)