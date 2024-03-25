class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # remain = []

        # for x in asteroids:
        #     # when there are no asteroids remain
        #     if len(remain)==0:
        #         remain.append(x)
        #         continue
            
        #     while len(remain)>0:
        #         prev = remain.pop()
        #         # if the two asteroids are in the same direction or they will never collide
        #         if prev*x>0 or prev<0:
        #             remain.append(prev)
        #             remain.append(x)
        #             break
        #         # deal with the collisions
        #         else:
        #             if abs(prev)>abs(x):
        #                 remain.append(prev)
        #                 break
        #             elif abs(prev)==abs(x):
        #                 break
        #             elif len(remain)==0:
        #                 remain.append(x)
        #                 break

        # return remain

        remain = []

        for x in asteroids:
            # if there are no asteroids remain
            if len(remain)==0:
                remain.append(x)
            else:
                while True:
                    # if the asteroids will collide
                    if remain[-1]>0 and x<0:
                        collide = remain[-1]+x
                        # same asteroid size
                        if collide==0:
                            remain.pop()
                            break
                        # the previous asteroid is smaller than the current one
                        elif collide<0:
                            remain.pop()
                        # the current asteroid is smaller than the previous one
                        else:
                            break

                        # if there are no asteroids remain
                        if len(remain)==0:
                            remain.append(x)
                            break
                    # if they won't collide, add it to the remaining
                    else:
                        remain.append(x)
                        break

        return remain