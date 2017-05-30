# Dynamic Programming
 
Dynamic Programming is a very important topic in competitive programming, showing up often on contests. Dynamic Programming simply means the use of **subproblems** in order to solve a larger problem. This involves calculating and storing the result of the correct answer for a certain subproblem and reusing it when combined with other subproblems.
 
## Implementation

A simple example of the effectiveness of DP is when computing the `n`th Fibonacci number.

### Recursive approach

A naive recursive solution would need to calculate `fib(x)` every single time `fib(x)` is called for every number `x`, making the approach extremely slow when `n` is large.

```cpp
fib(n) {
if (n == 0 || n == 1)
	return 1
return fib(n-1) + fib(n-2) // We are calculating fib(n-2) every time
```

### DP approach
A solution using dynamic programming just stores the results of the Fibonacci numbers after being computed, treating `fib(n-1)` as the subproblem.

```cpp
memo = {} //dictionary, map or array
 
fib(n) {
if (memo[n] != -1) // It has already been calculateed
	return memo[n]
if (n == 0 || n == 1)
	return 1
toReturn = fib(n-1) + fib(n-2)
memo[n] = toReturn //After calculating the result, store it for later use
return toReturn
```

This solution now ensures that you no longer need to recalculate results that you have already made, saving a lot of time when solving multiple queries.
 
In dynamic programming, the subproblems often involve finding the solution for a prefix, suffix or subset of an array or set of numbers.

## Resources
#### Great resources for learning dynamic programming by MIT Open Courseware
- [Dynamic Programming I](https://www.youtube.com/watch?v=OQ5jsbhAv_M)
- [Dynamic Programming II](https://www.youtube.com/watch?v=ENyox7kNKeY)
- [Dynamic Programming III](https://www.youtube.com/watch?v=ocZMDMZwhCY)

#### More advanced concepts with bitmasking
- [HackerEarth DP Bitmasking](https://www.hackerearth.com/practice/algorithms/dynamic-programming/bit-masking/tutorial/)


