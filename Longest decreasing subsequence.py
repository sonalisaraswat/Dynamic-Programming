def Lds(arr, n):
    lds = [1]*n
    max = 0
    for i in range(n):
        for j in range(i):
            if(arr[i]<arr[j] and lds[i]<lds[j]+1):
                lds[i] = lds[j]+1
    for i in range(n):
        if(max < lds[i]):
            max = lds[i]
    return max
arr = int(x for x in input("Input the array to find the longest decreasing subsequence: ").split())
n =len(arr)
print(Lds(arr, n))
