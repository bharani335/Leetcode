from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [ [1]*n for x in range(n)]
        cur = 0
        val = 1
        while cur < n-1:
            row, col = cur, cur
            while col + cur < n:
                matrix[row][col] = val
                val += 1
                col += 1
            col -= 1
            row += 1

            while row + cur < n:
                matrix[row][col] = val
                val += 1
                row += 1
            row -= 1
            col -= 1

            while col >= cur:
                matrix[row][col] = val
                val += 1
                col -= 1
            col += 1
            row -= 1

            while row > cur:
                matrix[row][col] = val
                val += 1
                row -= 1
            row += 1

            cur += 1
        for x in matrix:
            print(*x)
        return matrix


obj = Solution()
print(obj.generateMatrix(n=4))