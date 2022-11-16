import os

directory = input()
extensions = {}

for filename in os.listdir(directory):
    file = os.path.join(directory, filename)

    if os.path.isfile(file):
        extension = filename.split('.')[-1]

        if extension not in extensions:
            extensions[extension] = []

        extensions[extension].append(filename)

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in extensions:
    print(f".{extension}")

    for file in sorted(files):
        print(f"- - - {file}")