import sys
input = sys.stdin.readline

n, f = map(int, input().split())

surplus = []
sold = []

for i in range(n):
  p, c = map(int, input().split())
  sold.append(min(p, c))
  unsold = max(0, c - p)
  more = min(unsold, p)
  surplus.append(more)
  
surplus.sort(reverse=True)
print(sum(surplus[:f]) + sum(sold))
