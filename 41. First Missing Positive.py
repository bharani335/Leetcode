class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # 188ms Solution
        # unique = set( nums )
        # i = 1
        # while i in unique:
        #     i += 1
        # return i

        if 1 in nums:
            nums = list(set(nums))
            nums.sort()
            start = nums.index(1)
        else:
            return 1
        i = 1
        for x in (nums[start:]):
            if x != i:
                return i
            i += 1
        return i


Obj = Solution()
nums = [1, 2, 0]
nums = [3, 4, -1, 1]
nums = [7, 8, 9, 11, 12]
print(Obj.firstMissingPositive(nums))
