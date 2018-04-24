file=open('test.txt','r')
w=file.readlines()
w=[i.rstrip('\n') for i in w]
lengh=len(w)
ip=int(input('enter number of lines : '))
for x in range(lengh-ip,lengh):
    print(w[x])
file.close()
