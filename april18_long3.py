from sys import stdin,stdout

test=int(stdin.readline())
for x in range(test):
    l=[]
    old=''
    ips,n=stdin.readline().split(' ')
    if ips.count('a') > ips.count('b'):
        ips*=int(n)
        for i in ips:
            tmp=''
            if i=='a':
                old+=i
                l.append(old)
            else:
                tmp=old+i
                if tmp.count('a') > old.count('a'):
                    old+=i
                    l.append(old)
                else:
                    old+=i
    print(l)
