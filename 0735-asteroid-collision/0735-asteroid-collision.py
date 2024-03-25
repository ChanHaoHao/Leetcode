class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        remain = []

        for x in asteroids:
            if len(remain)==0:
                remain.append(x)
                continue
            while len(remain)>0:
                prev = remain.pop()
                # if the two asteroids are in the same direction or they will never collide
                if prev*x>0 or prev<0:
                    remain.append(prev)
                    remain.append(x)
                    break
                # deal with the collisions
                else:
                    if abs(prev)>abs(x):
                        remain.append(prev)
                        break
                    elif abs(prev)==abs(x):
                        break
                    elif len(remain)==0:
                        remain.append(x)
                        break

        return remain
