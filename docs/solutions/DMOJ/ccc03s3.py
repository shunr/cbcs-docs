tiles = int(input())
r = int(input())
c = int(input())
def prop(x, y, n):
  if board[y][x] == '.':
    board[y][x] = n
    if y > 0:
      prop(x, y-1, n)
    if y < r - 1:
      prop(x, y+1, n)
    if x > 0:
      prop(x-1, y, n)
    if x < c - 1:
      prop(x+1, y, n)
    
board = [[ i for i in list(input())] for j in range(r)]
rm = 0
found = True

while found:
  found = False
  for y in range(r):
    for x in range(c):
      if board[y][x] == '.':
        prop(x, y, rm)
        rm += 1
        found = True
        
dank = [0 for i in range(rm)]

for i in range(rm):
  for y in range(r):
    for x in range(c):
      if board[y][x] == i:
        dank[i] += 1
  
dank = list(reversed(sorted(dank)))
rooms = 0
for i in dank:
  if i > tiles:
    break
  else:
    tiles -= i
    rooms += 1
r = "room"
if rooms != 1:
  r += "s"
print(str(rooms) + " " + r + ", " + str(tiles) + " square metre(s) left over")