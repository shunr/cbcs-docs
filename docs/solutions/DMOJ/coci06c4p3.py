def gcf(a, b):
    for i in range(min(a, b), 0, -1):
      if a % i == 0 and b % i == 0:
        return i
    return 1
    
n = int(input())
wheels = [int(i) for i in input().split()]
for i in range(1, n):
  cf = gcf(wheels[0], wheels[i])
  print(str(int(wheels[0]/cf)) + "/" + str(int(wheels[i]/cf)))