input()
d = [int(i) for i in input().split()]
input()
q = [int(i) for i in input().split()]
if (10/max(d) > 25/min(q)):
  print("Dimes are better")
elif (25/max(q) > 10/min(d)):
  print("Quarters are better")
else:
  print("Neither coin is better")