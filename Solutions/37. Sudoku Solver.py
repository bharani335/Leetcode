from typing import List
from copy import copy


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        s = set(map(str, range(1, 10)))
        colp = [s.copy() for _ in range(9)]
        rowp = [s.copy() for _ in range(9)]
        boxp = [[s.copy() for _ in range(3)] for _ in range(3)]
        unassigned = set([(i, j) for i in range(9) for j in range(9) if board[i][j] == '.'])

        for i in range(9):
            for j in range(9):
                if (ch := board[i][j]) != '.':
                    colp[j].remove(ch)
                    rowp[i].remove(ch)
                    boxp[i // 3][j // 3].remove(ch)

        def find_min_digit_count_unassigned():
            min_count = 10
            mini, minj = -1, -1
            for i, j in unassigned:
                union = rowp[i] & colp[j] & boxp[i // 3][j // 3]
                if len(union) == 1:
                    return i, j
                elif len(union) < min_count:
                    min_count = len(union)
                    mini, minj = i, j
            return mini, minj

        def solve():
            i, j = find_min_digit_count_unassigned()
            if i == j == -1:
                return True
            unassigned.remove((i, j))
            for ch in rowp[i] & colp[j] & boxp[i // 3][j // 3]:
                board[i][j] = ch
                rowp[i].remove(ch)
                colp[j].remove(ch)
                boxp[i // 3][j // 3].remove(ch)
                if solve():
                    return True
                board[i][j] = '.'
                rowp[i].add(ch)
                colp[j].add(ch)
                boxp[i // 3][j // 3].add(ch)
            unassigned.add((i, j))
            return False

        solve()

    def print_board(self, board):
        for x in range(9):
            if x % 3 == 0:
                print("=========================")
            for y in range(9):
                if y % 3 == 0:
                    print("|", end=" ")
                print(board[x][y], end=" ")
            print("|")
        print("=========================")
# class Solution:
#     def solveSudoku(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         self.solve(board, num=1, pos= [0, 0])
#
#     def print_board(self, board):
#         for x in range(9):
#             if x % 3 == 0:
#                 print("=========================")
#             for y in range(9):
#                 if y % 3 == 0:
#                     print("|", end=" ")
#                 print(board[x][y], end=" ")
#             print("|")
#         print("=========================")
#
#     def valid(self, board, pos, num):
#         # Check num
#         if num > 9:
#             return False
#         # Check Column
#         temp = "".join(x for x in board[pos[0]])
#         if str(num) in temp:
#             return False
#         # Check Row
#         temp = "".join(x[pos[1]] for x in board)
#         if str(num) in temp:
#             return False
#         # Check Box
#         col = pos[0] // 3 * 3
#         row = pos[1] // 3 * 3
#         for x in range(col, col + 3):
#             for y in range(row, row + 3):
#                 if board[x][y] == str(num):
#                     return False
#         return True
#
#     def solve(self, board, num, pos):
#         x = pos[0]
#         while x in range(9):
#             y = pos[1]
#             cache = copy(board[x])
#             while y in range(9):
#                 pos = [x, y]
#                 if board[x][y] == ".":
#                     if str(num) not in cache and self.valid(board, pos, num):
#                         pos = [x, y + 1]
#                         board[x][y] = str(num)
#                         cache.append(str(num))
#                         if self.solve(board, num=1, pos=pos):
#                             return True
#                         else:
#                             board[x][y] = "."
#                             cache.remove(str(num))
#                             num += 1
#                             if num > 9:
#                                 return False
#                     else:
#                         num += 1
#                         while str(num) in cache:
#                             num += 1
#                         if num > 9:
#                             return False
#                 else:
#                     y += 1
#             x += 1
#             pos[0] = x
#             pos[1] = 0
#         return True


obj = Solution()
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
# obj.print_board(board)
# obj.solve(board, 1, pos=[0, 0])
obj.print_board(board)
obj.solveSudoku(board)
