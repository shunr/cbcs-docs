x = int(input())

vowels = list("aeiou")

def r(a, b):
  l1 = a.split()[-1]
  l2 = b.split()[-1]
  end1 = "aaaa"
  end2 = "noooo"
  found = False
  for i in range(len(l1) - 1, -1, -1):
    if l1[i] in vowels:
      end1 = l1[i:]
      found = True
      break
      
  for i in range(len(l2) - 1, -1, -1):
    if l2[i] in vowels:
      end2 = l2[i:]
      found = True
      break
  if found:
    return end1 == end2
  else:
    return l1 == l2

for i in range(x):
  l = [input().lower() for j in range(4)]
  if r(l[0], l[1]) and r(l[1], l[2]) and r(l[2], l[3]) :
    print("perfect")
  elif r(l[0], l[1]) and r(l[2], l[3]) :
    print("even")
  elif r(l[0], l[2]) and r(l[1], l[3]) :
    print("cross")
  elif r(l[0], l[3]) and r(l[1], l[2]) :
    print("shell")
  else:
    print("free")