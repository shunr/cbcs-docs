hotels = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
a, b = int(input()), int(input())
for _ in range(int(input())):
  hotels.append(int(input()))
hotels.sort()

ways = [-1 for i in range(len(hotels))]
ways[0] = 1

    
def findways(x):
  global hotels
  if x == 0:
    return 1
  if ways[x] != -1:
    return ways[x]
  k = 1
  s = 0
  while k <= x:
    dist = hotels[x] - hotels[x-k]
    if dist <= b:
      if dist >= a:
        s += findways(x-k)
      k += 1
    else:
      break
  ways[x] = s
  return ways[x]
    
    
findways(len(hotels)-1)
print(ways[len(hotels)-1])