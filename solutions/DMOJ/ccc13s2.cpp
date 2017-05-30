#include <stdio.h>
#include <algorithm>

int main() {
  int n;
  int *memes;
  scanf("%d", &n);
  int x;
  scanf("%d", &x);
  memes = new int [x];
  
  for (int i = 0; i < x; i++) {
    scanf("%d", &memes[i]);
  }
  int s = 0;
  int d = 0;
  bool rekt = false;
  int crossed = std::min(4, x);
  for (int i = 0; i < crossed; i++) {
    s += memes[i];
    if (s > n) {
      printf("%d", d);
      rekt = true;
      break;
    }
    d += 1;
  }
  if (!rekt) {
    for (int i = crossed; i < x; i++) {
      s += memes[i];
      s -= memes[i-4];
      if (s > n) {
        printf("%d", d);
        rekt = true;
        break;
      }
      d += 1;
    }
  }
  if (!rekt) {
    printf("%d", d);
  }
}