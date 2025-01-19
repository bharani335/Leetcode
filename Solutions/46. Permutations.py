from typing import List
import itertools


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        for x in itertools.permutations(nums):
            res.append(list(x))
        return res

        # 20ms Solution
        # return list(list(i) for i in permutations(nums))


Obj = Solution()
nums = [1, 9, 1]
print(Obj.permute(nums))
