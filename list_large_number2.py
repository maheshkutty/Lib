l=[3,40,34,5,9]
b=[]
a=max(l)
a=len(str(a))
#below function increment lenght of item
def calP(item,a):
    pr=str(item)
    for i in range(a):
        if pr==a:
            break
        if len(pr)<a: 
            pr=pr+str(int(item))
    return pr
for i in range(len(l)):
    b.append(calP(l[i],a))
#sorting of value
for i in range(len(b)):
    for j in range(len(b)):
        if b[i]>b[j]:
            temp=l[i]
            temp1=b[i]
            l[i]=l[j]
            b[i]=b[j]
            b[j]=temp1
            l[j]=temp
#make as string
def listToString(b):
    s=""
    for i in b:
        s=s+str(i)
    return s
print("Largest Possible value:",listToString(l))
        
