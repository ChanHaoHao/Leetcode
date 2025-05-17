class Solution:
    def maxScore(self, n: int, edges: List[List[int]]) -> int:
        scores = [1, 2]

        # The solution for n is f(n)
        # For n+1, it should be insert between n and n-1 to have the maximum value
        # So it can be solved recursively, which we add the previous solution + (n+1)*n + n*(n-1)
        # And substract the previous connected edge n*(n-1)
        for x in range(2, n):
            scores.append(scores[x-1] + (x+1)*x + (x+1)*(x-1) - x*(x-1))
        
        # and if the edges created a cycle, 2 will be the neighbor of 1
        if len(edges)==n:
            return scores[n-1]+2
        return scores[n-1]