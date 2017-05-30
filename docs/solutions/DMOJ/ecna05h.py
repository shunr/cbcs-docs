import sys

def input():
  return sys.stdin.readline().strip()
    
def meme(dp, d, start, end):
  if (start, end) in dp.keys():
    return dp[(start,end)]
  if start == end - 1:
    dp[(start, end)] = abs(d[start] - d[end])
  else:
    a = 0
    b = 0
    if d[start + 1] < d[end]:
      a = meme(dp, d, start + 1, end - 1) + d[start] - d[end]
    else:
      a = meme(dp, d, start + 2, end) + d[start] - d[start + 1]
    if d[start] < d[end - 1]:
      b = meme(dp, d, start, end - 2) + d[end] - d[end - 1]
    else:
      b = meme(dp, d, start + 1, end - 1) + d[end] - d[start]
    dp[(start,end)] = max(a,b)
  return dp[(start,end)]
  
  
i = 1  
while True:
  dp = {}
  line = [int(i) for i in input().split()]
  if line[0] == 0:
    break
  kek = line[1:]
  x = meme(dp, kek, 0, line[0] - 1)
  print("In game " + str(i) + ", the greedy strategy might lose by as many as " + str(x) + " points.")
  i += 1