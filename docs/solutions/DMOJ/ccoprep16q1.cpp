#include <bits/stdc++.h>

char grid[1000][1000];
char histo[1000][1000];

int main() {
  int n;
  scanf("%i", &n);
  for (int _ = 0; _ < n; _++) {
    
    
    int l, w;
    int best = 0;
    scanf("%i %i", &l, &w);
    for (int i = 0; i < l; i++) {
      for (int j = 0; j < w; j++) {
        int x;
        scanf(" %c", &x);
        if (x == 'R') {
          histo[j][i] = 0;
        } else {
          if (i > 0) {
            histo[j][i] = histo[j][i-1] + 1;
          } else {
            histo[j][i] = 1;
          }
        }
      }
    }
    
    for (int i = 0; i < l; i++) {
      for (int j = 0; j < w; j++) {
        if (histo[j][i] == 0) {
          grid[j][i] = 0;
        } else {
          if (j > 0 && histo[j-1][i] >= histo[j][i]) {
            grid[j][i] = grid[j-1][i] + 1;
          } else {
            grid[j][i] = 1;
          }
        }
        int kek = grid[j][i] * histo[j][i];
        if (kek > best) {
          best = kek;
        }
      }
    }
    
    for (int i = 0; i < l; i++) {
      for (int j = w-1; j >= 0; j--) {
        if (histo[j][i] == 0) {
          grid[j][i] = 0;
        } else {
          if (j < w-1 && histo[j+1][i] >= histo[j][i]) {
            grid[j][i] = grid[j+1][i] + 1;
          } else {
            grid[j][i] = 1;
          }
        }
        int kek = grid[j][i] * histo[j][i];
        if (kek > best) {
          best = kek;
        }
      }
    }
    
    /*for (int i = 0; i < l; i++) {
      for (int j = w-1; j >= 0; j--) {
        printf("%i ", grid[j][i]);
      }
      printf("\n");
    }*/
    
    printf("%i\n", best * 3);
    
  }
}