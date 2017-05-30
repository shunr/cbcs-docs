def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n-1)*n 

n = int(input())
if n <= 4:
  print(1)
else:
  print(int(fact(n)/(24*fact(n-4))))