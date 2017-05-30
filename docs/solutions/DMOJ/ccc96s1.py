def kek(n):
  return sum([i if n % i == 0 else 0 for i in range(1, n)])

for i in range(int(input())):
  n = int(input())
  gg = kek(n)
  if gg == n:
    print(str(n) + " is a perfect number.")
  elif gg > n:
    print(str(n) + " is an abundant number.")
  else:
    print(str(n) + " is a deficient number.")