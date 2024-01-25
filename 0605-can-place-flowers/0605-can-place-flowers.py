class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for x in range(len(flowerbed)):
            if n==0:
                return True
            elif flowerbed[x]==0 and (x==0 or flowerbed[x-1]==0) and (x==len(flowerbed)-1 or flowerbed[x+1]==0):
                n -= 1
                flowerbed[x] = 1

        return n==0
#         # deal with the first and the end pot seperately
#         # if there is no enough space to plant
#         if len(flowerbed)-sum(flowerbed) < n:
#             return False
#         # deal with the situation that the first pot is empty
#         elif flowerbed[0]==0:
#             if len(flowerbed)==1:
#                 return True
#             elif flowerbed[1]==0:
#                 n -= 1
#                 flowerbed[0] = 1

#         for x in range(1, len(flowerbed)-1):
#             if n<=0:
#                 return True
#             elif sum(flowerbed[x-1:x+2])==0:
#                 n -= 1
#                 flowerbed[x] = 1
        
#         # deal with the situation that the last pot is empty
#         if len(flowerbed)>2 and flowerbed[-2]+flowerbed[-1]==0:
#             flowerbed[-1] = 1
#             n -= 1


#         if n>0:
#             return False
#         else:
#             return True
        