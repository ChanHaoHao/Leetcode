class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs=[0]*len(spells)
        potions.sort()

        for i in range(len(spells)):
            l, r=0, len(potions)-1
            while l<=r:
                # this prevent mid to overflow
                mid=l+(r-l)//2
                if potions[mid]*spells[i]>=success:
                    r=mid-1
                else:
                    l=mid+1

            pairs[i]=len(potions)-l
        return pairs