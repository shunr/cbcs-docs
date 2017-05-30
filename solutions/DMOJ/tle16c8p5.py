from collections import *
SINK = 42069
n, m = map(int, input().split())
wanted = set()
graph = defaultdict(list, {0: [], SINK:[]})

edges = {}
for g in [int(i) for i in input().split()][1:]:
  wanted.add(g)
for i in range(1,n):
  girls = [int(i) for i in input().split()][1:]
  graph[0].append(i)
  graph[i].append(0)
  edges[(0, i)] = 1
  edges[(i, 0)] = 0
  for x in girls:
    if x in wanted:
      g = x + n
      graph[i].append(g)
      graph[g].append(i)
      graph[SINK].append(g)
      graph[g].append(SINK)
      edges[(i, g)] = 1
      edges[(g, i)] = 0
      edges[(g, SINK)] = 1
      edges[(SINK, g)] = 0
    
def bfs(G, E, s, t, parent):
  visited = set([s])
  q = deque([s])
  while q:
    x = q.popleft()
    if x == t:
      return True
    for n in G[x]:
      if n not in visited and E[(x, n)] > 0:
        q.append(n)
        visited.add(n)
        parent[n] = x
  return False

def ford(G, E, src, sink):
  parent = {}
  flow = 0
  while bfs(G, E, src, sink, parent):
    flow += 1
    x = sink
    while(x !=  src):
      p = parent[x]
      E[(p, x)] -= 1
      E[(x, p)] += 1
      x = p
  return flow
  
print(len(wanted) - ford(graph, edges, 0, SINK))