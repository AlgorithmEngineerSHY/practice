a='sssseeee'
from itertools import groupby
a=groupby(a)
print(a)
for i,j in a:
    print(i)
    print(list(j))