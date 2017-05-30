dim = [ int (i) for i in input().split()]
pos = [0,0]
while True:
  next = [ int (i) for i in input().split()]
  if next == [0, 0]:
    break
  pos[0] = max(min(pos[0] + next[0], dim[0]), 0)
  pos[1] = max(min(pos[1] + next[1], dim[1]), 0)
  print(str(pos[0]) + " " + str(pos[1]))