import sys
def input():
  return sys.stdin.readline().strip()
  
n, h = [int(k) for k in input().split()]
field = [[int(i) for i in input().split()] for j in range(n)]

q = [(0,0)]
visited = set()

while q:
  x = q.pop()
  t = field[x[1]][x[0]]
  if x == (n-1, n-1):
    print("yes")
    sys.exit()
  if x not in visited:
    if x[0] > 0 and abs(field[x[1]][x[0]-1] - t) <= h:
      q.append((x[0]-1,x[1]))
    if x[0] < n - 1 and abs(field[x[1]][x[0]+1] - t) <= h:
      q.append((x[0]+1,x[1]))
    if x[1] > 0 and abs(field[x[1]-1][x[0]] - t) <= h:
      q.append((x[0],x[1]-1))
    if x[1] < n - 1 and abs(field[x[1]+1][x[0]] - t) <= h:
      q.append((x[0],x[1]+1))
  visited.add(x)
  
print("no")