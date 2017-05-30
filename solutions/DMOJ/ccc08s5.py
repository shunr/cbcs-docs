import sys

def input():
  return sys.stdin.readline().strip()

moves = [(2,1,0,2), (1,1,1,1), (0,0,2,1), (0,3,0,0), (1,0,0,1)]
mem = {}

def rekt(state):
  global moves
  if state in mem.keys():
    return mem[state]
  rip = True
  for move in moves:
    if move[0] <= state[0] and move[1] <= state[1] and move[2] <= state[2] and move[3] <= state[3]:
      rip = False
      break
  if rip:
    mem[state] = 2
    return 2
  else:
    for move in moves:
      dank = (state[0]-move[0],state[1]-move[1],state[2]-move[2],state[3]-move[3])
      if dank[0] < 0 or dank[1] < 0 or dank[2] < 0 or dank[3] < 0:
        continue
      if rekt(dank) == 2:
        mem[state] = 1
        break
      elif rekt(dank) == 1:
        mem[state] = 2
    return mem[state]
      
for _ in range(int(input())):
  a, b, c, d = [int(i) for i in input().split()]
  print("Roland" if rekt((a,b,c,d)) == 2 else "Patrick")