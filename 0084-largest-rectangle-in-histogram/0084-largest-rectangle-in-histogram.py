class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        window=list()
        window.append((heights[0], 0))
        ans=heights[0]

        for x in range(1, len(heights)):
            # if the stack is in accending order, keep stacking
            if heights[x]>=heights[x-1]:
                window.append((heights[x], x))
            # else pop till there is nothing in the stack or the stack is back to accending order
            else:
                while len(window)!=0:
                    tmp=window.pop()
                    # back to the accending order
                    if tmp[0]<=heights[x]:
                        window.append(tmp)
                        break
                    # keep poping and calculate the area it can make (its index till the current)
                    else:
                        ans=max(ans, tmp[0]*(x-tmp[1]))
                    prev=tmp
                # save the heights index as the last height's index it popped (that will be the furthest it can reach)
                window.append((heights[x], prev[1]))
        
        # deal with the remaining heights
        while len(window)>0:
            tmp=window.pop()
            # since they all can reach the end of the stack, the width will be the distance to the end
            ans=max(ans, tmp[0]*(len(heights)-tmp[1]))

        return ans