"Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables."
"Global variables can be used by everyone, both inside of functions and outside."

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

y= "awesome"

def myfunc():
    global z
    z= "test"
    y= "fantastic"
    print("python is ", y)

myfunc()
#To create a global variable inside a function, you can use the global keyword.
print("python is so ", y, z)
#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

