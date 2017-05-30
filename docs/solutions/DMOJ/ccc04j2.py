a = int(input())
b = int(input())

for i in range(b - a + 1):
  if i % 60 == 0:
    print("All positions change in year " + str(a + i))