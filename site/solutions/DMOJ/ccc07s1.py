months = [31,28,31,30,31,30,31,31,30,31,30,31]

for _ in range(int(input())):
  y, m, d = [int(i) for i in input().split()]
  k = 9999 * (2007-18) + sum(months[:2]) + 27
  
  print("Yes" if 9999 * y + sum(months[:m]) + d <= k else "No")