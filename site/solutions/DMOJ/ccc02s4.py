import sys

def input():
  return sys.stdin.readline().strip()

g, n = int(input()), int(input())
dudes = []
time = []
best = [99999 for i in range(n)]
splits = [i+1 for i in range(n)]

for i in range(n):
  dudes.append(input())
  time.append(int(input()))
  
for i in range(g):
  best[i] = max(time[:i+1])


def dp(x):
  global best
  global time
  if best[x] != 99999:
    return best[x]
  kek = []
  for i in range(1, g+1):
    kek.append([max([j for j in time[x - i+1:x+1]])+dp(x-i), i ])
  split = 0
  dankest = 999999
  for i in kek:
    if i[0] < dankest:
      dankest = i[0]
      split = i[1]
  splits[x] = split
  best[x] = dankest
  return best[x]

dp(n-1)  
print("Total Time: " + str(best[n-1]))

j = n-1
holymolythiscodeisgarbage = []
while j >= 0:
  dab = []
  for i in range(splits[j]):
    dab.append(dudes[j])
    j -= 1
  holymolythiscodeisgarbage.append(dab[::-1])

PATRICK_LINGHONG_PETERS = holymolythiscodeisgarbage[::-1]
for linghong in PATRICK_LINGHONG_PETERS:
  print(" ".join(linghong))