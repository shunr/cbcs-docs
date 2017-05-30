n = 1
while True:
  s = int(input())
  n += s
  if s == 0:
    print("You Quit!")
    break
  if n == 100:
    print("You are now on square " + str(n))
    print("You Win!")
    break
  elif n > 100:
    n -= s
  elif n == 9:
    n = 34
  elif n == 40:
    n = 64
  elif n == 67:
    n = 86
  elif n == 99:
    n = 77
  elif n == 90:
    n = 48
  elif n == 54:
    n = 19
  print("You are now on square " + str(n))