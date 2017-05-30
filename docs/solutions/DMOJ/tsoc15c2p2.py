n = int(input())
for i in range(int(n/2), n - 1):
  s = ""
  for j in range(n):
    if abs(j-(n-1)/2) < abs(i - (n-1)/2):
      s += " "
    else:
      s += "*"
  print(s)
for i in range(int(n/2 + 1)):
  s = ""
  for j in range(n):
    if abs(j-(n-1)/2) < abs(i - (n-1)/2):
      s += " "
    else:
      s += "*"
  print(s)