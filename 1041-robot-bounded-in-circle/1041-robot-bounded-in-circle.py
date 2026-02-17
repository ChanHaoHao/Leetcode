class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 0: North, 1: West, 2: South, 3: East
        dirs = {0: [0, 1], 1: [-1, 0], 2: [0, -1], 3: [1, 0]}
        # L = dirs+1, R = dirs-1
        head, x, y = 0, 0, 0

        for c in instructions:
            if c == 'G':
                x += dirs[head][0]
                y += dirs[head][1]
            elif c == 'L':
                head = (head + 1) % 4
            elif c == 'R':
                head = (head + 3) % 4
        
        print(f"{head} {x} {y}")
        if head != 0 or (x == 0 and y == 0):
            return True
        return False