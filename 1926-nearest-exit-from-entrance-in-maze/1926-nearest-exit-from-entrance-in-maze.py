class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()

        height, width = len(maze), len(maze[0])
        visited = set()
        q.append([entrance[0], entrance[1]])
        visited.add((entrance[0], entrance[1]))

        step = 0
        while q:
            for _ in range(len(q)):
                y, x = q.popleft()

                for dirY, dirX in direction:
                    locY = y+dirY
                    locX = x+dirX

                    if locY>=0 and locY<height and locX>=0 and locX<width and maze[locY][locX]=="." and (locY, locX) not in visited:
                        # return the exit once it is found
                        if locY==0 or locY==height-1 or locX==0 or locX==width-1:
                            return step+1
                        q.append([locY, locX])
                        # add the point to visited once it is found, 
                        # so that visited points won't be added to the queue again, like:
                        # . . .
                        # . . .
                        # . . .
                        visited.add((locY, locX))
            step += 1
        
        return -1