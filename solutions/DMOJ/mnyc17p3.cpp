#include <iostream>
#include <string>
#include <algorithm>
#define ll unsigned __int128
#define inf 680564733841876000000000000000000000000

using namespace std;

int main() {
  string a;
  string b;
  cin >> a;
  cin >> b;
  int l = min(a.length(), b.length());
  int al = a.length();
  ll * bpre;
  ll * asuf;
  
  bpre = new ll[l+1]();
  asuf = new ll[l+1]();
  asuf[0] = 1;
  bpre[0] = 1;
  
  for (int i = 1; i <= l; i++) {
    asuf[i] = asuf[i-1] * (unsigned char) (a[al-i] - 63) % inf;
    bpre[i] = bpre[i-1] * (unsigned char) (b[i-1] - 63) % inf;
  }
  
  for (int i = l; i >= 0; i--) {
    if (asuf[i] == bpre[i] && (a[al-1] == b[i-1] || i == 0)) {
      cout << a << b.substr(i);
      break;
    }
  }
}