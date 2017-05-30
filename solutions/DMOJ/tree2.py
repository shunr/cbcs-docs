from heapq import *
import math
import sys

grid = {}

r, c = (int(i) for i in input().split())
bval = 0
bset = []
x, y = 0, 0;

def dist(x1, x2, y1, y2):
  return math.sqrt((x1-x2)**2 + (y1-y2)**2)

for i in range(r):
  kek = [int(x) if x not in 'X.' else x for x in input().split()]
  for j in range(c):
    grid[(j,i)] = kek[j]
    if kek[j] != '.' and kek[j] != 'X':
      if kek[j] > bval:
        bval = kek[j]
        bset.clear()
        bset.append((j, i))
      elif kek[j] == bval:
        bset.append((j, i))
    elif kek[j] == 'X':
      x = j
      y = i

succ = 999999
wheresmygoddamntree = tuple()
for b in bset:
  d = dist(x, b[0], y, b[1])
  if d < succ:
    wheresmygoddamntree = b
    succ = d

q = [(0, 0, (x, y))]
visited = set()
while q:
  heights, dist, v1 = heappop(q)
  if v1 in visited:
    continue
  visited.add(v1)
  pts = [(v1[0] + 1, v1[1]), (v1[0] - 1, v1[1]), (v1[0], v1[1] + 1), (v1[0], v1[1] - 1)]
  for p in pts:
    if p in grid:
      if p == wheresmygoddamntree:
        print(dist)
        sys.exit(0)
      k = 0 if grid[p] == "." else 1
      h = 0 if (grid[p] == "." or grid[p] == "X") else grid[p]
      heappush(q, (heights + h, dist + k, p))