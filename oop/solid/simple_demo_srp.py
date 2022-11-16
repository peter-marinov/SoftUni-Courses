# Read numbers separated by a ' ' and print they sum
# Modification 1: print their sum divided by 2
# Modification 2: if the sum is odd, printed divided by 2 otherwise divided by 3
# Modification 3: Return the result, not print it

def my_sum(numbers):
    the_sum = sum(numbers)
    if the_sum % 2 == 0:
        return the_sum / 2
    else:
        return the_sum / 3


numbers = [int(x) for x in input().split()]
print(my_sum(numbers))