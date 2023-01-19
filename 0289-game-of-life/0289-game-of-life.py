class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def check(x: int, y: int):
            if board[x][y]:
                num=-1
            else:
                num=0
            for a in range(-1,2):
                if x+a<0 or x+a>=height:
                    continue
                for b in range(-1,2):
                    if y+b<0 or y+b>=width:
                        continue
                    num+=board[x+a][y+b]
                    if num>3:
                        return num
            return num    
                    
        height = len(board)
        width = len(board[0])
        next_life = [[0 for x in range(width)] for y in range(height)]

        for x in range(height):
            for y in range(width):
                if board[x][y]:
                    if check(x,y)<2:
                        next_life[x][y]=0
                    elif check(x,y)==2 or check(x,y)==3:
                        next_life[x][y]=1
                    else:
                        next_life[x][y]=0
                else:
                    if check(x,y)==3:
                        next_life[x][y]=1
                        
        for x in range(height):
            for y in range(width):
                board[x][y] = next_life[x][y]