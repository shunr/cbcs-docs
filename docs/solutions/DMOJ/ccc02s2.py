n = int(input())
d = int(input())

for i in range(max(n, d), 0, -1):
  if n % i == 0 and d % i == 0:
    n /= i
    d /= i
    break
  
if d == 1:
  print(str(int(n)))
else:
  kek = int(n/d)
  print(((str(kek) + " ") if kek > 0 else "") + str(int(n % d)) + "/" + str(int(d)))