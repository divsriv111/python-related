import re
from collections import Counter
def pre_processing(str1,str2):
    '''Function to remove spaces and punctuations'''
    str1=str1.lower()
    str2=str2.lower()
    str1=[x for x in re.split('\W',str1) if x]
    str2=[x for x in re.split('\W',str2) if x]
    return (str1,str2)

def count(x):
    '''Function to count frequency of each words'''
    a=[]
    for i in x:
        for j in i:
            a.append(j)
    a=Counter(a)
    return a

def check_anagram(str1,str2):
    '''Function to check if anagram, prints true or false'''
    s1,s2=pre_processing(str1,str2)
    set1=count(s1)
    set2=count(s2)
    print(set1==set2)

test=[['dog','god'],['clint eastwood','old west action'],['aa','bb'],
      ['go go go','gggooo'],['abc','cba'],['hi man','hi    man'],['aabbcc','aabbc'],
      ['123','1 2'],['public relations......','crap built on lies'],['d og','god']]
for x in test:
    check_anagram(x[0],x[1])
