a=["hello","world","in","a","frame"]
l=len(max(a))
def stylePrint(a,l):    
    for i in range(len(a)):
        if i==0:
            s="*"*l+"**"
            print(s)
        sp=l-len(a[i])
        sp=" "*sp+"*"
        print("*"+a[i]+sp)
    print(s)
stylePrint(a,l)
