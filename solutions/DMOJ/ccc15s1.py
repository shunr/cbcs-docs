n = int(input())
k = []
for i in range(n):
    g = int(input())
    if g == 0:
        del k[-1]
    else:
        k.append(g)
        
print(sum(k))