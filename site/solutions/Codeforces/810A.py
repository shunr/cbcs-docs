import sys
input = sys.stdin.readline

n, k = map(float, input().split())

meme = sum(map(float, input().split()))
s = 0

while (round(meme/n) < k):
  meme += k
  s += 1
  n += 1
  
print s