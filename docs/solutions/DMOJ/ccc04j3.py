import itertools
n, m = int(input()), int(input())
s = [input() for i in range(n)]
d = [input() for i in range(m)]
for a in s:
    for b in d:
        print(a + " as " + b)