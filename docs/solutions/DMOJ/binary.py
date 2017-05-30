x = int(input())
for i in range(x):
  n = int(input())
  
  s = bin(n)[2:]
  if len(s) % 4 > 0:
    s = "0" * (4 - len(s) % 4) + s
  
  ss = list(s)
  
  for i in range(int(len(s)/4)):
    ss.insert(i * 4 + i, " ")
    
  print("".join(ss))