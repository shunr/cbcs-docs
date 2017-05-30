#include <stdio.h>
#include <algorithm>
#include <functional>
#define ll long long

struct kek {
  int a, b, q, pos;
  bool operator<(const kek& other) {
    return q > other.q;
  }
};

struct tree {
  int pos, m;
  bool operator<(const tree& other) {
    return m > other.m;
  }
};

int prent(int i){
  return i - (i & -i);
}

int next(int i){
  return i + (i & -i);
}

void update(ll * tree, int val, int i, int len){
  while(i < len){
    tree[i] += val;
    i = next(i);
  }
}

ll addup(ll * tree, int i){
  i++;
  int s = 0;
  while(i > 0){
    s += tree[i];
    i = prent(i);
  }
  return s;
}

ll sum(ll * tree, int l, int r){
  return addup(tree, r) - addup(tree, l-1);
}

int main() {
  
  int n, q;
  scanf("%i", &n);
  tree arr[100000];
  ll tree[100001];
  kek queries[100000];
  ll ans[100000];
  for (int i = 0; i < n; i++) {
    scanf("%i", &arr[i].m);
    arr[i].pos = i;
  }
  scanf("%i", &q);
  for (int i = 0; i < q; i++) {
    scanf("%i %i %i", &queries[i].a, &queries[i].b, &queries[i].q);
    queries[i].pos = i;
  }
  std::sort(arr, arr+n);
  std::sort(queries, queries+q);
  int i = 0, j = 0;
  while (i < q) {
    while (queries[i].q <= arr[j].m) {
      update(tree, arr[j].m, arr[j].pos+1, n+1);
      j++;
      
    }
    ans[queries[i].pos] = sum(tree, queries[i].a, queries[i].b);
    i++;
  }
  for(int i = 0; i < q; i++){
    printf("%i \n", ans[i]);
  }
}