from sys import stdin

n = int(stdin.readline())
a, b, c = [int(i) for i in stdin.readline().split()]
nmax = [0 for i in range(n+1)]

q = [a, b, c]
nmax[a] = 1
nmax[b] = 1
nmax[c] = 1
while q:
  x = q.pop()
  for v in [a,b,c]:
    if x+v <= n and nmax[x + v] < nmax[x] + 1:
      nmax[x+v] = nmax[x] + 1
      q.append(x+v)

print(nmax[n])