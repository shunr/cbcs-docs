#include <stdio.h>
#include <unordered_set>
#include <string>
#include <iostream>

int main() {
    int n;
    scanf("%d", &n);
    n = n * 2 - 1;
    std::unordered_set<std::string> set;
    for (int i = 0; i < n; i++) {
      char tmp[101];
      scanf("%100s", tmp);
      std::string x = tmp;
      std::pair <std::__detail::_Node_iterator<std::basic_string<char>, true, true>, bool> p = set.insert(x);
      if (p.second == false) {
        set.erase(p.first);
      }
    }
    std::cout << *set.begin();
}