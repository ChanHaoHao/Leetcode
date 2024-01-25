class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # the brute force using recursive (TLE)
        # def lcs_length(text1, text2):
        #     if len(text1)==0 or len(text2)==0:
        #         return 0
        #     elif text1[0]==text2[0]:
        #         return 1+lcs_length(text1[1::], text2[1::])
        #     else:
        #         return max(lcs_length(text1[1::], text2), lcs_length(text1, text2[1::]))

        # return lcs_length(text1, text2)

        # starting from the end of the string (DP), check each subproblems step by step and heirachy the result
        def iter_lcs(text1, text2):
            arrayL = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
            for i in range(len(text1)-1, -1, -1):
                for j in range(len(text2)-1, -1, -1):
                    if text1[i]==text2[j]:
                        arrayL[i][j] = arrayL[i+1][j+1]+1
                    else:
                        arrayL[i][j] = max(arrayL[i+1][j], arrayL[i][j+1])

            return arrayL[0][0]

        return iter_lcs(text1, text2)