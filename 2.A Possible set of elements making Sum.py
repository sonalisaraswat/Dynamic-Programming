def HowSum(TargetSum, Arr, Table):

    if TargetSum in Table:
        return Table[TargetSum]

    if TargetSum == 0:
        return []

    if TargetSum < 0:
        return None

    for ele in Arr:
        remainder = TargetSum - ele
        result = HowSum(remainder, Arr, Table)
        if result is not None:
            result.append(ele)
            Table[TargetSum] = result
            return result

    Table[TargetSum] = None
    return None


Table = {}
Arr = [7,5,4,3]
TargetSum = 14
print(HowSum(TargetSum, Arr, Table))   # output: [7, 7]
