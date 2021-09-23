# We can use elements of Array unlimited times.


def allCon(Target, Arr, Table):

    if Target in Table:
        return Table[Target]

    if Target == '':
        return ''

    B = None

    for a in Arr:
        if Target.startswith(a):
            suf = Target[len(a):]
            val = allCon(suf,Arr, Table)                # Returns either NONE or comma seperated elements(as single string)
            
            if val is not None:
                B = a+','+val
                
            if(Target == fin) and B is not None:       # place set only if parent is reached
                allPossible.append( B[:-1].split(',') )


    Table[Target] = B
    return B


# MAIN START

Target = 'abcdef'
Arr = ['abc','a','d','bcd','ef']
fin = Target
allPossible = []                                       # Array for storing; array of all possible sets making Target string.
Table = {}                                             # For MEMO
allCon(Target, Arr,Table)                              # Calling
print(allPossible)                                     # all sets are placed in 2D array T

# OUTPUT:
# [['abc', 'd', 'ef'], ['a', 'bcd', 'ef']]
