#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
from json import loads
from sys import stdin
from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    if len(nums) == 1:
        print(f"[0,0]" if nums[0]==target else f"[-1,-1]", file=f)
        return
    start = -1
    L, M, R = 0, 0, len(nums) - 1
    while L <= R:
        M = (L + R)//2
        print(L, M, R, start)
        if nums[M] > target:
            R = M - 1
        elif nums[M] < target:
            L = M + 1
        else:
            R = M - 1
            start = M
    print(L, M, R, start)
    if start == -1:
        print(f"[-1,-1]", file=f)
        return
    L, M, R = start, start, len(nums) - 1
    while L < R:
        M = (L + R)//2
        print(L, M, R)
        (L, R) = (L, M - 1) if nums[M] > target else (M + 1, R)
    print(f"[{start},{R if nums[R]==target else R-1}]", file=f)
    return

f = open("user.out","w") 
a = 0
for case in map(loads, stdin):
    if a==0:
        nums = case
        a += 1
    else:
        target = case
        searchRange(nums, target)
        a -= 1
exit(0)

# # 26ms Solution
# f = open("user.out", 'w')
# for nums, tar in zip(stdin, stdin):
#     if nums[1] == ']':
#         print("[-1,-1]", file=f)
#         continue
#     a = nums[1:-2].split(',')
#     tar = tar.rstrip()
#     t = int(tar)
#     i = bisect_left(a, True, key=lambda x: int(x) >= t)
#     if i == len(a) or a[i] != tar:
#         print("[-1,-1]", file=f)
#     else:
#         j = bisect_left(a, True, key=lambda x: int(x) > t)
#         print(f"[{i},{j-1}]", file=f)
# exit(0)
# @lc code=end

