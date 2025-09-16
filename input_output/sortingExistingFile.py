from itertools import count


name = []
with open("/Users/shashi/Documents/Project/python3/input_output/name.txt") as file:
    for line in file:
        name.append(line.rstrip())

for n in sorted(name, reverse=True):
    print(f"hello, {n}")
    if n.count(lin)