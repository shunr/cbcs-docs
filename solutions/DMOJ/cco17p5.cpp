#include <bits/stdc++.h>
#define need first
#define cost second

using namespace std;

typedef pair<int, int> ip;

array<ip, 200005> dudes;
priority_queue<int, vector<int>, greater<int>> buy;
int n;

struct comp
{
    bool operator() (const ip& a, const ip& b) const
    {
      if (a.first == b.first)
        return a.second < b.second;
      else
        return a.first > b.first;
    }
};

int main() {
  scanf("%i", &n);
  int a, b;
  int s = 0;
  int c = 0;
  for (int i = 0; i < n; i++) {
    scanf("%i %i", &dudes[i].need, &dudes[i].cost);
  }
  
  sort(dudes.begin(), dudes.end(), comp());
  for (int i = 0; i < n; i++) {
    //printf("%i %i | ", dudes[i].need, dudes[i].cost);
  }
  
  for (int i = 0; i < n; i++) {
    int need_ = dudes[i].need;
    int cost_ = dudes[i].cost;
  
  int diff = need_ - (n-i-1+s);
  buy.push(cost_);
  if (diff <= 0) {
    continue;
  } else {
    for (int j = 0; j < diff; j++) {
      c += buy.top();
      buy.pop();
    }
    s += diff;
  }
  }
  printf("%i", c);
  
}
/*
from heapq import *
from collections import deque
n = int(input())
dudes = []
buy = []
for _ in range(n):
  a, b = (int(i) for i in input().split())
  dudes.append((a, -b))
  dudes.sort(reverse=True)

s = 0
c = 0

#print(dudes)
for i in range(n):
  need, cost = (dudes[i][0], -dudes[i][1])
  diff = need - (n-i-1+s)
  #print(need,cost,diff)
  heappush(buy, cost)
  if diff <= 0:
    continue
  else:
    for j in range(diff):
      #print("Buying", s+s)
      c += heappop(buy)
      
    s+=diff

print(c)*/