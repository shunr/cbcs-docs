import math
n = int(input())
i = int(math.sqrt(n))
while n % i != 0:
  i -= 1
print (int(i + n/i) * 2)