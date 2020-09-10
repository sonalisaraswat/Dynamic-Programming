# Coin change problem using Dynamic Programming.
# A python program that takes the coins' denominations as integers.
# Total amount to be made "using least number of coins" as integers.
# Outputs the total number of coins to be needed, assuming we have many coins of each denomination.
# Also the denominations of those coins.
# Time complexity = O(total*(length of coins array));
# Space complexity = O(total)

print("First line of input should be space seperated denomination of coins used.")
print("Second line is the single integer value for amount.")

coins = [int(x) for x in input().split(" ")] # Space seperated denominations of coins
total = int(input())   # Total amount as integral value

def make(coins, total):
    c = len(coins)
    Amt = total + 1
    T = [float('inf') for i in range(Amt)]
    T[0] = 0
    R = [-1 for i in range(Amt)]
    for i in range(c):
        for j in range(Amt):
            if(j >= coins[i]):
                if((1 + T[j - coins[i]]) < T[j]):
                    T[j] = 1 + T[j - coins[i]]
                    R[j] = i
    print("Total coins used are ", T[total])
    k = total
    print("Demonitions used are: ")
    while(k != 0):
        dem = R[k]
        print(coins[dem])
        k = k - coins[dem]

make(coins, total) # Calling the function.

