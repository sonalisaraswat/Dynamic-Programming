def allCon(Target, Arr):
    if Target == '':
        return [[]]
    B = None
    for strg in Arr:
        if Target.startswith(strg):
            suf = Target[len(strg):]
            val = allCon(suf,Arr)
            if val is not None:
                for row in val:
                    row.insert(0, strg)
                if B is None:
                    B = val[:][:]
                else:
                    for row in val:
                        B.append(row)

    return B
Target = 'abcdef'
Arr = ['ab','cd','e','f','ef','a','b']
print(allCon(Target, Arr))

# OUTPUT: [['ab', 'cd', 'e', 'f'], 
#          ['ab', 'cd', 'ef'], 
#          ['a', 'b', 'cd', 'e', 'f'], 
#          ['a', 'b', 'cd', 'ef']]
