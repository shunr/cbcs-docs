from collections import Counter
from sys import stdin
alph = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ*")
ok = [[] for _ in range(26)]
roads = []

while True:
  g = stdin.readline().strip()
  k = [alph.index(i) for i in list(g)]
  if k[0] == 26:
    break
  ok[k[0]].append(k[1])
  ok[k[1]].append(k[0])
  roads.append(g)
  
q = [[0]]
done = []
paths = 0

def findpaths(path):
  global done
  global ok
  if path[-1] == 1:
    done.append(path)
    return
  for i in ok[path[-1]]:
    if i not in path:
      findpaths(path + [i])

findpaths([0])

kek = []
for p in done:
  paths += 1
  for j in range(len(p)-1):
    kek.append(alph[p[j]]+alph[p[j+1]])
    
s = 0
c = Counter(kek)
for d in c:
  if c[d] >= paths:
    #if d not in roads:
    #  print(d[::-1])
    #else:
    print(d)
    s += 1
    
print("There are " + str(s) + " disconnecting roads.")