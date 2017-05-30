#define MOD 1000000007
#define ll long long int
#include <bits/stdc++.h>

using namespace std;

ll comp[300002];
ll pre[300002];
ll suf[300002];
ll pow2[300002] = {1};
ll n;

int main() {
  
  ll runsum = 0;
  scanf("%i", &n);
  for (ll i = 0; i < n; i++) {
    cin >> comp[i];
  }
  
  for (ll i = 1; i < n; i++) {
    pow2[i] = (pow2[i-1] * 2) % MOD;
  }
  
  sort(comp, comp+n);
  
  pre[0] = comp[0] % MOD;
  suf[n-1] = comp[n-1] % MOD;
  for (ll i = 1; i < n; i++) {
    pre[i] = (pre[i-1] + comp[i]) % MOD;
    suf[n-1-i] = (suf[n-i] + comp[n-1-i]) % MOD;
  }
  
  for (ll i = 0; i < n-1; i++) {
    runsum += (pow2[i] * (suf[n-i-1]-pre[i]+MOD)%MOD) % MOD;
    runsum %= MOD;
  }
  cout << runsum % MOD;
  return 0;
}