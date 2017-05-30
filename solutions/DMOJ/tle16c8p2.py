n = int(input())

for i in range(n):
  g = bin(int(input()))[2:]
  for x in g:
    if x == "1":
      print("dank ", end="")
    else:
      print("meme ", end="")
  print()