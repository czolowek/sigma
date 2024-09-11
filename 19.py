with open("input.txt", "r", encoding="utf-8") as file:
    string = file.read()

name = string [::-1]

with open("output.txt", "w", encoding="utf-8") as fh:
    fh.write(name)






