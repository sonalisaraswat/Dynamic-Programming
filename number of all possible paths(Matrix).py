print("Enter the dimension: ")
N = int(input())
M = int(input())
def NumPath(N,M):
  if(N == 1 or M == 1):
    return 1
  return NumPath(N-1, M) + NumPath(N, M-1)
print(NumPath(N,M))
