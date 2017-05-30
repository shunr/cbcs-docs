s = 0
b = 0
ok = {}
for _ in range(int(input())):
  n = input()
  if n not in ok.keys():
    ok[n] = 0
  if ok[n] > b - ok[n]:
    s += 1
  ok[n] += 1
  b += 1

print(s)