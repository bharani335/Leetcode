from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i = m - 1
        j = 0
        while i >= 0 and j < n:
            if matrix[i][j] > target:
                i -= 1
                continue
            elif matrix[i][j] < target:
                j += 1
                continue
            else:
                return True
        return False

obj = Solution()
matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
matrix = [[1],[2],[3],[4],[5]]
matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
target = 2
for x in matrix:
    print(*x)
print(obj.searchMatrix(matrix, target))
