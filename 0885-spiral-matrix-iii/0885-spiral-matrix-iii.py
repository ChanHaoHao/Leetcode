class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        # greedy method - 
        # after observation, we know that going into spiral we need 1 right, 1 down, 2 left, 2 up, 3 right, etc...
        ans, count, step = [[rStart, cStart]], rows*cols-1, 1

        def in_matrix(r, c):
            nonlocal count, ans
            if r>=0 and r<rows and c>=0 and c<cols:
                count -= 1
                ans.append([r, c])

        while count:
            if step%2==1:
                for x in range(step):
                    cStart += 1
                    in_matrix(rStart, cStart)
                        
                for x in range(step):
                    rStart += 1
                    in_matrix(rStart, cStart)
            else:
                for x in range(step):
                    cStart -= 1
                    in_matrix(rStart, cStart)
                for x in range(step):
                    rStart -= 1
                    in_matrix(rStart, cStart)
            step += 1

        return ans