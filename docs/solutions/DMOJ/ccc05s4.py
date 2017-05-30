l = int(input())

def maxpath(key, arr):
  if key not in arr.keys():
    return 0
  else:
    meme = [maxpath(g, arr) for g in arr[key]]
    return max(meme) + 1
  
for kony in range(l):
  n = int(input())
  dudes = []
  visited = []
  graph = {}
  for i in range(n):
    dudes.append(input())
  for i in range(n-1, 0, -1):
    if dudes[i-1] not in visited:
      if dudes[i] not in graph.keys():
        graph[dudes[i]] = []
      graph[dudes[i]].append(dudes[i-1])
      visited.append(dudes[i])
  home = dudes[-1]
  
  print(n * 10 - maxpath(home, graph) * 20)