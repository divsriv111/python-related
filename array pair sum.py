def pair_sum(arr,sum):
    new=[]
    for i in arr:
        try:
            j=arr[arr.index(sum-i)]
            k=(i,j)
            if k not in new:
                new.append(k)
        except:
            continue
    return new

pair_sum([1,2,3,2],5)



