alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
inp = int(input())
for i in range(inp):
  num = list(input().replace('-',''))
  for j in range(len(num)):
    if num[j] in alph[0:3]:
      num[j] = '2';
    elif num[j] in alph[3:6]:
      num[j] = '3';
    elif num[j] in alph[6:9]:
      num[j] = '4';
    elif num[j] in alph[9:12]:
      num[j] = '5';
    elif num[j] in alph[12:15]:
      num[j] = '6';
    elif num[j] in alph[15:19]:
      num[j] = '7';
    elif num[j] in alph[19:22]:
      num[j] = '8';
    elif num[j] in alph[22:26]:
      num[j] = '9';
  num.insert(3, '-')
  num.insert(7, '-')
  print(''.join(num[0:12]));