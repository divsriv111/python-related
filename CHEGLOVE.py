t=int(input())
flag=''
for x in range(t):
    no_of_fingers=int(input())
    c_temp=input()
    s_temp=input()

    s_temp=s_temp.split(' ')
    c_temp=c_temp.split(' ')
    glove_finger=[int(x) for x in s_temp]
    chef_finger=[int(x) for x in c_temp]

    if glove_finger >= chef_finger:
        flag='front'
        glove_finger.reverse()
        print('after reversing',glove_finger)
        if glove_finger >= chef_finger:
            flag='both'
    else:
        glove_finger.reverse()
        if glove_finger >= chef_finger:
            flag='back'
        else:
            flag='none'
    print(flag)
