#include <iostream>
#include <stdio.h>

int main() {
  int n;
  scanf("%d", &n);
  char c[100000];
  int g[200000] = {0};
  int start = 100000;
  int end = 100000;
  scanf("%s", c);
  for (int i = 0; i < n; i++) {
      if (c[i] == '1') {
        start -= 1;
        g[start] = i + 1;
      } else {
        end += 1;
        g[end] = i + 1;
      }
  }
  for (int i = 0; i < 200000; i++) {
      if (g[i] != 0) {
        printf("%i \n", g[i]);
      }
  }
}