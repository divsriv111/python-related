file=open('test.txt','r')
n=int(input('enter number of lines you want to read: '))
for x in file:
    if n==0:
        break
    print(x)
    n-=1
file.close()
