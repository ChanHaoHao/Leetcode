class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        test = Counter(derived)
        if test[1]%2:
            return False
        return True
