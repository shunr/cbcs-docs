n = int(input())
t = 0
s = 0
for i in range(n):
    g = input().lower()
    t += g.count("t")
    s += g.count("s")
    
if s < t:
    print("English")
else:
    print("French")