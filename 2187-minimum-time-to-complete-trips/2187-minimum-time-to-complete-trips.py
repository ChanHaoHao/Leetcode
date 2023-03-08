class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # initialize the binary search
        l, r=1, min(time)*totalTrips

        while l<r:
            m=(l+r)//2
            
            # get the sum of how many trips could be done
            # if we do more trips, turn r to m
            # else turn l to m+1
            if sum(m//t for t in time)>=totalTrips:
                r=m
            else:
                l=m+1

        return l
