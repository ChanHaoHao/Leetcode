class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # find the duplicate points first, because if they are different, they need to move twice
        duplicates = a&b
        # find the difference between c and (a|b)
        diff = c^(a|b)

        # if there is no difference
        if diff==0:
            return 0

        # get the number of bits that need to move twice
        move2 = bin(duplicates&diff).count("1")

        return move2+bin(diff).count("1")