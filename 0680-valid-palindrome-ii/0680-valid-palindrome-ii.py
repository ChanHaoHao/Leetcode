class Solution:
    def validPalindrome(self, s: str) -> bool:
        def validation(s, front, back):
            while front<back:
                if s[front]!=s[back]:
                    return False
                front+=1
                back-=1
            return True
        front, back = 0, len(s)-1
        while front<back:
            if s[front] != s[back]:
                return validation(s, front+1, back) or validation(s, front, back-1)
            front+=1
            back-=1
        return True