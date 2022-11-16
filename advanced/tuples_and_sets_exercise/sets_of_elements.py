n, m = map(int, input().split())

n_set = set()
m_set = set()
final_set = set()

for _ in range(n):
    n_set.add(int(input()))

for _ in range(m):
    m_set.add(int(input()))

final_set = n_set.intersection(m_set)

for number in final_set:
    print(number)