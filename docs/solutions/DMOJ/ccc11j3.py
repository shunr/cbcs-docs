sumac = [int(input()), int(input())]
n = 2
while True:
  n += 1
  next = sumac[-2] - sumac[-1]
  sumac.append(next)
  if next > sumac[-2]:
    break
  
print(n)