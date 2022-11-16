# words = input().split()
# [print(f'{word * len(word)}', end='') for word in words]

print(''.join(map(lambda word: word * len(word), input().split())))