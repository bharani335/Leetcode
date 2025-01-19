class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 17ms Solution
        # if not nums:
        #     return []
        #
        # def bt(start, target, track, nums):
        #     if target == 0:
        #         # 结束条件
        #         res.append(track[:])
        #         return
        #     elif target<0:
        #         return
        #     else:
        #         for i in range(start,len(nums)):
        #             if i>start and nums[i]==nums[i-1]:
        #                 continue
        #             if nums[i]>target:
        #                 break
        #             bt(i+1, target-nums[i], track+[nums[i]], nums)
        #
        #     pass
        # res = []
        # track = []
        # nums.sort()
        # bt(0, target, track, nums)
        # return res

        def dfs(pos, cur, total):
            if total == target:
                res.append(cur[:])
                return
            if total > target:
                return
            for i in range(pos, list_size):
                if i > pos and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break

                dfs(i + 1, cur + [candidates[i]], total + candidates[i])

        res = []
        list_size = len(candidates)
        candidates.sort()
        dfs(0, cur=[], total=0)
        return res


obj = Solution()
candidates = [2, 3, 5]
target = 8
candidates = [10, 1, 2, 7, 6, 1, 5, 2, 4]
target = 8
print(obj.combinationSum2(candidates, target))