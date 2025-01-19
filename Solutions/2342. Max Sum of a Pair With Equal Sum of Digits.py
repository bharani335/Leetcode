from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dc = {}
        maxi = -1
        nums.sort(reverse=True)
        print(nums)
        for x in nums:
            y = sum(int(i) for i in str(x))
            if dc.get(y, 0):
                # print(dc[y])
                if dc[y] + x > maxi:
                    maxi = dc[y] + x
            else:
                dc[y] = x
            # print(x, y)
            # print(dc)
        return maxi

obj = Solution()
nums = [18, 43, 36, 13, 7]
nums = [10,12,19,14]
nums = [368,369,307,304,384,138,90,279,35,396,114,328,251,364,300,191,438,467,183]
print(obj.maximumSum(nums))
