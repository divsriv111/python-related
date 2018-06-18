def maxset(a):
    arr_set=[]
    arr_sum=[]
    temp=temp1=[]
    for item in a:
        if item>=0:
            temp.append(item)
        elif item<=0 and temp!=[]:
            arr_set.append(temp)
            arr_sum.append(sum(temp))
            temp=[]
    index=arr_sum.index(max(arr_sum))
    occurence=arr_sum.count(max(arr_sum))
    if occurence>1:
        last=0
        for i in range(occurence):
            last=arr_sum.index(max(arr_sum[last:]))
            temp1.append(len(arr_set[arr_sum.index[last]]))
        occurence1=temp1.count(max(temp1))
    else:
        return arr_set[index]

print(maxset([1, 2, 5, -7, 2, 3]))
print(maxset([-1, 2, 5, -7, 2, 3]))
