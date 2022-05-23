country = input()

while country != "End":
    price_trip = float(input())
    sum_current_destination = 0
    while sum_current_destination < price_trip:
        saved_money = float(input())
        sum_current_destination += saved_money
        
    print(f"Going to {country}!")
    country = input()