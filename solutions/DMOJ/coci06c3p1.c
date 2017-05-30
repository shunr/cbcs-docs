#include <stdio.h>

int main() {
  int dank[9];
  int a, b;
  int sum = 0;
  for (int i = 0; i < 9; i++) {
    int x;
    scanf("%d", &x);
    dank[i] = x;
    sum += x;
  }
  
  for (int i = 0; i < 9; i++) {
    for (int j = 0; j < 9; j++) {
      if (sum - dank[i] - dank[j] == 100) {
        a = dank[i];
        b = dank[j];
      }
    }
  }
  
  for (int i = 0; i < 9; i++) {
    if (dank[i] != a && dank[i] !=b) {
      printf( "%d\n", dank[i]);
    }
  }
  return 0;
}