#include <bits/stdc++.h>
#define f first
#define s second

using namespace std;

typedef pair<int, int> ipair;

ipair tree[2097152];
int e;

int lc(int i) {
  return 2*i+1;
}

int rc(int i) {
  return 2*i+2;
}

int p(int i) {
  return (i-1)/2;
}

int opp(int i) {
  return (i-1)/2;
}

ipair build(ipair * tree, int n) {
  if (tree[n].f != 0) return tree[n];
  tree[n] = max(build(tree, lc(n)), build(tree, rc(n)));
  return tree[n];
}

void propagate(ipair * tree, int n) {
  tree[n] = max(tree[lc(n)], tree[rc(n)]);
  if (n != 0) propagate(tree, p(n));
}

int wins(ipair * tree, int n, int curr) {
  if (n == 0) return curr;
  if (tree[p(n)] == tree[n]) {
    return wins(tree, p(n), curr + 1);
  } else {
    return curr;
  }
}

int replace(ipair * tree, int n, int val) {
  tree[e + n - 1].f = val;
  propagate(tree, p(e + n - 1));
}

int main() {
  int n, m;
  scanf("%i %i", &n, &m);

  e = pow(2, n);
  for (int i = e - 1; i < 2 * e - 1; i++) {
    scanf("%i", &tree[i].f);
    tree[i].s = i-e+1;
  }

  build(tree, 0);
  
  char q;
  int a, b;
  
  for (int i = 0; i < m; i++) {
    scanf(" %c", &q);
    if (q == 'R') {
      scanf("%i %i", &a, &b);
      replace(tree, a - 1, b);
    } else if (q == 'W') {
      printf("%i\n", tree[0].s + 1);
    } else if (q == 'S') {
      scanf("%i", &a);
      printf("%i\n", wins(tree, e + a - 2, 0));
    }
  }
}