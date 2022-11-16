from math import floor


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return 'value is not a float'
        return cls(floor(float_value))

    @classmethod
    def from_roman(cls, num):
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i, c in enumerate(num):
            if (i + 1) == len(num) or roman_numerals[c] >= roman_numerals[num[i + 1]]:
                result += roman_numerals[c]
            else:
                result -= roman_numerals[c]
        return cls(result)

    @classmethod
    def from_string(cls, value):
        error_message = 'wrong type'
        if not isinstance(value, str):
            return error_message
        try:
            number = int(value)
            return cls(number)
        except:
            return error_message


num = Integer.from_roman('IV')
print(num.value)
