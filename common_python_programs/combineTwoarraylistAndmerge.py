

def mergelist(lista, listb):
    return sorted(set(lista+listb))

a = [2,4,6,6,7,3,3,9]
b = [3,4,6,74,3,23,2,2]
c =mergelist(a,b)
print(c)
