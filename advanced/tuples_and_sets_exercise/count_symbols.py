text = input()

unique_symbols = set()
symbols_dict = {}

for symbol in text:
    if symbol not in symbols_dict.keys():
        symbols_dict[symbol] = 0
    symbols_dict[symbol] += 1

for key in sorted(symbols_dict.keys()):
    print(f'{key}: {symbols_dict[key]} time/s')

