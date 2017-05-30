a, b = [int(i) for i in input().split()]

first = list(input().strip())
second = list(input().strip())

dank = list(reversed(first)) + second
for _ in range(int(input())):
  swapped = []
  for i in range(1, a+b):
    if dank[i] in second and dank[i-1] in first and dank[i-1] not in swapped:
      swapped.append(dank[i-1])
      dank[i],dank[i-1] = dank[i-1],dank[i]

print(''.join(dank))