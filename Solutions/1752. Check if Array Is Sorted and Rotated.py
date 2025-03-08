from sys import stdin
from json import loads
from typing import List



def check(nums: List[int]) -> bool:
    return sum(nums[i - 1] > v for i, v in enumerate(nums)) <= 1
    
f = open("user.out","w") 
for arr in map(loads, stdin):
    if check(arr):
        print('true', file=f)
    else:
        print('false', file=f)
