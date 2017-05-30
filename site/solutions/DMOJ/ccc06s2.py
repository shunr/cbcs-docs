alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ ')
plain = list(input())
cipher = list(input())
new = list(input())

key = ['.' for i in alpha]

for i in range(len(plain)):
  key[alpha.index(cipher[i])] = plain[i]


msg = []
for c in new:
  msg.append(key[alpha.index(c)])

print(''.join(msg))