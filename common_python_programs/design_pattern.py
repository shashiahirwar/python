thikness=int(input())
c='H'
for i in range(thikness):
    print((c * i).rjust(thikness - 1) + c + (c * i).ljust(thikness - 1))

# Top pillars
for i in range(thikness + 1):
    print((c * thikness).center(thikness * 2) + (c * thikness).center(thikness * 6))

# Middle belt
for i in range((thikness + 1) // 2):
    print((c * thikness * 5).center(thikness * 6))

# Bottom pillars
for i in range(thikness + 1):
    print((c * thikness).center(thikness * 2) + (c * thikness).center(thikness * 6))

# Bottom cone
for i in range(thikness):
    print(((c * (thikness - i - 1)).rjust(thikness) + c + 
           (c * (thikness - i - 1)).ljust(thikness)).rjust(thikness * 6))