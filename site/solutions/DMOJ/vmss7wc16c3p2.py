n, m, a, b = [int(i) for i in input().split()]
graph = [[] for i in range(n+1)]
q = [a]
visited = []
for i in range(m):
  road = [int(r) for r in input().split()]
  graph[road[0]].append(road[1])
  graph[road[1]].append(road[0])
shahir = False

while q:
  for h in q:
    if h == b:
      print("GO SHAHIR!")
      shahir = True
      del q[:]
      break
    q.remove(h)
    visited.append(h)
    for g in graph[h]:
      if g not in visited:
        q.append(g)
      
if not shahir:
  print("NO SHAHIR!")