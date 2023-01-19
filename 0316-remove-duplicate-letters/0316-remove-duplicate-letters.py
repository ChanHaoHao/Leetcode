class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        temp = s
        count, selected= [0]*26, [False]*26
        #find all the elements and its count
        while len(s)>0:
            count[ord(s[0])-97] = len([temp for temp, char in enumerate(temp) if char == s[0]])
            s = s.replace(s[0],"")

        ans = []
        for x in temp:
            count[ord(x)-ord('a')]-=1

            #if the element is already selected, skip the rest and start the next
            if selected[ord(x)-ord('a')]:
                continue

            #(1) if there is something in the 
            while ans and ord(ans[-1])>ord(x) and count[ord(ans[-1])-ord('a')]>0:
                selected[ord(ans[-1])-ord('a')]=False
                ans.pop()

            ans.append(x)
            selected[ord(x)-ord('a')]=True
        return ''.join(ans)

                