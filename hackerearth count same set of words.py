from sys import stdin,stdout
import re

def count(word):
    word=[x for x in re.split('\W',word) if x]
    new=[]
    for i in word:
        new.append(''.join(sorted(i)))
    return new
    
arr=[]
test=int(stdin.readline())
for x in range(test):
    word=stdin.readline()
    arr.extend(count(word))
    
high=0
for i in arr:
    flag=arr.count(i)
    if flag>=high:
        high=flag
    

stdout.write(str(high)+'\n')
