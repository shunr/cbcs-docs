import math
a = int(input())

def isprime(n):
  if n == 2:
    return True
  elif n % 2 == 0 or n <= 1:
    return False
  for i in range(3, int(math.sqrt(n)), 2):
    if n % i == 0:
      return False
  return True

while True:
  if isprime(a):
    print(a)
    break
  else:
    a += 1