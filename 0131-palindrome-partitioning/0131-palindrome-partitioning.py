class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        n = len(s)

        def is_palindrome(substring):
            left=0
            right=len(substring)-1

            while left<right:
                if substring[left]!=substring[right]:
                    return False
                left+=1
                right-=1
            return True
        
        def backtrack(start, path):
            # if it is the end of the string
            if start==len(s):
                result.append(path)
                return
            
            for end in range(start+1, n+1):
                # if a palindrome is found, add it to the path, then go through all possible substrings
                if is_palindrome(s[start:end]):
                    backtrack(end, path+[s[start:end]])
        
        backtrack(0, [])
        return result