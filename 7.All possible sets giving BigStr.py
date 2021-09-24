def allCon(Target, Arr, Table):
    if Target in Table:
        return Table[Target]

    if Target == '':
        return [[]]

    B = None

    for strg in Arr:
        if Target.startswith(strg):
            suf = Target[len(strg):]
            val = allCon(suf,Arr,Table)
            if val is not None:
                for row in val:
                    row.insert(0, strg)
                if B is None:
                    B = val[:][:]
                else:
                    B.append(val[:][:])
                print(B)
                if Target == fin:
                    allPossible.append(B[:][:])
    h = str(B)
    Table[h] = B
    return B
Target = 'abcdef'
Arr = ['ab','cd','e','f','ef','a','b']
fin = Target
allPossible = []
Table = {}
allCon(Target, Arr,Table)
print(allPossible[:][:])
print(Table)
