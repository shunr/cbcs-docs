from sys import stdin

n = int(stdin.readline())
graph = {}
g2 = [[] for i in range(n+1)]
paths = [0 for i in range(n+1)]
paths[1] = 1
while True:
  p = [int(_) for _ in stdin.readline().split()]
  if p[0] == 0:
    break
  #if p[0] not in graph.keys():
  #  graph[p[0]] = []
  #if p[1] not in g2.keys():
  #  g2[p[1]] = [] 
  #graph[p[0]].append(p[1])
  g2[p[1]].append(p[0])

def meme(node):
  global g2
  if node == 1:
    return 1
  if paths[node] == 0:
    paths[node] = sum([meme(i) for i in g2[node]])
  return paths[node]


print(meme(n))