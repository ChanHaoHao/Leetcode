class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # this turns the row and col into a string and use it as a key for the dict
        def toString(nums):
            string = ""
            for x in nums:
                string+=str(x)+"."

            return string

        rows = dict()
        cols = dict()

        for x in range(len(grid[0])):
            tmp = toString(grid[x])
            if tmp in rows:
                rows[tmp] += 1
            else:
                rows[tmp] = 1

            tmp = []
            for y in range(len(grid[0])):
                tmp.append(grid[y][x])
            tmp = toString(tmp)
            if tmp in cols:
                cols[tmp] += 1
            else:
                cols[tmp] = 1

        ans = 0
        for x in rows:
            if x in cols:
                ans += rows[x]*cols[x]
        
        return ans