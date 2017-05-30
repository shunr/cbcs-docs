#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define at find_by_order
#define mp make_pair

using namespace std;
using namespace __gnu_pbds;

typedef tree<
  int, null_type,
  greater<int>,
  rb_tree_tag,
  tree_order_statistics_node_update> bst;

int ratingof[1000001];
unordered_map<int, int> idof;

int main() {
  bst tree;
  int n, a, b;
  char q;
  scanf("%i", &n);
  for (int i = 0; i < n; i++) {
    scanf(" %c", &q);
    if (q == 'N') {
      scanf("%i %i", &a, &b);
      tree.insert(b);
      ratingof[a] = b;
      idof[b] = a;
    } else if (q=='M') {
      scanf("%i %i", &a, &b);
      tree.erase(ratingof[a]);
      tree.insert(b);
      ratingof[a] = b;
      idof[b] = a;
    } else {
      scanf("%i", &a);
      printf("%i\n", idof[*tree.at(a-1)]);
    }
  }
}