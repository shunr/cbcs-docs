#include <stdbool.h>
#include <stdio.h>
#include <math.h>
#define ll long long

ll modpow(ll a, ll b, ll n) {
  __int128 x = 1;
  __int128 y = a;
  while (b > 0){
    if (b % 2 == 1) {
      x = x * y % n;
    }
    y = y * y % n;
    b = b / 2;
  }
  return x % n;
}

bool isprime(ll n) {
  if (n == 2) {
    return true;
  }
  else if (n <= 1 || n % 2 == 0) {
    return false;
  }
  ll rt = pow(n,0.5);
  for (ll i = 3; i <= rt; i+=2) {
    if (n % i == 0) {
      return false;
    }
  }
  return true;
}

bool fermat(ll n) {
  if (n == 1) {
    return false;
  }
  for (int i = 0; i < 2; i++) {
    ll rng = (rand() * rand()) % (n - 1) + 2; 
    if (modpow(rng, n - 1, n) != 1) {
      return false;
    }
  }
  return true;
}

int main() {
  ll meme;
  scanf("%lld", &meme);
  while (meme < 1000000000 && isprime(meme) == false) {
    meme += 1;
  }
  while (meme > 1000000000 && fermat(meme) == false) {
    meme += 1;
  }
  printf("%lld", meme);
}