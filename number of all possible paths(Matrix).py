# Start

#...............USING RECURSION.......................

print("Enter the dimension: ")    # We can only go 'down' or 'right'

N = int(input())
M = int(input())
def NumPath(N,M):
  if(N == 1 or M == 1):
    return 1
  return NumPath(N-1, M) + NumPath(N, M-1)     # down + right
print(NumPath(N,M))





#...............USING MEMO.......................

def MatTrav (Row, Col, Table):

    key = str(Row) + ',' + str(Col)   # Eg. '1,1' or '3,2' used for key

    if key in Table:                  # USING MEMO
        return Table[key]

    if Row == 1 or Col == 1:          # BASE CONDITION { '1,1' : 1, '1,2' : 1, '2,1' : 1 } and so on
        return 1

    Table[key] = MatTrav(Row-1, Col, Table) + MatTrav(Row, Col-1, Table)   # UPDATE MEMO

    return Table[key]                # FINAL VALUE


N = 18
M = 18
Table = {}     # dict to store key (str) and value (int)
print(MatTrav(N, M, Table))



