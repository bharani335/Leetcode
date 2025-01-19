from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Time Limit Exceeded
        # def will_reach_end(jumps_available, nums):
        #     if jumps_available <= 0:
        #         return False
        #     elif jumps_available >= len(nums):
        #         return True
        #     else:
        #         for i in range(jumps_available):
        #             if will_reach_end(nums[jumps_available], nums[jumps_available:]) is False:
        #                 jumps_available -= 1
        #             else:
        #                 return True
        #         return False
        # return will_reach_end(nums[0], nums)

        maximum_index_can_be_reached = 0
        current_index = 0
        while current_index <= maximum_index_can_be_reached and current_index < len(nums):
            maximum_index_can_be_reached = max(maximum_index_can_be_reached, current_index + nums[current_index])
            current_index += 1
        return True if maximum_index_can_be_reached >= len(nums) else False

        # 348ms Solution
        # maximum_index_can_be_reached = 0
        # current_index = 0
        # while current_index <= maximum_index_can_be_reached and current_index < len(nums):
        #     maximum_index_can_be_reached = max(maximum_index_can_be_reached, current_index + nums[current_index])
        #     current_index += 1
        # return True if maximum_index_can_be_reached >= len(nums) else False

print(Solution().canJump(nums=[2, 3, 1, 1, 4])) # True
print(Solution().canJump(nums=[3, 2, 1, 0, 4])) # False
print(Solution().canJump(nums=[2, 0, 6, 9, 8, 4, 5, 0, 8, 9, 1, 2, 9, 6, 8, 8, 0, 6, 3, 1, 2, 2, 1, 2, 6, 5, 3, 1, 2, 2, 6, 4, 2, 4, 3, 0, 0, 0, 3, 8, 2, 4, 0, 1, 2, 0, 1, 4, 6, 5, 8, 0, 7, 9, 3, 4, 6, 6, 5, 8, 9, 3, 4, 3, 7, 0, 4, 9, 0, 9, 8, 4, 3, 0, 7, 7, 1, 9, 1, 9, 4, 9, 0, 1, 9, 5, 7, 7, 1, 5, 8, 2, 8, 2, 6, 8, 2, 2, 7, 5, 1, 7, 9, 6])) # False
