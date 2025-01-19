from collections import Counter
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        strs.sort(key=lambda x: len(x))
        i = 0
        while i < len(strs):
            temp1 = Counter(strs[i])
            sub_arr = [strs[i]]
            j = i + 1
            while i < j < len(strs) and len(strs[j]) == len(strs[i]):
                temp2 = Counter(strs[j])
                if temp2 == temp1:
                    sub_arr.append(strs[j])
                    del strs[j]
                    continue
                j += 1
            ans.append(sub_arr)
            i += 1
        return ans


Obj = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Obj.groupAnagrams(strs))
