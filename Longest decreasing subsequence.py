def Lds(arr, n):
    lds = [1]*n
    for i in range(n):    # i goes from 0 to n-1
        for j in range(i):   # j goes from 0 to i-1
            if(arr[j] > arr[i] and lds[i] < lds[j]+1):
                lds[i] = lds[j]+1
    return max(lds)
arr = [int(x) for x in input("Input the array to find the longest decreasing subsequence: ").split(" ")]
n =len(arr)
print(Lds(arr, n))
