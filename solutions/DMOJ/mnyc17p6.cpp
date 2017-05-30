#include <bits/stdc++.h>

using namespace std;

typedef bitset<1000> bset;

int n, q;
bset tree[300020];
int arr[100002];
unordered_map<int, int> histo;
unordered_map<int, int> bitof;
deque<int> available;

int gp(int x) {
  return x/2;
}

int glc(int x) {
  return 2 * x;
}

int grc(int x) {
  return 2 * x + 1;
}

bset propagate(int i) {
  if (i >= n) return tree[i];
  tree[i] = (propagate(grc(i)) | propagate(glc(i)));
  return tree[i];
}

bset getsum(int node, int lo, int hi, int l, int r) {
   if (lo >= l && hi <= r) {
     return tree[node];
   } else if (l > hi || r < lo) {
     return bset();
   } else {
     int mid = (lo + hi) / 2;
     bset lc = getsum(glc(node), lo, mid, l, r);
     bset rc = getsum(grc(node), mid + 1, hi, l, r);
     return lc | rc;
   }
}

void update(int i) {
  if (i==1) return;
  int prnt = gp(i);
  tree[prnt] = tree[glc(prnt)] | tree[grc(prnt)];
  update(prnt);
}

int main() {
  int id = 0;
  int x, nn;
  n = 2;
  scanf("%i %i", &x, &q);
  nn = x;
  x -= 1 ;
  while (x >>= 1) n <<= 1;
  
  for (int i = 0; i < nn; i++) {
    int a;
    scanf("%i", &a);
    arr[i] = a;
    if (!histo.count(a)) {
      histo[a] = 0;
      bitof[a] = id;
      id++;
    }
    histo[a]++;
    tree[n+i].set(bitof[a], 1);
  }
  for (int i = id; i < 1001; i++) {
    available.push_back(i);
  }
  propagate(1);
  for (int i = 0; i < q; i ++) {
    int a, b, c;
    scanf("%i %i %i", &a, &b, &c);
    if (a == 2) {
      if (q > 100 && n > 100) { 
        printf("%i\n", getsum(1, 0, n - 1, b-1, c-1).count());
      } else {
        unordered_set<int> cheese;
        int DISGUSTING_CHEESE = 0;
        for (int j = b-1; j <= c-1; j++ ) {
          if (!cheese.count(arr[j])) {
            DISGUSTING_CHEESE++;
            cheese.insert(arr[j]);
          }
        }
        printf("%i\n", DISGUSTING_CHEESE);
      }
      
    } else {
      int val = arr[b-1];
      arr[b-1] = c;
      if (histo[val] > 1) {
        histo[val] -= 1;
      } else {
        int bi = bitof[val];
        bitof.erase(val);
        available.push_back(bi);
        histo.erase(val);
      }
      if (!bitof.count(c)) {
        int nextav = available.front();
        available.pop_front();
        bitof[c] = nextav;
      }
      tree[n+b-1].reset();
      tree[n+b-1].set(bitof[c], 1);
      update(n+b-1);
    }
  }
}