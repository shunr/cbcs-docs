init = int(input())
sum = 0
for i in range(init):
  sum += int(input())

new = int(input())

for i in range(new):
  init += 1
  sum += int(input())
  s = str(int(round(sum/init, 3)*1000))
  print(s[:-3] + '.' + s[-3:])