import math
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        cost = math.inf
        for today_price in prices:
            maxProfit = max(maxProfit, today_price - cost)
            cost = min(cost, today_price)
        return maxProfit

print(Solution().maxProfit([7, 6, 4, 3, 1]))  # 0
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # 5
print(Solution().maxProfit([7, 1, 5, 3, 6, 4, 0]))  # 5
