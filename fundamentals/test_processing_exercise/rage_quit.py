text = input().upper()

unique_symbols = ''
current_symbol = ''
repetitions = ''

for index in range(len(text)):
    if not text[index].isdigit():
        current_symbol += text[index]
    else: #symbol is digit - time to multiply
        for check_next_symbols in range(index, len(text)):
            if not text[check_next_symbols].isdigit():
                break
            repetitions += text[check_next_symbols]
        repetitions = int(repetitions)
        unique_symbols += repetitions * current_symbol
        current_symbol = ''
        repetitions = ''

print(f"Unique symbols used: {len(set(unique_symbols))}")
print(unique_symbols)
