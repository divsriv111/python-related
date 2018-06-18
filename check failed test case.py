f1=open('out','r')
f2=open('expected','r')
count=1
while count!=80:
    if f1.readline()!=f2.readline():
        print(count)
    count+=1
