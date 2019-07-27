a="abcbbbbcccbdddadcb"
dic={}
l=[]
e=0
s=0
k=2
a=input("Enter a string:")
k=int(input("K distinct element:"))
maxlen=0
wins=0
wine=1
#check for length of string
while e<len(a):
    c=a[e]
    #increment the value of keys 
    if c in dic.keys():
        dic[c]=dic[c]+1
    else:
        #store char of string which are unique as keys 
        dic[c]=1
    #check whether dic exceed the k distinct number
    while len(dic)>k:
        c=a[s]
        dic[c]=dic[c]-1
        #delete the keys when it become zero 
        if dic[c]==0:
            del dic[c]
        #store the bounds of substring
        if wine-wins<e-s+1:
            wins=s
            wine=e
        s=s+1
    maxlen=max(maxlen,e-s+1)
    e=e+1
print(maxlen)

print("Largest", k ,"unique substring:",a[wins:wine])
