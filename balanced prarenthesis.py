from sys import stdin,stdout
stdin=open('in','r')
stdout=open('out','w')
def test(ch):
    s=[]
    if len(ch)%2!=0 or ch[0] in ['}',']','}']:
        return 0
    opening=set('({[')
    matching=set([('(',')'),('{','}'),('[',']')])
    for i in ch:
        if i in opening:
            s.append(i)
        else:
            if len(s)==0:
                return 0
            if (s.pop(),i) not in matching:
                return 0
    return 1

t=int(stdin.readline())
for i in range(t):
    expression=stdin.readline().rstrip()
    if test(expression):
        stdout.write('YES\n')
    else:
        stdout.write('NO\n')
