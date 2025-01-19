class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
    #     # 30ms Solution
    #     path, res = [], []
    #     candidates.sort()
    #     self.helper(res, path, candidates, target, 0)
    #     return res
    #
    # def helper(self, res, path, candidates, target, idx):
    #     for i in range(idx, len(candidates)):
    #         new_target = target - candidates[i]
    #         if new_target < 0:
    #             return
    #         else:
    #             if new_target == 0:
    #                 res.append(path + [candidates[i]])
    #             else:
    #                 self.helper(res, path + [candidates[i]], candidates, new_target, i)


        # # 30ms Solution
        # result = []
        # candidates = sorted(candidates)
        #
        # def dfs(remain, stack):
        #     if remain == 0:
        #         result.append(stack)
        #         return
        #
        #     for item in candidates:
        #         if item > remain: break
        #         if stack and item < stack[-1]:
        #             continue
        #         else:
        #             dfs(remain - item, stack + [item])


        def dfs(i, cur, total):
            if total == target:
                res.append(cur[:])
                return
            if i >= list_size or total > target:
                return
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            i += 1
            dfs(i, cur, total)

        res = []
        list_size = len(candidates)
        dfs(i=0, cur=[], total=0)
        return res


obj = Solution()
candidates = [2, 3, 5]
target = 8
candidates = [2, 3, 5, 6, 7]
target = 7
print(obj.combinationSum(candidates, target))
