class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        def in_square(board):
            nums = {f"{i}{j}": set() for i in (0, 3, 6) for j in (0, 3, 6)}
            for x in range(0, 9):
                for y in range(0, 9):
                    if board[x][y] == '.':
                        continue
                    if board[x][y] in nums[f'{3 * (x // 3)}{3 * (y // 3)}']:
                        return False
                    else:
                        nums[f'{3 * (x // 3)}{3 * (y // 3)}'].add(board[x][y])

            return True

        ## по квадратам уникальность

        if not in_square(board):
            return False
        

        ## по строкам уникальность
        for x in board:
            tmp = set()
            for y in x:
                if y == '.':
                    continue
                if y in tmp:
                    return False
                else:
                    tmp.add(y)
        
        ## по столбцам уникальность
        for y in range(9):
            tmp = set()
            for x in board:
                if x[y] == '.':
                    continue
                if x[y] in tmp:
                    return False
                else:
                    tmp.add(x[y])
        
        ## прошли все проверки
        return True

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

a = Solution()
print(a.isValidSudoku(board))