from sys import stdin,stdout
stdin=open('in','r')
stdout=open('out','w')

test=int(stdin.readline())
for x in range(test):
    exp=stdin.readline()

    if exp.find('+')!=-1:
        lst=exp.split('+')
        l1=len(lst[0])
        l2=len(lst[1])-1
        sum=int(lst[0])+int(lst[1])
        l3=len(str(sum))
        stdout.write(' '*(l3+1-l1)+lst[0]+'\n')
        stdout.write(' '*(l3-l2)+'+'+lst[1])
        stdout.write('-'*(l3+1)+'\n')
        stdout.write(' '+str(sum)+'\n\n')
    elif exp.find('-')!=-1:
        lst=exp.split('-')
        l1=len(lst[0])
        l2=len(lst[1])
        diff=int(lst[0])-int(lst[1])
        l3=len(str(diff))
        temp=max(l1,l2,l3)
        stdout.write(' '*(temp-l1)+lst[0]+'\n')
        stdout.write(' '*(temp-l2)+'-'+lst[1])
        stdout.write('-'*(temp)+'\n')
        stdout.write(' '*(temp-l3)+str(diff)+'\n\n')
    elif exp.find('*')!=-1:
        lst=exp.split('*')
        l1=len(lst[0])
        l2=len(lst[1])
        result=int(lst[0])*int(lst[1])
        l3=len(str(result))
        temp=max(l1,l2,l3)
        if l1==1 and l2==2:
            stdout.write(' '+lst[0]+'\n')
            stdout.write('*'+lst[1])
            stdout.write('-'*(temp)+'\n')
            stdout.write(' '*(2-l3)+str(result)+'\n\n')
            continue
        else:
            stdout.write(' '*(l3-l1)+lst[0]+'\n')
            stdout.write(' '*(l3-l2)+'*'+lst[1])
            stdout.write(' '*(l3-temp)+'-'*(temp)+'\n')
        if l2==2:
            stdout.write(str(result)+'\n\n')
        else:
            for i,ch in enumerate(lst[1][-2::-1]):
                rst=int(ch)*int(lst[0])
                l=len(str(rst))
                stdout.write(' '*(l3-l-i)+str(rst)+'\n')
            stdout.write('-'*l3+'\n')
            stdout.write(str(result)+'\n\n')


