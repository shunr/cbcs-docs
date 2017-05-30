from itertools import permutations
x = [1,2,3,4,5,6,7]
tasks = [(1,7), (1,4), (2,1), (3, 4), (3,5)]

while True:
  a = int(input())
  b = int(input())
  if a == 0 and b == 0:
    break
  tasks.append((a, b))

perms = list(permutations(x))
perms.sort()
gg = len(tasks)
ok = False
for p in perms:
  indices = [0 for i in range(8)]
  for i in range(7):
    indices[p[i]] = i
  passed = 0
  for t in tasks:
    if indices[t[0]] > indices[t[1]]:
      break
    else:
      passed += 1
  if passed >= gg:
    kek = ""
    for w in p:
      kek += str(w) + " "
    print(kek)
    ok = True
    break

if not ok:
  print("Cannot complete these tasks. Going to bed.")