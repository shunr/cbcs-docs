import sys
from heapq import *
inf = 987654321

def input():
    return sys.stdin.readline()

n, m = [int(i) for i in input().split()]
graph = {}
weights = {}
for i in range(m):
  a, b, c = [int(_) for _ in input().split()]
  
  if a not in graph.keys():
    graph[a] = []
  if b not in graph.keys():
    graph[b] = []
  graph[a].append(b)
  graph[b].append(a)
  if (a, b) not in weights.keys():
    weights[(a, b)] = c
    weights[(b, a)] = c
  else:
    weights[(a, b)] = min(c, weights[(a, b)])
    weights[(b, a)] = min(c, weights[(a, b)])

def djik(G, w, s):
  d = {}
  for i in G:
    d[i] = inf
  q, visited = [(0, s)], set() 
  d[s] = 0
  while q:
    (dist, v1) = heappop(q)
    if v1 not in visited:
      visited.add(v1)
      for v2 in G[v1]:
        if v2 not in visited:
          newd = dist + w[(v1, v2)]
          heappush(q, (dist + w[(v1, v2)], v2))
          if d[v2] > newd:
            d[v2] = newd
  return d

geomatics = djik(graph, weights, 1)
for i in range(1, n+1):
  print(geomatics[i] if i in geomatics.keys() and geomatics[i] < inf else -1)