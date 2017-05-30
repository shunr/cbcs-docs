import math

a = int(input())
b = int(input())
s = 0

for i in range(math.ceil(a ** (1. / 3)), int(b ** (1. / 3))+2):
  if math.sqrt(i ** 3) == int(math.sqrt(i ** 3)):
    s += 1
    
print(s)