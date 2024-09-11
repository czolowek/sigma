string = "алабаламага села на крильцо почесать свое яйцо"

count = 0
char = ""

for c in string:
    if count < string.count(c):
        count = string.count(c)
        char = c

print(f"Символ '{char}' зустрічається в нашому речені '{count}' разів")