import re


str = "Shashi Ahirwar"
print(str[::-1])


def reverseString(s):
    result=""
    for ch in s:
         result = ch + result
    return result

print(reverseString("Shashi Ahirwar"))