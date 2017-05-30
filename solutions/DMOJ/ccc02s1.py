p = int(input())
g = int(input())
r = int(input())
o = int(input())
x = int(input())
s = []
max = 100
for a in range(max):
  for b in range(max - a):
    for c in range(max - a - b):
      for d in range(max - a - b - c):
        if a * p + b * g + c * r + d * o == x:
          s.append(a+b+c+d)
          print("# of PINK is " + str(a) + " # of GREEN is " + str(b) + " # of RED is " + str(c) + " # of ORANGE is " + str(d))


print("Total combinations is " + str(len(s)) + ".")
print("Minimum number of tickets to print is " + str(min(s)) + ".")