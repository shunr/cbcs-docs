import sys
from heapq import *
inf = sys.maxsize

# YEAH BOI
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
          heappush(q, (newd, v2))
          if d[v2] > newd:
            d[v2] = newd
  return d

def input():
  return sys.stdin.readline().strip()
  
def get_neighbors(G, x, y, k, h):
  n = []
  dank = G[(x, y)] > h
  if x > 0 and abs(G[(x, y)] - G[(x-1, y)]) <= 2:
    succ = 0
    if dank or G[(x-1, y)] > h:
      succ = 1
    n.append((x-1,y, succ))
  if x < k - 1 and abs(G[(x, y)] - G[(x+1, y)]) <= 2:
    succ = 0
    if dank or G[(x+1, y)] > h:
      succ = 1
    n.append((x+1,y, succ))
  if y > 0 and abs(G[(x, y)] - G[(x, y-1)]) <= 2:
    succ = 0
    if dank or G[(x, y-1)] > h:
      succ = 1
    n.append((x,y-1, succ))
  if y < k - 1 and abs(G[(x, y)] - G[(x, y+1)]) <= 2:
    succ = 0
    if dank or G[(x, y+1)] > h:
      succ = 1
    n.append((x,y+1, succ))
  return n 
  
for _ in range(int(input())):
  n = int(input())
  graph = {}
  dp = {}
  edges = {}
  for i in range(n):
    for j in range(n):
      graph[(i, j)] = int(input())
      dp[(i, j)] = []
  height = graph[(0,0)]
  for x, y in dp:
    dank = get_neighbors(graph, x, y, n, height)
    dp[(x, y)] = [(v[0], v[1]) for v in dank]
    for coord in dank:
      edges[((x,y),(coord[0],coord[1]))] = coord[2]
  kek = djik(dp, edges, (0,0))[(n-1, n-1)]
  print(kek if kek != inf else "CANNOT MAKE THE TRIP")
  print("")