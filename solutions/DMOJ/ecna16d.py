import sys
from heapq import *
from collections import defaultdict
inf = 987654321000

def input():
    return sys.stdin.readline()

n, m = [int(i) for i in input().split()]
graph = {"English": []}
costs = {}

for lang in input().split():
  graph[lang] = []
  
for i in range(m):
  a, b, c = input().split()
  graph[a].append(b)
  graph[b].append(a)
  costs[(a, b)] = int(c)
  costs[(b, a)] = int(c)

s = "English"

x = 0
q, visited = [(0, 0, s, s)], set()
while q:
  (dist, cost, v1, parent) = heappop(q)
  if v1 not in visited:
    visited.add(v1)
    if v1 != s:
      x += cost
    for v2 in graph[v1]:
      heappush(q, (dist + 1, costs[(v1, v2)], v2, v1))

if len(visited) != n + 1:
  print("Impossible")
else:
  print(x)