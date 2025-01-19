from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_to_right = [1]
        for num in nums:
            left_to_right.append(left_to_right[-1] * num)
        left_to_right.pop()
        right_to_left = 1
        for i in range(len(nums) - 1, -1, -1):
            x = nums[i]
            nums[i] = right_to_left * left_to_right[i]
            right_to_left *= x
        return nums


# print(Solution().productExceptSelf()) #
print(Solution().productExceptSelf([1, 2, 3, 4]))  # [24,12,8,6]
print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))  # [0,0,9,0,0]
