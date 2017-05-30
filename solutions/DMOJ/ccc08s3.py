import sys
def input():
  return sys.stdin.readline().strip()

for _ in range(int(input())):
  r, c = int(input()), int(input())
  grid = [list(input()) for i in range(r)]
  q = [[(0,0)]]
  visited = []
  GARBANZO_BEAN = False;
  while q:
    rs2007 = q.pop(0)
    x = rs2007[-1]
    if x[0] >= 0 and x[0] < c and x[1] >= 0 and x[1] < r:
      t = grid[x[1]][x[0]]
      if t == "*":
        OH_GOD_I_LOVE_MEMES = 1
      elif x == (c-1,r-1):
        print(len(rs2007))
        GARBANZO_BEAN = True;
        break
      elif x not in visited:
        if t == "-" or t =="+":
          q.append(rs2007 + [(x[0] - 1, x[1])])
          q.append(rs2007 + [(x[0] + 1, x[1])])
        if t == "|" or t =="+":
          q.append(rs2007 + [(x[0], x[1] + 1)])
          q.append(rs2007 + [(x[0], x[1] - 1)])
          
      visited.append(x)
  if not GARBANZO_BEAN:
    print(-1)