n = int(input())
memes = [int(input()) for i in range(n)]

while True:
  next = int(input())
  if next == 77:
    break
  elif next == 88:
    ind = int(input())
    memes[ind-1] += memes[ind]
    memes.pop(ind)
  else:
    ind = int(input())
    per = int(input())
    memes.insert(ind, memes[ind-1]*(100-per)/100)
    memes[ind-1] *= per/100
    
print(" ".join([str(int(m)) for m in memes]))