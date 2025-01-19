from json import loads
from sys import stdin


memo = {0: 0, 1: 1}
def fib(n: int) -> int:
    if n in memo:
        return memo[n]
    memo[n] = fib(n-2) + fib(n-1)
    return memo[n]



f = open("user.out","w") 
for n in map(loads, stdin):
    print(str(fib(n)), file = f)
exit(0)