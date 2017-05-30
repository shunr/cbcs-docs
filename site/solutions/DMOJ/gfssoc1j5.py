from collections import deque
import sys
input = sys.stdin.readline

n, m, t = (int(i) for i in input().split())
dp = [[99999 for i in range(n+1)] for j in range(n+1)]
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = (int(x) for x in input().split())
    graph[a].append(b)

for src in range(1, n + 1):
    dp[src][src] = 0
    q = deque([(src, 0)])
    visited = [False for i in range(n+1)]
    while q:
        a, v = q.popleft()
        if visited[a]:
            continue
        visited[a] = True
        for x in graph[a]:
            if not visited[x]:
                dp[src][x] = min(dp[src][x], v + 1)
                q.append((x, v + 1))

q = int(input())
for i in range(q):
    a, b = (int(i) for i in input().split())
    kek = dp[a][b]
    print(kek * t if kek!= 99999 else "Not enough hallways!")