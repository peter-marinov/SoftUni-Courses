username = input()
password = input()

data = input()

while data != password:
    data = input()

print(f"Welcome {username}!")