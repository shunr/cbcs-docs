import math
n = int(input())

def isprime(n):
  if n == 2:
    return True
  elif (n <= 1 or n % 2 == 0):
    return False
  rt = int(math.sqrt(n));
  for i in range(3, rt + 1, 2):
    if (n % i == 0):
      return False
  return True

for i in range(n):
  s = 0
  ub = [int(k) for k in input().split()]
  for j in range(ub[0], ub[1]):
    if isprime(j):
      s += 1
  print(s)