num = 5

is_prime = True
for i in range(2,num-1):
    if (num%i == 0):
        is_prime = False
        break
print(f"this a prime {num}")