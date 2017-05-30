import sys
from functools import reduce
import operator
from itertools import combinations

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

def input():
    return sys.stdin.readline().strip()

def to_standard(zeroes, deg):
  c = [0 for i in range(deg+1)]
  c[0] = 1
  c[-1] = prod(zeroes)
  for i in range(1, deg):
    c[i] = sum([prod(i) for i in list(combinations(zeroes, i))])
  return c
  
for _ in range(int(input())):
  n = int(input())
  z = [-int(i) for i in input().split()]
  x, y = [int(i) for i in input().split()]
  num = to_standard(z, n)
  multi = y/prod([x+i for i in z])
  for i in range(n + 1):
    num[i] = int(multi*num[i])
    
  print(str(num)[1:-1].replace(",", ""))