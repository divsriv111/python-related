from sys import stdout,stdin
test=int(stdin.readline())
for x in range(test):
    a,b=stdin.readline().split()
    a=int(a[::-1])
    b=int(b[::-1])
    sum=a+b
    stdout.write(str(int(str(sum)[::-1]))+"\n")
