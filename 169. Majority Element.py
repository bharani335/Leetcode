from collections import Counter


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return Counter(nums).most_common(1)[0][0]

        # return max(set(nums), key=nums.count)

        nums.sort()
        return nums[len(nums)//2]

obj = Solution()
nums = [3, 2, 3]
print(obj.majorityElement(nums))
