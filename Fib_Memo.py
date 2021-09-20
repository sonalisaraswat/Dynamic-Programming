# Function definition
def fib(n, Table):
  
    # just pick value from Table (if present)
    if n in Table:
        return Table[n]
      
    # Fill Table once for each value of n
    else:
        Table[n] = fib(n-1, Table) + fib(n-2, Table)
        
    return Table[n]

  
# START
Table = {0: 0, 1: 1, 2: 1}   # Memo = dict to store fib number

print(fib(6, Table))   # 8
print(fib(50, Table))  #12586269025
