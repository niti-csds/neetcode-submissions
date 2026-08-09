class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for i in range(9):
                #row
                if board[row][i] == '.':
                    continue 
                else:
                    if board[row][i] in seen:
                        return False
                    else:
                        seen.add(board[row][i])
        for col in range(9):
            seen_ = set()
            for i in range(9):
                if board[i][col] == '.':
                    continue
                else:
                    if board[i][col] in seen_:
                        return False
                    else:
                        seen_.add(board[i][col])
        for square in range(9): #9 small 3*3
            seen__ = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3)*3 +i
                    col = (square%3)*3 +j

                    if board[row][col] == '.':
                        continue
                    else:
                        if board[row][col] in seen__:
                            return False
                        else:
                            seen__.add(board[row][col])
        return True




