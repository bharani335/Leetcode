class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        size = len(nums)
        x = 0
        while x < size and nums[x] < target:
            x += 1
            continue
        
        return x
            
