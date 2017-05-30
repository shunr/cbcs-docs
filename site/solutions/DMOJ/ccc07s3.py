from sys import stdin

n = int(stdin.readline())
graph = {}

for _ in range(n):
  p = [int(k) for k in stdin.readline().split()]
  graph[p[0]] = p[1]
  
while True:
  pair = [int(k) for k in stdin.readline().split()]
  if pair[0] == 0:
    break
  done = False
  s = 0
  dude = pair[0]
  friendo = pair[1]
  curr = dude
  if pair[0] in graph.keys() and pair[1] in graph.keys():
    while not done:
      if graph[curr] == friendo:
        done = True
        break
      elif graph[curr] == dude:
        break
      else:
        curr = graph[curr]
        s += 1

  if done:
    print("Yes " + str(s))
  else:
    print("No")