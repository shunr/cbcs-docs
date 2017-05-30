#include <stdio.h>
#include <unordered_set>

#define ll long long

int main() {
    int n;
    scanf("%d", &n);;
    std::unordered_set<ll> set;
    for (int i = 0; i < n; i++) {
      ll x;
      scanf("%lld", &x);
      std::pair <std::__detail::_Node_iterator<long long int, true, false>, bool> p = set.insert(x);
      if (p.second == false) {
        set.erase(p.first);
      }
    }
    std::printf("%lld \n", *set.begin());
}