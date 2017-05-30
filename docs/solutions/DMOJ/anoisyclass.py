import sys

def input():
  return sys.stdin.readline().strip()

n = int(input())
m = int(input())
graph = [[] for i in range(n)]
rekt = set()

for i in range(m):
  a, b = [int(i) - 1 for i in input().split()]
  if b not in graph[a]:
    graph[a].append(b)

visited = set()
for i in range(n):
  if i in visited:
    continue
  q = [[i]]
  while q:
    rs2007 = q.pop()
    x = rs2007[-1]
    for g in graph[x]:
      if g in rs2007:
        print("N")
        sys.exit()
      q.append(rs2007 + [g])
    visited.add(x)    
print("Y")