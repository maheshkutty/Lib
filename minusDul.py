a=[1,2,3,4,56]
b=[4,8,9,1,5,89]
def minusDuplicate(a,b):
    for i in b:
        for j in a:
            if i==j:
                a.remove(j)
    return a
print(minusDuplicate(a,b))
a=set(a)
b=set(b)
print(a.difference(b))
