def main():
    print_square(3)


def print_square(n):
    for i in range(n):
        
        for j in range(n):
            print("#", end="")
        print()  # Move to the next line after printing one row

main()
