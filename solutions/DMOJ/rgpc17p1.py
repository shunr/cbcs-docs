def good(d,x1,y1,x2,y2):
  dist = (x1-x2)**2 + (y1-y2)**2
  dd = d**2
  return True if dist <= dd else False

n, d = [int(i) for i in input().split()]
s = 1
m = 1
x1, y1 = [int(i) for i in input().split()]
for i in range(1, n):
  x, y = [int(i) for i in input().split()]
  if good(d, x, y, x1, y1):
    s += 1
    if s > m:
      m = s
  else:
    s = 0
  x1, y1 = x, y
    
print(m)