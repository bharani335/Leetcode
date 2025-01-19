#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
from json import loads
from sys import stdin


def minCostClimbingStairs(cost: List[int]) -> int:
    cost.append(0)
    i = len(cost) - 3

    while i >= 0:
        cost[i] += cost[i+1] if cost[i+1] < cost[i+2] else cost[i+2]
        i -= 1

    return cost[0] if cost[0] < cost[1] else cost[1]
        
f = open("user.out","w") 
for cost in map(loads, stdin):
    print(minCostClimbingStairs(cost), file=f)

exit(0)
# @lc code=end
