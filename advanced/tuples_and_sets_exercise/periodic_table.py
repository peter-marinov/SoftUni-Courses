lines = int(input())

unique_elements = set()

for _ in range(lines):
    current_set = set(input().split())
    unique_elements = unique_elements.union(current_set)

print('\n'.join(unique_elements))