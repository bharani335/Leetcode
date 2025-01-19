from typing import List
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        for x in permutations(nums):
            if list(x) not in res:
                res.append(list(x))
        return res


Obj = Solution()
nums = [1, 9, 1]
print(Obj.permute(nums))
