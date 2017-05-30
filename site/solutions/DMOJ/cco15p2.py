import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = (int(i) for i in input().split())
graph = defaultdict(list)
weights = {}
dp = [[0 for i in range(300000)] for j in range(18)]
  
for i in range(m):
  a, b, c = (int(i) for i in input().split())
  graph[b].append(a)
  weights[(a,b)] = c

def meme(dp, G, w, s, x, path):
  best = -999999
  if x == s:
    return 0
  if dp[x][path] != 0:
    return dp[x][path]
  for n in G[x]:
    if (path & (1 << n)) == 0:
      best = max(meme(dp, G, w, s, n, (path | (1 << n))) + w[(n, x)], best)
  dp[x][path] = best
  return dp[x][path]
  
print(meme(dp, graph, weights, 0, n-1, 0 | (1 << n-1)))