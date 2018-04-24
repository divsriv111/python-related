import datetime
with open('file1.txt','r') as f1,open('file2.txt','r') as f2,open('file3.txt','r') as f3:
    v1=f1.readlines()
    v2=f2.readlines()
    v3=f3.readlines()
    v1=[i.rstrip('\n') for i in v1]
    v2=[i.rstrip('\n') for i in v2]
    v3=[i.rstrip('\n') for i in v3]
    v1=str(v1)
    v2=str(v2)
    v3=str(v3)
    now=datetime.datetime.now()
    with open(now.strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt",'w') as ff1:
        ff1.write(v1+v1+v3)

