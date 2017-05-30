#include "stdio.h"
#include "math.h"

int main() {

  while (1) {
    int n;
    scanf("%d", &n);
    if (n == 0) {
      break;
    }
    int k = 0;
    for (int i = 1; i < n; i++) {
        k += sqrt(n * n - i * i);
    }
    k += n;
    printf("%d\n", k*4 + 1);
  }
}