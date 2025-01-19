from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        minimum_jumps = 0
        current_index = 0
        while current_index + 1 < len(nums):
            minimum_jumps += 1
            if current_index + nums[current_index] + 1 >= len(nums):
                break
            current_index += 1
            maxi = nums[current_index] + current_index
            for i, j in enumerate(nums[current_index: current_index + nums[current_index-1]], current_index):
                if i+j >= maxi:
                    current_index = i
                    maxi = i+j
        return minimum_jumps


print(Solution().jump(nums=[1, 2, 3]))  # 2
print(Solution().jump(nums=[2, 1]))  # 1
print(Solution().jump(nums=[0]))  # 0
print(Solution().jump(nums=[2, 3, 0, 1, 4]))  # 2
print(Solution().jump(nums=[2, 3, 1]))  # 1
print(Solution().jump(nums=[1, 2, 1, 1, 1]))  # 3
print(Solution().jump(nums=[10,9,8,7,6,5,4,3,2,1,1,0]))  # 2
print(Solution().jump(nums=[3, 1, 1, 1, 1]))  # 2
print(Solution().jump(nums=[2,3,1,1,4]))  # 2
