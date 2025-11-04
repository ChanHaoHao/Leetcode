class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c]==word[0]:
                    visit = [[False] * COL for _ in range(ROW)]
                    index = 0
                    
                    def dfs(r, c, index):
                        if 0<=r<ROW and 0<=c<COL and not visit[r][c]:
                            if board[r][c]==word[index]:
                                visit[r][c] = True
                                if index==len(word)-1:
                                    return True

                                res = dfs(r+dirs[0][0], c+dirs[0][1], index+1) or dfs(r+dirs[1][0], c+dirs[1][1], index+1) or dfs(r+dirs[2][0], c+dirs[2][1], index+1) or dfs(r+dirs[3][0], c+dirs[3][1], index+1)
                                visit[r][c] = False
                                return res
                    
                    if dfs(r, c, index):
                        return True

        return False