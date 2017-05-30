n = int(input())
saws = [int(i) for i in input().split()]
logs = [int(i) for i in input().split()]
saws.sort()
logs.sort()
s = 0
for i in range(n):
    s += saws[i]*logs[n-i-1]

print(s)