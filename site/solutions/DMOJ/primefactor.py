def primefactor(n):
    i = 2
    f = []
    while i ** 2 <= n:
        if n % i:
            i += 1
        else:
            n //= i
            f.append(i)
    if n > 1:
        f.append(n)
    return f
    
for i in range(int(input())):
  n = int(input())
  print(' '.join([str(x) for x in primefactor(n)]))