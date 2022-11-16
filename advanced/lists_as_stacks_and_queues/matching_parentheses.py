expression = input()

stack = []

for idx in range(len(expression)):
    ch = expression[idx]
    if ch == '(':
        stack.append(idx)
    elif ch == ')':
        last_opening_bracket_idx = stack.pop()
        sub_expression = expression[last_opening_bracket_idx:idx + 1]
        print(sub_expression)