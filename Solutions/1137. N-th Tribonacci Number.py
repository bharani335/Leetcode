from json import loads
from sys import stdin


memo = {0: 0, 1: 1, 2: 1}
def tribonacci(n: int) -> int:
    if n in memo:
        return memo[n]
    memo[n] = tribonacci(n-3) + tribonacci(n-2) + tribonacci(n-1)
    return memo[n]



f = open("user.out","w") 
for n in map(loads, stdin):
    print(str(tribonacci(n)), file = f)
exit(0)