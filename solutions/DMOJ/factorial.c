#include <stdio.h>
#define ll long long
#define e32 4294967296

int main() {
  int n;
  scanf("%lld", &n);
  for (int i = 0; i < n; i++) {
  ll x;
  scanf("%lld", &x);
  ll a = 1;
  if (x < 34) {
    for (ll i = 1; i <= x; i++){
      a=(a*i)%e32;
    }
    printf("%lld\n", a);
  } else {
    printf("%lld\n", 0);  
  }
  }
}