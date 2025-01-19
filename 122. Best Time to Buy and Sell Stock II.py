import math
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # ans = 0
        # cost = prices[0]
        # flag = True
        # for today_price in range(1, len(prices)):
        #     if prices[today_price-1] > prices[today_price]:
        #         flag = False
        #         ans += (prices[today_price-1] - cost)
        #         cost = prices[today_price]
        #     else:
        #         flag = True
        #         cost = min(cost, prices[today_price])
        # if flag:
        #     ans += prices[-1] - cost
        # return ans

        # 46ms Solution
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit


print(Solution().maxProfit([1, 2, 3, 4, 5]))  # 4
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # 7
print(Solution().maxProfit([7, 6, 4, 3, 1]))  # 0
