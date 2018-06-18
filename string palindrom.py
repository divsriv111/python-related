import re,string
def isPalindrome(A):
    A=A.replace(' ','')
    A=A.lower()
    exclude = set(string.punctuation)
    A = ''.join(ch for ch in A if ch not in exclude)
    A=[x for x in A]
    temp=A[::-1]
    l=len(A)
    for i in range(l):
        if temp[i]!=A[i]:
            return 0        #not palindrom
    return 1            #is palindrom

print(isPalindrome('race car'))
