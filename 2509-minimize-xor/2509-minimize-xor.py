class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # # count the bits in num1 and num2 
        # # then determine how many 1's or 0's needed to be changed
        # bit2 = bin(num2)[2::]
        # bit2 = Counter(bit2)['1']

        # bit1 = bin(num1)[2::]
        # # reverse num1 to start from the smallest
        # res = bit1[::-1]
        # bit1 = Counter(bit1)['1']

        # if bit1>bit2:
        #     key = '1'
        #     addi = '0'
        # elif bit1<bit2:
        #     key = '0'
        #     addi = '1'
        # else:
        #     return num1

        # for x in range(abs(bit2-bit1)):
        #     if key in res:
        #         res = res[0:res.index(key)] + addi + res[res.index(key)+1::]
        #     else:
        #         res += addi

        # return int(res[::-1], 2)

        a, b = num1.bit_count(), num2.bit_count()
        res = num1
        # set to the largest possible int
        for i in range(32):
            # if num1 has more bit that num2, turn 1 into 0
            if a > b and (1 << i) & num1 > 0:
                res ^= 1<<i
                a -= 1
            # if num2 has more bit than num1, turn 0 into 1
            if a < b and (1 << i) & num1 == 0:
                res ^= 1 << i
                a += 1
        return res