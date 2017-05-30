import sys
import math
n, k = [int(sys.stdin.readline()) for i in range(2)]

grid = [[[0 for m in range(n-k+2)] for _k in range(k+1)] for _n in range(n+1)]

def pies(n, k, m):
  if grid[n][k][m] == 0:
    if k == 1 or n == k or m == n/k or n == k + 1:
      grid[n][k][m] = 1
    elif n > k:
      grid[n][k][m] = sum([pies(n-i,k-1, i) for i in range(int(math.ceil(n/k)), min(n-k+2, m+1))])
  return grid[n][k][m]
    
print(pies(n, k, n-k+1))