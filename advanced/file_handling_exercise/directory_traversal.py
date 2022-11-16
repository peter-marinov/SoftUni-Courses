import os
import re

directory = input()
output_file = './files/report.txt'
output = []
extensions = {}
pattern = r"[\\/]"
dir_length = len(re.split(pattern, directory))

for dir_files in os.walk(directory):
    if len(re.split(pattern, dir_files[0])) > dir_length + 1:
        continue

    for filename in dir_files[2]:
        file = os.path.join(directory, filename)

        if '.' in file:
            extension = filename.split('.')[-1]

            if extension not in extensions:
                extensions[extension] = []
            extensions[extension].append(filename)

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in extensions:
    output.append(f'.{extension}\n')

    for file in sorted(files):
        output.append(f'--- {file}\n')

with open(output_file, 'w') as file:
    file.write("".join(output))