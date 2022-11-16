
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    output_num = 0
    numbers = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CM': 900,
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    for key, value in numbers.items():
        if key in s:
            output_num += s.count(key) * value
            s = s.replace(key, '')
            print(key, output_num, s)
        if s == '':
            break


    return output_num

print(romanToInt('MCMXCIV'))