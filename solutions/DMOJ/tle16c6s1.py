import sys
def input():
  return sys.stdin.readline().strip()
  
t = int(input())
pref = [""] * t
for i in range(t):
  pref[i] = input()
dp = {}
n = int(input())
for i in range(n):
  s = input()
  if s not in dp.keys():
    dp[s] = []
  dp[s].append(i + 1)

for i in pref:
  if i in dp.keys():
    for j in dp[i]:
      print(j)