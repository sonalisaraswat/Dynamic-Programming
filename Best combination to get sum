def BestSum(TargetSum, Arr, Table):
    if TargetSum in Table:
        return Table[TargetSum]

    if TargetSum == 0:
        return ''

    if TargetSum < 0:
        return None

    smallcombi = None
    for ele in Arr:
        remainder = TargetSum - ele
        result = BestSum(remainder, Arr, Table)
        if result is not None:
            combi = result+' '+str(ele)
            if smallcombi is None or len(combi) < len(smallcombi):
                smallcombi = combi


    Table[TargetSum] = smallcombi
    return Table[TargetSum]


Table = {}
Arr = [5,3,4,7]
TargetSum = 7                             # {3,4} and {7}.......here answer is {7}
print(BestSum(TargetSum, Arr, Table))
print(Table)
