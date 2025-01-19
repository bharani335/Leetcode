from collections import Counter
from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pair = 0
        single = 0
        for x, y in Counter(nums).items():
            pair += y // 2
            single += y % 2
        return [pair, single]


obj = Solution()
nums = [1, 3, 2, 1, 3, 2, 2]
print(obj.numberOfPairs(nums))
