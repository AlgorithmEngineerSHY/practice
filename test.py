from functools import cmp_to_key

a=[[1,2],[1,3],[0,1]]

def nmsl(x,y):
    if y[1] != x[1]:
        return x[1] - y[1]
    else:
        return x[0] - y[0]

b=sorted(a, key=cmp_to_key(nmsl))
print(b)