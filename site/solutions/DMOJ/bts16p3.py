n = int(input())
ok = [i[0] for i in input().strip().split()]
i = 0
s = 0
while i < n:
  x = 1
  while i < n - 1 and ok[i+1] == ok[i]:
    i+=1
    x+=1
  for g in range(1, x + 1):
    s += x - g + 1
  i += 1
print(int(s)%1000000007)