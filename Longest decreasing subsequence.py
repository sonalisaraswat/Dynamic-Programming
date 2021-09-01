def Lds(arr, n):
    lds = [1]*n
    for i in range(n):
        for j in range(i):
            if(arr[i] < arr[j] and lds[i] < lds[j]+1):
                lds[i] = lds[j]+1
    return max(lds)
arr = [int(x) for x in input("Input the array to find the longest decreasing subsequence: ").split(" ")]
n =len(arr)
print(Lds(arr, n))
