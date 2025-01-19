#
# @lc app=leetcode id=1351 lang=python3
#
# [1351] Count Negative Numbers in a Sorted Matrix
#

# @lc code=start
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # negative_numbers = 0
        # for x in range(len(grid)):
        #     L, R = 0, len(grid[x]) - 1
        #     while L <= R:
        #         M = (L+R)//2
        #         print(L, M, R, grid[x][M], negative_numbers)
        #         if grid[x][M] < 0:
        #             negative_numbers += ((R-M) + 1)
        #             R = M - 1
        #         elif grid[x][M] >= 0:
        #             L = M + 1
        # return negative_numbers
        negative_numbers = 0
        for x in grid:
            for y in range(len(x)):
                print(x[y], negative_numbers)
                if x[y] < 0:
                    negative_numbers += (len(x) - y)
                    break
        return negative_numbers

# # 38ms Solution
# def countNegatives(grid: List[List[int]]) -> int:
#     c=0
#     for i in grid:
#         for j in i:
#             if j < 0:
#                 c+=1
#     return c
# f = open("user.out","w") 
# a = 0
# for case in map(loads, stdin):
#     for i in range(2):
#         if a==0:
#             b = case
#             a += 1
#         else:
#             print(str(countNegatives(b)), file = f)
#             a = a - 1
# exit(0)

# @lc code=end

