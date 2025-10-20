class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        # vis is used to store the visited string, since the string length is n, it can rotate at most n times
        vis = [False] * n
        res = s
        # double the length of s for convenience in extracting the rotated string t
        s = s + s
        i = 0
        while not vis[i]:
            vis[i] = True
            # since every number is between 0-9, adding more than 9 times will just repeat a previous state
            for j in range(10):
                # if b is even, the upper limit for k will be 0, otherwise 9
                k_limit = 0 if b % 2 == 0 else 9
                for k in range(k_limit + 1):
                    # before each accumulation, re-truncate t from the double length of s
                    t = list(s[i : i + n])
                    # change the odd number at each iteration
                    for p in range(1, n, 2):
                        t[p] = str((int(t[p]) + j * a) % 10)
                    # only works when b is odd, which makes the numbers at even position change
                    for p in range(0, n, 2):
                        t[p] = str((int(t[p]) + k * a) % 10)
                    t_str = "".join(t)
                    if t_str < res:
                        res = t_str
            # store which steps we have gone through
            i = (i + b) % n
        return res