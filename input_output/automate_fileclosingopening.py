name = input("what's the name ?   ")

with open("text.txt", "a") as file:
    file.write(f"{name}\n")