from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # pointer1 = 0
        # pointer2 = 1
        # pointer3 = 2
        # size = len(nums)
        # if size <= 2:
        #     return len(nums)
        # if nums[pointer1] != nums[pointer2]:
        #     pointer1, pointer2 = 1, 1
        # while pointer3 < size:
        #     print(nums,pointer1, pointer2, pointer3)
        #     if nums[pointer1] == nums[pointer3]:
        #         if pointer1 == pointer2:
        #             pointer2 += 1
        #             nums[pointer2] = nums[pointer3]
        #     else:
        #         pointer1 = pointer2 + 1
        #         pointer2 = pointer1
        #         nums[pointer1] = nums[pointer3]
        #     pointer3 += 1
        # print(nums, pointer1, pointer2, pointer3)
        # return pointer2

        # 39ms Solution
        if len(nums) <= 2:
            return len(nums)

        left = 2

        for right in range(2, len(nums)):
            if nums[right] != nums[left - 2]:
                nums[left] = nums[right]
                left += 1

        return left


nums = [-1, 0, 0, 0, 0, 3, 3]
print(Solution().removeDuplicates([1, 1, 1, 2, 2, 3]))  # [1,1,2,2,3] 5
# print(Solution().removeDuplicates(nums))  # [-1,0,3] 3
