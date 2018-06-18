from sys import stdin,stdout
ops=['(','+','-','*','/','^',')']
test=int(stdin.readline())
for x in range(test):
    op_arr=[]
    count=-1
    first=0
    s=stdin.readline()
    for ch in s:
        if ch not in ops:
            stdout.write(ch)
        elif ch in ops and ch==')':
            while(True):
                if op_arr==[]:
                    break
                if op_arr[count]=='(':
                    op_arr.pop()
                    count-=1
                    break
                else:
                    stdout.write(op_arr.pop())
                    count-=1
        else:
            if ch=='(':
                op_arr.append(ch)
                count+=1
                continue
            if ch in ops:
                if first==0:
                    op_arr.append(ch)
                    count+=1
                    first=1
                elif ops.index(ch) > ops.index(op_arr[count]):
                    op_arr.append(ch)
                    count+=1
                else:
                    while(True):
                        if op.arr==[]:
                            break
                        if ops.index(op_arr[count])<ops.index(ch):
                            op_arr.append(ch)
                            count+=1
                        else:
                            stdout.write(op_arr.pop())
                            count-=1
    while(op_arr!=[]):
        stdout.write(op_arr.pop())
        count-=1
    #stdout.write('\n')
