class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # result = []
        # while matrix:
        #     if matrix:
        #         result.extend(matrix[0])
        #         del matrix[0]
        #         matrix = list(zip(*matrix))
        #
        #     if matrix:
        #         result.extend(matrix[-1])
        #         del matrix[-1]
        #         matrix = list(zip(*matrix))
        #
        #     if matrix:
        #         result.extend(reversed(matrix[-1]))
        #         del matrix[-1]
        #         matrix = list(zip(*matrix))
        #
        #     if matrix:
        #         result.extend(reversed(matrix[0]))
        #         del matrix[0]
        #         matrix = list(zip(*matrix))
        #
        # return result

        # Copied
        return matrix and list(matrix.pop(0)) + self.spiralOrder(list(zip(*matrix))[::-1])

obj = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(obj.spiralOrder(matrix))