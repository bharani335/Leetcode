from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(list(set(nums)))
        return len(nums)


nums = [-1, 0, 0, 0, 0, 3, 3]
print(Solution().removeDuplicates(nums))  # [-1,0,3] 3
