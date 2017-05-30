import sys
def input():
  return sys.stdin.readline().strip()
  
t, n = int(input()), int(input())
bin = [[] for i in range(t)]
for i in range(n):
  part = [int(k) for k in input().split()]
  bin[part[2]-1].append((part[0], part[1]))
b = int(input())
dp = {}

def meme(cash, part):
  tup = (cash, part)
  if part >= t:
    return 0
  if tup in dp.keys():
    return dp[tup]
  good = False
  for x in bin[part]:
    if cash >= x[0]:
      v = meme(cash-x[0], part + 1)
      if tup not in dp.keys() or v + x[1] > dp[tup]:
        dp[tup] = v + x[1]
      good = True
  if not good:
    dp[tup] = 0
  return dp[tup]
  
print(meme(b, 0))