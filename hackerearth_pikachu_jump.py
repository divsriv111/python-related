from sys import stdin,stdout
test=int(stdin.readline())
for x in range(test):
    n=int(stdin.readline())
    arr=stdin.readline()
    arr=[int(x) for x in arr.split(' ')]
    b=[]
    a=[0]
    a.extend(arr)
    for i in range(1,n):
        b.append(a[i]-a[i-1])
    stdout.write(str(max(b))+'\n')
