class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)

        if n%2==1:
            return False

        lock = []
        unlock = []
        for x in range(n):
            if locked[x]=="1":
                if s[x]=="(":
                    lock.append(x)
                else:
                    if len(lock)!=0:
                        lock.pop()
                    elif len(unlock)!=0:
                        unlock.pop()
                    else:
                        return False
            else:
                unlock.append(x)
        
        if len(lock)>len(unlock):
            return False

        while len(lock)!=0:
            if lock[-1]>unlock[-1]:
                return False
            lock.pop()
            unlock.pop()
        return True
