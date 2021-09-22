# Counts total ways the Small Strings, can be used to get Target String
# A Small String can be used any number of times

def CountStr(TargetStr, SmallStrs, Table):

    if TargetStr in Table:
        return Table[TargetStr]

    if TargetStr == '':
        return 1

    totalCount = 0

    for strg in SmallStrs:
        if TargetStr.startswith(strg):                  # if any string is the prefix of target, remove it and check for rest of suffix
            #SmallStr.remove(strg)                      # used if we 'do not' want to 'reuse' the str once it is used from SmallStrs.
            suffix = TargetStr[len(strg):]

            ways = CountStr(suffix, SmallStrs, Table)   # CountStr return '1' or '0'(totalcount=0)
            totalCount += ways

    Table[TargetStr] = totalCount
    return totalCount


                                                        # Start
TargetStr = 'enterapotentpot'
SmallStrs = ['a', 'p', 'ent', 'enter','ot','o','t']
Table = {}
print(CountStr(TargetStr, SmallStrs, Table))             # 4
print(Table)                                   # {'erapotentpot': 0, 't': 1, 'ot': 2, 'pot': 2, 'entpot': 2, 'tentpot': 2, 'otentpot': 4, 'potentpot': 4, 'apotentpot': 4, 'enterapotentpot': 4}
