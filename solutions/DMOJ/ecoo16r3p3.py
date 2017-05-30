import sys
inf = sys.maxsize

def input():
  return sys.stdin.readline().strip()

n = int(input())
words = [input() for i in range(n)]

def best(word, dp):
  if word in dp.keys():
    return dp[word]
  if len(word) == 0:
    return 0
  least = inf
  for w in words:
    l = len(w)
    if w == word:
      least = 1
      break
    if l <= len(word) and word[0:l] == w:
      b = best(word[l:], dp) + 1
      if least > b:
        least = b
  dp[word] = least
  return dp[word]

dp = {}
for i in range(10):
  word = input().strip()
  best(word, dp)
  print(dp[word] - 1)