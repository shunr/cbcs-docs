n, m = [int(i) for i in input().split()]

graph = [[] for i in range(n + 1)] 
for i in range(m):
  kek = input().split()
  graph[int(kek[0])].append(int(kek[1]))
  graph[int(kek[1])].append(int(kek[0]))
  
visited = []
  
def meme(og, node, n):
  global visited
  if n == 5:
    return og in graph[node]
  else:
    gee = []
    for k in graph[node]:
      if k not in visited and k != og:
        visited.append(k)
        gee.append(meme(og, k, n + 1))
    return True in gee

memed = False
for i in range(1, n+1):
  if meme(i, i, 0):
    memed = True
    break
  else:
    del visited[:]

print("YES" if memed else "NO")