import sys

def input():
  return sys.stdin.readline().strip()
  
n, m, q = [int(i) for i in input().split()]
v = {}
vv = {}
inp = list(map(lambda x : int(x), input().split()))
prev = 0
for i in inp:
  vv[i] = prev
  prev += i
  v[i] = prev

for _ in range(q):
  a, b = (int(i) for i in input().split())
  if v[b] - vv[a] < m*2:
    print("Not enough")
  else:
    print("Enough")