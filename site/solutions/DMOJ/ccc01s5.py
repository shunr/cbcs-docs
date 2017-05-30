import sys

def input():
  return sys.stdin.readline().strip()
  
def issub(a, b):
  la = len(a)
  lb = len(b)
  if la > lb:
    return a[:lb] == b
  else:
    return b[:la] == a
  
m, n = int(input()), int(input())

b = [input() for i in range(n)]
a = [input() for i in range(n)]
dp = {}
q = []

for i in range(n):
  if a[i] == b[i]:
    print("1")
    print(i + 1)
    sys.exit()
  if issub(a[i], b[i]):
    q.append([i])
    dp[tuple([i])] = (a[i], b[i])

done = False

while q:
  x = []
  if m * n > 36:
    x = q.pop()
  else:
    x = q.pop(0)
  astr = dp[tuple(x)][0]
  bstr = dp[tuple(x)][1]
  if astr == bstr:
    print(len(x))
    for i in x:
      print(i + 1)
    done = True
    break
  if len(x) >= m:
    break
  for i in range(n):
    if issub(astr+a[i], bstr+b[i]):
      dp[tuple(x + [i])] = (astr+a[i], bstr+b[i])
      q.append(x + [i]);
      
  
if not done:
  print("No solution.")