import sys

def input():
  return sys.stdin.readline().strip()
  
n = int(input())
succ = set()
for i in range(n):
  d = (input().split())
  d.sort()
  if tuple(d) in succ:
    print("Twin snowflakes found.")
    sys.exit()
  else:
    succ.add(tuple(d))
print("No two snowflakes are alike.")