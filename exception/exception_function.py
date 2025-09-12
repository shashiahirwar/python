def main():
    x = get_int()
    print(f"x is a integer value: {x}")

def get_int():
    while True:
            try:
                return int(input("Enter a number: ")) # input() takes input as string, int() converts it to integer
                #similarly, you can use float() for decimal numbers
                #print(f"You entered:{x}") # the 'f' before the string allows for inline variable interpolation
            except ValueError:
                pass
main()
