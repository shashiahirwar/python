def main():
    x = int(input("Enter a number to square: ")) #input from user
    print(f"The square of {x} is {square(x)}")


def square(number):
    return number + number

if __name__ == "__main__":
    main()

