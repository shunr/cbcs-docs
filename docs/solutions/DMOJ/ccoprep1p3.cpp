#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp> 
#include <ext/pb_ds/tree_policy.hpp>
#define size() order_of_key(1000000000)

using namespace std;
using namespace __gnu_pbds;

typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> oset;

int rankof[100001];
int whoserank[100001];
oset *friendsof[100001];
int n, m, k;



void build(int a, int b) {
  if (friendsof[a] != friendsof[b]) {
    int big, small;
    int asize = friendsof[a]->size();
    int bsize = friendsof[b]->size();
    int ls;
    if (asize > bsize) {
      big = a;
      small = b;
      ls = bsize;
    } else {
      big = b;
      small = a;
      ls = asize;
    }
    oset *old = friendsof[small];
    for (int i = 0; i < ls; i++) {
      int f = *friendsof[small]->find_by_order(i);
      friendsof[whoserank[f]] = friendsof[big];
      friendsof[big]->insert(f);
    }
    old -> clear();
    oset().swap(*old);
  }
}

int main() {
  scanf("%i %i", &n, &m);
  for (int i = 1; i <= n; i++) {
    int x;
    scanf("%i", &x);
    rankof[i] = x;
    whoserank[x] = i;
    friendsof[i] = new oset();
    friendsof[i]->insert(x);
  }
  int a, b;
  char q;
  for (int i = 0; i < m; i++) {
    scanf("%i %i", &a, &b);
    build(a,b);
  }
  
  /*for (int i = 1; i <= n; i++) {
    printf("| %i: ", i);
    for (int j = 0; j < friendsof[i]->size(); j++) {
      printf("%i ", *friendsof[i]->find_by_order(j));
    }
  }
  printf("\n");*/
  scanf("%i", &k);
  for (int i = 0; i < k; i++) {
    scanf(" %c %i %i", &q, &a, &b);
    if (q=='B') {
      build(a, b);
    } else {
      if (b <= friendsof[a]->size()) {
        printf("%i\n", whoserank[*friendsof[a]->find_by_order(b-1)]);
      } else {
        printf("-1\n");
      }
    }
  }
}