class Solution:
    def intToRoman(self, num: int) -> str:
        # store the dict by index
        convert = {0: ["I", "V"], 1: ["X", "L"], 2: ["C", "D"], 3: ["M", "M"]}

        ans = ""
        for i in range(4, -1, -1):
            if num//10**i!=0:
                curr = num//10**i
                if 1<=curr<=3:
                    ans += convert[i][0]*curr
                elif 5<=curr<=8:
                    ans += convert[i][1]+convert[i][0]*(curr-5)
                elif curr==4:
                    ans += convert[i][0] + convert[i][1]
                elif curr==9:
                    ans += convert[i][0] + convert[i+1][0]
            num = num%10**i
        
        return ans