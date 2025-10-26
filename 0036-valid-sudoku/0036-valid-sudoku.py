class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        square = [[] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    if board[i][j] in rows[i]:
                        return False
                    rows[i].append(board[i][j])
                    if board[i][j] in cols[j]:
                        return False
                    cols[j].append(board[i][j])
                    if board[i][j] in square[i//3*3 + j//3]:
                        return False
                    square[i//3*3 + j//3].append(board[i][j])

        return True