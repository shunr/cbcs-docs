#include <algorithm>
#include <stdio.h>
#include <unordered_map>
#include <array>
#define rv vals[i]
#define rf food[i]
#define rt times[i]

using namespace std;

int h(int a, int b, int c) {
  return (a*101 + b)*301 + c;
}

int main() {
  int m, u, r;
  
  scanf("%d %d %d", &m, &u, &r);
  
  int vals[150];
  int times[150];
  int food[150];
  int* dp = new int[8000000];
  for (int i = 0; i < r; i++) {
    scanf("%d %d %d", &vals[i], &times[i], &food[i]);
  }
  for (int i = 0; i <= u; i++) {
    for (int j = 0; j <= m; j++) {
      if (food[0] <= i and times[0] <= j) {
        dp[h(0,i,j)] = vals[0];
      }
    }
  }

  for (int i = 1; i < r; i++) {
    for (int j = 0; j <= u; j++) {
      for (int k = 0; k <= m; k++) {
        bool bad = (j-rf < 0) || (k-rt < 0);
        if (bad) {
          dp[h(i,j,k)] = dp[h(i-1,j,k)];
        } else {
          dp[h(i,j,k)] = max(dp[h(i-1,j,k)], rv + dp[h(i-1,j-rf,k-rt)]);
        }
      }
    }
  }
  printf("%d", dp[h(r-1,u,m)]);

}