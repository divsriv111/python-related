def solve(A):
    A=A.replace(' ','')
    l=len(A)
    count=0
    for i in range(l):
        if i==int(l/2):
            continue
        if A[-1]!=A[0]:
            return l-1
        if A[l-1-i]!=A[i]:
            count+=1
    return count

print(solve("adpooefxzbcoejuvpvaboygp"))
#print(len("adpooefxzbcoejuvpvaboygp"))

print(solve("babb"))
