class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # check the two strings are the same
        if str1 + str2 != str2 + str1:
            return ""
        
        ans = ""
        # try all the prefix in the shorter string
        if len(str1)<len(str2):
            tmp = str1
            str1 = str2
            str2 = tmp

        # check all the prefix in str2
        for x in range(1, len(str2)+1):
            # if the len of the prefix can't be a factor of both strings
            if not len(str2)%x and not len(str1)%x:
                common_divisor = True
                # check the str1
                for y in range(len(str1)//x):
                    if str1[x*y:x*y+x]!=str2[0:x]:
                        common_divisor = False
                        break
                # if str2[0:x] is a common divisor of str1, check str2
                # if common_divisor:
                #     for y in range(len(str2)//x):
                #         if str2[x*y:x*y+x]!=str2[0:x]:
                #             common_divisor = False
                #             break
                if common_divisor:
                    ans = str2[0:x]
        return ans