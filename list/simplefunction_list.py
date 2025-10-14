from ctypes import sizeof


l=[1, 2, 2]
print(2 in l)
print(len(l))
l.append(3)
print(l)
l.remove(2)
print(l)

# Compute squares of even numbers from 0 to 9
squares = [x*x for x in range(10) if x % 2 == 0]
print(squares)
