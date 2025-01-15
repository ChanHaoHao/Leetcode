class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bit2 = bin(num2)[2::]
        bit2 = Counter(bit2)['1']

        bit1 = bin(num1)[2::]
        res = bit1[::-1]
        bit1 = Counter(bit1)['1']

        if bit1>bit2:
            key = '1'
            addi = '0'
        elif bit1<bit2:
            key = '0'
            addi = '1'
        else:
            return num1

        for x in range(abs(bit2-bit1)):
            if key in res:
                res = res[0:res.index(key)] + addi + res[res.index(key)+1::]
            else:
                res += addi

        return int(res[::-1], 2)