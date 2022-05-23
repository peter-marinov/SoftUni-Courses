num_himikali = int(input())
num_markeri = int(input())
litri_preparat = int(input())
discount = int(input())

himikal_price = 5.80
markeri_price = 7.20
preparat_price = 1.20 # per l

sum = num_himikali * himikal_price + num_markeri * markeri_price + \
      litri_preparat * preparat_price

discount_price = sum * discount / 100
final_price = sum - discount_price
print(final_price)