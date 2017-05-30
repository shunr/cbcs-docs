c, m = (int(i) for i in input().split())
kek = [[0 for i in range(m + 1)] for j in range(c + 1)]
    
for i in range(1, c+1):
  v, k = (int(i) for i in input().split())
  for j in range(m+1):
    dank = 0;
    if k <= j:
      dank = kek[i-1][j-k] + v
    kek[i][j] = max(kek[i-1][j], dank)
    
print(kek[c][m])