import sys

if len(sys.argv) <1:
    print("too few arguments")
elif len(sys.argv) >1:
    print("too many arguments")

else:
    print("hello, my name is", sys.argv[1]) 