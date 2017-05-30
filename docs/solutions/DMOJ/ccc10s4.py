from heapq import *

inf = 9999
n = int(input())
seen = {}
edges = []
for i in range(n):
  cage = [int(j) for j in input().split()]
  for j in range(cage[0]):
    edge = frozenset()
    if j < cage[0] - 1:
      edge = frozenset((cage[j+1], cage[j+2]))
    else:
      edge = frozenset((cage[j+1], cage[1]))
    weight = cage[cage[0] + j + 1]
    if edge in seen.keys():
      edges.append((weight, (i, seen[edge][0])))
      seen[edge] = (-1, 0)
    else:
      seen[edge] = (i, weight)
edges.sort()
def kruskal(edges, n):
  tree = set()
  a, (b,c) = edges[0]
  tree.add(b)
  tree.add(c)
  s = a
  while len(tree) < n:
    done = True
    
    for i in range(1, len(edges)):
      w, e = edges[i]
      if (e[0] not in tree and e[1] in tree) or (e[1] not in tree and e[0] in tree):
        s += w
        tree.add(e[0])
        tree.add(e[1])
        done = False
        break
    if done:
      s = 99999
      break
  return s

a = kruskal(edges, n)
for edge in seen:
  x, w = seen[edge]
  if x != -1:
    edges.append((w, (x, -1)))
edges.sort()
b = kruskal(edges, n + 1)
print(min(a, b))