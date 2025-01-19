# Sliding Window Pattern

class Solution:
    def rob(self, nums: List[int]) -> int:
        # 0ms Solution
        pick = notpick = 0
        # [2,7,9,3,1]
        for num in nums:
            temp = pick
            pick = max(pick, notpick + num)
            notpick = temp
        return max(pick, notpick)