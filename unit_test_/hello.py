def main():
    x= input("Enter your name: ")
    print(hello(x))

def hello(to="world"):
  #  print( "hello,", to)# this function prints only not returns anything hence it would be called in other program it would not work
    return f"hello, {to}"

if __name__ == "__main__":
    main()