alph = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
n = int(input())
for i in range(n):
  k = 0
  s = input().split()
  for w in s:
    if list(w)[0] in alph:
      k += 1
  print(k)