class Solution:
    def romanToInt(self, s: str) -> int:
        convert = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        # before = {"I": ["V", "X"], "X": ["L", "C"], "C": ["D", "M"]}

        # ans, n, i = 0, len(s), 0
        # while i<n:
        #     if s[i] in before and i+1<n and s[i+1] in before[s[i]]:
        #         ans += convert[s[i+1]]-convert[s[i]]
        #         i += 2
        #     else:
        #         ans += convert[s[i]]
        #         i += 1
        # return ans

        arr = [convert[s[0]]]
        for i in range(1, len(s)):
            tmp = convert[s[i]]
            if tmp> arr[-1]:
                arr[-1] *= -1
            arr.append(tmp)
        
        return sum(arr)