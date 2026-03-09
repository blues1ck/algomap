import numpy as np


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        n, m = len(matrix), len(matrix[0])
        x = 0
        while x < n - x and x < m - x:  # пока есть незакрытый слой
            for i in range(x, m - x):
                res.append(matrix[x][i])
            for j in range(x + 1, n - x):
                res.append(matrix[j][m - 1 - x])
            if n - 1 - x > x:  # есть нижняя строка
                for i in range(m - 2 - x, x - 1, -1):
                    res.append(matrix[n - 1 - x][i])
            if m - 1 - x > x:  # есть левый столбец
                for j in range(n - 2 - x, x, -1):
                    res.append(matrix[j][x])
            x += 1
        return res

a = Solution()
matr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

print(a.spiralOrder(matr))