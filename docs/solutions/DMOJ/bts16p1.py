g = input()
n = list(g)
up = 0
low = 0
for l in n:
  if l == l.upper():
    up += 1
  if l == l.lower():
    low += 1

if low > up:
  print(g.lower())
elif up > low:
  print(g.upper())
else:
  print(g)