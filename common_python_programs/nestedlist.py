import copy
from copy import deepcopy


a = [0, ['a','b'],2]
b = a.copy()
c = deepcopy(a)
c[1][0]='shashi'

print(a,b,c)