# Assuming that all elements in array are non-negative.
# We can use an element any number of times.
# Output True/ False ; if elements of given array can make up the given sum.

def CanSum(TargetSum, Arr, Table):

    if TargetSum in Table:
        return Table[TargetSum]
    if TargetSum == 0:
        return True
    if TargetSum < 0:
        return False

    for ele in Arr:
        remainder = TargetSum - ele
        if CanSum ( remainder, Arr, Table ) == True:   # if any case returns true; Table set to true for that reminder
            Table[TargetSum] = True                    # and also return true for original TargetSum
            print('true::' + str(TargetSum))
            return True

    Table[TargetSum] = False
    print('false::'+str(TargetSum))
    return False


Table = {}
Arr = [int(x) for x in input().split(' ')]
TargetSum = int(input())
print(CanSum(TargetSum, Arr, Table))
print(Table)
