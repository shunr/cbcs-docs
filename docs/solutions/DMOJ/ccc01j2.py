x = int(input())
m = int(input())
kek = False
for i in range(m):
  if (x * i) % m == 1:
    print(i)
    kek = True
    break
  
if not kek:
  print("No such integer exists.")