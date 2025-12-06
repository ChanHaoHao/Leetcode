class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        H, W = len(board), len(board[0])
        # die = []
        # reproduction = []

        # for h in range(0, H):
        #     for w in range(0, W):
        #         neighbors = 0
        #         for i in range(-1, 2):
        #             if h+i>-1 and h+i<H:
        #                 for j in range(-1, 2):
        #                     if w+j>-1 and w+j<W:
        #                         neighbors += board[h+i][w+j]
                
        #         if board[h][w]==1:
        #             if neighbors<=2:
        #                 die.append((h, w))
        #             elif neighbors>4:
        #                 die.append((h, w))
        #         elif neighbors==3:
        #             reproduction.append((h, w))
        
        # for i in range(len(die)):
        #     x, y = die[i]
        #     board[x][y] = 0
        # for i in range(len(reproduction)):
        #     x, y = reproduction[i]
        #     board[x][y] = 1

        for h in range(H):
            for w in range(W):
                neighbors = 0
                for i in range(-1, 2):
                    if h+i>-1 and h+i<H:
                        for j in range(-1, 2):
                            if w+j>-1 and w+j<W:
                                if board[h+i][w+j]==1 or board[h+i][w+j]==2:
                                    neighbors += 1
                neighbors -= board[h][w]

                if (neighbors<2 or neighbors>3) and board[h][w]==1:
                    board[h][w] = 2
                elif neighbors==3 and board[h][w]==0:
                    board[h][w] = 3
        
        for h in range(H):
            for w in range(W):
                if board[h][w] == 2:
                    board[h][w] = 0
                elif board[h][w] == 3:
                    board[h][w] = 1
