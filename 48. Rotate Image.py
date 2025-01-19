from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        g_cur = len(matrix) - 1
        row, col = 0, 0

        while g_cur > 0:
            l_cur = 0
            while l_cur < g_cur:
                matrix[row+l_cur][col+g_cur], matrix[row+g_cur][col+g_cur-l_cur], matrix[row+g_cur-l_cur][col], matrix[row][col+l_cur] = matrix[row][col+l_cur], matrix[row+l_cur][col+g_cur], matrix[row+g_cur][col+g_cur-l_cur], matrix[row+g_cur-l_cur][col]
                print(row, col)
                l_cur += 1
            row += 1
            col += 1
            g_cur -= 2

    # def rotate(self, matrix: List[List[int]]) -> None:
    #     y = len(matrix)
    #     for x in range(len(matrix)//2):
    #         y -= 1
    #         matrix[x], matrix[y] = matrix[y], matrix[x]
    #     x, y = 0, 1
    #     while x+y < (len(matrix)-1)*2:
    #         print(x,y)
    #         matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
    #         y += 1
    #         if y > len(matrix)-1:
    #             x += 1
    #             y = x+1

obj = Solution()
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
for x in matrix:
    print(*x)
print(obj.rotate(matrix))
for x in matrix:
    print(*x)