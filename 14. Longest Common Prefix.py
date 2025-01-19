class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # 4ms solution
        # shortest = min(strs,key=len)
        # for i in strs:
        #     while len(shortest)>0:
        #         if i.startswith(shortest):
        #             break
        #         else:
        #             shortest=shortest[:-1]
        # return shortest

        # My Solution
        def return_common_prefix(val1, val2):
            for x in range(min(len(val1), len(val2)), -1, -1):
                if val1[:x] == val2[:x]:
                    return val1[:x]
            return False

        res = strs[0]
        for string in strs[1:]:
            res = return_common_prefix(res, string)
            if not res:
                return ""
        return res


Obj = Solution()
strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]
# strs = ["ab", "a"]
print(Obj.longestCommonPrefix(strs))
