# Find if Target string can be formed from given small strings
def CanStr(TargetStr, SmallStrs, Table):

    if TargetStr in Table:
        return Table[TargetStr]

    if TargetStr == '':                                                 # no suffix left to check all prefix matched, so return True.
        return True

    for strg in SmallStrs:
        if TargetStr.startswith(strg):                                   # if any string is the prefix of target, remove it and check for rest of suffix.
            suffix = TargetStr[len(strg):]
            if CanStr(suffix, SmallStrs, Table) == True:                 # CanStr() only return True / False.
                Table[suffix] = True
                return True

    Table[TargetStr] = False
    return False


# Start
TargetStr = 'abcdef'
SmallStrs = ['abc', 'de', 'ab', 'cde','f']
Table = {}
print(CanStr(TargetStr, SmallStrs, Table))                                #True
print(Table)                                                              #{'': True, 'f': True, 'def': True}


# WORKING:  abcdef = abc + def (matched prefix; now recur for suffix )
#           def    = de + f    (matched prefix; now recur for suffix )
#           f      = f + ''    (matched prefix; now recur for suffix )
#           '' returns True
