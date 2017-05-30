from sys import stdin
while True:
  line = [int(i) for i in stdin.readline().strip().split()]
  n = line[0]
  if n == 0:
    break
  diff = []
  for i in range(1, n):
    diff.append(line[i+1] - line[i])
  if diff:
    for l in range(1, n):
      memed = True
      for i in range(n - 1):
        if diff[i] != diff[i%l]:
          memed = False
          break
      if memed:
        print l
        break
  else:
    print 0