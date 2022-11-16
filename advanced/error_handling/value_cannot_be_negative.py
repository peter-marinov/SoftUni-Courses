class ValueCannotBeNegative(Exception):
    """Value is below 0"""
    

for i in range(5):
    number = int(input())

    if number < 0:
        raise ValueCannotBeNegative
