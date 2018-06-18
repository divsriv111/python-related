def callme():
    a = list(input())
    b = list(input())
    l1=len(a)
    l2=len(b)
    if l1>l2:
        for i in range(l2):
            check=a.__contains__(b[i])
            if check:
                index=a.index(b[i])
                a[index]=''
                b[i]=''
    else:
        for i in range(l1):
            check=b.__contains__(a[i])
            if check:
                index=b.index(a[i])
                b[index]=''
                a[i]=''
    a=a+b
    a=[x for x in a if x]
    print(len(a))
callme()
