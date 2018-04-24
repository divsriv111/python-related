from sys import stdin,stdout
test=int(stdin.readline())
for i in range(test):
    l,m=stdin.readline().split(' ')
    count=0
    l=int(l)
    m=int(m)
    while True:
        if l > m:
            stdout.write(str(count)+'\n')
            break
        else:
            l*=3
            m*=2
            count+=1
