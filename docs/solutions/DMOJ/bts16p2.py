n = int(input())
set = []
for i in range(n):
  cmd = input().split()
  if cmd[0] == '1':
    if cmd[1] not in set:
      print('true')
      set.append(cmd[1])
    else:
      print('false')
  elif cmd[0] == '2':
    if cmd[1] not in set:
      print('false')
    else:
      print('true')
      set.remove(cmd[1])
  elif cmd[0] == '3':
    if cmd[1] not in set:
      print('-1')
    else:
      print(set.index(cmd[1]))
  elif cmd[0] == '4':
      s = ""
      for k in list(sorted(set)):
        s += k + " "
      print(s)