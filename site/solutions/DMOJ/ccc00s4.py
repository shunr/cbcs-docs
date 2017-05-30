n = int(input())
clubs = [int(input()) for i in range(int(input()))]
shortest = [696969 for i in range(n+1)]
shortest[0] = 0

for i in range(n):
  for club in clubs:
    if i + club < n + 1:
      if shortest[i] + 1 < shortest[i+club]:
        shortest[i+club] = shortest[i] + 1

s = shortest[n]

if s < 9999:
  print("Roberta wins in " + str(s) + " strokes.")
else:
  print("Roberta acknowledges defeat.")