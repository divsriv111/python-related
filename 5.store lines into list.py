file=open('check.txt','r')
w=[]
w=file.readlines()
w=[i.strip('\n') for i in w]
print(w)
file.close()
