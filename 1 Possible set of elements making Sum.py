def HowSum(TargetSum, Arr, Table):

    if TargetSum in Table:
        return Table[TargetSum]

    if TargetSum == 0:
        return 'a'

    if TargetSum < 0:
        return None

    for ele in Arr:
        remainder = TargetSum - ele
        result = HowSum(remainder, Arr, Table)
        if result is not None:
            Table[TargetSum] = result+','+str(ele)
            return result+','+str(ele)

    Table[TargetSum] = None
    return None


Table = {}
Arr = [5,4,3,7]
TargetSum = 7
print(HowSum(TargetSum, Arr, Table))
