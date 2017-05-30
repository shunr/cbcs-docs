oogs = ["ook", "ookook", "oog", "ooga", "ug", "mook", "mookmook", "oogam", "oogum", "ugug"]

def ways(word, dp):
  if word in dp.keys():
    return dp[word]
  if len(word) < 2:
    if len(word) == 0:
      dp[word] = 1
    else:
      dp[word] = 0
    return dp[word]
  
  s = 0
  for oog in oogs:
    if len(oog) <= len(word) and word[0:len(oog)] == oog:
      second = word[len(oog):]
      s += ways(second, dp)
  dp[word] = s
  return dp[word]
  
for i in range(10):
  dp = {}
  word = raw_input().strip()
  ways(word, dp)
  print(dp[word])