class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """  

        n = len(matrix)            
        to_change = []
        for i in range(n - 1):
            for j in range(i, n - i - 1):
                to_change.append([i, j])
        for x in to_change:
            i, j = x[0], x[1]
            tmp = matrix[i][j]
            for _ in range(3):
                matrix[i][j] = matrix[n - 1 - j][i]
                i, j = n - 1 - j, i 
            matrix[i][j] = tmp
        return True

a = Solution()
# a.rotate([[1, 2], [3, 4]])
a.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
# a.rotate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
# a.rotate([[i * 5 + j + 1 for j in range(5)] for i in range(5)])  # 5x5
# a.rotate([[i * 6 + j + 1 for j in range(6)] for i in range(6)])  # 6x6

