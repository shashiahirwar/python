with open("/Users/shashi/Documents/Project/python3/input_output/names.csv") as file:
    lines = file.readlines()
    for line in lines:
        name, fruit = line.rstrip().split(",")
        print(f"hello {name}, you like {fruit}")