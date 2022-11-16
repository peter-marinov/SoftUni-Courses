import re

sentence = input()

pattern = r'(?<=\s)(([a-z0-9]+[\.\-\_a-z0-9]*)@[a-z\-]+(\.[a-z]+)+)\b'

results = re.findall(pattern, sentence)

for result in results:
    print(result[0])