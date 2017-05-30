#include <bits/stdc++.h>
#define INF 9999999
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
#define mp make_pair
char _;
using namespace std;
typedef pair<int, int> ip;
vector<vector<ip>> G;
int p[5001];
int visited[5001] = {0};

int main() {
  int n, t, k, d;
  int min_pencil = INF;
  scan(n); scan(t);
  priority_queue<ip, deque<ip>, greater<ip>> q;
  for (int i = 0; i < n; i++) {
    G.push_back(vector<ip>());
    p[i] = -1;
  }
  for (int i = 0; i < t; i++) {
    int x, y, c;
    scan(x); scan(y); scan(c);
    G[x-1].push_back(mp(y-1, c));
    G[y-1].push_back(mp(x-1, c));
  }
  scan(k);
  for (int i = 0; i < k; i++) {
    int z, pz;
    scan(z); scan(pz);
    p[z-1] = pz;
  }
  scan(d);
  d-=1;
  q.push(mp(0, d));
  while (!q.empty()) {
    int node, v;
    ip x = q.top();
    node = x.second;
    v = x.first;
    q.pop();
    visited[node] = 1;
    if (v >= min_pencil) break;
    if (p[node] != -1) {
      int kek = p[node] + v;
      if (min_pencil > kek) min_pencil = kek;
    }
    for (int i = 0; i < G[node].size(); i++) {
      ip next = G[node][i];
      if (visited[next.first]) continue;
      q.push(mp(v + next.second, next.first));
    }
    
  }
  printf("%i", min_pencil);
}