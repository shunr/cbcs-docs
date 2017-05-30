import sys
from heapq import *
inf = sys.maxsize

def input():
  return sys.stdin.readline()

n, m = [int(i) for i in input().split()]
graph = {}
for i in range(m):
  a, b = [int(_) for _ in input().split()]
  if a not in graph.keys():
    graph[a] = []
  graph[a].append(b)
a, b = [int(_) for _ in input().split()]

def taller(G, a, b):
  q = [a]
  visited = set()
  while q:
    x = q.pop()
    if x not in G.keys():
      continue
    if b in G[x]:
      return True
      break
    for g in G[x]:
      if g not in visited:
        q.append(g)
    visited.add(x)
  return False
  
if taller(graph, a, b):
  print("yes")
elif taller(graph, b, a):
  print("no")
else:
  print("unknown")