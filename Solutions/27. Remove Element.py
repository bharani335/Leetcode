from collections import Counter
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [x for x in nums if x != val]
        return len(nums)


nums = [3, 2, 2, 3, 3, 3, 3]
val = 3
print(Solution().removeElement(nums, val))
