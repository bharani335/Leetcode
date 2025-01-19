from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1, 1]
        if rowIndex == 0:
            return [1]
        for x in range(rowIndex - 1):
            local_res = [*res]
            for y in range(1, len(res)):
                res[y] = local_res[y-1] + local_res[y]
            res.append(1)
        return res

    # def getRow(self, rowIndex: int) -> List[int]:
    #     r = [1]
    #     for _ in range(rowIndex):
    #         r = [1, *(map(sum, zip(r, r[1:]))), 1]
    #     return r

obj = Solution()
print(obj.getRow(rowIndex=1))