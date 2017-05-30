n = int(input())
k = int(input())
g = n % k
if k > n:
  print(k-n)
else:
  print(min(g, k - g))