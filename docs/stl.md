# STL Containers
 
Both Java and C++ have large standard libraries with many amazing containers and functions. It is important to know your language because it can save you a lot of time coding.

## Complexity Specifications

| C++ | Java | Insertion | Delete | Access | Notes |
|---|---|---|---|---|---|
| *`vector`* | *`ArrayList`* | `O(1)` back, `O(N)` otherwise | `O(1)` back `O(N)` otherwise | `O(1)` | Resizable array |
| *`set`* | *`SortedSet`* | `O(logn)` | `O(logn)` | `O(logn)` | Maintains sorted order, implemented as BST |
| *`unordered_set`* | *`HashSet`* | `O(1)` | `O(1)` | It is average case `O(1)` to check if a set contains an element |
| *`deque`* | *`Deque`* | `O(1)` front or back `O(N)` otherwise | `O(1)` front or back `O(N)` otherwise | `O(1)` | Double ended queue |
| *`list`* | *`List`* | `O(1)` anywhere | `O(1)` anywhere | `O(N)` to get iterator |
| *`unordered_map`* | *`HashMap`* | `O(1)` | `O(1)` | `O(1)` access It is average case `O(1)` to check if a HashMap contains a key | Sorted alternatives are *`std::map`* and *`SortedMap`*, worse complexity |