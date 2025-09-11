def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        try:
            n = int(input("what is n? "))
            if n > 0:
                return n
        except ValueError:
            print("Please enter a valid integer.")
def meow(n):
    for _ in range(n):
        print("Meow!")

main()