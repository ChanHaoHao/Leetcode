class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy=max(candies)
        # res=[]

        # for i in candies:
        #     if i+extraCandies<maxCandy:
        #         res.append(False)
        #     else:
        #         res.append(True)
        res=[i+extraCandies>=maxCandy for i in candies]
        return res