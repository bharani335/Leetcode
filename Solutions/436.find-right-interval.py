# @before-stub-for-debug-begin
from bisect import bisect_left
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=436 lang=python3
#
# [436] Find Right Interval
#

# @lc code=start
from collections import OrderedDict
from json import loads
import math
from sys import stdin
from typing import List


def findRightInterval(intervals: List[List[int]]) -> List[int]:
    # TimeLimitExceeded
    # SIZE = len(intervals)
    # result = []
    # for i in range(SIZE):
    #     end = intervals[i][1]
    #     right_interval = [-1, math.inf]
    #     for j in range(SIZE):
    #         print(right_interval[1], intervals[j][0], end)
    #         print(right_interval[1] > intervals[j][0] >= end)
    #         right_interval = [j, intervals[j][0]] if right_interval[1] > intervals[j][0] >= end else right_interval
    #     result.append(right_interval[0])
    # return result


    # # 433ms Worst Solution
    # order = OrderedDict()
    # for x, y in enumerate(intervals):
    #     order[x] = y
    #     # print(order[x], order.items())

    # sortedlist = sorted(order.items(), key=lambda x: x[1][0])
    # print(sortedlist, type(sorted))
    # res = []
    # for i in range(len(intervals)):
    #     target = intervals[i][1]
    #     cur_res = -1
    #     if target > sortedlist[-1][1][0]:
    #         res.append(cur_res)
    #         continue
    #     elif target < sortedlist[0][1][0]:
    #         res.append(sortedlist[0][1][0])
    #         continue
    #     L, M, R = 0, 0, len(intervals)-1
    #     while L <= R:
    #         M = (L + R)//2
    #         if sortedlist[M][1][0] >= target:
    #             R = M - 1
    #             cur_res = sortedlist[M][0]
    #         elif sortedlist[M][1][0] < target:
    #             L = M + 1
    #         print(L, M, R)
    #     res.append(cur_res)
    # return res

    # 220ms Solution
    n = len(intervals)
    indices = list(range(n))
    print(indices)
    indices.sort(key=lambda x : intervals[x][0])
    starts = [intervals[i][0] for i in indices]
    print(indices)
    print(starts)
    ret = []
    for _, e in intervals:
        if (i := bisect_left(starts, e)) != n:
            ret.append(indices[i])
        else:
            ret.append(-1)
    return ret

f = open("user.out","w") 
a = 0
for case in map(loads, stdin):
    res = findRightInterval(case)
    print(f'[{",".join(str(x) for x in res)}]', file=f)
exit(0)

# @lc code=end

