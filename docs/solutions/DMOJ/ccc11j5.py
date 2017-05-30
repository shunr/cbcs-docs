n = int(input())
g = [[] for i in range(n+1)]



def meme(n):
  if g[n] == []:
    return 2
  else:
    prod = 1
    for child in g[n]:
      prod *= meme(child)
    return prod + 1

for i in range(1, n):
  g[int(input())].append(int(i))
  
print(meme(n)-1)