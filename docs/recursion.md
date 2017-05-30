# Recursion

![recursion](https://i.stack.imgur.com/CLwKE.jpg)

Recursion is a fundamental concept that is incredibly useful in competitive programming. It is commonly used to solve problems in graph theory and implemented in algorithms such as [depth and beadth first search](graph.md). Recursion also provides a very simple and straightforward way of thinking about [dynamic programming](dp). Recursion is very powerful and necessary for many problems.

The idea with recursion is that a function will be called, but in order to return a value it relies on the same function being called. It will continue to “wait” until a base case is reached, where afterwards all of the other functions can return values.

## Example
A common example is a recursive solution to finding the `n`th Fibonacci number
 
```python
fib(n) {
	if (n == 0 || n == 1)
		return 1
	return fib(n-1) + fib(n-2)
}
```
### Explanation 
This function begins with the parameter `n`, the answer in the first call of the function depends on the previous two Fibonacci numbers since `fib(n) = fib(n-1) + fib(n-2)`. This means that the function will be executed again to solve for these two numbers, since none of these numbers are known yet, it will continue calling this function until the base case is reached. In mathematical terms, the Fibonacci sequence is based on a formula that is based on the first and second terms. In math class you have probably learned about such recursive sequences, the value of the next term depends on the current term or terms.
 
## Practice problems
- [CCC '13 S3 - Chances of Winning](https://dmoj.ca/problem/ccc13s3)
- [VM7WC '16 #4 Silver - Tests or Test Cases?](https://dmoj.ca/problem/vmss7wc16c4p2)
- [CCC '96 S3 - Pattern Generator](https://dmoj.ca/problem/ccc96s3)
- [CCC '03 S3 - Floor Plan](https://dmoj.ca/problem/ccc03s3) **includes graph theory*

