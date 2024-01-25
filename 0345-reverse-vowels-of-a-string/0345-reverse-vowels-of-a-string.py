class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_list = ["a", "e", "i", "o", "u",
                        "A", "E", "I", "O", "U"]
        # l, r = 0, len(s)-1

        # while l<r:
        #     if s[l] not in vowel_ascii_list:
        #         l+=1
        #         continue
            
        #     if s[r] not in vowel_ascii_list:
        #         r-=1
        #         continue

        #     if (s[l] in vowel_ascii_list) and (s[r] in vowel_ascii_list):
        #         tmp = [s[l], s[r]]
        #         s = s[0:l]+tmp[1]+s[l+1:r]+tmp[0]+s[r+1::]

        #         l+=1
        #         r-=1
            
        # return s

        # store all the vowels into vowel list, then pop the list whenever a vowel is found
        vowel = []
        for x in s:
            if x in vowel_list:
                vowel.append(x)
        
        ans = ""
        for x in s:
            if x in vowel_list:
                ans+=vowel.pop()
            else:
                ans+=x
        return ans