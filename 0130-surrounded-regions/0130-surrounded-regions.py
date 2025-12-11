class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        H, W = len(board), len(board[0])
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for h in range(H):
            if board[h][0]=="O" and (h,0) not in visited:
                queue = [(h,0)]
                while queue:
                    local_h, local_w = queue.pop()
                    board[local_h][local_w] = "N"

                    for dir in dirs:
                        cur_h, cur_w = local_h+dir[0], local_w+dir[1]
                        if 0<=cur_h<H and 0<=cur_w<W and board[cur_h][cur_w]=="O" and (cur_h, cur_w) not in visited:
                            queue.append((cur_h, cur_w))
        for h in range(H):
            if board[h][W-1]=="O" and (h,W-1) not in visited:
                queue = [(h,W-1)]
                while queue:
                    local_h, local_w = queue.pop()
                    board[local_h][local_w] = "N"

                    for dir in dirs:
                        cur_h, cur_w = local_h+dir[0], local_w+dir[1]
                        if 0<=cur_h<H and 0<=cur_w<W and board[cur_h][cur_w]=="O" and (cur_h, cur_w) not in visited:
                            queue.append((cur_h, cur_w))
        for w in range(W):
            if board[0][w]=="O" and (0,w) not in visited:
                queue = [(0,w)]
                while queue:
                    local_h, local_w = queue.pop()
                    board[local_h][local_w] = "N"

                    for dir in dirs:
                        cur_h, cur_w = local_h+dir[0], local_w+dir[1]
                        if 0<=cur_h<H and 0<=cur_w<W and board[cur_h][cur_w]=="O" and (cur_h, cur_w) not in visited:
                            queue.append((cur_h, cur_w))
        for w in range(W):
            if board[H-1][w]=="O" and (H-1, w) not in visited:
                queue = [(H-1,w)]
                while queue:
                    local_h, local_w = queue.pop()
                    board[local_h][local_w] = "N"

                    for dir in dirs:
                        cur_h, cur_w = local_h+dir[0], local_w+dir[1]
                        if 0<=cur_h<H and 0<=cur_w<W and board[cur_h][cur_w]=="O" and (cur_h, cur_w) not in visited:
                            queue.append((cur_h, cur_w))
        
        for h in range(H):
            for w in range(W):
                if board[h][w]=="O":
                    board[h][w] = "X"
                elif board[h][w]=="N":
                    board[h][w] = "O"