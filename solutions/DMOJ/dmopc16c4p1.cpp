#include <stdio.h>

int main() {
  int n;
  long long pows[64];
  long long kek = 1;
  for (int i = 0; i < 64; i++) {
    pows[i] = kek;
    kek *= 2;
  }
  scanf("%i", &n);
  for (int i = 0; i < n; i++) {
    long long x;
    bool done = false;
    scanf("%lld", &x);
    for (int j = 0; j < 64; j++) {
      if (x == pows[j]) {
        printf("%s\n", "T");
        done = true;
        break;
      }
    }
    if (!done) {
      printf("%s\n", "F");
    }
  }
}