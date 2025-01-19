from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k != 0:
            nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]

        # 195ms Solution
        n = k % len(nums)
        nums[:] = nums[-n:] + nums[:-n]


Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)
