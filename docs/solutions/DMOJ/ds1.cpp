#include <bits/stdc++.h>
#define MAX 100005

typedef long long ll;

ll BIT[MAX], HBIT[MAX];
int n, m;

void update(ll* tree, int i, int val){
  for (; i < MAX; i += (i & -i)){
    tree[i] += val;
  }
}

ll get(ll* tree, int i){
  ll s = 0;
  for (; i > 0; i -= (i & -i)){
    s += tree[i];
  }
  return s;
}

ll sum(ll* tree, int l, int r){
  return get(tree, r) - get(tree, l-1);
}

int main() {
  char q;
  ll v, a, b;
  scanf("%d %d", &n, &m);
  for (int i = 1; i <= n; i++) {
    scanf("%d", &v);
    update(BIT, i, v);
    update(HBIT, v, 1);
  }
  for (int i = 1; i <= m; i++) {
    scanf(" %c", &q);
    int old;
    switch(q) {
      case 'C':
        scanf("%d %d", &a, &b);
        old = get(BIT, a) - get(BIT, a-1);
        update(BIT, a, b-old);
        update(HBIT, old, -1);
        update(HBIT, b, 1);
        break;
      case 'Q':
        scanf("%d", &a);
        printf("%lld\n", get(HBIT, a));
        break;
      case 'S':
        scanf("%d %d", &a, &b);
        printf("%lld\n", sum(BIT, a, b));
        break;
    }
  }
  return 0;
}