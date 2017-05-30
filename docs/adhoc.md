# Ad Hoc
 
![telescoping series](http://calculus.nipissingu.ca/tutorials/finiteseriesgifs/telescoping_sums.gif)

Ad hoc problems are those whose algorithms do not fall into standard categories with well-studied solutions. Each ad hoc problem is different meaning there is no specific or general techniques that exist to solve them. These problems may require novel observations and optimizations to get the solution to run within the given time.

## Case Study
 
To demonstrate, we will solve this [Ad Hoc Example Problem](http://codeforces.com/contest/810/problem/C).

### Solution

The input can first be sorted in `O(n log n)` time.
Next, we must precompute all powers of `2` from `2` to `n-2`. This can be found in `O(n)` time with dynamic programming.
 
We will solve this problem using [telescoping series](https://www.khanacademy.org/math/calculus-home/series-calc/series-basics-challenge/v/telescoping-series). The question is really asking us to find the maximum and the minimum element of every possible subset of elements (of which there exists `2^n`). 

#### Observation 1
It is important to note that for each pair of elements `a[i]` and `a[j]` in the (sorted) array, there are `2^(j-i-1)` subsets in which `a[i]` is the minimum value and `a[j]` is the maximum value.

Therefore, the answer can be written as the sum of `2^(j-i-1) * (a[j]-a[i])` for all `j > i`.
This can be computed in `O(n^2)` time by iterating through all possible pairs `(i,j)`; however, given the constraint `n <= 300 000`, this algorithm will not run within the 2 second time limit.

#### Observation 2

Our solution must be optimized. Let’s write out the first few terms of this relation:
When `j-i-1 = 0`, you add to the total:
```
2^0 * (a[1]-a[0]) + 2^0 * (a[2] - a[1]) + ... + 2^0 * (a[n-1] - a[n-2])
= 2^0 * (a[1] - a[0] + a[2] - a[1] + ... + a[n-2] - a[n-3] + a[n-1] - a[n-2])
= 2^0 * (a[n-1] - a[0]) (the first and last elements of the array)
```
 
When `j-i-1 = 1`, you add to the total:
```
2^1 * (a[2] - a[0] + a[3] - a[1] + ... +  a[n-2] - a[n-4] + a[n-1] - a[n-3])
= 2^1 * (a[n-1]+a[n-2] - a[0] - a[1]) (the first two and last two elements of the array)
```
 
The key to this problem is noticing that the pattern continues until `j-i-1 = n-2`.

#### Conclusion

Thus:
```
let pre[i] be prefix sum of the array up to i
let suf[i] be suffix sum of the array from i onwards
```

The relation can be generalized to:
The answer is the sum from `i=0` to `i=n-2` of `(2^i) * (suf[n-1-i]-pre[i])`
 
This can be computed in `O(n)` time giving a final time complexity of `O(nlogn + n + n)` = `O(nlogn)` which will run within the time constraints.

### C++ Implementation
```cpp
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
```