n = int(input())
a = int(input())
b = int(input())
c = int(input())
s = 0
while True:
  n -= 1
  s += 1
  a += 1
  if a % 35 == 0:
    n += 30
  if n == 0:
    break
  n -= 1
  s += 1
  b += 1
  if b % 100 == 0:
    n += 60
  if n == 0:
    break
  n -= 1
  s += 1
  c += 1
  if c % 10 == 0:
    n += 9
  if n == 0:
    break
  
print("Martha plays " + str(s) + " times before going broke.")