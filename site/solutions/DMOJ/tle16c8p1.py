binder = set(list(input())[1:])
n = int(input())
for i in range(n):
  x = set(list(input())[1:])
  dank = True
  for g in binder:
    if g not in x:
      print("no")
      dank = False
      break
  if dank:
    print("yes")