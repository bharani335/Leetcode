from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        hindex = 0
        citations.sort(reverse=True)
        for i, j in enumerate(citations, 1):
            if i > j:
                break
            hindex = i
        return hindex


print(Solution().hIndex([3, 0, 6, 1, 5]))  # 3
print(Solution().hIndex([1, 3, 1]))  # 1
print(Solution().hIndex([3, 0, 6, 1, 5]))  # 3
print(Solution().hIndex([3, 0, 6, 1, 5]))  # 3
print(Solution().hIndex([3, 0, 6, 1, 5]))  # 3
print(Solution().hIndex([3, 0, 6, 1, 5]))  # 3
