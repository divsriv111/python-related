var=str()
with open('check.txt','r') as f:
   w=f.readlines()
w=[i.rstrip('\n') for i in w]
for x in range(0,len(w)):
    var=var+str(w[x])
print(var)
