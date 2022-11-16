import os

while True:
    command = input().split("-")

    if command[0] == "End":
        break

    if command[0] == "Create":
        file = open(f"./files/{command[1]}", "w")
        file.close()

    elif command[0] == "Add":
        with open(f"./files/{command[1]}", "a") as file:
            file.write(f"{command[2]}n")

    elif command[0] == "Replace":
        try:
            with open(f"./files/{command[1]}", "r+") as file:
                lines = file.readlines()

            for i in range(len(lines)):
                lines[i] = lines[i].replace(command[2], command[3])

            with open(f"./files/{command[1]}", "w") as file:
                file.write("".join(lines))

        except FileNotFoundError:
            print("An error occurred")

    elif command[0] == "Delete":
        try:
            os.remove(f"./files/{command[1]}")
        except FileNotFoundError:
            print("An error occurred")

