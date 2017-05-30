from sys import stdin

r, c = [int(_) for _ in stdin.readline().strip().split()]
cages = []
for _ in range(int(stdin.readline())):
    cages.append(tuple(int(_) for _ in stdin.readline().strip().split()))
  
dp = [[0 for i in range(c)] for j in range(r)]
dp[0][0] = 1
for i in range(r):
    for j in range(c):
        if dp[i][j] == 0:
            s = 0
            if (i, j+1) not in cages:
                s+=dp[i-1][j]
            if (i+1, j) not in cages:
                s+=dp[i][j-1]
            dp[i][j] = s
                
print(dp[r-1][c-1])