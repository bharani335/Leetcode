from functools import reduce


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return min(set(nums), key=nums.count)

        #Copied
        return reduce(lambda x,y: x^y, nums)

obj = Solution()
nums = [4,1,2,1,2]
print(obj.singleNumber(nums))