from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        maxi = [len(nums)-1, nums[-1]]
        for x in range(len(nums) - 2, -1, -1):
            if maxi[1] <= nums[x]:
                maxi[0] = x
                maxi[1] = nums[x]
                continue
            else:
                mini = [x, nums[x]]
                for y in range(x + 1, len(nums)):
                    if mini[1] < nums[y] < maxi[1]:
                        maxi[0] = y
                        maxi[1] = nums[y]
                # if maxi[0] == x+1:
                nums[x], nums[maxi[0]] = nums[maxi[0]], nums[x]
                temp = nums[x+ 1:]
                nums[x + 1:] = sorted(temp)
                return nums
        nums.sort()
        return nums

    # def nextPermutation(self, nums: List[int]) -> None:
    #     i = j = len(nums) - 1
    #     while i > 0 and nums[i - 1] >= nums[i]:
    #         i -= 1
    #
    #     if i == 0:  # nums are in descending order
    #         nums.reverse()
    #         return
    #
    #     k = i - 1  # find the last "ascending" position
    #     while nums[j] <= nums[k]:
    #         j -= 1
    #     nums[k], nums[j] = nums[j], nums[k]
    #     l, r = k + 1, len(nums) - 1  # reverse the second part
    #
    #     while l < r:
    #         nums[l], nums[r] = nums[r], nums[l]
    #         l += 1;
    #         r -= 1


obj = Solution()
nums = [2, 3, 1]
# nums = [1, 2, 3]
# nums = [1, 1, 5]
# nums = [5, 1, 1]
# nums = [1, 1, 1]
# nums = [3, 2, 1]
# nums = [1, 3, 2] # [2,1,3]
# nums = [2,3,1,3,3] # [2,3,3,1,3]
print(obj.nextPermutation(nums))
